Title: Starfield
Date: 2024-03-04 10:00
Authors: Al Sweigart
Summary: <a href="{filename}starfield.md">Asterisks in cycles of density. Click here to view the animation...<br><img src="{static}/images/starfield-screenshot.webp" class="scrollArtPreview"></a>
og_image: starfield-screenshot.webp
og_description: Asterisks in cycles of density.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/starfield-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/starfield-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>


"Starfield" creates a simple field of asterisks that cycle in density from completely empty to completely full and back again. The speed, asterisk character, and density change rate can be customized.

Links
=====

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/starfield.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/starfield.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/6bLte9gq/)


<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Starfield
const tat = new Tatjs(document.getElementById('outputTextarea'));

const DELAY = 60;
const STAR_CHAR = '\*';
const EMPTY_CHAR = ' ';

let change_amount = 0.005;
let density = 0.0;
let width = 220;
let line = '';

let running = true;

async function main() {
    while (running) {
        //width = 80; // TODO add a getWidth() kind of function to bextjs

        if (density < 0 || density > 1) {
            change_amount *= -1;
        }
        density += change_amount;

        line = '';
        for (let i = 0; i < width; i++) {
            if (Math.random() < density) {
                line += STAR_CHAR;
            } else {
                line += EMPTY_CHAR;
            }
        }
        tat.print(line);
        await sleep(DELAY);
    }
}

main();
</script>