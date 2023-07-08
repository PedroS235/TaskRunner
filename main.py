import yaml
from task import TasksExecutor
import sys
from logger import Logger
import platform


def check_os_version():
    if platform.system() == "Windows":
        return "Windows"
    elif platform.system() == "Linux":
        return "Linux"
    elif platform.system() == "Darwin":
        return "MacOS"
    else:
        return None


def main(file_path):
    with open(file_path, "r") as f:
        tasks = yaml.load(f, Loader=yaml.FullLoader)

    detected_os = check_os_version()
    if detected_os is None:
        logger.error("Unsupported OS")
        exit(1)
    if detected_os != tasks["OS"]:
        logger.error(
            "Detected OS does not match OS defined on your tasks.yaml"
        )
        logger.error(
            f"Detected OS is {detected_os} and tasks.yaml OS is {tasks['OS']}"
        )
        exit(1)
    logger.info(f"Detected OS: {detected_os}")
    tasks_executor = TasksExecutor(tasks["tasks"])
    tasks_executor.start()


if __name__ == "__main__":
    logger = Logger()
    file_path = ""
    if len(sys.argv) == 1:
        logger.info("Reading tasks.yaml from current directory...")
        file_path = "./tasks.yaml"
    elif len(sys.argv) == 2:
        logger.info(f"Reading tasks.yaml from {sys.argv[1]}...")
        file_path = sys.argv[1]
    else:
        logger.error(
            "Invalid number of arguments. Usage: python main.py [file_path]"
        )
        exit(1)
    main(file_path)
