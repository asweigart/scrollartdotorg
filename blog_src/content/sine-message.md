Title: Sine Message
Date: 2024-03-04 10:04
Modified: 2024-03-04 10:04
Authors: Al Sweigart
Summary: <a href="{filename}sine-message.md">Text moving in a sine wave pattern.<br><img src="{static}/images/sine-message-screenshot.webp" style="max-width: 640px;"></a>
og_image: sine-message-screenshot.webp
og_description: Text moving in a sine wave pattern.

<img src="{static}/images/sine-message-screenshot.webp" style="max-width: 640px;">

"Sine Message" is a simple text message that moves in a sine wave across the screen. The message, scroll speed, and wave speed are customizeable.

* **[VIEW FULLSCREEN](/static/sinemessage-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/sinemessage.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/sinemessage.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/edoq7pu6/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
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
        print(padding + MESSAGE);
        step += STEP_INCREASE;
        await sleep(DELAY);
    }
}

main();
</script>
