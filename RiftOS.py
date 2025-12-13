import os
import shutil
import subprocess
import time
import tkinter as tk
from rich.console import Console
from rich.text import Text
from rich.style import Style
import webbrowser

#---------------colours------------------------------------
red = "\033[31m"
white = "\033[97m"
light_blue = "\033[96m"
blue = "\033[94m"
yellow = "\033[93m"
light_red = "\033[91m"
green = "\033[92m"
purple = "\033[95m"
reset = "\033[0m"



riftos_version = "2.0  Pre Release"

console = Console()
user_name = "user"
host_name = "RiftOS"  # default hostname, can change per OS
current_path = "/"  # initial working directory

def get_prompt_text():
    user_style = Style(color="blue", bold=True)
    host_style = Style(color="green", bold=True)
    path_style = Style(color="cyan")

    user = Text(user_name, style=user_style)
    at = Text("@", style="white")
    host = Text(host_name, style=host_style)
    path = Text(current_path, style=path_style)

    prompt = user + at + host + Text(":", style="white") + path + Text("$ ", style="white")

    # get terminal width
    term_width = shutil.get_terminal_size().columns
    prompt_len = len(prompt.plain)

    # calculate left padding
    padding = max((term_width - prompt_len) // 3,0)

    return Text(" " * padding) + prompt






# -----------------cc-boot------------------------------------

def ccboot():
        print(light_blue + r"""      
            ------------------------Do NOT use this app on linux or mac it only works on windows-----------------------                                   
                                                  -----CC-boot tool---- 
                                                  |      -RiftOS-     | 
                                                  |     -GalaxyOS-    |                     
                                                  |       -...-       |                
                                                  |       -CT-        |                                        
                                                  -------------------- V1.3                    
          

              """)
        print("Please choose an OS to boot 1 2 3 or 4:")
        os_choice = input(">")
        if os_choice == '1':
            print('Booting To RiftOS Terminal Type h for ui...')
            time.sleep(1)
            os.system('cls')
            riftos()
        elif os_choice == '2':
            print('Booting To GalaxyOS')
            time.sleep(1)
            os.system('cls')
            galaxy()
            riftos()
        elif os_choice == '':
            print('No OS Found Booting RiftOS by default.')
            time.sleep(1)
            os.system('cls')
            riftos()
        elif os_choice == '4':
            ct()
        elif os_choice == "rt":
            print('Rebooting To CC BootTool...')
            time.sleep(1)
            os.system('cls')
            ccboot()

        else:
            print('No OS Found booting RiftOS by default.')
            time.sleep(1)
            os.system('cls')
            riftos()

#---------------------------------------------help menu------------------------------------------------
def help():
    os.system('cls')
    os.system('title Help Menu')
    print(white + r"""     

          
                                     -----------------HELP-MENU-----------------------------------------
                             These are the most simple commands to use RiftOS. Use ff for a more advanced command menu.
                                                 ║      --Help--    ║
                                                 ║     ---ff---     ║
                                                 ║     --reboot-    ║    
                                                 ║      --ghome--   ║                     
                                                 ║  ---1,2,3,4...-  ║             
                                                 ║    ---r-ver---   ║           
                                                 ║     ---ct---     ║             
                                                 ║      -----       ║                
                                                 ║      -----       ║         
                                                 ║      -----       ║                  
                                                 ║      -----       ║                       
                                                 --------------------


              """)




#-------------------------------------------------galaxy os--------------------------------------------------
    
def galaxy():
    global current_path
    current_path = "/root/Env/GalaxyOS"
    global host_name
    host_name = "GalaxyOS"
    os.system('cls')
    print(light_blue + r"""             

                        ░           ▒                    
                                   ▒░                    
                    ▒    ░    ░    ░░▓░▒░                
               ░░░░▒░ ░░░▒░░░░░▒░░░   ░░░▒▒  ░                     ---------------------------------------
           ░  ░▓▒▒ ░ ░░░░░░░░░▒░░▒▒▒▒░▓░░░   ░░░░                       GalaxyOS Terminal Environment
     ▒░░  ░  ░░ ░ ░░░░▓░▓▒░▒▒░▒░░░░▒░░░▒▓░ ░░    ░░    ▓           ---------------------------------------
   ▒   ░ ░    ▒░ ░▒░░▒▓▒░░▒░░░▒▒▓▒░▒░░░░░░▒░▒ ░    ░ ░                                   
  ░░░░     ░ ▒▒▒░░░░░░▒▒▒▒▒▒▓▒▒▒▒░▒░▒▒░░░░░▒▓▒░     ░░░░                                
  ░░░   ░ ▓░░ ░░░▒░▒▒▒▒▒▒▓▓▒▓▓▒▓▒▒░▒▒▒▒░░░▒░▓░░░▒    ░   
░       ░░   ░ ░░░▒▓▒▒▓▓▓▓▓▓▓█▓▓▓▓▒▒░░▒█░░░░ ░▒▒░░░░░░ ▒ 
      ░ ▒ ░  ░░░░▒▓░░▒▒▓▓███████▓▓▓▒░░▒▓░░░ ░ ░░░▒ ░░░ ░░
░        ░▒░░░░░░▒▒░░▒▓▒▓▓█▓▓█▓▓▓▓▓▒░░░▓░░░░ ░▒░░   ░ ░▒░
░░       ░░ ░░░░░░▒▒░░▒▓▓▓▓█▓▓▒▓▓▒▒▒░▓░▒░░▒░ ░░░ ░ ░    ░
 ▓ ░     ░░    ░░░░▓░░░▒▒▓▓▒▒▒▒▒▓▒▒▒░░░░▒▒░░░▒█▓░     ░░ 
  ░ ░░    ░░  ░░░ ░░░▓░░▒░░░▒░░░░░▒░▒░░░░░▒░░ ░   ▒▒   ▓▒
  ░░ ░     ░░░ ░░▒░ ░ ░▒░▓░░░░░▒░░░▒ ░░░░░░  ▒░ ░░░░ ░   
  ░░░  ░ ░ ░ ░░░  ░▒░░  ░░░░░░░░░░░▒░▒░    ░   ░░░░▒     
    ░░▒ ░░░     ▒░░ ░▒░ ░░░   ░        ░  ░░ ▒  ░        
      ░░ ░░    ░░░░▒▓▒▒▒░░░ ░ ░░ ░░░░ ░ ▓░░█▒░           
        ▒▒        ░░ ▒░░░▒░ ░ ░░░░░░░ ░░                 
            ░   ░        ░                               
          ▒    ░ ▒ ░        ░▒░                                                                                                                                               .                                                                                                            .                                                                                                  .                                     
                """)


# --------------------------------------------RIFTOS HOME SCREEN--------------------------------------------


def home5():
    global current_path
    current_path = "/root/home5"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""      
                 ---------------------------------------------------------------------------------------                                   
                                            ______ _  __ _   _____ _____ 
                                            | ___ (_)/ _| | |  _  /  ___|
                                            | |_/ /_| |_| |_| | | \ `--. 
                                            |    /| |  _| __| | | |`--. \
                                            | |\ \| | | | |_\ \_/ /\__/ /
                                            \_| \_|_|_|  \__|\___/\____/Alpha 1.9 beta 
          

              """)


def home6():
    global current_path
    current_path = "/root/home6"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""  
                 ---------------------------------------------------------------------------------------                         
                                       __________.__  _____  __  ________    _________
                                       \______   \__|/ ____\/  |_\_____  \  /   _____/
                                        |       _/  \   __\\   __\/   |   \ \_____  \ 
                                        |    |   \  ||  |   |  | /    |    \/        \
                                        |____|_  /__||__|   |__| \_______  /_______  /
                                               \/                        \/        \/         

              """)
    
def home3():
    global current_path
    current_path = "/root/home3"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""  
                 ---------------------------------------------------------------------------------------                         
                              /$$$$$$$  /$$  /$$$$$$   /$$      /$$$$$$   /$$$$$$ 
                              | $$__  $$|__/ /$$__  $$ | $$     /$$__  $$ /$$__  $$
                              | $$  \ $$ /$$| $$  \__//$$$$$$  | $$  \ $$| $$  \__/
                              | $$$$$$$/| $$| $$$$   |_  $$_/  | $$  | $$|  $$$$$$ 
                              | $$__  $$| $$| $$_/     | $$    | $$  | $$ \____  $$
                              | $$  \ $$| $$| $$       | $$ /$$| $$  | $$ /$$  \ $$
                              | $$  | $$| $$| $$       |  $$$$/|  $$$$$$/|  $$$$$$/
                              |__/  |__/|__/|__/        \___/   \______/  \______/ 
                                                             

              """)
    

def home4():
    global current_path
    current_path = "/root/home4"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""  
                 ---------------------------------------------------------------------------------------                         
                                      ____   ____  _____  ______   ___   _____
                                     |    \ |    ||     ||      | /   \ / ___/
                                     |  D  ) |  | |   __||      ||     (   \_ 
                                     |    /  |  | |  |_  |_|  |_||  O  |\__  |
                                     |    \  |  | |   _]   |  |  |     |/  \ |
                                     |  .  \ |  | |  |     |  |  |     |\    |
                                     |__|\_||____||__|     |__|   \___/  \___|
                                         

              """)
    
def home1():
    global current_path
    current_path = "/root/home1"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""  
                 ---------------------------------------------------------------------------------------                         
                                           ____  _ ______  ____  _____
                                          / __ \(_) __/ /_/ __ \/ ___/
                                         / /_/ / / /_/ __/ / / /\__ \ 
                                        / _, _/ / __/ /_/ /_/ /___/ / 
                                       /_/ |_/_/_/  \__/\____//____/  
                                         

              """)
    
def home2():
    global current_path
    current_path = "/root/home2"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""  
                 ---------------------------------------------------------------------------------------                         
                                 ██▀███   ██▓  █████▒▄▄▄█████▓ ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓██▒▓██   ▒ ▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒██▒▒████ ░ ▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ░██░░▓█▒  ░ ░ ▓██▓ ░ ▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░██░░▒█░      ▒██▒ ░ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░▓   ▒ ░      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                   ░▒ ░ ▒░ ▒ ░ ░          ░      ░ ▒ ▒░ ░ ░▒  ░ ░
                                   ░░   ░  ▒ ░ ░ ░      ░      ░ ░ ░ ▒  ░  ░  ░  
                                    ░      ░                       ░ ░        ░  
                                                 
                                         

              """)
    
def home7():
    global current_path
    current_path = "/root/home7"
    global host_name
    host_name = "RiftOS"
    os.system('cls')
    os.system('title RiftOS')
    print(white + r"""  
                 ---------------------------------------------------------------------------------------                         
                                           ____  _ ______  ____  _____
                                          / __ \(_) __/ /_/ __ \/ ___/
                                         / /_/ / / /_/ __/ / / /\__ \ 
                                        / _, _/ / __/ /_/ /_/ /___/ / 
                                       /_/ |_/_/_/  \__/\____//____/  
                                         

              """)
    
    

    
    

#-------------------------------------------ff--------------------------------------------------------

def commandmenu():
    print(white + r""" 
          
                                                   ╔════════════╗                       
                                                   ║   --FF--   ║
                                                   ║   --CT--   ║
                                                   ║   --Cls--  ║
                                                   ║  --Clear-- ║ 
                                                   ║-1,2,3,4...-║
                                                   ║  --...--   ║
                                                   ║  --...--   ║
                                                   ║  --...--   ║
                                                   ║ --get-ver--║
                                                   ║  ---os---  ║
                                                   ║  --Tut--   ║
                                                   ║ --Ghome--  ║
                                                   ║ -Time-show-║  
                                                   ║   --Nm--   ║
                                                   ║  --Get--   ║
                                                   ║  --...--   ║
                                                   ║  --...--   ║
                                                   ╚════════════╝

                                                             """)
    #-------------------------------------confirmation--------------------------------------------------------------
def confirm():
    print(white + r"""

                                                ╔═══════════════════╗
                                                ║   Are You Sure?   ║
                                                ║       Y/N         ║
                                                ╚═══════════════════╝
          



          """)
    





 


    

# --------------FIRST LOOP CMD-RIFTOS TERMINAL-------------------------------------------------


def riftos():
    while True:
        cmd = console.input(get_prompt_text()).strip()
        global host_name
        host_name = "RiftOS"

        if cmd.lower() == 'help':
            help()
            

        elif cmd.lower() in ("os-ver", "get-ver", "ver", "version", "rift-ver", "r-ver", "os"):
            print(f"{blue}                                    Operating System RiftOS  {riftos_version}{reset}")

        elif cmd.lower() == 'get':
            print('                                            Using get ', riftos_version)
            

        elif cmd.startswith(("http://", "https://")):
         print(f"{light_blue}                                   Opening link...{reset}")
         webbrowser.open(cmd)

            




        elif cmd.lower() == 'reboot':
            os.system('cls')
            print('Rebooting To CC BootTool...')
            time.sleep(1)
            os.system('cls')
            ccboot()

        
            



        elif cmd.lower() == ("home", "h"):
            home1()            


        elif cmd.lower() == '1':
            home1()

        elif cmd.lower() == '2':
            home2()


        elif cmd.lower() == '3':
            home3()

        elif cmd.lower() == '4':
            home4()

        elif cmd.lower() == '5':
            home5()

        elif cmd.lower() == '6':
            home6()
        
        elif cmd.lower() == '7':
            home7()



        elif cmd.lower() == 'userset':
            user = input('Enter New Username: ')
            global user_name
            user_name = user


        

            
            
                
    #----------------cd directories-----------------------
        elif cmd.lower() == 'cd downloads':
            current_path = "/root/Downloads"
        elif cmd.lower() == 'cd desktop':
            current_path = "/root/Desktop"
        elif cmd.lower() == 'cd documents':
            current_path = "/root/Documents"
        elif cmd.lower() == 'cd trash':
            current_path = "/root/Trash"
        elif cmd.lower() == 'cd /':
            current_path = "/root"
        elif cmd.lower() == 'cd root':
            current_path = "/root"
        elif cmd.lower() == 'cd root/home1':
            current_path = "/root/home1"
        elif cmd.lower() == 'cd root/home2':
            current_path = "/root/home2" 

        elif cmd.lower() == 'cd add':
            cd = input('Enter Directory Path> ')
            current_path = cd






        elif cmd.lower() == 'ff':
            commandmenu()



        elif cmd.startswith("open"):
            filename = cmd[5:]
            try:
                os.startfile(filename)
            except FileNotFoundError:
                print("File not found!")




        elif cmd.lower() in ("riftos", "rift"):
            os.system('cls')
            print('Booting RiftOS To Terminal Type home for ui...')
            time.sleep(1)
            os.system('cls')
            riftos()
        


        elif cmd.lower() in ("gos", "ghome", "galaxyos", "galaxy","gh"):
            galaxy()

        elif cmd.lower() == 'ct':
            ct()

        elif cmd.lower() in ("cls", "clear"):
            os.system('cls')


        elif cmd.lower() == 'colorb':
            os.system('color 1')
            print('Changed colour to blue.')

        elif cmd.lower() == 'colorg':
            os.system('color 2')
            print('Changed colour to green.')

        elif cmd.lower() == 'colorr':
            os.system('color 4')
            print('Changed colour to red.')
        
        elif cmd.lower() == 'colorw':
            os.system('color 7')
            print('Changed colour to white.')
        
        elif cmd.lower() == 'colory':
            os.system('color 6')
            print('Changed colour to yellow.')

        elif cmd.lower() == 'colorp':
            os.system('color 5')
            print('Changed colour to purple.')


            
        elif cmd.lower() in ("apps", "app", "applications", "launch"):
                os.system('cls')
                print(white + r""" 
          
                                                    ╔════════════╗                       
                                                    ║Applications║
                                                    ║ --Batch--  ║ 
                                                    ║ --Python-- ║
                                                    ║ --Notepad--║ 
                                                    ║  --Calc--  ║
                                                    ║  --....--  ║
                                                    ╚════════════╝

                                                             """)
                apps = input(' > ')
                if apps.lower() == '1':
                    print('Launching Batch Environment...')
                    time.sleep(1)
                    os.system('cls')
                    os.system('title Batch Environment')
                    os.system('cmd.exe')

                elif apps.lower() == '2':
                    print('Launching Python Environment...')
                    time.sleep(1)
                    os.system('cls')
                    os.system('title Python Environment')
                    os.system('python')
                    print('Exited Python Environment.')
                elif apps.lower() == '3':
                    print('No Application Found.')
                    print('Launching Notepad...')
                    time.sleep(1)
                    os.system('cls')
                    os.system('notepad.exe')
                




# ----------------CT TERMINAL------------------------------------------------


def ct():
    global host_name
    host_name = "Ct-RiftOS"
    global current_path
    current_path = "/root/Env/DeveloperTerminal" 
    os.system('cls')
    os.system('title CT-RiftOS')
    print('Booting CT terminal.')
    os.system('cls')
    print('CT Succesfully Booted.')
    time.sleep(1)
    while True:
        ct = console.input(get_prompt_text()).strip()

        def rtb():
            text = input(f"{green}Enter text to echo: {reset}")
            print(f"{blue}{text}{reset}")

        def rtg():
            text = input(f"{green}Enter text to echo: {reset}")
            print(f"{green}{text}{reset}")

        def rty():
            text = input(f"{green}Enter text to echo: {reset}")
            print(f"{yellow}{text}{reset}")

        def rtr():
            text = input(f"{green}Enter text to echo: {reset}")
            print(f"{red}{text}{reset}")

        def rtw():
            text = input(f"{green}Enter text to echo: {reset}")
            print(f"{white}{text}{reset}")

        def crtb():
            text = input(f"{green}Enter text to echo: {reset}")
            os.system('cls')
            print(f"{blue}{text}{reset}")

        def calc():
            try:
                expr = input(f"{light_blue}Enter math expression: {reset}")
                result = eval(expr)
                print(f"{yellow}Result: {result}{reset}")
            except Exception as e:
                print(f"{red}Error: {e}{reset}")

        def show_time():
            print(f"{green}Current time: {time.strftime('%H:%M:%S')}{reset}")

        if ct.lower() == 'rtb':
            rtb()

        elif ct.lower() == 'rtg':
            rtg()

        elif ct.lower() == 'rty':
            rty()

        elif ct.lower() == 'rtr':
            rtr()

        elif ct.lower() == 'rtw':
            rtw()

        elif ct.lower() == 'crtb':
            crtb()

        elif ct.lower() == 'home':
            home1()
            riftos()
        
        elif ct.lower() == 'h':
            home1()
            riftos()

        elif ct.lower() == 'ghome':
            galaxy()

        elif ct.lower() == 'time-show':
            show_time()

        elif ct.lower() == 'calc':
            calc()

        elif ct.lower() == 'set-rest':
            home1()
            time.sleep(2)
            os.system('cls')

        elif ct.lower() == 'rm-ct-h':
            os.system('cls')
            error = input(f"{red}ERROR ROOT FOLDER NOT FOUND: {reset}")
            time.sleep(5)
            os.system('cls')
            print(f"{red}OUTPUT = : {reset}")
            time.sleep(100)

        elif ct.lower() == 'rift':
            os.system('cls')
            riftos()

        
            #----------------cd directories-----------------------
        elif ct.lower() == 'cd downloads':
            current_path = "/root/Downloads"
        elif ct.lower() == 'cd desktop':
            current_path = "/root/Desktop"
        elif ct.lower() == 'cd documents':
            current_path = "/root/Documents"
        elif ct.lower() == 'cd trash':
            current_path = "/root/Trash"
        elif ct.lower() == 'cd /':
            current_path = "/root"
        elif ct.lower() == 'cd root':
            current_path = "/root"
        elif ct.lower() == 'cd root/home1':
            current_path = "/root/home1"
        elif ct.lower() == 'cd root/home2':
            current_path = "/root/home2" 

        elif ct.lower() == 'cd add':
            cd1 = input('Enter Directory Path> ')
            current_path = cd1



        elif ct.lower() in ("ct-ver", "ver", "os", "version"):
            print(f"{blue}Ct Version 1.1{reset}")


        elif ct.lower() in ("cls", "clear"):
            print(f"{white}Clearing Screen...{reset}")
            os.system('cls')
        
        elif ct.lower() in ("apps", "app", "applications", "launch"):
                os.system('cls')
                print(white + r""" 
          
                                                    ╔════════════╗                       
                                                    ║Applications║
                                                    ║ --Batch--  ║ 
                                                    ║ --Python-- ║
                                                    ║ --Notepad--║ 
                                                    ║  --Calc--  ║
                                                    ║  --....--  ║
                                                    ╚════════════╝

                                                             """)
                apps = input(' > ')
                if apps.lower() == '1':
                    print('Launching Batch Environment...')
                    time.sleep(1)
                    os.system('cls')
                    os.system('title Batch Environment')
                    os.system('cmd.exe')

                elif apps.lower() == '2':
                    print('Launching Python Environment...')
                    time.sleep(1)
                    os.system('cls')
                    os.system('title Python Environment')
                    os.system('python')
                    print('Exited Python Environment.')
                elif apps.lower() == '3':
                    print('No Application Found.')
                    print('Launching Notepad...')
                    time.sleep(1)
                    os.system('cls')
                    os.system('notepad.exe')
                
                elif apps.lower() == '4':
                    print('Launching Built In RiftOS Calculator...')
                    os.system('cls')
                    calc()

                else:
                    print('No Application Found.')
                    os.system('cls')




                   
                    


            

            
        
        elif ct.lower() == 'colorb':
            os.system('color 1')
            print('Changed colour to blue.')

        elif ct.lower() == 'colorg':
            os.system('color 2')
            print('Changed colour to green.')

        elif ct.lower() == 'colorr':
            os.system('color 4')
            print('Changed colour to red.')
        
        elif ct.lower() == 'colorw':
            os.system('color 7')
            print('Changed colour to white.')
        
        elif ct.lower() == 'colory':
            os.system('color 6')
            print('Changed colour to yellow.')

        elif ct.lower() == 'colorp':
            os.system('color 5')
            print('Changed colour to purple.')
        
        elif ct.lower() == 'systest':
            print('If you crash during the test then there is a problem with Rift. But we will fix it.')
            print('If it says enter text or whatever just press enter those are just some features like repeat.')
            test = input()
            help()
            time.sleep(1)
            confirm()
            time.sleep(1)
            commandmenu()
            time.sleep(1)
            calc()
            time.sleep(1)
            rtr()
            time.sleep(1)
            rtg()
            time.sleep(1)
            rtb()
            time.sleep(1)
            rty() 
            time.sleep(1)
            rtw()
            time.sleep(1)
            show_time()
            time.sleep(1)
            galaxy()
            time.sleep(1)
            confirm()
            time.sleep(1)
            commandmenu()
            time.sleep(1)
            calc()
            time.sleep(1)
            rtr()
            time.sleep(1)
            rtg()
            time.sleep(1)
            rtb()
            time.sleep(1)
            rty() 
            time.sleep(1)
            rtw()
            time.sleep(1)
            show_time()
            time.sleep(1)
            galaxy()
            time.sleep(1)
            confirm()
            time.sleep(1)
            commandmenu()
            time.sleep(1)
            calc()
            time.sleep(1)
            rtr()
            time.sleep(1)
            rtg()
            time.sleep(1)
            rtb()
            time.sleep(1)
            rty() 
            time.sleep(1)
            rtw()
            time.sleep(1)
            show_time()
            time.sleep(1)
            galaxy()
            time.sleep(1)
 
            os.system('cls')
            print('test completed if you did not have any problems then it succeeded...')
            ct()






        elif ct.lower() == 'userset':
            user1 = input('Enter New Username: ')
            global user_name
            user_name = user1


     
            

        
        elif ct.lower() == 'home':
            home1()            


        elif ct.lower() == '1':
            home1()

        
        elif ct.lower() == '2':
            home2()


        elif ct.lower() == '3':
            home3()


        elif ct.lower() == '4':
            home4()

        elif ct.lower() == '5':
            home5()

        elif ct.lower() == '6':
            home6()

        elif ct.lower() == '7':
            home7()
            

        elif ct.lower() == 'get-ver':
            print('Latest RiftOS Version is 1.9.')






        elif ct.lower() == 'help':
            print(white + r"""                      THE HELP COMMAND IS OUTDATED PLEASE USE e FOR A BETTER COMMAND MENU.                         
                                                      --Help-- (Opens This Menu)
                                                     ---rm-ct-h  --- Deletes Root Folder For CT terminal.
                                                      --rm-ct  -- Clears Everything In CT Terminal.
                                                      --ct-ver-- Shows CT Version.    
                                                     ---Calc--- Opens a simple calculator   
                                                     ---Enter--- Click The Enter Button To Exit Out Of Anywhere.  
                                                     ---Time-show--- Shows Current Time.
                                                      --Home--- Goes to the original RiftOS home screen with ct terminal
                                                     ---Ghome--- goes to GalaxyOS home screen with ct terminal
                                                     ---Rt then first letter of a colour--- Repeats You With A Colour.
                                                      ---Crtb --- Clears the screen then Repeats You With Blue.
                                                      ---...---

                                                                  """)
        elif ct.lower() == 'reboot':
            os.system('cls')
            print('Rebooting To CC BootTool...')
            time.sleep(1)
            os.system('cls')

ccboot()





            
















