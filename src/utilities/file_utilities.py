from pathlib import Path
import sys
import os
import whisper
from docx import Document
from datetime import datetime
import os
import glob
import whisper
from docx import Document
from datetime import datetime
import torch


current_dir = Path(__file__).resolve().parent
print(current_dir)
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

from app_logger import get_logger

#****** TODO: This shits broken - don't try to use it!*****
class FileUtils:

    def __init__(self, path, file, shared_model, output_format, model_size, output_path):
        self.logger = get_logger()
        self.path = path
        self.file = file
        self.shared_model = shared_model
        self.output_format = output_format
        self.model_size = model_size
        self.output_path = output_path


    

    # ==========================================
    # THE BATCH PROCESSING PIPELINE
    # ==========================================
    def process_audio_directory(self):
        try:

            current_dir = Path(__file__).resolve().parent
            print(current_dir)
          
            self.logger.info(f"Start <print_mp3_files> will add sophitication as i go babysteps")
            path = Path(self.path)
            
            # Check if the path exists and is a directory
            if not path.is_dir():
                print(f"Error: '{self.path}' is not a valid directory.")
                return

            # path.walk() efficiently steps through the directory tree
            # for root, dirs, files in path.walk():
            # for file in files:
                    # Check the file extension case-insensitively
            #        if file.lower().endswith('.mp3'):
            
            
            try:
                # you gotta call the transcibe class in the loop or call a worker thread?  can you thread a decent gpu?  do you need to?  idfk.
                print(f"-> Successfully saved transcript to: {saved_at}\n")
            except Exception as e:
                print(f"[ERROR] Failed to process {os.path.basename(self.path)}: {str(e)}\n")

            print("Batch processing complete.")
        except Exception as e:
            self.logger.info(f"Shit just failed {e}")
            print(f"Shit just failed {e}")


# Example usage:
# print_mp3_files("/path/to/your/music/folder")

if __name__ == "__main__":
    kwargs = {
        "path": r"data/mp3s",
        "file" : None,
        "shared_model":  None,
        "output_format":  "md",
        "model_size": "base",
        "output_path": r"data/output"
    }
    fileio = FileUtils(**kwargs)
    result = fileio.process_audio_directory()