import time

def countdown_timer():
    # Get user input for mm:ss
    user_input = input("Enter the time in mm:ss format: ")
    
    try:
        minutes, seconds = map(int, user_input.split(':'))
        total_seconds = minutes * 60 + seconds
    except ValueError:
        print("Invalid format. Please use mm:ss (e.g., 02:30)")
        return

    print(f"Timer started for {user_input}...")

    while total_seconds >= 0:
        # Calculate minutes and seconds for the display
        mins, secs = divmod(total_seconds, 60)
        
        # Format the time as 00:00
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # The '\r' allows us to overwrite the same line in the console
        print(timer_display, end="\r")
        
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!      ") # Extra spaces to clear the old numbers

if __name__ == "__main__":
    countdown_timer()