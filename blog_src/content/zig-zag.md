Title: Zig-zag
Date: 2024-03-04 10:01
Authors: Al Sweigart
Summary: <a href="{filename}zig-zag.md">A simple back and forth animation. Click here to view the animation...<br><img src="{static}/images/zig-zag-screenshot.webp" class="scrollArtPreview"></a>
og_image: zig-zag-screenshot.webp
og_description: A simple back and forth animation.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/zig-zag-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/zigzag-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

"Zig-zag" is just about the simplest scroll art you can have, and was one of the first ones Al Sweigart wrote. It was originally written for his [The Big Book of Small Python Projects](https://inventwithpython.com/bigbookpython/) but was later cut.


* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/zigzag.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/zigzag.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/bq6rLvpf/)


<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:ZigZag
const tat = new Tatjs(document.getElementById('outputTextarea'));

const DELAY = 60;

let width = 80;
let line = '';

let ZIG_NUM_CHARS = 8;
let ZIG_CHAR = '*';

let running = true;
let indentSize = 0;

async function main() {
    while (running) {
        //width = 80; // TODO add a getWidth() kind of function to bextjs

        for (let i = 0; i < width - ZIG_NUM_CHARS; i++) {
            tat.print(' '.repeat(indentSize), ZIG_CHAR.repeat(ZIG_NUM_CHARS));
            indentSize += 1;
            await sleep(DELAY);
            if (!running) break;
        }

        for (let i = 0; i < width - ZIG_NUM_CHARS; i++) {
            tat.print(' '.repeat(indentSize), ZIG_CHAR.repeat(ZIG_NUM_CHARS));
            indentSize -= 1;
            await sleep(DELAY);
            if (!running) break;
        }
    }
}

main();
</script>