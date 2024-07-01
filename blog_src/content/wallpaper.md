Title: Wallpaper
Date: 2024-03-23 10:00
Authors: Al Sweigart
Summary: <a href="{filename}wallpaper.md">The standard wallpaper scroll art, including several designs and tessellations. Click here to view the animation...<br><img src="{static}/images/wallpaper-screenshot.webp" class="scrollArtPreview"></a>
og_image: wallpaper-screenshot.webp
og_description: The standard wallpaper scroll art, including several designs and tessellations.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/wallpaper-screenshot.webp" style="display: none;">



Shining Carpet **[VIEW FULLSCREEN - Shining Carpet](/static/wallpaper-shining-carpet-fullscreen.html)**

<div><textarea id="outputTextarea1" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Little Hex **[VIEW FULLSCREEN - Little Hex](/static/wallpaper-little-hex-fullscreen.html)**

<div><textarea id="outputTextarea2" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Big Hex **[VIEW FULLSCREEN - Big Hex](/static/wallpaper-big-hex-fullscreen.html)**

<div><textarea id="outputTextarea3" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Hex in Hex **[VIEW FULLSCREEN - Hex in Hex](/static/wallpaper-hex-in-hex-fullscreen.html)**

<div><textarea id="outputTextarea4" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Brick **[VIEW FULLSCREEN - Brick](/static/wallpaper-brick-fullscreen.html)**

<div><textarea id="outputTextarea5" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Clover **[VIEW FULLSCREEN - Clover](/static/wallpaper-clover-fullscreen.html)**

<div><textarea id="outputTextarea6" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Skull **[VIEW FULLSCREEN - Skull](/static/wallpaper-skull-fullscreen.html)**

<div><textarea id="outputTextarea7" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Leaves **[VIEW FULLSCREEN - Leaves](/static/wallpaper-leaves-fullscreen.html)**

<div><textarea id="outputTextarea8" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Overlapping Diamonds **[VIEW FULLSCREEN - Overlapping Diamond](/static/wallpaper-overlapping-diamonds-fullscreen.html)**

<div><textarea id="outputTextarea9" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

This piece is based on programs in my free programming book, [*The Big Book of Small Python Projects*](https://inventwithpython.com/bigbookpython/): [*Project 35 - Hex Grid*](https://inventwithpython.com/bigbookpython/project35.html) and [*Project 65 - Shining Carpet*](https://inventwithpython.com/bigbookpython/project65.html). The "wallpaper" style of scroll art displays a static, forever-repeating pattern. While the simplicty makes it less exciting than other forms of scroll art, it is approachable and forces creativity in design. The same short program can display any wallpaper pattern. You only need to change the wallpaper data:

    import time

    DELAY = 0.4
    WIDTH = 80

    wallpaper_rows = [  # Change as desired; All rows must be the same length.
        r'_ \ \ \_/ __',
        r' \ \ \___/ _',
        r'\ \ \_____/ ',
        r'/ / / ___ \_',
        r'_/ / / _ \__',
        r'__/ / / \___',
    ]

    x_repeat = WIDTH // len(wallpaper_rows[0])

    while True:
        # Display each row in wallpaper_rows:
        for row in wallpaper_rows:
            print(row * x_repeat)
            time.sleep(DELAY)

The above produces the hexagon pattern of the carpet in the Overlook Hotel in the 1980 movie, *The Shining*:

    _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
     \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
    \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ 
    / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
    _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
    __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___
    _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
     \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
    \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ 
    / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
    _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
    __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___
    _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
     \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _

By changing the `wallpaper_rows` array...

    wallpaper_rows = [  # Change as desired; All rows must be the same length.
        r'\__   ',
        r'/  \__',
        r'\     ',
        r'/   __',
        r'\__/  ',
        r'/     ',
    ]

...you create a brand new wallpaper:

    \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   
    /  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__
    \     \     \     \     \     \     \     \     \     \     \     \     \     
    /   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __
    \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  
    /     /     /     /     /     /     /     /     /     /     /     /     /     
    \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   
    /  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__
    \     \     \     \     \     \     \     \     \     \     \     \     \     
    /   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __
    \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  
    /     /     /     /     /     /     /     /     /     /     /     /     /     

Tessellations are a natural pattern to create wallpaper scroll art. An [internet image search for "tessellations"](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images) can provide inspiration, especially if you change the search settings to [Line Drawing](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images&iaf=type%3Aline) or [Black and White](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images&iaf=color%3AMonochrome).

The wallpaper program exhibited here contains several different wallpaper patterns which you can select by changing the `WALLPAPER` constant to one of the dictionary key values in the `WALLPAPERS_PATTERNS` variable.

(It was working on these tessellations that made me learn of a bug in Python where raw strings cannot end with a backslash, even if escaped.)

Links
=====

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/wallpaper.py)
* [JavaScript source code in JSFiddle - Shining Carpet](https://jsfiddle.net/asweigart/eatbh7k4/)
* [JavaScript source code in JSFiddle - Little Hex](https://jsfiddle.net/asweigart/etbn9gvf/)
* [JavaScript source code in JSFiddle - Big Hex](https://jsfiddle.net/asweigart/3wvhq0x7/)
* [JavaScript source code in JSFiddle - Hex in Hex](https://jsfiddle.net/asweigart/7rmzq1a0/)
* [JavaScript source code in JSFiddle - Brick](https://jsfiddle.net/asweigart/1L49oq5k/)
* [JavaScript source code in JSFiddle - Clover](https://jsfiddle.net/asweigart/067j8fak/)
* [JavaScript source code in JSFiddle - Skull](https://jsfiddle.net/asweigart/cok7p1Ls/)
* [JavaScript source code in JSFiddle - Leaves](https://jsfiddle.net/asweigart/q3x6ykvL/)
* [JavaScript source code in JSFiddle - Overlapping Diamonds](https://jsfiddle.net/asweigart/45xbpc8m/)




<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">





<script>// SCROLL CODE:Wallpaper Shining Carpet
running = true;

async function main1() {    
    const tat = new Tatjs(document.getElementById('outputTextarea1') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '_ \\ \\ \\_/ __',
        ' \\ \\ \\___/ _',
        '\\ \\ \\_____/ ',
        '/ / / ___ \\_',
        '_/ / / _ \\__',
        '__/ / / \\___'
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main1, 0);
</script>



<script>// SCROLL CODE:Wallpaper Little Hex

running = true;

async function main2() {    
    const tat = new Tatjs(document.getElementById('outputTextarea2') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '/ \\_',
        '\\_/ '
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main2, 0);  
</script>



<script>// SCROLL CODE:Wallpaper Big Hex

running = true;

async function main3() {    
    const tat = new Tatjs(document.getElementById('outputTextarea3') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        ' /   \\    ',
        '/     \\___',
        '\\     /   ',
        ' \\___/    '
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main3, 0);    
</script>



<script>// SCROLL CODE:Wallpaper Hex in Hex

running = true;

async function main4() {    
    const tat = new Tatjs(document.getElementById('outputTextarea4') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        ' / __ \\ \\__/',
        '/ /  \\ \\____',
        '\\ \\__/ / __ ',
        ' \\____/ /  \\'
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main4, 0);
</script>



<script>// SCROLL CODE:Wallpaper Brick

running = true;

async function main5() {    
    const tat = new Tatjs(document.getElementById('outputTextarea5') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '       |',
        '_______|',
        '   |    ',
        '___|____'
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main5, 0);
</script>



<script>// SCROLL CODE:Wallpaper Clover

running = true;

async function main6() {    
    const tat = new Tatjs(document.getElementById('outputTextarea6') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '\\__   ',
        '/  \\__',
        '\\     ',
        '/   __',
        '\\__/  ',
        '/     '
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main6, 0);
</script>



<script>// SCROLL CODE:Wallpaper Skull

running = true;

async function main7() {    
    const tat = new Tatjs(document.getElementById('outputTextarea7') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '/ ___ \\ ^ ',
        ' /   \\ VVV',
        '|() ()|   ',
        ' \\ ^ / ___',
        '\\ VVV /   ',
        ')|   |() ('
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main7, 0);
</script>



<script>// SCROLL CODE:Wallpaper Leaves

running = true;

async function main8() {    
    const tat = new Tatjs(document.getElementById('outputTextarea8') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '  /\\  ',
        '_/  \\_',
        '\\    /',
        ' \\__/ '
    ];

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main8, 0);
</script>



<script>// SCROLL CODE:Wallpaper Overlapping Diamonds

running = true;

async function main9() {    
    const tat = new Tatjs(document.getElementById('outputTextarea9') || document.getElementById('outputTextarea'));
    const DELAY = 400
    const WIDTH = 200
    const wallpaper_rows = [
        '  /\\  /\\',
        '\\/  \\/  ',
        '/   /   ',
        '\\   \\   ',
        '/\\  /\\  ',
        '  \\/  \\/',
        '  /   / ',
        '  \\   \\ '
    ]

    const x_repeat = Math.floor(WIDTH / wallpaper_rows.length);
    let step = 0;

    while (running) {
        // Display each row in wallpaper_rows:
        tat.print(wallpaper_rows[step % wallpaper_rows.length].repeat(x_repeat));
        await sleep(DELAY);
        step += 1;
    }
}
setTimeout(main9, 0);
</script>



