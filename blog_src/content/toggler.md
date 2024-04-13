Title: Toggler
Date: 2024-03-04 10:07
Authors: Al Sweigart
Summary: <a href="{filename}toggler.md">Triangular patterns toggled between two characters, with variants. Click here to view the animation...<br><img src="{static}/images/toggler1-screenshot.webp" class="scrollArtPreview"></a>
og_image: toggler1-screenshot.webp
og_description: Triangular patterns toggled between two characters, with variants.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/toggler1-screenshot.webp" style="display: none;">


Toggler 1 **[VIEW FULLSCREEN](/static/toggler-1-fullscreen.html)**

<div><textarea id="outputTextarea1" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Toggler 2 **[VIEW FULLSCREEN](/static/toggler-2-fullscreen.html)**

<div><textarea id="outputTextarea2" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>



In "Toggler 1", each column prints one of two characters. Randomly, a "toggler" appears and switches which character the column prints and then moves to the left or right. This creates triangle-shaped regions of toggled values. As more togglers spawn and overlap, the implied shapes become more chaotic and inscrutable. "Toggler 2" is similar, though it creates two togglers going in both directions, sometimes skipping one or two columns as they move.

Links
=====

Toggler 1:

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/toggler1.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/toggler1.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/q5hc9tLf/)

Toggler 2:

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/toggler2.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/toggler2.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/t35mx9pc/)



<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Toggler 1
running = true;


async function main() {
    const tat = new Tatjs(document.getElementById('outputTextarea1') || document.getElementById('outputTextarea'));

    let width = 220;
    const DELAY = 50;
    const TRUE_CHAR = '@';
    const FALSE_CHAR = '.';
    const TOGGLER_DENSITY = 0.10;
    const MOVEMENTS = [1, -1];

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
        tat.print(line);
        await sleep(DELAY);
    }
}

setTimeout(main, 0);
</script>


<script>// SCROLL CODE:Toggler 2
running = true;

async function main() {
    const tat = new Tatjs(document.getElementById('outputTextarea2') || document.getElementById('outputTextarea'));

    let width = 220;
    const DELAY = 50;
    const TRUE_CHAR = '@';
    const FALSE_CHAR = '.';
    const TOGGLER_DENSITY = 0.10;
    const MOVEMENTS = [1, 2, 3];


    let columnChars = Array.from({length: width}, () => false);
    let togglers = [];

    while (running) {
        if (Math.random() < TOGGLER_DENSITY) {
                let pos = Math.floor(Math.random() * width);
                let mov = MOVEMENTS[Math.floor(Math.random() * MOVEMENTS.length)];
                // Create the right-moving toggler:
                togglers.push({
                    position: pos, 
                    movement: mov
                });
                // Create the left-moving toggler:
                togglers.push({
                    position: pos, 
                    movement: -mov
                });
                // Toggler the starting column since the two togglers will cancel each other out:
                columnChars[pos] = !columnChars[pos];
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
        tat.print(line);
        await sleep(DELAY);
    }
}

main();
</script>
-->
