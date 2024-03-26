Title: Diamond Sky
Date: 2024-03-23 10:00
Modified: 2024-03-23 10:00
Authors: Al Sweigart
Summary: <a href="{filename}diamond-sky.md">Diamonds of various sizes.<br><img src="{static}/images/diamond-sky-screenshot.webp" style="max-width: 640px;"></a>
og_image: diamond-sky-screenshot.webp
og_description: Scroll art piece; Diamonds of various sizes.

<img src="{static}/images/diamond-sky-screenshot.webp" style="max-width: 640px;">

This piece is based on [*Project 16 - Diamonds*](https://inventwithpython.com/bigbookpython/project16.html) from my free programming book, [*The Big Book of Small Python Projects*](https://inventwithpython.com/bigbookpython/project16.html) for creating ASCII art diamonds of various sizes. I wrote [*Diamond Sky*]({filename}diamond-sky.md) before I created [*Full of Squares*]({filename}full-of-squares.md) but they share similar styles.

This is the first piece where the code has a `rows` array that contains the next few rows to display. If the program randomly generates a diamond that is 12 rows high, the `rows` array is expanded to fit the next 12 rows. This is a bit more advanced than the wallpaper TODO


* **[VIEW FULLSCREEN](/static/diamond-sky-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/diamondsky.py)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/7x15u60w/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>// SCROLL CODE


let bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
let running = true;

// Code adapted from my diamonds.py program here: https://inventwithpython.com/bigbookpython/project16.html

const DELAY = 100;  // Pause after each row in milliseconds.
const WIDTH = 200;  // Number of columns in output.
const MIN_DIAMOND_SIZE = 1;
const MAX_DIAMOND_SIZE = 8;

const CHANCE_FOR_FILLED_DIAMOND = 0.3;  // Set between 0.0 and 1.0

const NUM_DIAMONDS_PER_ROW = 2;

const EMPTY = '                ...,';

function getOutlineDiamond(size) {
    if (size <= 0) throw new Error('Size must be greater than 0');
    let rows = [];
    // Make the top half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(size - i - 1).fill(null).concat('/').concat(new Array(i * 2).fill(' ')).concat('\\'));
    }
    // Make the bottom half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(i).fill(null).concat('\\').concat(new Array((size - i - 1) * 2).fill(' ')).concat('/'));
    }
    return rows;
}

function getFilledDiamond(size) {
    if (size <= 0) throw new Error('Size must be greater than 0');
    let rows = [];
    // Make the top half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(size - i - 1).fill(null).concat(new Array(i + 1).fill('/')).concat(new Array(i + 1).fill('\\')));
    }
    // Make the bottom half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(i).fill(null).concat(new Array(size - i).fill('\\')).concat(new Array(size - i).fill('/')));
    }
    return rows;
}

async function main() {
    let nextRows = [];
    while (running) {
        for (let j = 0; j < NUM_DIAMONDS_PER_ROW; j++) {
            let size = Math.floor(Math.random() * (MAX_DIAMOND_SIZE - MIN_DIAMOND_SIZE + 1)) + MIN_DIAMOND_SIZE;

            let diamond;
            if (Math.random() < CHANCE_FOR_FILLED_DIAMOND) {
                diamond = getFilledDiamond(size);
            } else {
                diamond = getOutlineDiamond(size);
            }

            let xStart = Math.floor(Math.random() * (WIDTH - 1 - (size * 2)));

            // Make sure there are enough rows in `nextRows`:
            while (nextRows.length < size * 2) {
                nextRows.push(new Array(WIDTH).fill(null).map(() => EMPTY[Math.floor(Math.random() * EMPTY.length)]));
            }

            // Add the diamond to `nextRows`
            for (let y = 0; y < diamond.length; y++) {
                for (let x = 0; x < diamond[y].length; x++) {
                    if (diamond[y][x] === null) continue;  // Skip null values, equivalent to Python's None
                    nextRows[y][x + xStart] = diamond[y][x];
                }
            }
        }

        // Print the row and then remove it:
        print(nextRows[0].join(''));
        nextRows.shift();

        // Pause for a bit before printing the next row:
        await sleep(DELAY);
    }
}

main();

</script>
