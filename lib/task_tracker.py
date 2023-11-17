class TaskTracker:
    # user facing properties
    # none

    def __init__(self):
        # Parameters
        #   task_list: []
        # Returns
        #   nothing
        # Side effects
        #   sets the task list to empty
        pass

    def add_task(self, task):
        # Parameters
        #   task: Task
        # Returns
        #   nothing
        # Side effects
        #  add task to task_list
        pass

    def get_incomplete(self):
        # Parameters
        #   none
        # Returns
        #   a list of tasks where task.complete == False
        # Side effects
        #  none
        pass

    def get_complete(self):
        # Parameters
        #   none
        # Returns
        #   a list of tasks where task.complete == True
        # Side effects
        #  none
        pass

    def complete_task(self):
        # Parameters
        #   task: task.task
        # Returns
        #   none
        # Side effects
        #  set task.complete to True
        pass

    def give_up(self):
        # Parameters
        #   none
        # Returns
        #   nothing
        # Side effects
        #  marks all tasks as complete