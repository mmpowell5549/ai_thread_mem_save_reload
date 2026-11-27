import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


class AppLogger:
    """A thread-safe centralized logging class supporting console and rotating file outputs."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        # Ensure a strict Singleton pattern across all modules
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(
        self, log_dir: str = "logs", log_level: int = logging.INFO
    ) -> None:
        if self._initialized:
            return

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Standardized log format
        self.log_format = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Configure Root Logger
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(log_level)

        # Clear any existing default handlers to avoid duplicate logs
        if self.root_logger.hasHandlers():
            self.root_logger.handlers.clear()

        self._setup_handlers()
        self._initialized = True

    def _setup_handlers(self) -> None:
        """Configures console output and a rotating file log system."""
        # 1. Streams to the standard system terminal output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.log_format)
        self.root_logger.addHandler(console_handler)

        # 2. Automatically rolls over logs when file size hits 5MB
        file_handler = RotatingFileHandler(
            filename=self.log_dir / "app.log",
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8",
        )
        file_handler.setFormatter(self.log_format)
        self.root_logger.addHandler(file_handler)


def get_mem_logger() -> logging.Logger:
    """The central calling function.

    Automatically resolves the calling module's identity dynamically using Python
    3.13's stack inspect rules.
    """
    # Initialize the core singleton parameters (safe to re-call)
    AppLogger()

    # Walk back up the execution stack frame to find who invoked this function
    current_frame = sys._getframe()
    calling_frame = current_frame.f_back

    # If invoked directly from a raw shell environment or missing frame
    if not calling_frame:
        return logging.getLogger("app")

    # Extract the module name property safely
    module_name = calling_frame.f_globals.get("__name__", "app")
    return logging.getLogger(module_name)
