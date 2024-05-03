from os import system , kill , getpid , name , remove
from colorama import Fore , init
from pystyle import Colorate , Colors
from time import sleep , time
from threading import Thread as thr
from datetime import datetime
from getpass import getuser
from socket import socket , AF_INET , SOCK_STREAM , gethostbyname
from requests import get
from urllib.parse import urlparse

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = '''                                                         
                      ╔╦╗╦ ╦╔═╗  ╔╗ ╔═╗╔╗ ╔═╗  ╦ ╦╔═╗╔═╗╔═╗  ╦╔═╦╦  ╦  ╔═╗╦═╗  The BABA-YAGA Killer
                       ║ ╠═╣║╣   ╠╩╗╠═╣╠╩╗╠═╣  ╚╦╝╠═╣║ ╦╠═╣  ╠╩╗║║  ║  ║╣ ╠╦╝    Terminal and Cmd    
                       ╩ ╩ ╩╚═╝  ╚═╝╩ ╩╚═╝╩ ╩   ╩ ╩ ╩╚═╝╩ ╩  ╩ ╩╩╩═╝╩═╝╚═╝╩╚═      Version 0.1

                ╚╦═══════════════════════════════════════════════════════════════════════════╦╝
           ╔═════╩═══════════════════════════════════════════════════════════════════════════╩═════╗

                              Welcome To ( The BABA YAGA KILLER TERMINAL )

           ╚═══════════════════════════════════════════════════════════════════════════════════════╝
'''

print(Colorate.Horizontal(Colors.blue_to_red,banner,1))

def main():
    system('title [+] --- The BABA YAGA KILLER Terminal - Created By John Wick --- [+]')
    while True:
        try:
            c2 = input(Fore.LIGHTRED_EX+"\n  ╔═══"+Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTYELLOW_EX+f"{getuser()}"+Fore.LIGHTRED_EX+"]"+Fore.LIGHTRED_EX+"\n  ╚══\x1b[38;2;0;255;189m>>> "+Fore.LIGHTGREEN_EX)
            if c2 == '.exit':
                print(f'\n  {red}[{yellow}+{red}] {cyan}Bye {red}Bye {yellow}Bro {green}!');sleep(1);kill(getpid(), 9)
            elif c2 == 'cmd':
                print(f'\n  {yellow}Created {red}By {cyan}John Wick\n  {white}({green}c{white}){yellow} Version {red}1{blue}.{red}0 {magenta}2024 {cyan}OS {red}:{green} Wick')
            elif c2 == 'cls':
                system('cls' if name == 'nt' else 'clear')
                print(Colorate.Horizontal(Colors.blue_to_red,banner,1))
            elif c2 == 'clear':
                system('cls' if name == 'nt' else 'clear')
                print(Colorate.Horizontal(Colors.blue_to_red,banner,1))
            elif c2 == 'ls':
                system('dir')
            elif c2 == 'ifconfig':
                system('ipconfig')
            elif c2 == 'now':
                d = datetime.now()
                print(f'\n  {yellow}Date {red}& {cyan}Time {red}:{green}',d)
            elif c2 == 'uname':
                print(f'\n  {red}John {yellow}Wick {green}OS {blue}Version {red}1{yellow}.{green}0')
            elif c2.split()[0] == 'ping':
                for _ in range(5):
                    try:
                        target = {c2.split()[1]}
                        ip = gethostbyname(target)
                        start_time = time()
                        client_socket = socket(AF_INET, SOCK_STREAM)
                        client_socket.settimeout(5)
                        client_socket.connect(({ip}, 80))
                        client_socket.close()
                        end_time = time.time()
                        response_time = (end_time - start_time) * 1000
                        print(f"{red}Connected to {cyan}{ip}{cyan}:{green} time{green}={green}{response_time:.2f}ms {yellow}protocol{yellow}={yellow}TCP {magenta}port{magenta}={magenta}80")
                    except Exception as e:
                        print(f"\n {blue}Connection timed out")
                    time.sleep(0.4)
            elif c2.split()[0] == 'waf':
                url = c2.split()[1]
                parsed_url = urlparse(url)
                target = parsed_url.netloc
                try:
                    response = get(f"http://ip-api.com/json/{target}")
                    response.raise_for_status()
                    data = response.json()
                    isp = data['as']
                    city = data['city']
                    zone = data['timezone']
                except:
                    pass
                b = f'''
                      ╔╦╗╦ ╦╔═╗  ╔╗ ╔═╗╔╗ ╔═╗  ╦ ╦╔═╗╔═╗╔═╗  ╦╔═╦╦  ╦  ╔═╗╦═╗  The BABA-YAGA Killer
                       ║ ╠═╣║╣   ╠╩╗╠═╣╠╩╗╠═╣  ╚╦╝╠═╣║ ╦╠═╣  ╠╩╗║║  ║  ║╣ ╠╦╝    Terminal and Cmd    
                       ╩ ╩ ╩╚═╝  ╚═╝╩ ╩╚═╝╩ ╩   ╩ ╩ ╩╚═╝╩ ╩  ╩ ╩╩╩═╝╩═╝╚═╝╩╚═      Version 0.1

                  ╚╦═══════════════════════════════════════════════════════════════════════════╦╝
             ╔═════╩═══════════════════════════════════════════════════════════════════════════╩═════╗

                URL  : {url}
                ISP  : {isp}
                CITY : {city}
                ZONE : {zone}

             ╚═══════════════════════════════════════════════════════════════════════════════════════╝

'''
                print(Colorate.Horizontal(Colors.blue_to_green,b,1))
            elif c2 == 'apt update':
                system('mkdir wick-os')
                system('cd wick-os && curl https://github.com/thebabayagakiller/WICK-OS && cd wick-os && python main.py')
            elif c2.split()[0] == 'rm':
                remove(c2.split()[2])
            elif c2.split()[0] == 'mkdir':
                system(f'mkdir {c2.split()[1]}')
            elif c2.split()[0] == 'cat':
                f = open(f'{c2.split()[1]}','r')
                for fil in f:
                    print(fil)
            elif c2.split()[0] == 'nano':
                system(f'notepad {c2.split()[1]}')
            else:
                system(c2)
        except:
            pass

thr(target=main).start()
