import json
DATA_FILE = 'tasks.json'

def load_tasks():
    """Load the task list from DATA_FILE.

    Returns:
        list[dict]: saved tasks; an empty list if the file is missing,
        corrupted, or does not contain a list.
    """
    try:
        with open(DATA_FILE,'r',encoding = 'utf-8') as file:
            data = json.load(file) 
    except FileNotFoundError:
        print(f"No saved tasks found ({DATA_FILE}). Starting with an empty list.")
        return []
    except (json.JSONDecodeError, OSError):
        print(f"Could not read {DATA_FILE}. Starting with an empty list.")
        return []

    if not isinstance(data, list):
        print(f"{DATA_FILE} does not contain a task list. Starting empty.")
        return []
    return data

def save_tasks(tasks):
    """Save the task list to DATA_FILE, overwriting the previous content.

    Args:
        tasks (list[dict]): tasks in the shared data structure.
    """
    with open(DATA_FILE,'w',encoding = 'utf-8') as f:
        json.dump(tasks,f,indent = 4,ensure_ascii = False)
