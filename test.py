from Logger import Logger
from LogStrategy import ConsoleLogStrategy, FileLogStrategy, UpperCaseFileLogStrategy
import unittest
import threading
import tempfile
import os


class TestLoggerThreadSafe(unittest.TestCase):

    def setUp(self):
        """Подготовка перед каждым тестом."""
        self.file_path = tempfile.TemporaryDirectory()  # Используем временную директорию

    def tearDown(self):
        """Очистка временных файлов после каждого теста."""
        self.file_path.cleanup()  # Удаляем временные файлы

    def run_multithreaded_logging(self, logger, expected_message, filename=None):
        """Метод для многопоточного логгирования и проверки результата."""

        def log_messages():
            for i in range(10):
                logger.log("INFO", f"Application started successfully {i}")

        threads = [threading.Thread(target=log_messages) for _ in range(5)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        if filename and os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()
            self.assertIn(expected_message, content)
        elif filename:
            self.fail(f"File {filename} was not created.")

    def test_console_log_multithreaded(self):
        """Тест многопоточного логгирования в консоль."""
        logger = Logger(ConsoleLogStrategy())
        self.run_multithreaded_logging(logger, f"[INFO] Application started successfully 0")

    def test_file_log_multithreaded(self):
        """Тест многопоточного логгирования в файл."""
        logger = Logger(FileLogStrategy(self.file_path.name))
        timestamp = FileLogStrategy(self.file_path.name).get_timestamp()
        filename = FileLogStrategy(self.file_path.name).get_filename()
        expected_message = f"{timestamp} [INFO] Application started successfully 0"

        self.run_multithreaded_logging(logger, expected_message, os.path.join(self.file_path.name, filename))

    def test_uppercase_file_log_multithreaded(self):
        """Тест многопоточного логгирования в файл с верхним регистром."""
        logger = Logger(UpperCaseFileLogStrategy(self.file_path.name))
        timestamp = FileLogStrategy(self.file_path.name).get_timestamp()
        filename = FileLogStrategy(self.file_path.name).get_filename()
        expected_message = f"{timestamp} [INFO] APPLICATION STARTED SUCCESSFULLY 0"

        self.run_multithreaded_logging(logger, expected_message, os.path.join(self.file_path.name, filename))


if __name__ == '__main__':
    unittest.main()
