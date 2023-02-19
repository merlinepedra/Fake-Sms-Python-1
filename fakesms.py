import re
import os
import time
import platform
import base64

print("[*] Checking Requirements Module")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import strstyle
        from strstyle import *
    except ImportError:
        os.system("python3 -m pip install strstyle -q -q -q")
        import strstyle
        from strstyle import *
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import strstyle
        from strstyle import *
    except ImportError:
        os.system("python -m pip install strstyle -q -q -q")
        import strstyle
        from strstyle import *
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
banner = Center.XCenter("""
************************************************************************
*                _______ _    _  _______     ____  __  __ ______        *
*               / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\ \`      *
*              | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |      *
*             < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) |> >     *
*              | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/| |      *
*               \_\                                           /_/       *
*                                                                       *
************************************************************************               
                            \n\n
""")

def check_net1():
    print(termcolor.colored("[*] Checking Internet Connection:- ", 'cyan'))
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(strstyle.green("\n[*] Connected to the Internet"))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        menu()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(strstyle.red('[*] NO Internet Connection!...'))


def menu():
    ans = True
    while ans:
        print(termcolor.colored("""
      1.Usage
      2.Send SMS
      3.Exit/Quit
      """, 'yellow'))
        ans = input(strstyle.cyan('[*] Choose From Above:- '))
        if ans == "1":
            print("\033c")
            usage1()
        elif ans == "2":
            print("\033c")
            main_check1()
        elif ans == "3":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            print(strstyle.green('\n [+] Thanks For Using Fake-SMS! See You Tomorrow'))
            ans = None
        else:
            print(strstyle.red('[*] Not A Valid Choice!...'))


def usage1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))

    print(termcolor.colored('''
      \n    1. Your Country Code Must Be without +
    2. Country Code Example: 91
    3. Your Phone Number Must be Start Without 0
    4. Full Usage: 913443210111

    ..........NOTE: Only One Text Message Is Allowed Per Day...........

      ''', 'magenta'))


def main_check1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))

    x = input(strstyle.magenta('\n[*] Enter Your Number:- '))
    y = input(strstyle.magenta('\n[*] Enter Your Message:- '))
    message = base64.b64decode('aHR0cHM6Ly90ZXh0YmVsdC5jb20vdGV4dA=='.encode('ascii')).decode('ascii')
    resp = requests.post(f'{message}', {
        'phone': x,
        'message': y,
        'key': 'textbelt',
    })
    print(strstyle.yellow(f'\n[*] Sending Message To:-  ',{x}))
    time.sleep(2)
    z = str(resp.json())
    n = 'False'
    if re.search(n, z):
        print(strstyle.red('\n[ X ] Message not sent! Please Try Again SomeTime Or Use Any Eurpose Based Vpn'))
    else:
        print(strstyle.green('\n[ ✔ ] Message sent ', 'green'))


def op():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check_net1()
        elif platform.system().startswith("Linux"):
            print("\033c")
            check_net1()
        else:
            print(strstyle.red("Please Use Windows Or Linux OS!"))
    except KeyboardInterrupt:
        print(strstyle.red("\n [*]You Pressed The Exit Button!"))
        quit()
op()
