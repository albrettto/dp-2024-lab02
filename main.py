from logger import Logger
from log_strategy import ConsoleLogStrategy, FileLogStrategy, UpperCaseFileLogStrategy

if __name__ == "__main__":
    # Пример логирования в консоль
    logger = Logger(ConsoleLogStrategy())
    logger.log("INFO", "Application started successfully")
    logger.log("WARN", "Warning message")
    logger.log("ERROR", "An error occurred")

    file_path = "C:\\Users\\ahusa\\PycharmProjects\\dp-2024-lab02"

    # Пример логирования в файл
    logger.set_log_strategy(FileLogStrategy(file_path))
    logger.log("INFO", "Application started successfully")
    logger.set_file_path(file_path + "\\Logs")
    logger.log("INFO", "Application started successfully")
    logger.log("WARN", "Warning message")
    logger.log("ERROR", "An error occurred")

    # Пример логирования в файл в верхнем регистре
    logger.set_log_strategy(
        UpperCaseFileLogStrategy(file_path))
    logger.log("INFO", "Application started successfully")
    logger.set_file_path(file_path + "\\Logs")
    logger.log("WARN", "Warning message")
    logger.log("ERROR", "An error occurred")
