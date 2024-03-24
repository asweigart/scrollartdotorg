Title: Striped Triangles
Date: 2024-03-04 10:10
Modified: 2024-03-04 10:10
Authors: Al Sweigart
Summary: <a href="{filename}striped-triangles.md">Striped triangles in cyclic densities.<br><img src="{static}/images/striped-triangles-screenshot.webp" style="max-width: 640px;"></a>
og_image: striped-triangles-screenshot.webp
og_description: Striped triangles in cyclic densities.

<img src="{static}/images/striped-triangles-screenshot.webp" style="max-width: 640px;">

"Striped Triangles" follows the increasing/decreasing density cycles of [Starfield]({filename}starfield.md) and a triangular grid structure like [Tri Grid Scaffolding]({filename}tri-grid-scaffolding.md). However, the triangles are one of four striped designs using the back and forward slashes. Notice how the triangles taken on a woven, wood-knot look at certain densities.

* **[VIEW FULLSCREEN](/static/stripedtriangles-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/stripedtriangles.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/stripedtriangles.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/f1pwqtez/)

<textarea id="bextOutput" readonly style="height: 400px;"></textarea><br />
<button type="button" onclick="running = !running;">&#x23FB; Off</button>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
let width = 220;
let running = true;

const DELAY = 60;
let CHANGE_AMOUNT = 0.06;


async function main() {
    let density = 0.0;

    while (running) {

        // The width of a pair of triangles is 8 characters:
        //   /\ \ \
        //  / /\ \
        // / / /\
        // 12345678
        let numTrianglePairs = Math.floor((width - 2) / 6);

        density += CHANGE_AMOUNT;
        if (density < 0 || density >= 1.0) {
            CHANGE_AMOUNT *= -1;
        }

        // Draw a row that starts with an upright triangle on the left side.
        let row1 = '  ';
        let row2 = ' ';
        let row3 = '';
        for (let i = 0; i < numTrianglePairs; i++) {
            if (Math.random() < density) {
                if (Math.random() < 0.5) {
                    row1 += '\\';
                    row2 += '\\ \\';
                    row3 += '\\ \\ \\';
                } else {
                    row1 += '/';
                    row2 += '/ /';
                    row3 += '/ / /';
                }
            } else {
                row1 += ' ';
                row2 += '   ';
                row3 += '     ';
            }

            if (Math.random() < density) {
                if (Math.random() < 0.5) {
                    row1 += '\\ \\ \\';
                    row2 += '\\ \\';
                    row3 += '\\';
                } else {
                    row1 += '/ / /';
                    row2 += '/ /';
                    row3 += '/';
                }
            } else {
                row1 += '     ';
                row2 += '   ';
                row3 += ' ';
            }
        }
        print(row1);
        await sleep(DELAY);
        print(row2);
        await sleep(DELAY);
        print(row3);
        await sleep(DELAY);
        
        // Draw a row that starts with an upside down triangle on the left side.
        row1 = '';
        row2 = ' ';
        row3 = '  ';
        for (let i = 0; i < numTrianglePairs; i++) {
            if (Math.random() < density) {
                if (Math.random() < 0.5) {
                    row1 += '\\ \\ \\';
                    row2 += '\\ \\';
                    row3 += '\\';
                } else {
                    row1 += '/ / /';
                    row2 += '/ /';
                    row3 += '/';
                }
            } else {
                row1 += '     ';
                row2 += '   ';
                row3 += ' ';
            }

            if (Math.random() < density) {
                if (Math.random() < 0.5) {
                    row1 += '\\';
                    row2 += '\\ \\';
                    row3 += '\\ \\ \\';
                } else {
                    row1 += '/';
                    row2 += '/ /';
                    row3 += '/ / /';
                }
            } else {
                row1 += ' ';
                row2 += '   ';
                row3 += '     ';
            }
        }
        print(row1);
        await sleep(DELAY);
        print(row2);
        await sleep(DELAY); 
        print(row3);
        await sleep(DELAY);
    }
}

main();

</script>