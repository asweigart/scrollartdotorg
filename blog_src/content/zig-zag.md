Title: Zig-zag
Date: 2024-03-04 10:01
Modified: 2024-03-04 10:01
Authors: Al Sweigart
Summary: <a href="{filename}zig-zag.md">A simple back and forth animation.<br><img src="{static}/images/zig-zag-screenshot.webp" style="max-width: 640px;"></a>

<img src="{static}/images/zig-zag-screenshot.webp" style="max-width: 640px;">

"Zig-zag" is just about the simplest scroll art you can have, and was one of the first ones Al Sweigart wrote. It was originally written for his [The Big Book of Small Python Projects](https://inventwithpython.com/bigbookpython/) but was later cut.

* **[VIEW FULLSCREEN](/static/zigzag-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/zigzag.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/zigzag.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/bq6rLvpf/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
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
            print(' '.repeat(indentSize), ZIG_CHAR.repeat(ZIG_NUM_CHARS));
            indentSize += 1;
            await sleep(DELAY);
            if (!running) break;
        }

        for (let i = 0; i < width - ZIG_NUM_CHARS; i++) {
            print(' '.repeat(indentSize), ZIG_CHAR.repeat(ZIG_NUM_CHARS));
            indentSize -= 1;
            await sleep(DELAY);
            if (!running) break;
        }
    }
}

main();
</script>