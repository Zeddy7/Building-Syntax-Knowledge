days =  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_tasks = {
     'monday' : [],
     'tuesday' : [],
     'wednesday' : [], 
     'thursday' : [],
     'friday' : [],
     'saturday' : [],
     'sunday' : []
}

def add_tasks():
    while True:
        day = input("\nWhich day's tasks do you want to create? ").lower()
        if day in days:
            break
        else:
            print('Invalid day')
            continue
    
    no_of_tasks = int(input('\nHow many tasks do you want to enter? '))
    
    for i in range(no_of_tasks):
        task = input(f'Task {i+1}: ')
        days_tasks[day].append(task)
    
    print(f'\n{day.capitalize()} tasks:')
    for i, task in enumerate(days_tasks[day]):
        print(f'{i+1}. {task}')


while True:
    add_tasks()
    
    next_day = input('\nDo you want to enter another day (y/n)? ').lower()
    
    if next_day == 'y':
        continue
    
    elif next_day == 'n':
        break
    
print("\nWeekly task summary:")
for days, tasks in days_tasks.items():
    if tasks:
        print(f"\n{days.capitalize()}'s tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")
    
print('\nAll tasks for the week entered.')
