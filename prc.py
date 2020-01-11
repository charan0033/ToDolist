def update_list(tasks,last_date,priority):
    with open("tasks.txt","w") as f:
        with open("date.txt","w") as f1:
            with open("priority.txt","w") as f2:

                f.truncate(0)
                f1.truncate(0)
                f2.truncate(0)
                for k in tasks:
                    f.write(k)
                    f.write("\n")
                for k in last_date:
                    f1.write(k)
                    f1.write("\n")
                for k in priority:
                    f2.write(k)
                    f2.write("\n")
            f2.close()
        f1.close()
    f.close()
def read_list():
    tasks = []
    with open("tasks.txt","r") as f:
        tasks = f.readlines()
        task_list = []
        for task in tasks:
            task_list.append(task.strip('\n'))
        f.close()
        return task_list
def read_date():
    dates = []
    with open("date.txt","r") as f:
        dates = f.readlines()
        date_list = []
        for date in dates:
            date_list.append(date.strip("\n"))
        f.close()
        return date_list

def read_priority():
    priority = []
    with open("priority.txt","r") as f:
        priority = f.readlines()
        prio_list = []
        for p in priority:
            prio_list.append(p.strip("\n"))
        f.close()
        return prio_list
def todo_list(tasks,last_date,priority):
    a = []
    for k in range(len(tasks)):
        a.append(tasks[k])
        a.append(last_date[k])
        a.append(priority[k])
        a.append("\n")
    return a
def dele(tasks,last_date,priority,q):
    for i in range(len(tasks)):
        if(q==tasks[i]):
            pos = i
    tasks.remove(q)
    last_date.remove(last_date[i])
    priority.remove(priority[i])
def prio_order(tasks,last_date,priority):
    ord = []
    for i in range (len(tasks)):
        if(priority[i]=='High'):
            ord.append(i+1)
    for i in range(len(tasks)):
        if(priority[i]=='Medium'):
            ord.append(i+1)
    for i in range(len(tasks)):
        if(priority[i]=='Low'):
            ord.append(i+1)
    return ord
def swap_list(todo,ord):
    a = []
    for i in ord:
        i = i*3-3+(i-1)
        a.append(todo[i])
        a.append(todo[i+1])
        a.append(todo[i+2])
        a.append("\n")
    return a