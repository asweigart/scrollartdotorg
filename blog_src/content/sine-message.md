Title: Sine Message
Date: 2024-03-04 10:04
Authors: Al Sweigart
Summary: <a href="{filename}sine-message.md">Text moving in a sine wave pattern. Click here to view the animation...<br><img src="{static}/images/sine-message-screenshot.webp" class="scrollArtPreview"></a>
og_image: sine-message-screenshot.webp
og_description: Text moving in a sine wave pattern.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/sine-message-screenshot.webp" style="display: none;">


**[VIEW FULLSCREEN](/static/sinemessage-fullscreen.html)**

<div><textarea id="outputTextarea" readonly class="tatjsOutput" style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>


"Sine Message" is a simple text message that moves in a sine wave across the screen. The message, scroll speed, and wave speed are customizeable.

* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/sinemessage.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/sinemessage.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/edoq7pu6/)

<script src="/static/textarea_terminal.js"></script><link rel="stylesheet" href="/static/textarea_terminal.css">
<script>// SCROLL CODE:SineMessage
const tat = new Tatjs(document.getElementById('outputTextarea'));

const DELAY = 100;
let width = 120;
let running = true;

const MESSAGE = 'Hello, world!';
const STEP_INCREASE = 0.004;


async function main() {
    let step = 0.0;
    while (running) {
        let multiplier = (width - MESSAGE.length) / 2;
        let padding = ' '.repeat(Math.floor((Math.sin(step * (180 / Math.PI)) + 1) * multiplier));
        tat.print(padding + MESSAGE);
        step += STEP_INCREASE;
        await sleep(DELAY);
    }
}

main();
</script>
