from pathlib import Path
from datetime import datetime
from faster_whisper import WhisperModel
from docx import Document
import os
import sys
from pathlib import Path

from app_logger import get_mem_logger


# Class names chosen based on likely libs that are going to be imported so don't call the wrong func due to type ahead etc
class TranscribeData:

    def __init__(self, path, file, output_format, model_size, output_path):
        self.logger = get_mem_logger()
        self.path = path
        self.file = file
        self.output_format = output_format
        self.model_size = model_size
        self.output_path = output_path
        self.shared_model = None
        self.initalize_model()

    def initalize_model(self):
        # 2. INITIALIZE MODEL ONCE (Outside the loop)
        print(f"[{datetime.now().strftime('%T')}] Loading Faster-Whisper '{self.model_size}' model onto GPU...")
        self.logger.info(f"[{datetime.now().strftime('%T')}] Loading Faster-Whisper '{self.model_size}' model onto GPU...")

        # Register NVIDIA cuBLAS and cuDNN DLLs inside .venv for Windows
        venv_nvidia = Path(sys.prefix) / "Lib" / "site-packages" / "nvidia"
        for sub in ("cublas", "cudnn"):
            bin_dir = venv_nvidia / sub / "bin"
            if bin_dir.exists():
                os.add_dll_directory(str(bin_dir))
                os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ["PATH"]

        
        # compute_type="int8" is optimal for GTX 1050 (Pascal / sm_61) GPUs
        self.shared_model = WhisperModel(
            self.model_size,
            device="cuda",
            compute_type="int8"
        )
        
        print(f"[{datetime.now().strftime('%T')}] Model loaded successfully. Starting batch...")
        self.logger.info(f"[{datetime.now().strftime('%T')}] Model loaded successfully. Starting batch...")

    # ==========================================
    # THE BATCH PROCESSING PIPELINE
    # ==========================================
    def process_audio_file(self):
        try:
            # faster-whisper returns a generator for segments and an info object
            segments, info = self.shared_model.transcribe(self.file, beam_size=5)
            detected_language = info.language

            def format_timestamp(seconds: float) -> str:
                mins, secs = divmod(int(seconds), 60)
                hours, mins = divmod(mins, 60)
                return f"{hours:02d}:{mins:02d}:{secs:02d}"

            self.output_format = self.output_format.lower().strip(".")

            # Ensure output directory exists and build full .md file path
            out_dir = Path(self.output_path)
            out_dir.mkdir(parents=True, exist_ok=True)
            base_filename = Path(self.file).stem
            output_file = out_dir / f"{base_filename}.md"

            self.logger.info(f"[{datetime.now().strftime('%T')}] Begin transcription and write output...")
            
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# Transcript: {base_filename}\n\n")
                f.write(f"- **Language:** {detected_language}\n\n")
                
                # Transcription runs on the GPU as each segment is yielded here
                for seg in segments:
                    timestamp = format_timestamp(seg.start)
                    text = seg.text.strip()
                    print(f"[{timestamp}] {text}")  # Replaces verbose=True progress output
                    f.write(f"**[{timestamp}]** {text}\n\n")

            self.logger.info(f"[{datetime.now().strftime('%T')}] Model Finished Transcription")
            print(f"-> Successfully saved transcript to: {output_file}\n")
            self.logger.info(f"[{datetime.now().strftime('%T')}] Successfully saved transcript to: {output_file}")

            '''# Export to Word Doc
            elif self.output_format in ["doc", "docx"]:
                output_file = out_dir / f"{base_filename}.docx"
                doc = Document()
                doc.add_heading(f"Transcript: {base_filename}", level=1)
                for seg in segments:
                    p = doc.add_paragraph()
                    p.add_run(f"[{format_timestamp(seg.start)}] ").bold = True
                    p.add_run(seg.text.strip())
                doc.save(output_file)'''

        except Exception as e:
            self.logger.info(f"Shit just failed {e}")
            print(f"Shit just failed {e}")


# Example usage:
if __name__ == "__main__":
    kwargs = {
        "path": r"data/mp3s",
        "file": r"C:\Users\<yourusername>\source\ai_thread_mem_save_reload\data\mp3s\Heart_Wisdom-HH_Dalai_Lama-Heart_Sutra_pt1-051701.mp3",
        "output_format": "md",
        "model_size": "base",
        "output_path": r"data/output"
    }
    transcribe = TranscribeData(**kwargs)
    transcribe.process_audio_file()
