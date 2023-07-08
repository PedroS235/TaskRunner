import subprocess as sp
from logger import Logger


class TasksExecutor:
    def __init__(self, tasks):
        self.tasks = tasks
        self.logger = Logger()

    def execute_task(self, task, id):
        task_name = task["name"]
        task_cmds = task["cmds"]

        self.logger.info(f"Executing TASK[{id}]: {task_name}")
        for cmd in task_cmds:
            cmd_output = sp.run(cmd, shell=True)

            if cmd_output.returncode != 0:
                self.logger.error(f"TASK[{id}] failed: {task_name}")
                exit(cmd_output.returncode)

    def start(self):
        self.logger.info(f"Executing a total of {len(self.tasks)} TASKS...")
        print(50 * "-")
        print()

        for id, task in enumerate(self.tasks):
            self.execute_task(task, id + 1)
            print(50 * "-")
            print()
