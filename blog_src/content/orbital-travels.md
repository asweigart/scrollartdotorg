Title: Orbital Travels    
Date: 2024-04-11 10:00
Authors: Al Sweigart
Summary: <a href="{filename}orbital-travels.md">A collection of random points moving in sine waves. Click here to view the animation...<br><img src="{static}/images/orbital-travels-screenshot.webp" class="scrollArtPreview"></a>
og_image: orbital-travels-screenshot.webp
og_description: A collection of random points moving in sine waves.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/orbital-travels-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/orbital-travels-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>

Several of my attempts to make scroll art are built off of complex ideas and complicated code that produce mediocre results. Orbital Travels was an absurdly simple idea that turned into one of my favorite pieces of scroll art: show multiple characters moving back and forth in a sine wave at different rates. The results delighted me. They reminded me the helix picture of an orbiting moon as it follows the Earth. With a fixed Earth, the moon's orbit looks circular. But when you follow the movement of the Earth, you can see that the Moon is actually moving in a helix path. I decided to name this piece Orbital Travels.

Links
=====


* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/orbitaltravels.py)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/eLhmxy9g/)


<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:Orbital Travels
const tat = new Tatjs(document.getElementById('outputTextarea'));
const DELAY = 50;
let WIDTH = 120;
let running = true;
const ALL_CHARS = '@O0o*.,vV';
const EMPTY = ' ';
let CHARS = [];
let SINE_STEP_INCS = [];
let sine_steps = [];
for (let i = 0; i < Math.floor(Math.random() * 8) + 7; i++) {
    CHARS.push(ALL_CHARS[Math.floor(Math.random() * ALL_CHARS.length)])
    SINE_STEP_INCS.push(Math.random() * 0.1 + 0.0001)
    sine_steps.push(Math.random() * Math.PI);
}
async function main() {
    while (running) {
        let row = Array(WIDTH).fill(EMPTY);
        for (let i = 0; i < CHARS.length; i++) {
            row[Math.floor((Math.sin(sine_steps[i]) + 1) / 2 * WIDTH)] = CHARS[i];
            sine_steps[i] += SINE_STEP_INCS[i];
        }
        tat.print(row.join(''));
        await tat.sleep(DELAY);
    }
}
main();
</script>
