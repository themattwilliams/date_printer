# This script requires pyautogui. Install it via pip if you haven't: pip install pyautogui
import pyautogui
import time
from datetime import datetime

def type_date_with_underscores():
    # Format today's date with underscores
    formatted_date = datetime.now().strftime('_%Y_%m_%d')
    
    # Wait for a short period to switch to the target application
    time.sleep(.001)  # Adjust this delay as needed

    # Type out the date string where the cursor is located
    pyautogui.typewrite(formatted_date)

if __name__ == "__main__":
    type_date_with_underscores()
