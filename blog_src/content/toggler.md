Title: Toggler
Date: 2024-03-04 10:07
Modified: 2024-03-04 10:07
Authors: Al Sweigart
Summary: <a href="{filename}toggler.md">Triangular patterns toggled between two characters, with variants.<br><img src="{static}/images/toggler1-screenshot.webp" style="max-width: 640px;"></a>

<img src="{static}/images/toggler1-screenshot.webp" style="max-width: 640px;">

In "Toggler 1", each column prints one of two characters. Randomly, a "toggler" appears and switches which character the column prints and then moves to the left or right. This creates triangle-shaped regions of toggled values. As more togglers spawn and overlap, the implied shapes become more chaotic and inscrutable. "Toggler 2" is similar, though it creates two togglers going in both directions, sometimes skipping one or two columns as they move.

Toggler 1:

* **[VIEW FULLSCREEN](/static/toggler1-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/toggler1.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/toggler1.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/q5hc9tLf/)

Toggler 2:

* **[VIEW FULLSCREEN](/static/toggler2-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/toggler2.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/toggler2.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/t35mx9pc/)


<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
let width = 220;
let running = true;
const DELAY = 50;
const TRUE_CHAR = '@';
const FALSE_CHAR = '.';
const TOGGLER_DENSITY = 0.10;
const MOVEMENTS = [1, -1];

async function main() {
    let columnChars = Array.from({length: width}, () => false);
    let togglers = [];

    while (running) {
        if (Math.random() < TOGGLER_DENSITY) {
            // Add a new toggler:
            togglers.push({
                position: Math.floor(Math.random() * width), 
                movement: MOVEMENTS[Math.floor(Math.random() * MOVEMENTS.length)]
            });
        }

        // Remove out of bounds togglers:
        togglers = togglers.filter(toggler => toggler.position > 0 && toggler.position < width);

        // Move the togglers and toggle the column chars:
        for (let toggler of togglers) {
            // Toggle the column:
            columnChars[toggler.position] = !columnChars[toggler.position];

            // Move the toggler:
            toggler.position += toggler.movement;
        }

        // Print the columns:
        let line = '';
        for (let columnChar of columnChars) {
            if (columnChar) {
                line += TRUE_CHAR;
            } else {
                line += FALSE_CHAR;
            }
        }
        print(line);
        await sleep(DELAY);
    }
}

main();
</script>
