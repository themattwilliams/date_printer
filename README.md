```
# Date Typer Script

This Python script allows for automatic typing of today's date in the format `YYYY_MM_DD` (e.g., `2024_02_06`), making it perfect for appending dates to file names, note titles, or any other naming convention that requires a standardized date format. By utilizing `pyautogui`, the script simulates keyboard input to type the date string into any active application after a brief delay, facilitating seamless integration into your workflow.

## Features

- **Automatic Date Formatting:** Outputs the date in `YYYY_MM_DD` format.
- **Customizable Delay:** Adjust the delay to switch to the target application before typing.
- **Global Shortcut Execution:** Instructions included for setting up a Windows shortcut to run the script with a key combination.

## Prerequisites

- Python 3.x installed on your system.
- `pyautogui` library installed.

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/date-typer-script.git
   ```
2. **Install `pyautogui`:**
   ```
   pip install pyautogui
   ```

## Usage

1. Save the `type_date.py` script to a preferred location on your computer.
2. Create a shortcut on Windows to run the script:
    - Right-click on the desktop or in a folder and choose `New` > `Shortcut`.
    - Set the location to your Python executable followed by the script path. Example:
      ```
      C:\path\to\python.exe C:\path\to\type_date.py
      ```
    - Complete the shortcut wizard.
3. Assign a shortcut key via the shortcut properties:
    - Right-click the shortcut, select `Properties`, then the `Shortcut` tab.
    - Click in the `Shortcut key` box and press your desired key combination.
    - Click `OK` to save your settings.
4. Press the assigned shortcut key, switch to the target application within the delay period, and the script will type today's date.

## Customization

To adjust the delay before the script types the date, edit the `time.sleep(5)` line in `type_date.py`, replacing `5` with your preferred delay in seconds.

## Contributing

Contributions to enhance the script or its documentation are welcome! Please feel free to submit pull requests or open issues to discuss potential improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
