Title: Full of Squares
Date: 2024-03-23 10:00
Authors: Al Sweigart
Summary: <a href="{filename}full-of-squares.md">Squares of various sizes. Click here to view the animation...<br><img src="{static}/images/full-of-squares-screenshot.webp" class="scrollArtPreview"></a>
og_image: full-of-squares-screenshot.webp
og_description: Squares of various sizes.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/full-of-squares-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/full-of-squares-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

The [box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character) are used to draw squares of various sizes.

Links
=====

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/fullofsquares.py)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/oqa41cjd/)


<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Full of Squares
const tat = new Tatjs(document.getElementById('outputTextarea'));


let running = true;
// Constants for settings:
const DELAY = 100;  // Pause after each row in milliseconds.
const WIDTH = 200  // Number of columns in output.
const MIN_SQUARE_SIZE = 1;
const MAX_SQUARE_SIZE = 7;
const CHANCE_OF_FILLED_SQUARE = 0.0;
const NUM_SQUARES_PER_ROW = 3;

const UP_DOWN_CHAR         = String.fromCharCode(9474);  // Character 9474 is '│'
const LEFT_RIGHT_CHAR      = String.fromCharCode(9472);  // Character 9472 is '─'
const DOWN_RIGHT_CHAR      = String.fromCharCode(9484);  // Character 9484 is '┌'
const DOWN_LEFT_CHAR       = String.fromCharCode(9488);  // Character 9488 is '┐'
const UP_RIGHT_CHAR        = String.fromCharCode(9492);  // Character 9492 is '└'
const UP_LEFT_CHAR         = String.fromCharCode(9496);  // Character 9496 is '┘'

const UP_DOWN_RIGHT_CHAR   = String.fromCharCode(9500);  // Character 9500 is '├'
const UP_DOWN_LEFT_CHAR    = String.fromCharCode(9508);  // Character 9508 is '┤'
const DOWN_LEFT_RIGHT_CHAR = String.fromCharCode(9516);  // Character 9516 is '┬'
const UP_LEFT_RIGHT_CHAR   = String.fromCharCode(9524);  // Character 9524 is '┴'
const CROSS_CHAR           = String.fromCharCode(9532);  // Character 9532 is '┼'


const EMPTY = ' '.repeat(25) + '...,' + String.fromCharCode(9633);  // The characters in this string are used to fill outside the squares.
const SQUARE_INTERIOR = ' ';  // The characters in this string are used to fill the square interiors.


function getOutlineSquare(size) {
    console.assert(size >= 0);
    
    let rows = [];
    // Make the top row of the square:
    rows.push(DOWN_RIGHT_CHAR + (LEFT_RIGHT_CHAR.repeat(size * 2)) + DOWN_LEFT_CHAR);

    // Make the middle segment of the square:
    for (let i = 0; i < size; i++) {
        rows.push(UP_DOWN_CHAR + SQUARE_INTERIOR.repeat(size * 2) + UP_DOWN_CHAR);
    }

    // Make the bottom row of the square:
    rows.push(UP_RIGHT_CHAR + (LEFT_RIGHT_CHAR.repeat(size * 2)) + UP_LEFT_CHAR);

    return rows;
}


function getFilledSquare(size) {
    console.assert(size >= 0);
    
    let rows = [];
    // Make the top row of the square:
    rows.push(DOWN_RIGHT_CHAR + (DOWN_LEFT_RIGHT_CHAR.repeat(size * 2)) + DOWN_LEFT_CHAR);

    // Make the middle segment of the square:
    for (let i = 0; i < size; i++) {
        rows.push(UP_DOWN_RIGHT_CHAR + (CROSS_CHAR.repeat(size * 2)) + UP_DOWN_LEFT_CHAR);
    }

    // Make the bottom row of the square:
    rows.push(UP_RIGHT_CHAR + (UP_LEFT_RIGHT_CHAR.repeat(size * 2)) + UP_LEFT_CHAR);

    return rows;
}

async function main() {
    let nextRows = [];
    while (running) {
        for (let j = 0; j < NUM_SQUARES_PER_ROW; j++) {
            const size = Math.floor(Math.random() * (MAX_SQUARE_SIZE - MIN_SQUARE_SIZE + 1)) + MIN_SQUARE_SIZE;

            let square;
            if (Math.random() < CHANCE_OF_FILLED_SQUARE) {
                square = getFilledSquare(size);
            } else {
                square = getOutlineSquare(size);
            }

            const xStart = Math.floor(Math.random() * (WIDTH - 1 - (size * 2 + 2)));

            // Make sure there are enough rows in `nextRows`:
            while (nextRows.length < size + 2) {
                    nextRows.push(Array.from({length: WIDTH}, () => EMPTY[Math.floor(Math.random() * EMPTY.length)]));            
            }

            // Add the square to `nextRows`
            for (let y = 0; y < square.length; y++) {
                for (let x = 0; x < square[y].length; x++) {
                    nextRows[y][x + xStart] = square[y][x];
                }
            }
        }

        // Print the row and then remove it:
        tat.print(nextRows[0].join(''));
        nextRows.shift();

        // Pause for a bit before printing the next row:
        await sleep(DELAY);
    }
}

main();
</script>
