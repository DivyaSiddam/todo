tasks = []  # This will store our tasks in memory

def add_task(title):
    tasks.append({"title": title, "completed": False})

def get_tasks():
    return tasks

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
