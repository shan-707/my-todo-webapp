FILEPATH = "C:\Shan\python\To_Do_Web\Tasks_file.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as fh:
        tasks_local = fh.readlines()
    return tasks_local

def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as fh:
        fh.writelines(todos)

