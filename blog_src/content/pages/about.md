Title: About
Date: 2024-03-04 10:00
Modified: 2024-03-04 10:00
Authors: Al Sweigart
Summary: About the SAM.

The Scroll Art Museum is an online gallery of "scroll art." Scroll art is a form of [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) where a program generates output in a command line terminal. Once the terminal window fills up, it begins to scroll the text upwards. This is used to create an animated effect. The SAM is a collection of several scroll art examples.

The benefit of scroll art is that beginner programmers can create scroll art apps with a minimal amount of experience. <b>Scroll art requires knowing only the programming concepts of `print()`, looping, and variables.</b> Every programming langauge has these features, so <b>scroll art can be created in any programming language</b> without installing additional software libraries. You don't have to learn heavy abstract coding concepts or limit yourself to boring interest rate calculations.

Many scroll art programs are under a couple dozen lines long. Here's the Python source code for "Starfield":

    # Press Ctrl-C to stop the program.
    import random, time, os

    change_amount = 0.5  # How fast the density changes.
    density = 0.0

    while True:
        width = os.get_terminal_size()[0] - 1
        if density < 0 or density > 100:
            change_amount *= -1  # Reverse the density direction.
        density = density + change_amount

        line = ''  # Create the line of asterisks.
        for i in range(width):
            if random.randint(0, 100) < density:
                line = line + '*'  # Add an asterisk.
            else:
                line = line + ' '  # Add an empty space.

        print(line)
        time.sleep(0.02)

You can look at the infinitely generated output on the [Starfield exhibit page]({filename}/starfield.md) or this excerpt here:

```
   *                            *                                              
  *  *             *           *  *                                  *        *
   **   *  *                                  *      *  *    ** *              
 *            **     *                       *          *         *   *      **
 *  * *** * *   *                    *             *                     *     
                      * *    *     ***       * ** **   *  **    *     *        
    * ** *     *  **       *     *                 * * * ** *  *   *  *        
  *     *        ** *      *   *      *   *            *        **  **   ** *  
   *    *  ** *   *  *           *** *       *     *** *       * *        **  *
 ***  *  ****  * *          **   *  *   ** *       *       *     *  *** *    **
 * *     * *  * *  ***  ****   * *  *****      **** * *    *  *  **     * ** * 
      * *  *   *   *  ***  ***          ***    **  *   *    **  *    ****  ****
    ** ***** * ******* *  ** * *  *** **  ***  *  *    *         **  *   ****  
  ** **  ** *  ***  **   ***** *** * **    *   ***    * **** ***    ****  * * *
** *  ****   * *  *  *** **** ** ***   ***  **** **    *  ***** * * * *** * ** 
* * *  ***   **  *   ** *   ***     *******  * *  *  * *  * ***  * *  **** *  *
*  *  *** ** *** ** * * ****   **  * ***********  ***   *** ** **** ** ********
  ** ** **** * **  *** * ** ***  * **   * ******   ***    *** ** ******** *****
**** ***    **** ******* ****** ***** *   ******** *****  ***   *  ****  ***** 
*  ***** ****** ****** **** ** * ****   ** ** **  ** ****   *  * ******* ***** 
**** * * **    ****** *** * **** ******** * ****** ** * ** *************** * **
*** ********** **** *** *** *** *** * ******* ******** * * ***** ****** ** ****
*** *** ** ***** **** *** * ****  ***** * **** *** ** ** ************* ***  ***
***** ** ********** ************* * *** ***** ** ***  * ******* *****  ***** **
*********** * ********** ***  ********** *** ************* **** ** ******* ****
***** ** ****  ***************** ******* * ** ***************** ***************
************************************** ***** **********************************
*******************************************************************************
*******************************************************************************
******** ****** **************************** ***** ***************** * ********
**  ******* ***** *********** ****************************** ******* **********
* ***************** ***** ***************** ******* ******************** ******
 ********** ** ********** *** * ******************* ******* *******************
***** ******** *** **** ** * * **  *  * * *** * ********* *********************
* ***** *** ****** * **** ** ************ ****** ***** ****  ******* ********* 
 **** *   **** * ** ********  * ** ** ** * ** *** ***  ********** ************ 
**  *   **** **     **** **  *****   ****** * ****** ****   ****   * * * ******
 ** * * ***  **   * *** ***  *****  *  ****  * ******** **   ****  *** ******* 
* ** * *  **** * ** **************** ** *  ***    *  ************ *** ****** **
***  * **    * ** *****   **  * **** ***    **** *  *****  * *   * ** **  **** 
  *    * ******* * * * *****   **  *  * *   * *** ***** **  *** ****   *  * * *
   * *   * * *  * *  *     *   *          * ** *  ******   *** **  ** ******  *
  *** **   * **   ***     ****  ***   *  *    **** *   ** **  **  *  ****  ** *
*******   **** *     *  * ** ****  ** **** *   *** ***  ** **  *      *  **   *
*   *    * *        *   ** *     * *  * * ***      ***** * * * ** *  **** *  * 
  *      * * *        **   * * **  **    * *    *    *  ** **   *         * ** 
******   * ** *  * ****  *   ****    ** *  * * *  **** ****  **** * * *  * *  *
 *    *   *  **  *      *  * *** ******    *****  * **  ** * *    **    *      
 *  **    *   *  *    *  * *     * **   ***   * * *  **  **  *  *              
*** *    *  * * *    *    *  *    * * *     * *  **         **    * *  * * **  
**  **    ****  * **  **    * *  **     *  *  * *         *   **  * *  *   *   
                      *     *      * *   *    *            *             *     
  *               *        *          *    **    *      *  *       *    * *  * 
 *        *                  * *         *           *   *    *    *        *  
         *     *                      *    *                *           **     
       *                         *              *                   **         
                                                       *     *                 
```



What Are the Limitations of Scroll Art?
=======================================

Scroll art creates the illusion of movement and the infinite. Scroll art "animation" is just a byproduct of the window scrolling old text up as new text is printed. It's the same as if you were manually scrolling down a text file in a word processor. Any text produced by a `print()` call cannot be erased, it can only be pushed upwards as new text is printed. But the programs that produce scroll art are designed to run forever and produce an infinite amount of text.

Scroll art's animation isn't the same as the animation of most computer graphics that redraws the screen or flip books that have a series of images. But there is still a wide variety of possible scroll art programs to write. The constraints of scroll art form a garden for creativity.

Scroll art is an idea that isn't dependent on modern computers. All of the scroll art at the SAM could be recreated on 1970s and 1980s personal computers.


Who is Al Sweigart?
===================

Al Sweigart coined the term "scroll art" and is the curator of [scrollart.org](https://scrollart.org). He has written several programming books for beginners, including [Automate the Boring Stuff with Python](https://automatetheboringstuff.com). All of his books are freely available under a Creative Commons license at [https://inventwithpython.com](https://inventwithpython.com). His [The Big Book of Small Python Projects]() has several "scroll art" animated works, which he later expanded upon to create "scroll art" and the SAM.


