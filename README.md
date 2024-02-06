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
   git clone https://github.com/themattwilliams/date_printer.git
   ```
2. **Install `pyautogui`:**
   ```
   pip install pyautogui
   ```

## Convert Script to Executable

To convert the `date_printer.py` script into an executable file for easier distribution and usage, follow these steps:

1. **Install PyInstaller:**
   ```
   python.exe -m pip install pyinstaller
   ```

2. **Navigate to Your Script's Directory:**
   Ensure you're in the directory containing your `date_printer.py` script.

3. **Create the Executable:**
   Use Python to call PyInstaller, specifying the `--onefile` and `--noconsole` options to create a single executable without a console window:
   ```
   python.exe -m PyInstaller --onefile --noconsole .\date_printer.py
   ```
   This command generates the executable in the `dist` directory within your script's folder.

## Usage

After converting `date_printer.py` to an executable, you can run it directly without needing to open Python or a terminal. Simply double-click the executable or assign it to a shortcut with a custom key combination for quick access.

## Customization

The script includes a predefined delay of 0.01 seconds before typing the date, designed for almost instantaneous action. This delay can be adjusted by editing the `time.sleep(0.01)` line in `date_printer.py`, though for most use cases, the default setting should suffice.

## Contributing

Contributions to improve the script or its documentation are warmly welcomed! Feel free to submit pull requests or open issues to suggest enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
