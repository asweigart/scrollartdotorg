Title: Proton Stream
Date: 2024-03-23 10:00
Authors: Al Sweigart
Summary: <a href="{filename}proton-stream.md">Lightning streams from a ghost exterminator's device. Click here to view the animation...<br><img src="{static}/images/proton-stream-screenshot.webp" class="scrollArtPreview"></a>
og_image: proton-stream-screenshot.webp
og_description: Lightning streams from a ghost exterminator's device.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/proton-stream-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/proton-stream-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>


Multiple streams that are always within a set range of each other.

Links
=====

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/protonstream.py)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/7amoxbzg/)

<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Proton Stream
const tat = new Tatjs(document.getElementById('outputTextarea'));

let running = true;

// Constants for settings:
const DELAY = 10;  // Pause after each row in milliseconds.
const WIDTH = 60;  // Number of columns in output.
const NUM_STREAMS = 5;  // Number of streams on the screen.
const MAX_DISTANCE = NUM_STREAMS * 4;  // How many spaces streams must be within each other.
const MOVE_CHANCE = 0.75;  // How often a stream tries to move left or right, rather than continue straight.

const EMPTY_CHAR = ' ';
const STREAM_CHARS = 'oO@';

let streams = Array(NUM_STREAMS).fill(Math.floor(WIDTH / 2));


(async function main() {
    while (running) {
        let columns = Array(WIDTH).fill(EMPTY_CHAR);

        streams.forEach((stream, i) => {
            if (Math.random() < MOVE_CHANCE) {
                // Move stream:
                if (Math.random() < 0.5) { // Adjusting for bias
                    if (stream > 0 && streams.every(other => Math.abs((stream - 1) - other) <= MAX_DISTANCE)) {
                        // Move stream left:
                        streams[i] -= 1;
                    }
                } else {
                    if (stream < WIDTH - 1 && streams.every(other => Math.abs((stream + 1) - other) <= MAX_DISTANCE)) {
                        // Move stream right:
                        streams[i] += 1;
                    }
                }
            }

            columns[stream] = STREAM_CHARS[i % STREAM_CHARS.length];
        });

        /*
        // Eh, sparks just don't make it look that good.
        // Add sparks:
        if (Math.random() < SPARK_CHANCE) {
            // Find range where sparks can appear:
            const leftmostSparkColumn = Math.max(0, Math.min(...streams) - SPARK_RANGE);
            const rightmostSparkColumn = Math.min(WIDTH - 1, Math.max(...streams) + SPARK_RANGE);

            // Add sparks:
            Array.from({length: randomNumSparks()}, () => Math.floor(Math.random() * (rightmostSparkColumn - leftmostSparkColumn + 1) + leftmostSparkColumn))
                 .forEach(x => {
                     if (!STREAM_CHARS.includes(columns[x])) {  // Don't overlap a stream with a spark
                         columns[x] = SPARK_CHARS[Math.floor(Math.random() * SPARK_CHARS.length)];
                     }
                 });
        }
        */

        tat.print(columns.join(''));
        await sleep(DELAY);
    }
})();


</script>
