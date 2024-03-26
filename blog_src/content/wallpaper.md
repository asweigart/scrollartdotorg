Title: Wallpaper
Date: 2024-03-23 10:00
Modified: 2024-03-23 10:00
Authors: Al Sweigart
Summary: <a href="{filename}wallpaper.md">The standard wallpaper scroll art, including several designs and tessellations.<br><img src="{static}/images/wallpaper-screenshot.webp" style="max-width: 640px;"></a>
og_image: wallpaper-screenshot.webp
og_description: The standard wallpaper scroll art, including several designs and tessellations.

<img src="{static}/images/wallpaper-screenshot.webp" style="max-width: 640px;">

This piece is based on programs in my free programming book, [*The Big Book of Small Python Projects*](https://inventwithpython.com/bigbookpython/): [*Project 35 - Hex Grid*](https://inventwithpython.com/bigbookpython/project35.html) and [*Project 65 - Shining Carpet*](https://inventwithpython.com/bigbookpython/project65.html). The "wallpaper" style of scroll art displays a static, forever-repeating pattern. While the simplicty makes it less exciting than other forms of scroll art, it is approachable and forces creativity in design. The same short program can display any wallpaper pattern. You only need to change the wallpaper data:

    import time

    DELAY = 0.4
    WIDTH = 80

    wallpaper_rows = [  # Change as desired; All rows must be the same length.
        r'_ \ \ \_/ __',
        r' \ \ \___/ _',
        r'\ \ \_____/ ',
        r'/ / / ___ \_',
        r'_/ / / _ \__',
        r'__/ / / \___',
    ]

    x_repeat = WIDTH // len(wallpaper_rows[0])

    while True:
        # Display each row in wallpaper_rows:
        for row in wallpaper_rows:
            print(row * x_repeat)
            time.sleep(DELAY)

The above produces the hexagon pattern of the carpet in the Overlook Hotel in the 1980 movie, *The Shining*:

    _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
     \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
    \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ 
    / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
    _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
    __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___
    _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
     \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
    \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ 
    / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
    _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
    __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___
    _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
     \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _

By changing the `wallpaper_rows` array...

    wallpaper_rows = [  # Change as desired; All rows must be the same length.
        r'\__   ',
        r'/  \__',
        r'\     ',
        r'/   __',
        r'\__/  ',
        r'/     ',
    ]

...you create a brand new wallpaper:

    \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   
    /  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__
    \     \     \     \     \     \     \     \     \     \     \     \     \     
    /   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __
    \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  
    /     /     /     /     /     /     /     /     /     /     /     /     /     
    \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   \__   
    /  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__
    \     \     \     \     \     \     \     \     \     \     \     \     \     
    /   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __/   __
    \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  
    /     /     /     /     /     /     /     /     /     /     /     /     /     

Tessellations are a natural pattern to create wallpaper scroll art. An [internet image search for "tessellations"](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images) can provide inspiration, especially if you change the search settings to [Line Drawing](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images&iaf=type%3Aline) or [Black and White](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images&iaf=color%3AMonochrome).

The wallpaper program exhibited here contains several different wallpaper patterns which you can select by changing the `WALLPAPER` constant to one of the dictionary key values in the `WALLPAPERS_PATTERNS` variable.

(It was working on these tessellations that made me learn of a bug in Python where raw strings cannot end with a backslash, even if escaped.)

* **[VIEW FULLSCREEN](/static/wallpaper-fullscreen.html)**
* [Python source code](https://github.com/asweigart/scrollart/blob/main/python/wallpaper.py)
* [JavaScript source code in JSFiddle](https://jsfiddle.net/asweigart/7x15u60w/)

<div><textarea id="bextOutput" readonly style="height: 400px;"></textarea><br /><button type="button" onclick="running = !running;">&#x23FB; Off</button>
<button type="button" onclick=""></button>
</div>

<script src="/static/bext.js"></script><link rel="stylesheet" href="/static/bext.css">
<script>


</script>
