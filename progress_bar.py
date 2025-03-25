from datetime import datetime
from time import sleep

progressPreviousCall = -1
progressNumberOfCall = 0


def progressReset():
    """
    Resets the progress tracking variables to their initial states.

    This function should be called before starting a new progress tracking 
    sequence to ensure accurate progress calculations.
    """
    global progressPreviousCall, progressNumberOfCall
    progressPreviousCall = -1
    progressNumberOfCall = 0


def progress(numberOfCalls: int, message: str = "Progress"):
    """
    Displays a dynamic progress bar in the terminal.

    Args:
        numberOfCalls (int): The total number of expected calls to this function. 
                             Used to calculate progress percentage.
        message (str): A message to display alongside the progress bar. 
                       Messages longer than 25 characters will be truncated.

    The progress bar shows:
        - A truncated message (up to 25 characters).
        - The current progress percentage.
        - A progress bar of 50 characters.
        - Estimated time remaining (ETA).

    Example:
        >>> for i in range(100):
        >>>     progress(100, message="Processing")
        >>>     sleep(0.1)
    """
    global progressPreviousCall, progressNumberOfCall
    progressNumberOfCall += 1
    now = datetime.now()

    # Calculate percentage of progress
    percentage = int(progressNumberOfCall / numberOfCalls * 100)
    percentage_str = f"{percentage}%"

    # Generate the progress bar visualization (max length: 50)
    per50 = int(progressNumberOfCall / numberOfCalls * 50)
    progressBar = "█" * per50

    # Truncate message if it exceeds the maximum length of 25 characters
    if len(message) > 25:
        message = message[:22] + "..."

    # Estimate Time Remaining (ETA) calculation
    eta = "N/A"
    if progressPreviousCall != -1 and progressNumberOfCall != numberOfCalls:
        timeSinceLastCall = now - progressPreviousCall
        eta_duration = timeSinceLastCall * (numberOfCalls - progressNumberOfCall)
        seconds = eta_duration.seconds
        minutes = seconds // 60
        milliseconds = int(eta_duration.microseconds / 1000)

        if minutes >= 1:
            eta = f"{minutes}m"
            seconds -= minutes * 60
            if seconds >= 1:
                eta += f"{seconds:02d}s"
        elif seconds >= 1:
            eta = f"{seconds}s"
            if milliseconds > 0:
                eta += f"{milliseconds:03d}ms"
        elif milliseconds >= 1:
            eta = f"{milliseconds:03d}ms"
        else:
            eta = str(eta_duration)

    # Update the time of the previous call for ETA calculation
    progressPreviousCall = now

    # Print progress bar
    print(f"{message:<25} | {percentage_str:<4} | {progressBar:<50} | {eta:<20}", end="\r")


if __name__ == "__main__":
    # Example usage
    for i in range(10):
        progress(10, message="Message")
        sleep(0.1)

    for i in range(90):
        progress(100, message="A too long message that will be cropped")
        sleep(0.1)

    print()  # Move to the next line after the progress bars
