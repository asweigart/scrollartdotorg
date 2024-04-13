Title: Contribute
Date: 2024-03-04 10:00
Modified: 2024-03-04 10:00
Authors: Al Sweigart
Summary: How to contribute your scroll art to the SAM.

Currently the Scroll Art Museum only has pieces from Al Sweigart. Email him with your contributions: <a href="mailto:al@inventwithpython.com">al@inventwithpython.com</a>. The SAM is meant to feature scroll art from many artists.


What is the Format for Contributions to the SAM?
=================================================

First, you should provide a GitHub link to your program or another website where the source code generally lives so viewers can always find the latest version. Second, you should provide a way to show sample output on the SAM web page.

Ideally, your program would be written in JavaScript and use [BextJS](https://github.com/asweigart/bextjs) which provides Python-style `print()`, `sleep()`, and `input()` functions. This provides a way to easily show the generated output on the Scroll Art Museum website.

However, you could also simply send a couple thousand rows of your program's output at a width of at most 220 columns. The SAM web page will feature it in this scrolling text JavaScript template code:

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>TITLE GOES HERE</title>
      <style>body { font-family: monospace; }</style>
    </head>
    <script>
    var scrollToBottomInterval = null;

    function scrollToBottom() {
        var scrollSpeedSlider = document.getElementById('scrollSpeedSlider');
        var scrollSpeedValues = {
            "1": 20, // Very Slow
            "2": 15, // Slow
            "3": 8  // Fast
        };
        scrollToBottomInterval = setInterval(function() {
            // Calculate how much the page has been scrolled
            var scrollHeight = document.documentElement.scrollHeight;
            var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            var clientHeight = document.documentElement.clientHeight;

            // If we haven't reached the bottom yet, scroll down by 10 pixels
            if (scrollTop + clientHeight < scrollHeight) {
                window.scrollBy(0, 20); // Scroll down by 20 pixels
                scrollHeight = document.documentElement.scrollHeight; // update scrollHeight setting
            } else {
                // If we reached the bottom, clear the interval
                clearInterval(scrollToBottomInterval);
            }
        }, scrollSpeedValues[scrollSpeedSlider.value] * 10);
    }

    // Stop scrolling when ESC key is pressed
    document.addEventListener('keydown', function(event) {
        if (event.key === "Escape") {
            clearTimeout(scrollToBottomInterval);
        }
    });

    // Stop scrolling when user manually scrolls
    window.addEventListener('wheel', function() {
        clearTimeout(scrollToBottomInterval);
    });

    // Stop scrolling when user uses arrow keys
    window.addEventListener('keydown', function(event) {
        if (event.key.startsWith("Arrow")) {
            clearTimeout(scrollToBottomInterval);
        }
    });
    </script>
    <body><label for="scrollSpeedSlider">Speed</label><input type="range" min="1" max="3" value="2" id="scrollSpeedSlider"> <button id="scrollButton" onclick="scrollToBottom()">Auto Scroll</button>
    <div style="white-space: pre; line-height: 1em;">

    ! ! ! ! ! SCROLL ART GOES HERE ! ! ! ! !
    
    </div></body></html>


