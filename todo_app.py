from sys import argv


class App(object):
    def __init__(self):
        pass

    def start_screen(self):
        print(str('\n\
        Command Line Todo application\n\
        =============================\n\
        \n\
        Command line arguments:\n\
        -l   Lists all the tasks\n\
        -a   Adds a new task\n\
        -r   Removes an task\n\
        -c   Completes an task'))
    

    def check_argument(self):
        arg = self.get_arguments()
        if arg == None:
            self.start_screen()
        elif arg == '-l':
            self.list_printer()
        elif arg == '-a':
            self.add_todo()
            return argv[2]
        elif arg == '-c':
            return arg
        elif arg == '-r':
            self.remove_todo()
            return argv[2]


    def get_arguments(self):
        if len(argv) >1:
            return argv[1]
        return None

# class ToDo(object):
#     def __init__(self):
#         pass

    def read_todos(self):
        raw_list = []
        list_of_tasks = open('data_file.txt', "r")
        for line in list_of_tasks:
            raw_list.append(line)
        return raw_list
                


# # class ToDoController(object):
#     def __init__(self):
#         pass
        
    def list_printer(self):
        raw_list = self.read_todos()
        print('\n')
        if self.read_todos() == []:
            print('No todos for today! :)')
        line_counter = 0
        for line in raw_list:
            line_counter += 1
            print(str(line_counter)+ ' - '+  str(line))

    def add_todo(self):
        with open('data_file.txt', 'a') as list_of_tasks:
            list_of_tasks.write(argv[2]+ '\n')
        return self.list_printer()
    
    def run(self):
        self.check_argument()
    # def check_todo(self):
    #     self.read_todos = checked_list

# DONT FORGET TO DO IT LATER!!!!
    # def remove_todo(self):
    #     rem_todo = self.read_todos()
    #     x = argv[2]
    #     del rem_todo[int(x)-1]
    #     with open('data_file.txt', 'w') as new_list:
    #     return rem_todo

my_screen = App()
my_screen.run()