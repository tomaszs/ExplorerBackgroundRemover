
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

## How to Auto-Start the Script with Windows

You can configure the script to start automatically with Windows using one of the following methods:

### **Method 1: Using Task Scheduler**

1. **Open Task Scheduler**:
   - Press `Win + S`, type `Task Scheduler`, and press Enter.

2. **Create a New Task**:
   - Click **Action** → **Create Task**.
   - In the **General** tab:
     - Enter a name (e.g., `Background Remover`).
     - Check **Run with highest privileges**.
     - Select **Configure for: Windows 10/11**.

3. **Set the Trigger**:
   - Go to the **Triggers** tab and click **New**.
   - Choose **At startup** or another desired trigger (e.g., logon).

4. **Set the Action**:
   - Go to the **Actions** tab and click **New**.
   - Select **Start a program**.
   - Browse to your Python executable (e.g., `C:\Python39\python.exe`).
   - In the **Add arguments (optional)** field, enter:
     ```plaintext
     "C:\path\to\background_remover.py"
     ```
   - Replace `C:\path\to\background_remover.py` with the full path to your script.

5. **Finish and Test**:
   - Save the task and restart your computer to ensure the script starts automatically.

### **Method 2: Using a Batch File**

1. **Create a Batch File**:
   - Open Notepad and paste the following:
     ```plaintext
     @echo off
     python "C:\path\to\background_remover.py"
     ```
   - Replace `C:\path\to\background_remover.py` with the full path to your script.
   - Save the file as `background_remover.bat` (e.g., on your Desktop).

2. **Add to Startup Folder**:
   - Press `Win + R`, type `shell:startup`, and press Enter.
   - Copy your `background_remover.bat` file into the Startup folder.
   - The script will now start automatically whenever you log in.

### **Method 3: Using NSSM (Non-Sucking Service Manager)**

1. **Download NSSM**:
   - Go to [nssm.cc/download](https://nssm.cc/download) and download the appropriate version for your system.

2. **Install the Service**:
   - Extract the NSSM archive and open Command Prompt as Administrator.
   - Navigate to the extracted NSSM folder and run:
     ```bash
     nssm install BackgroundRemover
     ```
   - In the GUI:
     - **Path**: Browse to your Python executable (e.g., `C:\Python39\python.exe`).
     - **Arguments**: Enter the path to your script:
       ```plaintext
       "C:\path\to\background_remover.py"
       ```
     - **Startup directory**: Set to the folder containing the script.

3. **Start the Service**:
   - Run:
     ```bash
     nssm start BackgroundRemover
     ```
   - The script will now run as a Windows service and start with Windows.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
