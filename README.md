# Date Printer Script

This Python script facilitates the automatic typing of today's date prefixed with an underscore and formatted as `YYYY_MM_DD` (e.g., `_2024_02_06`). It's designed to seamlessly integrate into workflows requiring dates to be appended to file names, note titles, or any other naming conventions that benefit from a standardized date format. Utilizing `pyautogui`, the script simulates keyboard input, typing the date string into any active application with a minimal delay, making it ideal for quick file renaming or note-taking.

## Features

- **Prefixed Date Formatting:** Automatically outputs the date in `_YYYY_MM_DD` format, ideal for appending to existing file names or titles.
- **Minimal Delay:** Set to 0.01 seconds to quickly switch to the target application and type the date.
- **Ease of Use:** Can be run using a Windows shortcut with a custom key combination for fast access.

## Prerequisites

- Python 3.x installed on your system.
- `pyautogui` library installed.

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/date_printer.git
   ```
2. **Install `pyautogui`:**
   ```
   pip install pyautogui
   ```

## Usage

1. Save the `date_printer.py` script to a preferred location on your computer.
2. Adjust the script to set the desired delay (already set to 0.01 seconds for immediate action) and ensure the date format includes the leading underscore.
3. Create a shortcut on Windows to run the script:
    - Right-click on the desktop or in a folder and choose `New` > `Shortcut`.
    - Set the location to your Python executable followed by the script path. Example:
      ```
      C:\path\to\python.exe C:\path\to\date_printer.py
      ```
    - Complete the shortcut wizard.
4. Assign a shortcut key via the shortcut properties:
    - Right-click the shortcut, select `Properties`, then the `Shortcut` tab.
    - Click in the `Shortcut key` box and press your desired key combination.
    - Click `OK` to save your settings.
5. When you press the assigned shortcut key, the script will immediately activate, allowing you to switch to the target application where the script will type today's date.

## Customization

The script includes a predefined delay of 0.01 seconds before typing the date, designed for almost instantaneous action. This delay can be adjusted by editing the `time.sleep(0.01)` line in `date_printer.py`, though for most use cases, the default setting should suffice.

## Contributing

Contributions to improve the script or its documentation are warmly welcomed! Feel free to submit pull requests or open issues to suggest enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
