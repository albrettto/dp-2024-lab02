from abc import ABC, abstractmethod
from datetime import datetime
import os


class LogStrategy(ABC):
    @abstractmethod
    def write(self, message: str):
        pass

    @abstractmethod
    def set_file_path(self, file_path: str):
        pass

    @staticmethod
    def get_timestamp() -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_filename() -> str:
        return f"DP.P1.{datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.log"


class ConsoleLogStrategy(LogStrategy):
    def set_file_path(self, file_path: str):
        pass

    def write(self, message: str):
        print(message)


class FileLogStrategy(LogStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def set_file_path(self, file_path: str):
        self.file_path = file_path

    def write(self, message: str):
        log_file_path = os.path.join(self.file_path, self.get_filename())
        with open(log_file_path, 'a') as log_file:
            log_file.write(message + '\n')

class UpperCaseFileLogStrategy(FileLogStrategy):
    def set_file_path(self, file_path: str):
        super().set_file_path(file_path)

    def write(self, message: str) -> None:
        super().write(message.upper())


""" Другой вариант решения """
# class UpperCaseFileLogStrategy(LogStrategy):
#     def __init__(self, file_path: str):
#         self.file_path = file_path
#
#     def set_file_path(self, file_path: str):
#         self.file_path = file_path
#
#     def write(self, message: str):
#         log_file_path = os.path.join(self.file_path, self.get_filename())
#         with open(log_file_path, 'a') as log_file:
#             log_file.write(message.upper() + '\n')

