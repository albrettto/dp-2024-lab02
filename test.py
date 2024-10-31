import unittest
from unittest.mock import mock_open, patch
import os
from writers import ConsoleLogWriter, FileLogWriter, UpperCaseFileLogWriter


class TestConsoleLogWriter(unittest.TestCase):

    @patch('builtins.print')
    def test_write_logs_to_console(self, mock_print):
        writer = ConsoleLogWriter()
        writer.write("Test message")
        mock_print.assert_called_once_with("Test message")


class TestFileLogWriter(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_write_logs_to_file(self, mock_file):
        writer = FileLogWriter('test_log_path')
        writer.write("Test message")

        # Создание пути для проверки
        expected_path = os.path.join('test_log_path', writer.get_filename())

        # Проверка, что файл открывается с правильными параметрами
        mock_file.assert_called_once_with(expected_path, 'a')

        # Проверка, что сообщение записывается в файл
        mock_file().write.assert_called_once_with("Test message\n")

    def test_set_file_path(self):
        writer = FileLogWriter('initial_path')
        writer.set_file_path('new_path')
        self.assertEqual(writer.file_path, 'new_path')


class TestUpperCaseFileLogWriter(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_write_logs_in_upper_case(self, mock_file):
        writer = UpperCaseFileLogWriter('test_log_path')
        writer.write("Test message")

        # Создание пути для проверки
        expected_path = os.path.join('test_log_path', writer.get_filename())

        # Проверка, что файл открывается с правильными параметрами
        mock_file.assert_called_once_with(expected_path, 'a')

        # Проверка, что сообщение записывается в файл в верхнем регистре
        mock_file().write.assert_called_once_with("TEST MESSAGE\n")

    def test_set_file_path(self):
        writer = UpperCaseFileLogWriter('initial_path')
        writer.set_file_path('new_path')
        self.assertEqual(writer.file_path, 'new_path')


if __name__ == '__main__':
    unittest.main()
