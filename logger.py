# Colors
CRESET = "\033[0m"  # Text Reset
CRED = "\033[1;31m"  # Red
CBLUE = "\033[1;34m"  # Blue
CYELLOW = "\033[1;33m"  # Yellow


class Logger:
    def __init__(self):
        self.colors = {
            "info": CBLUE,
            "warn": CYELLOW,
            "error": CRED,
            "reset": CRESET,
        }

    def info(self, text):
        print(f"{self.colors['info']}[Info] -> {self.colors['reset']}{text}")

    def warn(self, text):
        print(f"{self.colors['warn']}[Warn] -> {self.colors['reset']}{text}")

    def error(self, text):
        print(f"{self.colors['error']}[Error] -> {self.colors['reset']}{text}")
