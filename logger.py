from interfaces.ilogger import ILogger
from interfaces.writer import Writer
from interfaces.timestamp_provider import TimestampProvider
from enums.level_enum import LogLevel
from singleton import Singleton
import threading


class Logger(Singleton, ILogger):
    """Потокобезопасный логгер с поддержкой смены стратегии записи."""

    _lock = threading.Lock()

    def __init__(self, writer: Writer):
        """Инициализирует логгер с заданной стратегией записи."""
        self.writer = writer

    def set_writer(self, writer: Writer):
        """Устанавливает новую стратегию записи для логгера."""
        self.writer = writer

    def _format_message(self, level: str, message: str) -> str:
        """Форматирует сообщение с временной меткой и уровнем логирования."""
        return f"{TimestampProvider.get_timestamp_in_message()} [{level}] {message}"

    def log(self, level: LogLevel, message: str):
        """Логирует сообщение с указанным уровнем, используя текущую стратегию записи."""
        formatted_message = self._format_message(level.value, message)
        with self._lock:
            self.writer.write(formatted_message)
