from src.diary import Diary
from src.diary_entry import DiaryEntry
import inquirer

def main():
    diary = Diary()
    
    while True:
        main_menu_options = '\n'.join(['1: Add diary entry', '2: Retrieve all entries', '3: Get an entry you can read in time', '4: Go to task manager', '5: Exit'])
        print(f'Type a number: \n{main_menu_options}')
        selection = input('Type a number: ')
        print(selection)
        if selection == '1':
            diary.add_diary_entry(DiaryEntry('title', 'contents'))
        elif selection == '5':
            break
