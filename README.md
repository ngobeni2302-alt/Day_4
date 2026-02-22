# Day_4
How to use input() in Python

**Definition**

- **`input(prompt=None)`**: Built-in function that reads a line of text from standard input and returns it as a `str`. If `prompt` is provided, it is written to standard output before reading. If end-of-file (no more input) is reached before any data is read, `input()` raises `EOFError`.

**Line-by-Line Explanation for [input.py](input.py#L1-L24)**

- **Line 1:** `n = "What will you do ?"` : Assigns a string to the variable `n`.
- **Line 2:** `t = "Rebuild it"` : Assigns a string to `t`.
- **Line 3:** `s = "Just the way it was, brick for brick"` : Assigns a string to `s`.
- **Line 4:** `a = "Why do we fall sir?"` : Assigns a string to `a`.
- **Line 5:** `k = "So that we can learn to pick ourselves up"` : Assigns a string to `k`.
- **Line 6:** `o = "You still haven't given up on me"` : Assigns a string to `o`.
- **Line 7:** `p = "Never!"` : Assigns the stop-marker string to `p`.
- **Line 8:** `print(n)` : Prints the value of `n` to standard output.
- **Line 10-12 (comment):** Explains intended behavior: read inputs until the final marker `p` is entered and print each input only once (ignore duplicates). Note: the code's comment says to print inputs once, but the implementation does not actually print the user inputs.
- **Line 13:** `stop_marker = p` : Sets `stop_marker` to the string stored in `p`. This is the value that will stop the input loop when entered.
- **Line 14:** `seen = set()` : Creates an empty `set` named `seen` used to track which input lines have already been seen (to ignore duplicates).
- **Line 16:** `try:` : Starts a `try` block to catch `EOFError` when there is no more input.
- **Line 17:** `while True:` : Begins an infinite loop that will keep reading input until broken.
- **Line 18:** `user = input()` : Calls `input()` to read one line from standard input and stores the returned string in `user`. This call will raise `EOFError` if input ends.
- **Line 19:** `if user in seen:` : Checks whether this `user` string has already been seen.
- **Line 20:** `continue` : If `user` was seen before, skip the rest of the loop and read the next line (this prevents duplicate processing).
- **Line 21:** `seen.add(user)` : Adds the new `user` string to the `seen` set so future duplicates are detected.
- **Line 22:** `if user == stop_marker:` : Compares the read string to the stop-marker value.
- **Line 23:** `break` : If the stop-marker was entered, break out of the loop and stop reading further input.
- **Line 24-25:** `except EOFError:\n    pass` : When end-of-file is reached (no more input), the `EOFError` is caught and ignored so the program exits cleanly.

**Notes & Observations**

- The code ignores duplicate inputs by using the `seen` set.
- Although the comment says "Print each input only once", the code does not actually call `print()` for the user inputs; it only prints `n` at the start. To print each unique input, a `print(user)` should be added after `seen.add(user)` (and before the `if user == stop_marker:` check, or adjusted as desired).
- `input()` returns strings — if you need numeric values, convert them explicitly (for example, `int(input())`).

If you want, I can also update `input.py` to print each unique input (or adjust the stop behavior). Would you like me to make that change?
