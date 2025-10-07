from __future__ import annotations
from apscheduler.schedulers.background import BackgroundScheduler
from .task_planner import get_tasks
from .agent_core import run_task


def start_scheduler() -> BackgroundScheduler:
    scheduler = BackgroundScheduler()
    def job():
        for task in get_tasks():
            run_task(task)
    scheduler.add_job(job, "interval", hours=24, id="refresh_kb")
    scheduler.start()
    return scheduler
