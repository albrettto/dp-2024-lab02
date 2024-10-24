from log_strategy import LogStrategy
from singleton import Singleton
import threading

class Logger(Singleton):
    _lock = threading.Lock()

    def __init__(self, log_strategy: LogStrategy):
        self.log_strategy = log_strategy

    def set_log_strategy(self, log_strategy: LogStrategy):
        self.log_strategy = log_strategy

    def set_file_path(self, file_path: str):
        self.log_strategy.set_file_path(file_path)

    def _format_message(self, level: str, message: str) -> str:
        return f"{LogStrategy.get_timestamp()} [{level}] {message}"

    def log(self, level: str, message: str):
        formatted_message = self._format_message(level, message)
        with self._lock:
            self.log_strategy.write(formatted_message)