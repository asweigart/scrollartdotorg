Title: Diagonal Maze
Date: 2024-03-04 10:05
Modified: 2024-03-04 10:05
Authors: Al Sweigart
Summary: The classic Commodore 64 pattern.

"Diagonal Maze" is a simple random distribution of the diagonal line characters. These are different from the / forward slash and \ backslashes because they connect the actual corners of the text cell boundaries. By randomly printing them, they naturally form a maze-like pattern. This is no solveable maze, of course,

* [View fullscreen](/static/diagonalmaze-fullscreen.html)
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/diagonalmaze.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/diagonalmaze.ts)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
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
        print(line);
        await sleep(DELAY);
    }
}

main();
</script>
