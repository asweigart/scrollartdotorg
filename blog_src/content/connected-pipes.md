Title: Connected Pipes    
Date: 2024-03-23 10:00
Authors: Al Sweigart
Summary: <a href="{filename}connected-pipes.md">Random squiggles that form a sort of connected pipework. There are some isolated sections but no dead ends. Click here to view the animation...<br><img src="{static}/images/connected-pipes-screenshot.webp" class="scrollArtPreview"></a>
og_image: connected-pipes-screenshot.webp
og_description: Random squiggles that form a sort of connected pipework. There are some isolated sections but no dead ends.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/connected-pipes-screenshot.webp" style="display: none;">

Elongated **[VIEW FULLSCREEN](/static/connected-pipes-elongated-fullscreen.html)**

<div><textarea id="outputTextarea1" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Squarish **[VIEW FULLSCREEN](/static/connected-pipes-squarish-fullscreen.html)**


<div><textarea id="outputTextarea2" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>


I wanted to make use of the [box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character) to form some sort of random but connected shape, something like the old [Pipe Dream game (which apparently was called Pipe Mania when originally released in 1989)](https://en.wikipedia.org/wiki/Pipe_Mania).

Ensuring that there are no dead ends is a constraint satisfaction problem: I build the pipes one row at a time from left to right. For each space in the row, I consider the adjacent spaces to the left and above. Only the current and previously printed rows need to be kept in memory. The space to the right and below the current space always has both possibilities of connection or no connection. So if there are connections from the left and from above, I know the box-drawing character I choose needs to go to the left or to the right, and it's random chance as to whether it'll have a connection to the right and below.

There are two forms of this piece, configurable by the VERTICAL_STYLE_FACTOR variable. When set to 1.0, the program never sets the space to have a right-connecting pipe. This should mean that there are only straight vertical lines, because how could there be left-right horizontal connections if there's never a right connection?

I was surprised by this result. But then I realized at the very end, when a space only has only one dead end connection from the left space or the above space, it will randomly include connections down and right. This was a measure I added earlier for more variation, and it was just good fortune it produced the "elongated" vertical effect.

I also feature the squarish form (where VERTICAL_STYLE_FACTOR is set to 0.0) for comparison. You can change this value anywhere within the 0.0 to 1.0 range to set this effect.

Links
=====

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/connectedpipes.py)
* [JavaScript source code in JSFiddle - Elongated](https://jsfiddle.net/asweigart/k6Lqhtyd/)
* [JavaScript source code in JSFiddle - Squarish](https://jsfiddle.net/asweigart/hj5xnze8/)


<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Connected Pipes Elongated
running = true;

// Main loop
(async function main() {
    let e = document.getElementById('outputTextarea1') || document.getElementById('outputTextarea');
    e.style.lineHeight = '1';
    const tat = new Tatjs(e);

    // Constants for settings:
    const DELAY = 200;  // Pause after each row in milliseconds.
    const WIDTH = 200;

    // This setting changes the behavior to create the "long vertical style" if greater than 0.0:
    const VERTICAL_STYLE_FACTOR = 1.0;  // Set between 0.0 and 1.0

    // Constants for printed characters:
    const UP_DOWN_CHAR = String.fromCharCode(9474);  // Character 9474 is '│'
    const LEFT_RIGHT_CHAR = String.fromCharCode(9472);  // Character 9472 is '─'
    const DOWN_RIGHT_CHAR = String.fromCharCode(9484);  // Character 9484 is '┌'
    const DOWN_LEFT_CHAR = String.fromCharCode(9488);  // Character 9488 is '┐'
    const UP_RIGHT_CHAR = String.fromCharCode(9492);  // Character 9492 is '└'
    const UP_LEFT_CHAR = String.fromCharCode(9496);  // Character 9496 is '┘'
    const UP_DOWN_RIGHT_CHAR = String.fromCharCode(9500);  // Character 9500 is '├'
    const UP_DOWN_LEFT_CHAR = String.fromCharCode(9508);  // Character 9508 is '┤'
    const DOWN_LEFT_RIGHT_CHAR = String.fromCharCode(9516);  // Character 9516 is '┬'
    const UP_LEFT_RIGHT_CHAR = String.fromCharCode(9524);  // Character 9524 is '┴'
    const CROSS_CHAR = String.fromCharCode(9532);  // Character 9532 is '┼'
    const EMPTY = ' ';

    // The previous printed row; initialize to up-left-right characters:
    let prevRow = Array(WIDTH).fill(UP_LEFT_RIGHT_CHAR);


    while (running) {

        let row = [];  // Character strings to print in this row.
        for (let i = 0; i < WIDTH; i++) {
            let prevChar = prevRow[i];
            let leftConnect, upConnect, downConnect, rightConnect;

            // Figure out if we need to connect the left side:
            leftConnect = i > 0 && "─┌└├┬┴┼".includes(row[i - 1]);

            // Figure out if we need to connect the up side:
            upConnect = "│┌┐├┤┬┼".includes(prevChar);

            // The downward and right side connection can be either:
            downConnect = Math.random() < 0.5;

            if (i == WIDTH - 1) {
                if (!upConnect && !downConnect && leftConnect && !rightConnect) {
                    // Make this a left-down pipe:
                    downConnect = true;
                } else if (!upConnect && downConnect && !leftConnect && !rightConnect) {
                    // Make this an empty space:
                    downConnect = false;
                } else if (upConnect && !downConnect && !leftConnect && !rightConnect) {
                    // Make this an up-down pipe:
                    downConnect = true;
                }
            } else {
                rightConnect = Math.random() < 0.5;
            }

            // Override rightConnect value if VERTICAL_STYLE_FACTOR is greater than 0.0:
            if (Math.random() < VERTICAL_STYLE_FACTOR) {
                rightConnect = false;
            }

            let char;
            // Get the character to print based on the connections to the four other sides:
            if (upConnect && downConnect && leftConnect && rightConnect) char = CROSS_CHAR;
            else if (upConnect && downConnect && leftConnect) char = UP_DOWN_LEFT_CHAR;
            else if (upConnect && downConnect && rightConnect) char = UP_DOWN_RIGHT_CHAR;
            else if (upConnect && downConnect) char = UP_DOWN_CHAR;
            else if (upConnect && leftConnect && rightConnect) char = UP_LEFT_RIGHT_CHAR;
            else if (upConnect && leftConnect) char = UP_LEFT_CHAR;
            else if (upConnect && rightConnect) char = UP_RIGHT_CHAR;
            else if (upConnect) char = Math.random() < 0.5 ? UP_DOWN_CHAR : UP_RIGHT_CHAR;  // Randomly end or continue the line upwards
            else if (downConnect && leftConnect && rightConnect) char = DOWN_LEFT_RIGHT_CHAR;
            else if (downConnect && leftConnect) char = DOWN_LEFT_CHAR;
            else if (downConnect && rightConnect) char = DOWN_RIGHT_CHAR;
            else if (downConnect) char = DOWN_RIGHT_CHAR;  // Force the line to go down and to the right
            else if (leftConnect && rightConnect) char = LEFT_RIGHT_CHAR;
            else if (leftConnect) char = Math.random() < 0.5 ? LEFT_RIGHT_CHAR : DOWN_LEFT_CHAR;  // Randomly end or bend the line leftwards
            else if (rightConnect) char = DOWN_RIGHT_CHAR;  // Force the line to go down and to the right
            else char = EMPTY;

            row.push(char);
        }

        tat.print(row.join(''));
        prevRow = row;
        await sleep(DELAY);
    }
})();

</script>




<script>// SCROLL CODE:Connected Pipes Squarish
running = true;

// Main loop
(async function main() {
    let e = document.getElementById('outputTextarea2') || document.getElementById('outputTextarea');
    e.style.lineHeight = '1';
    const tat = new Tatjs(e);


    // Constants for settings:
    const DELAY = 200;  // Pause after each row in milliseconds.
    const WIDTH = 200;

    // This setting changes the behavior to create the "long vertical style" if greater than 0.0:
    const VERTICAL_STYLE_FACTOR = 0.0;  // Set between 0.0 and 1.0 // SQUARISH HAS THIS SET TO 0.0

    // Constants for printed characters:
    const UP_DOWN_CHAR = String.fromCharCode(9474);  // Character 9474 is '│'
    const LEFT_RIGHT_CHAR = String.fromCharCode(9472);  // Character 9472 is '─'
    const DOWN_RIGHT_CHAR = String.fromCharCode(9484);  // Character 9484 is '┌'
    const DOWN_LEFT_CHAR = String.fromCharCode(9488);  // Character 9488 is '┐'
    const UP_RIGHT_CHAR = String.fromCharCode(9492);  // Character 9492 is '└'
    const UP_LEFT_CHAR = String.fromCharCode(9496);  // Character 9496 is '┘'
    const UP_DOWN_RIGHT_CHAR = String.fromCharCode(9500);  // Character 9500 is '├'
    const UP_DOWN_LEFT_CHAR = String.fromCharCode(9508);  // Character 9508 is '┤'
    const DOWN_LEFT_RIGHT_CHAR = String.fromCharCode(9516);  // Character 9516 is '┬'
    const UP_LEFT_RIGHT_CHAR = String.fromCharCode(9524);  // Character 9524 is '┴'
    const CROSS_CHAR = String.fromCharCode(9532);  // Character 9532 is '┼'
    const EMPTY = ' ';

    // The previous printed row; initialize to up-left-right characters:
    let prevRow = Array(WIDTH).fill(UP_LEFT_RIGHT_CHAR);

    while (running) {

        let row = [];  // Character strings to print in this row.
        for (let i = 0; i < WIDTH; i++) {
            let prevChar = prevRow[i];
            let leftConnect, upConnect, downConnect, rightConnect;

            // Figure out if we need to connect the left side:
            leftConnect = i > 0 && "─┌└├┬┴┼".includes(row[i - 1]);

            // Figure out if we need to connect the up side:
            upConnect = "│┌┐├┤┬┼".includes(prevChar);

            // The downward and right side connection can be either:
            downConnect = Math.random() < 0.5;

            if (i == WIDTH - 1) {
                if (!upConnect && !downConnect && leftConnect && !rightConnect) {
                    // Make this a left-down pipe:
                    downConnect = true;
                } else if (!upConnect && downConnect && !leftConnect && !rightConnect) {
                    // Make this an empty space:
                    downConnect = false;
                } else if (upConnect && !downConnect && !leftConnect && !rightConnect) {
                    // Make this an up-down pipe:
                    downConnect = true;
                }
            } else {
                rightConnect = Math.random() < 0.5;
            }

            // Override rightConnect value if VERTICAL_STYLE_FACTOR is greater than 0.0:
            if (Math.random() < VERTICAL_STYLE_FACTOR) {
                rightConnect = false;
            }

            let char;
            // Get the character to print based on the connections to the four other sides:
            if (upConnect && downConnect && leftConnect && rightConnect) char = CROSS_CHAR;
            else if (upConnect && downConnect && leftConnect) char = UP_DOWN_LEFT_CHAR;
            else if (upConnect && downConnect && rightConnect) char = UP_DOWN_RIGHT_CHAR;
            else if (upConnect && downConnect) char = UP_DOWN_CHAR;
            else if (upConnect && leftConnect && rightConnect) char = UP_LEFT_RIGHT_CHAR;
            else if (upConnect && leftConnect) char = UP_LEFT_CHAR;
            else if (upConnect && rightConnect) char = UP_RIGHT_CHAR;
            else if (upConnect) char = Math.random() < 0.5 ? UP_DOWN_CHAR : UP_RIGHT_CHAR;  // Randomly end or continue the line upwards
            else if (downConnect && leftConnect && rightConnect) char = DOWN_LEFT_RIGHT_CHAR;
            else if (downConnect && leftConnect) char = DOWN_LEFT_CHAR;
            else if (downConnect && rightConnect) char = DOWN_RIGHT_CHAR;
            else if (downConnect) char = DOWN_RIGHT_CHAR;  // Force the line to go down and to the right
            else if (leftConnect && rightConnect) char = LEFT_RIGHT_CHAR;
            else if (leftConnect) char = Math.random() < 0.5 ? LEFT_RIGHT_CHAR : DOWN_LEFT_CHAR;  // Randomly end or bend the line leftwards
            else if (rightConnect) char = DOWN_RIGHT_CHAR;  // Force the line to go down and to the right
            else char = EMPTY;

            row.push(char);
        }

        tat.print(row.join(''));
        prevRow = row;
        await sleep(DELAY);
    }
})();

</script>
