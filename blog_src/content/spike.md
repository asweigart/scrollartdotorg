Title: Spike    
Date: 2024-03-04 10:09
Modified: 2024-03-04 10:09
Authors: Al Sweigart
Summary: <a href="{filename}spike.md">A simple spike pattern.<br><img src="{static}/images/spike-screenshot.webp" style="max-width: 640px;"></a>

<img src="{static}/images/spike-screenshot.webp" style="max-width: 640px;">

While "Spike" is a quickly repeating pattern, the exponential movement gives the impression of rythmic growth and retraction.


* **[VIEW FULLSCREEN](/static/spike-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/spike.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/spike.ts) 
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/eLhmxy9g/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
const DELAY = 100;
let width = 120;
let running = true;

async function main() {
    while (running) {
        //width = 80; // TODO add a getWidth() kind of function to bextjs

        for (let i = 1; i * i < width; i++) {
            print('-'.repeat(i * i));
            await sleep(DELAY);
            if (!running) break;
        }

        for (let i = Math.floor(Math.sqrt(width)) - 1; i > 1; i--) {
            print('-'.repeat(i * i));
            await sleep(DELAY);
            if (!running) break;
        }
    }
}

main();
</script>
