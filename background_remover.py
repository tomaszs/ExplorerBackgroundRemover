import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rembg import remove
import ctypes
import platform


class BackgroundRemovalHandler(FileSystemEventHandler):
    def on_created(self, event):
        """Handle folder creation events."""
        print(f"Detected event: {event.src_path} (is_directory={event.is_directory})")
        if event.is_directory:
            folder_name = os.path.basename(event.src_path)
            if folder_name.lower() == "without background":
                parent_dir = os.path.dirname(event.src_path)
                print(f"'without background' folder detected at: {event.src_path}")
                process_images(parent_dir, event.src_path)

    def on_moved(self, event):
        """Handle folder rename events."""
        print(f"Detected rename/move: {event.src_path} -> {event.dest_path}")
        if event.is_directory:
            folder_name = os.path.basename(event.dest_path)
            if folder_name.lower() == "without background":
                parent_dir = os.path.dirname(event.dest_path)
                print(f"'without background' folder detected after rename at: {event.dest_path}")
                process_images(parent_dir, event.dest_path)


def process_images(source_dir, target_dir):
    """
    Processes all images in the source_dir and saves the background-removed versions in the target_dir.
    """
    print(f"Processing images from: {source_dir} to: {target_dir}")
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            print(f"Processing: {filename}")
            try:
                with open(file_path, 'rb') as input_file:
                    input_image = input_file.read()
                    output_image = remove(input_image)
                output_path = os.path.join(target_dir, filename)
                with open(output_path, 'wb') as output_file:
                    output_file.write(output_image)
                print(f"Saved processed image: {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


def is_admin():
    """Check if the script is running with administrative privileges."""
    if platform.system() == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        return os.geteuid() == 0
    return False


def run_as_admin():
    """Re-run the script with administrative privileges."""
    if platform.system() == "Windows":
        print("Restarting script with admin privileges...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        print("Please run this script with sudo.")
        sys.exit()


def monitor_folders(path):
    """Monitor the file system for folder creation and rename events."""
    print(f"Monitoring path: {path}")
    event_handler = BackgroundRemovalHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
    try:
        monitor_folders("/")
    except Exception as e:
        print(f"Error starting folder monitor: {e}")
