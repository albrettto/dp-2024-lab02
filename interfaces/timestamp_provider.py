from datetime import datetime


class TimestampProvider:
    """Класс для предоставления временной метки."""

    @staticmethod
    def get_timestamp_in_message() -> str:
        """Возвращает текущую временную метку в формате 'YYYY-MM-DD HH:MM:SS'."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_timestamp_in_filename() -> str:
        """Возвращает текущую временную метку в формате 'YYYY-MM-DD.HH-MM-SS'."""
        return datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
