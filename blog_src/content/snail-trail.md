Title: Spike    
Date: 2024-03-04 10:09
Authors: Al Sweigart
Summary: <a href="{filename}spike.md">A simple spike pattern. Click here to view the animation...<br><img src="{static}/images/spike-screenshot.webp" class="scrollArtPreview"></a>
og_image: spike-screenshot.webp
og_description: A simple spike pattern.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/spike-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/spike-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

While "Spike" is a quickly repeating pattern, the exponential movement gives the impression of rythmic growth and retraction.

Links
=====


* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/spike.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/spike.ts) 
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/eLhmxy9g/)


<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Spike
const tat = new Tatjs(document.getElementById('outputTextarea'));

const DELAY = 100;
let width = 120;
let running = true;

async function main() {
    while (running) {
        //width = 80; // TODO add a getWidth() kind of function to bextjs

        for (let i = 1; i * i < width; i++) {
            tat.print('-'.repeat(i * i));
            await sleep(DELAY);
            if (!running) break;
        }

        for (let i = Math.floor(Math.sqrt(width)) - 1; i > 1; i--) {
            tat.print('-'.repeat(i * i));
            await sleep(DELAY);
            if (!running) break;
        }
    }
}

main();
</script>
