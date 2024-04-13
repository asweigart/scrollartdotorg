Title: Tri Grid Scaffolding
Date: 2024-03-04 10:11
Authors: Al Sweigart
Summary: <a href="{filename}tri-grid-scaffolding.md">A triangular grid in cyclic densities. Click here to view the animation...<br><img src="{static}/images/tri-grid-scaffolding-screenshot.webp" class="scrollArtPreview"></a>
og_image: tri-grid-scaffolding-screenshot.webp
og_description: A triangular grid in cyclic densities.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/tri-grid-scaffolding-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/trigridscaffolding-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>


"Tri Grid Scaffolding" presents a grid of triangles that is slowly filled in and then dismantled each cycle. 

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/trigridscaffolding.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/trigridscaffolding.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/cod509ph/)

<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:TriGridScaffolding
const tat = new Tatjs(document.getElementById('outputTextarea'));

let width = 220
const DELAY = 60;
let CHANGE_AMOUNT = 0.04;

let running = true;

async function main() {
    let density = 0.0;
    while (running) {
        let triangleWidth = Math.floor((width - 2) / 4);
        let row1 = '';
        let row2 = '';

        density += CHANGE_AMOUNT;
        if (density < 0.0 || density >= 1.0) {
            CHANGE_AMOUNT *= -1;
        }
    
        for (let j = 0; j < 2; j++) {
            if (j === 0) {
                // On j == 0, handle the two rows of begins-with-rightside-up-triangles:
                //  /\  /\  /\
                // /__\/__\/__\
                row1 = '';
                row2 = '';
            } else if (j == 1) {
                // On j == 1, handle the two rows of begins-with-upside-down-triangles:
                // \  /\  /
                // _\/__\/_
                row1 = '\\ ';
                row2 = '_\\';
            }
            
            for (let i = 0; i < triangleWidth; i++) {
                if (Math.random() < density) {
                    row1 += ' /';
                    row2 += '/';
                } else {
                    row1 += '  ';
                    row2 += ' ';
                }

                if (Math.random() < density) {
                    row2 += '__';
                } else {
                    row2 += '  ';
                }

                if (Math.random() < density) {
                    row1 += '\\ ';
                    row2 += '\\';
                } else {
                    row1 += '  ';
                    row2 += ' ';
                }
            }

            tat.print(row1);
            await sleep(DELAY);
            tat.print(row2);
            await sleep(DELAY);
        }
    }
}

main();
</script>