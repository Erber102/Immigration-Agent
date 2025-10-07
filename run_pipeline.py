from __future__ import annotations

from src.pipeline.task_planner import get_tasks
from src.pipeline.agent_core import run_task


def main():
    for task in get_tasks():
        print(f"Running task: {task['goal']}")
        run_task(task)


if __name__ == "__main__":
    main()
