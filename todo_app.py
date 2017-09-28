from sys import argv


class StartScreen(object):
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
    
    def run(self):
        self.check_argument()

    def check_argument(self):
        arg = self.get_arguments()
        if arg == None:
            self.start_screen()
        elif arg == '-l':
            self.list_printer()
        elif arg == '-a':
            self.add_todo()
            return argv[2]
        elif arg == '-r':
            return arg
        elif arg == '-r':
            return arg


    def get_arguments(self):
        if len(argv) >1:
            return argv[1]
        return None

    def read_todos(self):
        raw_list = []
        list_of_tasks = open('data_file.txt', "r")
        for line in list_of_tasks:
            raw_list.append(line)
        return raw_list
                

    def list_printer(self):
        raw_list = self.read_todos()
        print('\n')
        if self.read_todos() == []:
            print('No todos for today! :)')
        line_counter = 0
        for line in raw_list:
            line_counter += 1
            print(str(line_counter)+ ' - '+ str(line))

    def add_todo(self):
        with open('data_file.txt', 'a') as list_of_tasks:
            list_of_tasks.write(argv[2]+ '\n')
        return self.list_printer()
            
         

my_screen = StartScreen()
my_screen.run()