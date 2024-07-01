Title: Create
Date: 2024-03-04 10:00
Modified: 2024-03-04 10:00
Authors: Al Sweigart
Summary: A brief guide to designing scroll art programs.

Writing scroll art programs only requires cursory amounts of programming knowledge. The inspiration for new scroll art programs comes from understanding the space and limitations that your program's output lives in. The programs in this article are written in Python. If you'd like an introduction to programming for complete beginners, I recommend reading my book, [Automate the Boring Stuff with Python](https://automatetheboringstuff.com) which is freely available under a Creative Commons license.

Design Tips
===========

This website is under development, but here's some tips for your scroll art programs:

* Most of your programs won't be that good or interesting, so focus on producing a lot of small, simple programs rather than one one "grand idea."

* Remember that you can't erase lines once printed, and that text only scrolls upwards.
Linux and macOS can show emoji characters, but Windows is limited to the characters in the [Windows Glyph List 4](https://en.wikipedia.org/wiki/Windows_Glyph_List_4) set.

* Remember that scroll art uses a monospace font.

* Scroll art programs tend to be short. If yours is over a hundred lines long, you may be overthinking it.

* The text/ASCII look lowers expectations, so don't be afraid to be simple or subtle.

* You can control scroll speed/timing: fast, slow, varying

* Try to stick to the standard library so your audience doesn't need to install additional modules to run your programs.

* Try to keep the program in a single source code file so it can be easily copy/pasted and shared on sites like [Pastebin](https://pastebin.com).

* Scroll art makes for great practice if you are learning a new programming language. Try to recreate scroll art you've seen or made before.

* Scroll art can be infinitely long.

* Static tessellations are kind of boring. Randomness creates non-repeating patterns.

* Increasing and decreasing density (like in [Starfield]({filename}/starfield.md)) is a useful trick.

* The output of your scroll art program can be written to a text file if you like.

* Have the program detect the width of the terminal (like `os.get_terminal_size()[0]` in Python) so it adjusts itself automatically.

* Re-check the terminal width, in case the user resizes it while the program runs.

* Use constants or command-line arguments for easy configuring: width, rows, speed, etc.

* A constant width setting is useful if you are writing the output to a text file.

* Your program should support infinite or finite mode.

* If finite, have it end at the end of a "period" or "cycle" of the scrolling pattern.

* Pressing Ctrl-C stops terminal programs.

* It's best to show the credits (your name and an email or website) at the end 

* Hexagons are easy to draw: Use slashes and underscores.

* The vertical pipe | character tends to look ugly.

* Use the _ underscore (not - dash) for horizontal lines.

* Keep it simple at first: Add color and emoji later.

* Use . periods instead of spaces for visibility.

* Consider using [emoji](https://en.wikipedia.org/wiki/Emoji) or the [box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character) in the output of your programs.

* Characters I commonly use: _ / \ . : , ; * # @ O 0 ( ) [ ] { } < > ~ ╲ ╱ ╳ │ ─ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼



Where to Look for Inspiration
============================

* Do an image search for [tessellations](https://duckduckgo.com/?t=ffab&q=tessellations&iax=images&ia=images), [cellular automata](https://duckduckgo.com/?q=cellular+automata&t=ffab&iar=images&iax=images&ia=images) (including [1D cellular automata](1D cellular automata)), [geometric art](https://duckduckgo.com/?q=geometric+art&t=ffab&iar=images&iax=images&ia=images), [geometric icons](https://duckduckgo.com/?q=geometric+icons&t=ffab&iar=images&iax=images&ia=images), [isometric art](https://duckduckgo.com/?q=isometric+art&t=ffab&iar=images&iax=images&ia=images), and [Islamic art](https://duckduckgo.com/?q=islamic+art&t=ffab&iar=images&iax=images&ia=images).

* Don't forget to set the image search settings [from "All colors" to "Black and white"](https://duckduckgo.com/?q=tessellations&t=ffab&iar=images&iax=images&ia=images&iaf=color%3AMonochrome) or [from "All types" to "Line drawing"](https://duckduckgo.com/?q=tessellations&t=ffab&iar=images&iax=images&ia=images&iaf=color%3AMonochrome).

* Look at the history of ASCII art ([Wikipedia](https://en.wikipedia.org/wiki/ASCII_art)) and look through [some examples](https://github.com/asweigart/asciiartjsondb/blob/main/asciiartdb-asciiarteu.txt). ASCII art is the computer era version of typewriter art: ["A Visual History of Typewriter Art from 1893 to Today"](https://www.themarginalian.org/2014/05/23/typewriter-art-laurence-king/), ["Looking Back on 100 Years of Typewriter Art"](https://hyperallergic.com/242249/looking-back-on-100-years-of-typewriter-art/)

* Download and run [FIGlet](https://en.wikipedia.org/wiki/FIGlet), a popular program for creating lettered banners such as this: 

```
 _____ ___ ____ _      _   
|  ___|_ _/ ___| | ___| |_ 
| |_   | | |  _| |/ _ \ __|
|  _|  | | |_| | |  __/ |_ 
|_|   |___\____|_|\___|\__|
```


JSFiddle Template
==================


Here is a template preloaded with the [BextJS](https://github.com/asweigart/bextjs) code so that you can create your own scroll art in the browser with the [JSFiddle.net](https://jsfiddle.net) JavaScript sandbox:

[BextJS Template: https://jsfiddle.net/asweigart/5skyrhc1/](https://jsfiddle.net/asweigart/5skyrhc1/)

BextJS provides a `print()` function to print strings to the &lt;textarea&gt; element and a `sleep()` function to pause for a certain number of milliseconds. Note thtat you must put the `await` keyword in front of every `sleep()` function call.

On the JSFiddle site, scroll down the HTML area until you find the **`// !!!! INSERT YOUR SCROLL ART PROGRAM CODE BELOW !!!!`** comment and place your JavaScript code there. The above BextJS template currently preloaded with some short "Hello, world!" code. You can replace this with your own scroll art code experiments and not have to worry about getting a programming environment set up on your computer.

All of the scroll art featured on this website have a "JavaScript source code in JSFiddle" link to JSFiddle preloaded with their code, so you can make experiment with changes and view the results in the browser.
