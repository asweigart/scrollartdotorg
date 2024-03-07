Title: Matrix Screensaver
Date: 2024-03-04 10:06
Modified: 2024-03-04 10:06
Authors: Al Sweigart
Summary: <a href="{filename}matrix-screensaver.md">Hacker-themed trails of ones and zeros.<br><img src="{static}/images/matrix-screensaver-screenshot.webp" style="max-width: 640px;"></a>

<img src="{static}/images/matrix-screensaver-screenshot.webp" style="max-width: 640px;">

The Matrix is a 1999 hacker movie that had an iconic "digital stream" of green alphanumerics scrolling down the screen like trails of rain down a window. Several [screensavers](https://en.wikipedia.org/wiki/Screensaver) were created to mimic this design. This scroll art follows suit, though streaming upwards due to the limitations of scroll art.


* **[VIEW FULLSCREEN](/static/matrixscreensaver-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/matrixscreensaver.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/matrixscreensaver.ts)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.

let running = true;
let width = 220;
const DELAY = 100;
const DENSITY = 0.02;
const MIN_STREAM_LENGTH = 6;
const MAX_STREAM_LENGTH = 14;
const STREAM_CHARS = ['0', '1'];

async function main() {
    let columns = Array.from({length: width}, () => 0);

    while (running) {
        let line = '';
        for (let i = 0; i < width; i++) {
            if (columns[i] === 0) {
                if (Math.random() < DENSITY) {
                    // Restart the stream in this column:
                    columns[i] = Math.floor(Math.random() * (MAX_STREAM_LENGTH - MIN_STREAM_LENGTH)) + MIN_STREAM_LENGTH;
                }
            }
            if (columns[i] > 0) {
                // Add a random stream character for this column:
                line += STREAM_CHARS[Math.floor(Math.random() * STREAM_CHARS.length)];
                columns[i] -= 1;
            } else {
                // Add empty space for this column:
                line += ' ';
            }
        }
        print(line);
        await sleep(DELAY);
    }
}

main();
</script>
