Title: Ducklings
Date: 2024-03-04 10:04
Modified: 2024-03-04 10:04
Authors: Al Sweigart
Summary: <a href="{filename}ducklings.md">Cute combinatorial explosion of ASCII art ducks.<br><img src="{static}/images/ducklings-screenshot.webp" style="max-width: 640px;"></a><br>

<img src="{static}/images/ducklings-screenshot.webp" style="max-width: 640px;">

"Ducklings" generates a wide variety of duckling ASCII art. The ducklings have multiple possible directions (left or right), eyes (aloof, happy, or wide), bills (open or closed), wing direction (out, up, or down), and body size (chubby and very chubby) for 24 different styles.

* **[VIEW FULLSCREEN](/static/ducklings-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/ducklings.py)
* [TypeScript source code (compiles to Node JavaScript)](https://github.com/asweigart/scrollart/blob/main/typescript/ducklings.ts)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/o4sgvucn/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button></div>
<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>

bextRowBuffer = 256;  // Change this to whatever size you want, or -1 for infinite buffer.
const DELAY = 150;
let width = 220;
const DENSITY = 0.10;
const DUCKLING_WIDTH = 5;
let running = true;

class Duckling {


    constructor() {
        this.direction = ['LEFT', 'RIGHT'][Math.floor(Math.random() * 2)];
        this.bill = ['CLOSED', 'OPEN'][Math.floor(Math.random() * 2)];
        this.body = ['CHUBBY', 'VERY_CHUBBY'][Math.floor(Math.random() * 2)];
        this.wing = ['DOWN', 'OUT', 'UP'][Math.floor(Math.random() * 3)];

        if (this.body == 'CHUBBY') {
            // Chubby ducklings can only have beady eyes.
            this.eyes = 'BEADY';
        } else {
            this.eyes = ['ALOOF', 'HAPPY', 'WIDE'][Math.floor(Math.random() * 3)];
        }

        this.nextBodypart = 'HEAD';
    };

    getHeadStr() {
        let headStr = '';
        if (this.direction === 'LEFT') {
            // Get the bill:
            if (this.bill === 'OPEN') {
                headStr += '>';
            } else if (this.bill === 'CLOSED') {
                headStr += '=';
            }

            // Get the eyes:
            if (this.eyes === 'BEADY' && this.body === 'CHUBBY') {
                headStr += '"';
            } else if (this.eyes === 'BEADY' && this.body === 'VERY_CHUBBY') {
                headStr += '" ';
            } else if (this.eyes === 'WIDE') {
                headStr += "''";
            } else if (this.eyes === 'HAPPY') {
                headStr += '^^';
            } else if (this.eyes == 'ALOOF') {
                headStr += '``';
            }

            headStr += ') '; //  Back of the left-facing head.
        } else if (this.direction === 'RIGHT') {
            headStr += ' (';  // Back of the right-facing head.

            // Get the eyes:
            if (this.eyes === 'BEADY' && this.body === 'CHUBBY') {
                headStr += '"';
            } else if (this.eyes === 'BEADY' && this.body === 'VERY_CHUBBY') {
                headStr += ' "';
            } else if (this.eyes === 'WIDE') {
                headStr += "''";
            } else if (this.eyes === 'HAPPY') {
                headStr += '^^';
            } else if (this.eyes == 'ALOOF') {
                headStr += '``';
            }

            // Get the bill:
            if (this.bill === 'OPEN') {
                headStr += '<';
            } else if (this.bill === 'CLOSED') {
                headStr += '=';
            }
        }

        if (this.body === 'CHUBBY') {
            // Get an extra space so chubby ducklings are the same width as very chubby ducklings.
            headStr += ' ';
        }

        return headStr;
    }

    getBodyStr() {
        let bodyStr = '(';
        if (this.direction === 'LEFT') {
            // Get the interior body space:
            if (this.body === 'CHUBBY') {
                bodyStr += ' ';
            } else if (this.body === 'VERY_CHUBBY') {
                bodyStr += '  ';
            }

            // Get the wing:
            if (this.wing === 'OUT') {
                bodyStr += '>';
            } else if (this.wing === 'UP') {
                bodyStr += '^';
            } else if (this.wing === 'DOWN') {
                bodyStr += 'v';
            }
        } else if (this.direction === 'RIGHT') {
            // Get the wing:
            if (this.wing === 'OUT') {
                bodyStr += '<';
            } else if (this.wing === 'UP') {
                bodyStr += '^';
            } else if (this.wing === 'DOWN') {
                bodyStr += 'v';
            }
            
            // Get the interior body space:
            if (this.body === 'CHUBBY') {
                bodyStr += ' ';
            } else if (this.body === 'VERY_CHUBBY') {
                bodyStr += '  ';
            }
        }

        bodyStr += ')';

        if (this.body === 'CHUBBY') {
            // Get an extra space so chubby ducklings are the same width as very chubby ducklings.
            bodyStr += ' ';
        }

        return bodyStr;
    }

    getFeetStr() {
        if (this.body === 'CHUBBY') {
            return ' ^^  ';
        } else if (this.body === 'VERY_CHUBBY') {
            return ' ^ ^ ';
        } else {
            return '';
        }
    }

    getNextBodyPart() {
        if (this.nextBodypart === 'HEAD') {
            this.nextBodypart = 'BODY';
            return this.getHeadStr();
        } else if (this.nextBodypart === 'BODY') {
            this.nextBodypart = 'FEET';
            return this.getBodyStr();
        } else if (this.nextBodypart === 'FEET') {
            this.nextBodypart = 'DONE';
            return this.getFeetStr();
        }
    }
}


async function main() {
    let ducklingLanes = Array.from({length: (Math.floor(width / DUCKLING_WIDTH))}, () => null);

    while (running) {
        let line = '';
        for (let laneNum = 0; laneNum < ducklingLanes.length; laneNum++) {
            let ducklingObj = ducklingLanes[laneNum];
            if (ducklingLanes[laneNum] === null && Math.random() < DENSITY) {
                // Place a new duckling in this lane:
                ducklingObj = new Duckling();
                ducklingLanes[laneNum] = ducklingObj;
            }

            if (ducklingObj !== null) {
                line += ducklingObj.getNextBodyPart();
                // Delete the duckling if we've finished drawing it:
                if (ducklingObj.nextBodypart == 'DONE') {
                    ducklingLanes[laneNum] = null;
                }
            } else {
                // Draw five spaces since there is no duckling in this lane:
                line += ' '.repeat(DUCKLING_WIDTH);
            }
        }
        print(line);
        await sleep(DELAY);
    }
}

main();
</script>