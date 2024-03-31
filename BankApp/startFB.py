from cmd import Cmd
import main
import os
from time import sleep

class MyPrompt(Cmd):
    prompt = 'firstBank$ '
    intro = "Welcome to First Bank, enter run to start the app or exit to quit.".center(100)

    def do_run(self, arg):
        runBankApp = main.MainExec()
        runBankApp.run()
    
    def do_exit(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Exiting...")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    prompt = MyPrompt()
    prompt.cmdloop()