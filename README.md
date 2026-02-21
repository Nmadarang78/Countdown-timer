# Simple Python Countdown

A minimalist CLI tool to run a countdown timer from a user-specified `mm:ss` format.

## How it Works

The script converts your input into total seconds and uses a `while` loop to decrement the time. To keep the interface clean, it uses the carriage return (`\r`) symbol to overwrite the current line in your terminal rather than printing a new one every second.

## Key Features

* **`divmod()`**: Efficiently calculates minutes and remaining seconds in one line.
* **F-String Formatting**: `:02d` ensures a professional two-digit look (e.g., `05:09`).
* **Zero Dependencies**: Uses only the built-in `time` library.

## Requirements

* Python 3.x
* Any standard terminal/command prompt.
