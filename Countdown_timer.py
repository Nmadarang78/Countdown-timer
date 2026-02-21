import time

def countdown_timer():
    # Loop until we get valid input
    while True:
        user_input = input("Enter time (mm:ss): ")
        
        try:
            # Check for the colon and convert to integers
            if ":" not in user_input:
                raise ValueError
                
            minutes, seconds = map(int, user_input.split(':'))
            
            # Optional: Ensure seconds aren't 60 or more
            if seconds >= 60:
                print("Seconds must be less than 60.")
                continue
                
            total_seconds = minutes * 60 + seconds
            break  # Exit the input loop if successful
            
        except ValueError:
            print("Invalid format! Please enter numbers as mm:ss (e.g., 01:30).")

    # The Countdown Loop
    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!      ")

if __name__ == "__main__":
    countdown_timer()