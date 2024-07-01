"""
Generates the *-fullscreen.html files for the static folder, because I don't want to use the website's theme for those pages.

There's probably a better way to do this.
"""

import os, re
from pelican import signals
#from jinja2 import Template

FULLSCREEN_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>

<textarea id="outputTextarea" class="tatjsOutput" readonly style="height: calc(100vh - 40px); border: none;"></textarea><br />

<div id="fullscreenControls">
<button type="button" onclick="running = !running;">&#x23FB; Off</button>&nbsp;&nbsp;&nbsp;

<input type="text" id="foregroundColorSetting" style="width: 70px">
<input type="text" id="backgroundColorSetting" style="width: 70px">
<button type="button" onclick="changeColorTheme(document.getElementById('foregroundColorSetting').value, document.getElementById('backgroundColorSetting').value)">&#x1F197;</button>
<button type="button" onclick="swapColors();">&#x1F504;</button>&nbsp;&nbsp;&nbsp;&nbsp;

<button type="button" onclick="changeColorTheme('black', 'white');">&#x1F4A1;</button>
<button type="button" onclick="changeColorTheme('white', 'black');">&#x1F3B1;</button>
<button type="button" onclick="changeColorTheme('white', '#A10901');">&#x2764;&#xFE0F;</button>
<button type="button" onclick="changeColorTheme('#993D28', '#FCAF1B');">&#x1F36F;</button>
<button type="button" onclick="changeColorTheme('#1B2463', '#00003E');">&#x1F319;</button>
<button type="button" onclick="changeColorTheme('#C2FA6F', '#554E80');">&#x1F9EA;</button>
<button type="button" onclick="changeColorTheme('#FFE082', '#1565C0');">&#x1F324;&#xFE0F;</button>
<button type="button" onclick="changeColorTheme('#E7B6BF', '#924C38');">&#x1FAB5;</button>
<button type="button" onclick="changeColorTheme('#00FF00', '#FF007F');">&#x1F349;</button>
<button type="button" onclick="changeColorTheme('#9CD54A', '#4A5A20');">&#x1F334;</button>
<button type="button" onclick="changeColorTheme('#08FF08', '#111111');">&#x1F60E;</button>

&nbsp;&nbsp;&nbsp;&nbsp;<button type="button" onclick="document.getElementById('fullscreenControls').style.display = 'none'; document.getElementById('outputTextarea').style.height = '100vh';">X</button>

</div>

<script src="/static/textarea_terminal.js"></script>
<link rel="stylesheet" href="/static/textarea_terminal.css">


<script>

function setColorsBasedOnTextFields() {
    let fg = document.getElementById('foregroundColorSetting').value;
    let bg = document.getElementById('backgroundColorSetting').value;
    changeColorTheme(fg, bg);
}
document.addEventListener('DOMContentLoaded', (event) => {
document.getElementById('foregroundColorSetting').addEventListener('keydown', function(event) {
    // Check if the Enter key was pressed
    if (event.key === "Enter" || event.keyCode === 13) {
        // Prevent the default action to avoid form submission or any other default behavior
        event.preventDefault();
        setColorsBasedOnTextFields();
    }
});
document.getElementById('backgroundColorSetting').addEventListener('keydown', function(event) {
    // Check if the Enter key was pressed
    if (event.key === "Enter" || event.keyCode === 13) {
        // Prevent the default action to avoid form submission or any other default behavior
        event.preventDefault();
        setColorsBasedOnTextFields();
    }
});
});
function changeColorTheme(foregroundColor, backgroundColor) {
  document.body.style.backgroundColor = backgroundColor; 
  document.getElementById('outputTextarea').style.backgroundColor = backgroundColor;
  document.getElementById('outputTextarea').style.color = foregroundColor;
  document.getElementById('foregroundColorSetting').value = foregroundColor;
  document.getElementById('backgroundColorSetting').value = backgroundColor;
}

function swapColors() {
  let fg = document.getElementById('foregroundColorSetting').value;
  let bg = document.getElementById('backgroundColorSetting').value;
  changeColorTheme(bg, fg);
}


{{ fullscreen_source_code }}

</script>

</body>
</html>
"""


def extract_fullscreen_source_code_from_md_file(filename):
    """Takes a .md markdown and extracts data from it in the format of:

    
    [{'fullscreen_filename': <filename info>, 'title': <title>, 'scroll_code': <scroll js code>},
     {'fullscreen_filename': <filename info>, 'title': <title>, 'scroll_code': <scroll js code>},
     ...
    ] 
    """
    with open(filename) as file_obj:
        file_contents = file_obj.read()

    return_value  = []

    source_codes = re.findall('<script>// SCROLL CODE:(.*?)</script>', file_contents, flags=re.DOTALL)

    if len(source_codes) == 0:
        #raise Exception('Could not find <script> pattern in ' + filename)
        return None # Not all articles are scroll art pieces that will need fullscreen versions. Just skip it.

    for source_code in source_codes:

        d = {}

        d['title'] = source_code[0:source_code.find('\n')]
        #print('!!!', d['title'])
        d['fullscreen_filename'] = d['title'].lower().replace(' ', '-') + '-fullscreen.html'
        d['scroll_code'] = '//' + source_code  # The original // JS comment was cut out by the re.findall regex.

        return_value.append(d)

    return return_value






def generate_fullscreen_static_pages(sender):
    print("sam_fullscreen_generate_plugin.py: Generating SAM fullscreen static pages...")

    md_folder = os.path.join(os.path.dirname(__file__), '..', 'content')

    print('sam_fullscreen_generate_plugin.py: ', end='')
    for md_filename in os.listdir(md_folder):
        # Go through the markdown files for each scroll art piece...
        if not md_filename.endswith('.md'): continue  # skip non-.md and non-fullscreen files

        print('File ' + md_filename + '... ', end='')
        
        fullscreen_data = extract_fullscreen_source_code_from_md_file(os.path.join(md_folder, md_filename))
        if fullscreen_data is None:
            print('(skipped) ', end='')
            continue  # This file doesn't need a fullscreen.

        for fullscreen_single_data in fullscreen_data:
            # Each markdown page can have multiple fullscreen pages to create...
            
            # I decided to not use Jinja2 since the replacement is so simple, but I'm leaving the jinja template code here for now:
            #template = Template(FULLSCREEN_PAGE_TEMPLATE)
            with open(os.path.join(os.path.dirname(__file__), '..', 'content', 'static', fullscreen_single_data['fullscreen_filename']), 'w', encoding='utf-8') as file_obj:
                # Render the html for the full screen:
                rendered_fullscreen_html = FULLSCREEN_PAGE_TEMPLATE.replace('{{ title }}', fullscreen_single_data['title']).replace('{{ fullscreen_source_code }}', fullscreen_single_data['scroll_code'])
                #rendered_fullscreen_html = template.render(title = fullscreen_single_data['title'], fullscreen_source_code=fullscreen_single_data['scroll_code'])
                file_obj.write(rendered_fullscreen_html)

    print('\nsam_fullscreen_generate_plugin.py: Done generating fullscreen static pages.')

def register():
    signals.initialized.connect(generate_fullscreen_static_pages)
    #signals.content_written.connect(generate_fullscreen_static_pages)


