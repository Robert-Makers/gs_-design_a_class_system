from src.task import Task

class TaskTracker:
    # user facing properties
    # none

    def __init__(self):
        self.task_list = []
        # Parameters
        #   task_list: []
        # Returns
        #   nothing
        # Side effects
        #   sets the task list to empty

    def add_task(self):
        task_text = input("What's the task?")
        self.task_list.append(Task(task_text))
        # Parameters
        #   task: Task
        # Returns
        #   nothing
        # Side effects
        #  add task to task_list

    def get_incomplete(self):
        incomplete_list = [task.text for task in self.task_list if not task.complete]
        print(incomplete_list)
        # Parameters
        #   none
        # Returns
        #   a list of tasks where task.complete == False
        # Side effects
        #  none

    def get_complete(self):
        complete_list = [task.text for task in self.task_list if task.complete]
        print(complete_list)
        # Parameters
        #   none
        # Returns
        #   a list of tasks where task.complete == True
        # Side effects
        #  none

    def complete_task(self):
        task_text = input("What task have you finished?")
        task_to_complete = [task for task in self.task_list if task_text == task.text]
        task_to_complete[0].complete_task()
        # Parameters
        #   task: task.task
        # Returns
        #   none
        # Side effects
        #  set task.complete to True

    def give_up(self):
        for task in self.task_list:
            task.complete_task()
        # Parameters
        #   none
        # Returns
        #   nothing
        # Side effects
        #  marks all tasks as complete