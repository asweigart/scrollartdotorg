Title: Diagonal Maze
Date: 2024-03-04 10:05
Authors: Al Sweigart
Summary: <a href="{filename}diagonal-maze.md">The classic Commodore 64 pattern. Click here to view the animation...<br><img src="{static}/images/diagonal-maze-screenshot.webp" class="scrollArtPreview"></a>
og_image: diagonal-maze-screenshot.webp
og_description: The classic Commodore 64 pattern.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/diagonal-maze-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/diagonalmaze-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

"Diagonal Maze" is a simple random distribution of the diagonal line characters. These are different from the / forward slash and \ backslashes because they connect the actual corners of the text cell boundaries. By randomly printing them, they naturally form a maze-like pattern. This is no solveable maze, of course,

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/diagonalmaze.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/diagonalmaze.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/x2c4jkvp/)

Links
=====

<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:DiagonalMaze
const tat = new Tatjs(document.getElementById('outputTextarea'));

const DELAY = 150;
let width = 220;
let running = true;

async function main() {
    while (running) {
        let line = '';
        for (let i = 0; i < width; i++) {
            if (Math.random() < 0.5) {
                line += String.fromCharCode(9585);
            } else {
                line += String.fromCharCode(9586);
            }
        }
        tat.print(line);
        await sleep(DELAY);
    }
}

main();
</script>
