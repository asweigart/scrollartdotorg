Title: Starfield
Date: 2024-03-04 10:00
Modified: 2024-03-04 10:00
Authors: Al Sweigart
Summary: Asterisks in cycles of density.

"Starfield" creates a simple field of asterisks that cycle in density from completely empty to completely full and back again. The speed, asterisk character, and density change rate can be customized.

* [View fullscreen](/static/starfield-fullscreen.html)
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/starfield.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/starfield.ts)


<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
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
        print(line);
        await sleep(DELAY);
    }
}

main();
</script>