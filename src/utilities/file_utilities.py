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

from utilities.transcribe import TranscribeData

from app_logger import get_mem_logger

class FileUtils:

    def __init__(self, path, file, output_format, model_size, output_path, format):
        self.logger = get_mem_logger()
        self.path = path
        self.file = file
        self.output_format = output_format
        self.model_size = model_size
        self.output_path = output_path
        self.format = format

    # ==========================================
    # TO SUPPORT BATCH PROCESSING PIPELINE - streaming pub sub would work too - don't read the dir just add this to your sub handler func
    # ==========================================
    def read_directory(self):
        try:
        
            current_dir = Path(__file__).resolve().parent
            print(current_dir)
          
            self.logger.info(f"Start traverse directory")
            path = Path(self.path)
            
            if not path.is_dir():
                print(f"Error: '{self.path}' is not a valid directory.")
                return

            path.walk() 
            for root, dirs, files in path.walk():
                for file in files:
                    #**** TODO this is not going to work with docx, excel, md, etc right now.  might work with txt and other simple ascii utf-8 type stuff.
                    if file.lower().endswith(self.format):
                        try:
                            #**** TODO this is hard coded to transcribe an mp3 right now.  but this is the 'hub' right now long term want a dispatcher so can have 
                            # and Abstract Class Factory pattern.
                            full_file_path = (root / file).resolve()
                            kwargs = {
                                "path": r"data/mp3s",
                                "file": str(full_file_path),
                                "output_format": "md",
                                "model_size": "base",
                                "output_path": r"data/output"
                            }
                            # kwargs["file"] = file
                            transcribe = TranscribeData(**kwargs)
                            transcribe.initalize_model()
                            transcribe.process_audio_file()
                            print(f"-> Successfully saved transcribed\n")
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
        "file": r"C:\Users\<yourusername>\source\ai_thread_mem_save_reload\data\mp3s\Heart_Wisdom-HH_Dalai_Lama-Heart_Sutra_pt1-051701.mp3",
        "output_format": "md",
        "model_size": "base",
        "output_path": r"data/output",
        "format": ".mp3"
    }
    fileio = FileUtils(**kwargs)
    result = fileio.read_directory()

    
    