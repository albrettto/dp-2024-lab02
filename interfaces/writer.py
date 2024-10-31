from abc import ABC, abstractmethod


class Writer(ABC):
    """Интерфейс для стратегий записи логов."""

    @abstractmethod
    def write(self, message: str):
        """Записывает сообщение в соответствующий выходной поток."""
        pass
