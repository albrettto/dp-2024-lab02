from enums.level_enum import LogLevel
from logger import Logger
from writers import ConsoleLogWriter, FileLogWriter, UpperCaseFileLogWriter

if __name__ == "__main__":
    # Пример логирования в консоль
    file_path = "C:\\Users\\ahusa\\PycharmProjects\\dp-2024-lab02"
    logger = Logger(ConsoleLogWriter())
    logger.log(LogLevel.INFO, "Application started successfully")
    logger.log(LogLevel.WARN, "Warning message")
    logger.log(LogLevel.ERROR, "An error occurred")

    # Пример логирования в файл
    file_log_strategy = FileLogWriter(file_path)
    logger.set_log_strategy(file_log_strategy)
    logger.log(LogLevel.INFO, "Application started successfully")
    # Смена пути файла для этого логгера
    file_log_strategy.set_file_path(file_path + "\\Logs")
    logger.log(LogLevel.INFO, "Application started successfully")
    logger.log(LogLevel.WARN, "Warning message")
    logger.log(LogLevel.ERROR, "An error occurred")

    # Пример логирования в файл в верхнем регистре
    upper_case_file_log_writer = UpperCaseFileLogWriter(file_path)
    logger.set_log_strategy(upper_case_file_log_writer)
    logger.log(LogLevel.INFO, "Application started successfully")
    # Смена пути файла для этого логгера
    upper_case_file_log_writer.set_file_path(file_path + "\\Logs")
    logger.log(LogLevel.WARN, "Warning message")
    logger.log(LogLevel.ERROR, "An error occurred")
