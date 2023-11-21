from lib.diary import Diary
import inquirer

def main():
    diary = Diary()

    while True:
        options = [
            inquirer.List('choice', 'What would you like to do in your diary?', choices=['Add entry', 'Retrieve entries', 'Retrieve one entry you can read now', 'Exit'])
        ]
        answer = inquirer.prompt(options)
        action = answer['choice']
        
        if action == 'Add entry':
            pass
        elif action == 'Retrieve entries':
            pass
        elif action == 'Retrieve one entry you can read now':
            pass
        elif action == 'Exit':
            break


main()