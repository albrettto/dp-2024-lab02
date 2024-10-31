from abc import ABC, abstractmethod
from interfaces.writer import Writer


class ILogger(ABC):
    """Интерфейс для логгера, определяющий основные методы для настройки и записи логов."""

    @abstractmethod
    def set_writer(self, writer: Writer):
        """Устанавливает стратегию записи логов."""
        pass

    @abstractmethod
    def log(self, level: str, message: str):
        """Записывает сообщение с указанным уровнем логирования."""
        pass
