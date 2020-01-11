import PySimpleGUI as sg
from prc import *
sg.theme('DarkAmber')
while True:  # Event Loop
    tasks = read_list()
    last_date = read_date()
    priority = read_priority()
    todo = todo_list(tasks,last_date,priority)
    ord = prio_order(tasks,last_date,priority)
    todo = swap_list(todo,ord)
    layout = [
        [sg.Text('ToDo')],
        [sg.InputText('', key='todo_item'), sg.Button(button_text='Add', key="add_save")],
        [sg.Listbox(values=todo, size=(50, 10), key="items"),sg.Button('Delete'), sg.Button('Edit')]
    ]
    layout1 = [
        [sg.InputCombo(['High','Medium','Low'],key = 'ch')],
         [sg.Button('OK')]
        ]
    layout2 = [
        [sg.InputText('DD-MM-YYYY',key = 'dt')],
         [sg.Button('OK')]
        ]
    window = sg.Window('ToDo App', layout)
    window1 = sg.Window('Priority',layout1)
    window2 = sg.Window('Date',layout2)
    event, values = window.Read()
    if event == "add_save":
        tasks.append(values['todo_item'])
        button, date1 = window2.read()
        last_date.append(date1['dt'])
        window2.Close()
        pri, choice = window1.read()
        priority.append(choice['ch'])
        window1.Close()
        todo = todo_list(tasks, last_date, priority)
        window.FindElement('items').Update(values=todo)
        window.FindElement('add_save').Update("Add")
        update_list(tasks, last_date, priority)
    elif event == "Delete":
        q = values["items"][0]
        todo.remove(values["items"][0])
        dele(tasks, last_date, priority, q)
        todo = todo_list(tasks, last_date, priority)
        window.FindElement('items').Update(values=todo)
        update_list(tasks, last_date, priority)
    elif event == "Edit":
        edit_val = values["items"][0]
        todo.remove(values["items"][0])
        dele(tasks, last_date, priority, edit_val)
        todo = todo_list(tasks, last_date, priority)
        window.FindElement('items').Update(values=todo)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
        update_list(tasks, last_date, priority)
    elif event == None:
        break
window.Close()