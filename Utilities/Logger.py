import logging
import os
from datetime import datetime


class LoggerUtil:
    @staticmethod
    def get_logger():
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Logs')
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        log_path = os.path.join(log_folder, f'test_run_{current_time}.log')
        log_instance = logging.getLogger("AutomationLogger")
        if not log_instance.handlers:
            log_instance.setLevel(logging.DEBUG)
            file_log_handler = logging.FileHandler(log_path, mode='a')
            file_log_handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            ))

            stream_log_handler = logging.StreamHandler()
            stream_log_handler.setFormatter(logging.Formatter(
                '%(levelname)s: %(message)s'
            ))
            log_instance.addHandler(file_log_handler)
            # log_instance.addHandler(stream_log_handler)

        return log_instance
