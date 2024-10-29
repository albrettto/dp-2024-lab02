from abc import ABC, abstractmethod
from interfaces.timestamp_provider import TimestampProvider


class FilePathManager(ABC):
    """Интерфейс для управления путями к файлам логов."""

    @abstractmethod
    def set_file_path(self, file_path: str):
        """Устанавливает путь к файлу для записи логов."""
        pass

    @staticmethod
    def get_filename() -> str:
        """Генерирует имя файла лога с текущей временной меткой."""
        return f"DP.P1.{TimestampProvider.get_timestamp_in_filename()}.log"
