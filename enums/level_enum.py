from enum import Enum


class LogLevel(Enum):
    """
    Enum для представления уровней логирования.

    Значения:
        TRACE (1): Подробные сообщения.
        INFO (2): Информационные сообщения.
        WARN (3): Предупреждения.
        ERROR (4): Ошибки.
        FATAL (5): Критические ошибки.
    """

    TRACE = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5
