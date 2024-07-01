Title: Starfield on the Apple IIe
Category: Misc
Date: 2024-04-04 10:00
Authors: Al Sweigart
Summary: <a href="{filename}apple-iie-starfield.md">The term "scroll art" is new but these text-based programs don't require modern computers. Here is a video of the Starfield program running on a 1983 Apple IIe.<br><img src="{static}/images/apple-iie-starfield.webp" class="scrollArtPreview"></a>
og_image: proton-stream-screenshot.webp
og_description: The term "scroll art" is new but these text-based programs don't require modern computers. Here is a video of the Starfield program running on a 1983 Apple IIe.

<!-- For some reason, we need this image otherwise the screenshot in the Summary won't appear. I have display: none because I don't want the image to show up in the page. -->
<img src="{static}/images/apple-iie-starfield.webp" style="display: none;">

The term "scroll art" is new but these text-based programs don't require modern computers. Here is a video of the Starfield program (ported to [Applesoft BASIC](https://en.wikipedia.org/wiki/Applesoft_BASIC)) running on a 1983 [Apple IIe](https://en.wikipedia.org/wiki/Apple_IIe). This is the benefit of scroll art for learning to code: the concepts are simple enough that they can be applied to any programming language and any computer, even those from nearly a half-century ago!

The computer is an Apple IIe, though the monitor connected to it is from a [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64) at the [Recurse Center](https://en.wikipedia.org/wiki/Recurse_Center). The source code for the program appears at the beginning after the LIST command is run. This program is running at full speed with no inserted delays! The diagonal color stripe is not a part of the program; it's a "rolling bar" artifact of the CRT display and [flickering](https://en.wikipedia.org/wiki/Flicker_(screen)) that you don't see with the naked eye but appears when you record the CRT screen.

<video width="360" height="640" controls class="scrollArtPreview">
    <source src="{static}/images/apple-iie-starfield.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

Joshua Bell has written [an Applesoft BASIC emulator](https://www.calormen.com/jsbasic/) online that you can try out in your browser without installing anything.

Here is the BASIC source code:

```
5 HOME
10 CHANGE = 0.05
20 DENSITY = 0
30 WIDTH = 39
40 IF DENSITY < 0 OR DENSITY > 1 THEN CHANGE = -CHANGE
50 DENSITY = DENSITY + CHANGE
60 ROW$ = ""
70 FOR I = 1 TO WIDTH
80 IF RND(1) < DENSITY THEN GOTO 92
90 ROW$ = ROW$ + " "
91 GOTO 100
92 ROW$ = ROW$ + "*"
100 NEXT I
110 PRINT ROW$
120 GOTO 40
```

