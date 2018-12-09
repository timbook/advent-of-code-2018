import re

with open('../data/07-input.txt', 'r') as f:
    lines = f.read()

rx = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."

tree_items = re.findall(rx, lines)

firsts = [item[0] for item in tree_items]
lasts = [item[1] for item in tree_items]
all_tasks = set(firsts + lasts)

first = lambda item: item[0]
last = lambda item: item[1]

def get_available():
    for task in all_tasks:
        rel_items = [item for item in tree_items if last(item) == task]
        prereqs = [item for item in rel_items if first(item) in completed]
        if (len(rel_items) == len(prereqs)):
            can_do.append(task)

can_do = []
completed = []
while all_tasks:
    get_available()
    if can_do:
        can_do.sort()
        completed.append(can_do.pop(0))
    all_tasks -= set(completed + can_do)

print("::: PART A:")
print(f"COMPLETION ORDER: {''.join(completed)}\n")

#==============================================================================

workers = {1:'idle', 2:'idle', 3:'idle', 4:'idle', 5:'idle'}

def free_workers(w):
    return [k for k, v in w.items() if v == 'idle']

def task_time(char):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return 61 + letters.index(char)

def count_down(w, tasks):
    for k, v in w.items():
        if v != 'idle':
            new_val = v[1] - 1
            if new_val == 0:
                completed.append(w[k][0])
                tasks -= set(completed + can_do)
                w[k] = 'idle'
            else:
                w[k][1] = new_val

    return tasks

clock = 0
can_do = []
completed = []
in_process = []
all_tasks = set(firsts + lasts)
while all_tasks:

    get_available()

    # When there are tasks that can be done, and there are
    # free workers, assign tasks to those workers
    # while can_do and any_workers_free(workers):
    can_do.sort()
    for w in free_workers(workers):
        ready_tasks = [can for can in can_do if can not in in_process]
        if ready_tasks:
            task = ready_tasks[0]
            can_do.remove(task[0])
            in_process.append(task)
            workers[w] = [task, task_time(task)]

    # Count down clock
    # If any tasks are now done, idle the workers and append the 
    # completed task and remove from all_tasks
    clock += 1
    all_tasks = count_down(workers, all_tasks)

print("::: PART B")
print(f"Time's up at: {clock}")
