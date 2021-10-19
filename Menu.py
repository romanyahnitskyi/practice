
class menu_option:
    def __init__ (self,command_num,command_name):
        self.command_num=command_num
        self.command_name = command_name
    def print_obj(self):
        print ( f'If you want to {self.command_name} enter {self.command_num}')
class menu:
    def __init__(self,menu_list):
        self.menu_list=menu_list
    def print(self):
        for i in range (len(self.menu_list)):
            self.menu_list[i].print_obj()


