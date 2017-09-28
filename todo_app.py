from sys import argv


class StartScreen(object):
    def __init__(self):
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
        self.get_arguments()
        self.list_printer()


    def get_arguments(self):
        raw_list = []
        if argv[1] == '-l':
            list_of_tasks = open('data_file.txt', "r")
            for line in list_of_tasks:
                raw_list.append(line)
            return raw_list
                

    def list_printer(self):
        raw_list = self.get_arguments()
        line_counter = 1
        for line in raw_list:
            print(str(line_counter)+ " - "+ line)


my_screen = StartScreen()
my_screen.run()