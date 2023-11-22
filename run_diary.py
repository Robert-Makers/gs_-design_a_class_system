from src.diary import Diary
from src.diary_entry import DiaryEntry
from src.task_tracker import TaskTracker

def main():
    diary = Diary()
    tracker = TaskTracker()
    
    while True:
        main_menu_options = '\n'.join(['1: Add diary entry', '2: Retrieve all entries', '3: Get an entry you can read in time', '4: Go to task manager', '5: Exit'])
        print(f'Type a number: \n{main_menu_options}')
        selection = input('Type a number: ')
        if selection == '1':
            # print('adding entry')
            diary.add_diary_entry()
        if selection == '2':
            # print('getting entries')
            diary.retrieve_entries()
        if selection == '3':
            diary.select_entry_for_time()
        if selection == '4':
            while True:
                task_menu_options = '\n'.join(['1: Add a new task', '2: Show incomplete tasks', '3: Show complete tasks', '4: Complete a task', '5: Exit'])
                print(f'Type a number: \n{task_menu_options}')
                selection = input('Type a number: ')
                if selection == '1':
                    tracker.add_task()
                if selection == '2':
                    tracker.get_incomplete()
                if  selection == '3':
                    tracker.get_complete()
                if selection == '4':
                    tracker.complete_task()
                elif selection == '5':
                    break

        elif selection == '5':
            break

if __name__ == '__main__':
    main()