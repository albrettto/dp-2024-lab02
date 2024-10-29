import os
from interfaces.writer import Writer
from interfaces.file_path_manager import FilePathManager


class ConsoleLogWriter(Writer):
    """Стратегия записи логов в консоль."""

    def write(self, message: str):
        """Выводит сообщение в консоль."""
        print(message)


class FileLogWriter(Writer, FilePathManager):
    """Стратегия записи логов в файл."""

    def __init__(self, file_path: str):
        """Инициализирует экземпляр с указанным путем к файлу."""
        self.file_path = file_path

    def set_file_path(self, file_path: str):
        """Устанавливает новый путь к файлу для записи логов."""
        self.file_path = file_path

    def write(self, message: str):
        """Записывает сообщение в файл."""
        log_file_path = os.path.join(self.file_path, self.get_filename())
        with open(log_file_path, "a") as log_file:
            log_file.write(message + "\n")


class UpperCaseFileLogWriter(FileLogWriter):
    """Стратегия записи логов в файл с преобразованием текста в верхний регистр."""

    def set_file_path(self, file_path: str):
        """Устанавливает новый путь к файлу для записи логов."""
        super().set_file_path(file_path)

    def write(self, message: str) -> None:
        """Записывает сообщение в файл в верхнем регистре."""
        super().write(message.upper())
