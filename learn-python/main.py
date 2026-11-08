# from datetime import date

# print(date.today())  # 2026-11-02

from enum import StrEnum


class TaskStatus(StrEnum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    DONE = "done"


print(TaskStatus.BLOCKED)
