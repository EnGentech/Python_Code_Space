from cmd import Cmd
import main
import os
from time import sleep

class MyPrompt(Cmd):
    prompt = 'firstBank$ '
    intro = "Simple command processor example."

    def do_run(self, arg):
        runBankApp = main.MainExec()
        runBankApp.run()
    
    def do_exit(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Exiting...")
        sleep(5)
        return True

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    prompt = MyPrompt()
    prompt.cmdloop()