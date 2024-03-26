Title: Cube Wall
Date: 2024-03-04 10:03
Modified: 2024-03-04 10:03
Authors: Al Sweigart
Summary: <a href="{filename}cube-wall.md">Random cube wallpaper.<br><img src="{static}/images/cube-wall-screenshot.webp" style="max-width: 640px;"></a>
og_image: cube-wall-screenshot.webp
og_description: Random cube wallpaper.

<img src="{static}/images/cube-wall-screenshot.webp" style="max-width: 640px;">

"Cube Wall" has a subtly 3D look by adding random shading to the cubes it draws.


* **[VIEW FULLSCREEN](/static/cubewall-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/cubewall.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/cubewall.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/5Lz0wfbr/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>// SCROLL CODE

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
const DELAY = 100;
const DENSITY = 0.35;
const width = 220;
let running = true;

async function main() {

    while (running) {
        let segmentWidth = Math.floor(width / 18);

        let row1 = '';
        let row2 = '';
        let row3 = '';
        let row4 = '';
        let row5 = '';
        let row6 = '';

        let top1Shading = '';
        let top1ShadingBottom = '';
        let top2Shading = '';
        let top2ShadingBottom = '';
        let bottom1Shading = '';
        let bottom1ShadingBottom = '';
        let bottom2Shading = '';
        let bottom2ShadingBottom = '';
        let side1Shading = '';
        

        for (let i = 0; i < segmentWidth; i++) {
            if (Math.random() < DENSITY) {
                top1Shading = '/////';
                top1ShadingBottom = '_/_/_';
            } else {
                top1Shading = '     ';
                top1ShadingBottom = '_____';
            }

            if (Math.random() < DENSITY) {
                top2Shading = '/////';
                top2ShadingBottom = '_/_/_';
            } else {
                top2Shading = '     ';
                top2ShadingBottom = '_____';
            }

            if (Math.random() < DENSITY) {
                bottom1Shading = '\\\\\\\\\\';
                bottom1ShadingBottom = '_\\_\\_';
            } else {
                bottom1Shading = '     ';
                bottom1ShadingBottom = '_____';
            }

            if (Math.random() < DENSITY) {
                bottom2Shading = '\\\\\\\\\\';
                bottom2ShadingBottom = '_\\_\\_';
            } else {
                bottom2Shading = '     ';
                bottom2ShadingBottom = '_____';
            }

            if (Math.random() < DENSITY) {
                if (Math.random() < 0.5) {
                    side1Shading = '\\\\';
                } else {
                    side1Shading = '//';
                }
            } else {
                side1Shading = '  ';
            }

            row1 += `  /${top1Shading}/\\${bottom2Shading}\\  `;
            row2 += ` /${top1Shading}/${side1Shading}\\${bottom2Shading}\\ `;
            row3 += `/${top1ShadingBottom}/${side1Shading.repeat(2)}\\${bottom2ShadingBottom}\\`;
            row4 += `\\${bottom1Shading}\\${side1Shading.repeat(2)}/${top2Shading}/`;
            row5 += ` \\${bottom1Shading}\\${side1Shading}/${top2Shading}/ `;
            row6 += `  \\${bottom1ShadingBottom}\\/${top2ShadingBottom}/  `;
        }

        print(row1); await sleep(DELAY);
        print(row2); await sleep(DELAY);
        print(row3); await sleep(DELAY);
        print(row4); await sleep(DELAY);
        print(row5); await sleep(DELAY);
        print(row6); await sleep(DELAY);
    }
}

main();
</script>