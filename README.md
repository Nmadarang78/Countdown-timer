# Simple Python Countdown

A minimalist CLI tool to run a countdown timer from a user-specified `mm:ss` format.

## How it Works

The script converts your input into total seconds and uses a `while` loop to decrement the time. To keep the interface clean, it uses the carriage return (`\r`) symbol to overwrite the current line in your terminal rather than printing a new one every second.

## The Code

```python
import time

def timer(user_input):
    # Split "02:30" into [2, 30] and convert to total seconds
    m, s = map(int, user_input.split(':'))
    total = m * 60 + s

    while total >= 0:
        # Format seconds back into 00:00 display
        mins, secs = divmod(total, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        
        time.sleep(1)
        total -= 1
    
    print("Time's up!      ")

# Usage
timer(input("Enter time (mm:ss): "))

```

## Key Features

* **`divmod()`**: Efficiently calculates minutes and remaining seconds in one line.
* **F-String Formatting**: `:02d` ensures a professional two-digit look (e.g., `05:09`).
* **Zero Dependencies**: Uses only the built-in `time` library.

## Requirements

* Python 3.x
* Any standard terminal/command prompt.
