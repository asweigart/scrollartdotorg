Title: Math Function
Date: 2024-03-04 10:08
Modified: 2024-03-04 10:08
Authors: Al Sweigart
Summary: <a href="{filename}math-func.md">Bitmap patterns based on Cartesian coordinate inputs to a math function.<br><img src="{static}/images/math-func-screenshot.webp" style="max-width: 640px;"></a>
og_image: math-func-screenshot.webp
og_description: Bitmap patterns based on Cartesian coordinate inputs to a math function.

<img src="{static}/images/math-func-screenshot.webp" style="max-width: 640px;">

"Math Function" is a highly configurable, deterministic piece that paints a bitmap based on the output of a mathematical function given the X and Y coordinates as inputs. Al Sweigart has a blog post, ["Algorithmic Art with the BitFieldDraw Module"](https://inventwithpython.com/blog/2021/08/02/algorithmic-art-with-the-bitfielddraw-module/) that features the output of several functions. The function featured here is `(x ^ y) % 5`. This blog post was based on ideas from [Martin Kleppe's social media posts](https://threadreaderapp.com/thread/1378106731386040322?refresh=1627428184), which were covered in this [Metafilter post](https://www.metafilter.com/192164/Patterns).


Math Function (x ^ y) % 5

* **[VIEW FULLSCREEN](/static/mathfunc-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/mathfunc.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/mathfunc.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/du8bhgnx/)


Math Function (x & y) & (x ^ y) % 19

* **[VIEW FULLSCREEN](/static/mathfunc2-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/mathfunc2.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/mathfunc2.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/xdh8Lvny/)

Math Function ((x | y) % 7)

* **[VIEW FULLSCREEN](/static/mathfunc3-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/mathfunc3.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/mathfunc3.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/6L8s9cxt/)


<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>// SCROLL CODE

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
const DELAY = 100;
let width = 220;

let running = true;
const FUNC = (x, y) => ((x ^ y) % 5) !== 0;
const TOP_BLOCK = String.fromCodePoint(9600);
const BOTTOM_BLOCK = String.fromCodePoint(9604);
const FULL_BLOCK = String.fromCodePoint(9608);
const EMPTY_BLOCK = ' ';


async function main() {
    let y = 0;
    while (running) {
        let line = '';
        for (let x = 0; x < width; x++) {
            let topBit = FUNC(x, y);
            let bottomBit = FUNC(x, y + 1);

            // Flipping the bits because I think they often look better this way:
            topBit = !topBit;
            bottomBit = !bottomBit;

            if (topBit && bottomBit) {
                line += FULL_BLOCK;
            } else if (topBit && !bottomBit) {
                line += TOP_BLOCK;
            } else if (!topBit && bottomBit) {
                line += BOTTOM_BLOCK;
            } else {
                line += ' ';
            }
        }
        print(line);
        y += 2;
        await sleep(DELAY);
    }
}

main();
</script>

