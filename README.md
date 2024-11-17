# Background Remover

A Python script to monitor your system for specific folder creation or renaming events, such as creating a folder named `without background`, and automatically processes images in the parent folder to remove their backgrounds.

## Features
- Monitors the entire system for folder creation or renaming events.
- Automatically processes images in the parent folder when a `without background` folder is created or renamed.
- Uses [rembg](https://github.com/danielgatis/rembg) for background removal.

## Requirements
- Python 3.8 or newer
- Administrator/root privileges to monitor the entire file system

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/background-remover.git
   cd background-remover
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have administrator/root privileges:
   - **Windows**: Run the script in an Administrator Command Prompt.
   - **Linux/Mac**: Run with `sudo`.

## Usage
Run the script as follows:
```bash
python background_remover.py
```

The script monitors the entire file system for the creation or renaming of a folder named `without background`. When detected:
1. It processes all images (`.png`, `.jpg`, `.jpeg`, `.bmp`) in the parent folder.
2. Saves the background-removed images in the `without background` folder.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
