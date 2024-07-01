Title: Towers and Towers    
Date: 2024-07-02 10:00
Modified: 2024-07-02 10:00
Authors: Al Sweigart
Summary: <a href="{filename}towers-and-twoers.md">XX.<br><img src="{static}/images/towers-and-towers-screenshot.webp" style="max-width: 640px;"></a>
og_image: towers-and-towers-screenshot.webp
og_description: XX

<img src="{static}/images/towers-and-towers-screenshot.webp" style="max-width: 640px;">

DESCRIPTIONXX


* **[VIEW FULLSCREEN](/static/towers-and-towers-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/towersandtowers.py)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/XX/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
let running = true;
const WIDTH = process.stdout.columns - 1;
const DELAY = 7.5;  // in milliseconds
const AFTER_TOWER_DELAY = 750;  // in milliseconds

const EMPTY_CHAR = ' ';
const CORNER_CHAR = '+';
const TOP_CHAR = '-';
const SIDE_CHAR = '|';
const INTERIOR_CHARS = ':|. ';

const MIN_TOWER_WIDTH = 8;
const MAX_TOWER_WIDTH = 20;

const MIN_TOWER_HEIGHT = 4;
const MAX_TOWER_HEIGHT = 17;

const TOWER_HEIGHT_MAX_DIFF = 8;

const WIPE_AFTER = 8;

let step = 1;
let columns = Array(WIDTH).fill(EMPTY_CHAR);

async function main() {
    while (running) {
        if (step % WIPE_AFTER === 0) {
            for (let i = 0; i < 60; i++) {
                console.log();
                await sleep(DELAY);
            }
            await sleep(AFTER_TOWER_DELAY);
            columns = Array(WIDTH).fill(EMPTY_CHAR);
        }

        // Tower 1 top (tower 1 is slightly higher than tower 2):
        let tower1_left = Math.floor(Math.random() * ((WIDTH / 2) - MAX_TOWER_WIDTH));
        let tower1_width = Math.floor(Math.random() * (MAX_TOWER_WIDTH - MIN_TOWER_WIDTH + 1)) + MIN_TOWER_WIDTH;
        columns[tower1_left] = CORNER_CHAR;
        columns[tower1_left + tower1_width] = CORNER_CHAR;
        for (let i = tower1_left + 1; i < tower1_left + tower1_width; i++) {
            columns[i] = TOP_CHAR;
        }

        console.log(columns.join(''));
        await sleep(DELAY);

        // Tower 1 top body that is above tower 2's top:
        columns[tower1_left] = SIDE_CHAR;
        columns[tower1_left + tower1_width] = SIDE_CHAR;
        let interior_char = INTERIOR_CHARS[step % INTERIOR_CHARS.length];
        for (let i = tower1_left + 1; i < tower1_left + tower1_width; i++) {
            columns[i] = interior_char;
        }

        for (let i = 0; i < Math.floor(Math.random() * TOWER_HEIGHT_MAX_DIFF); i++) {
            console.log(columns.join(''));
            await sleep(DELAY);
        }

        // Tower 2 top:
        let tower2_left = Math.floor(Math.random() * (WIDTH - MAX_TOWER_WIDTH));
        let tower2_width = Math.floor(Math.random() * (MAX_TOWER_WIDTH - MIN_TOWER_WIDTH + 1)) + MIN_TOWER_WIDTH;
        columns[tower2_left] = CORNER_CHAR;
        columns[tower2_left + tower2_width] = CORNER_CHAR;
        for (let i = tower2_left + 1; i < tower2_left + tower2_width; i++) {
            columns[i] = TOP_CHAR;
        }

        console.log(columns.join(''));
        await sleep(DELAY);

        // Tower 2 body (and 1):
        columns[tower2_left] = SIDE_CHAR;
        columns[tower2_left + tower2_width] = SIDE_CHAR;
        interior_char = INTERIOR_CHARS[step % INTERIOR_CHARS.length];
        for (let i = tower2_left + 1; i < tower2_left + tower2_width; i++) {
            columns[i] = interior_char;
        }

        for (let i = 0; i < Math.floor(Math.random() * (MAX_TOWER_HEIGHT - MIN_TOWER_HEIGHT + 1)) + MIN_TOWER_HEIGHT; i++) {
            console.log(columns.join(''));
            await sleep(DELAY);
        }

        await sleep(AFTER_TOWER_DELAY);
        step += 1;
    }
}

main();

</script>
