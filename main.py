from os import system , kill , getpid , name , remove , rmdir
from colorama import Fore , init
from pystyle import Colorate , Colors
from time import sleep , time
from threading import Thread as thr
from datetime import datetime
from getpass import getuser
from socket import socket , AF_INET , SOCK_STREAM , gethostbyname
from requests import get
from urllib.parse import urlparse
from platform import uname

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
            if c2 == 'exit':
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
                system(f'ping {c2.split()[1]}')
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

            elif c2.split()[0] == 'rm':
                remove(f'{c2.split()[2]}')
            elif c2.split()[0] == 'rmdir':
                rmdir(f'{c2.split()[2]}')
            elif c2.split()[0] == 'mkdir':
                system(f'mkdir {c2.split()[1]}')
            elif c2.split()[0] == 'cat':
                f = open(f'{c2.split()[1]}','r')
                for fil in f:
                    print(fil)
            elif c2.split()[0] == 'nano':
                system(f'notepad {c2.split()[1]}')
            elif c2 == 'help':
                banr = f'''{yellow}                      ╔╦╗╦ ╦╔═╗  ╔╗ ╔═╗╔╗ ╔═╗  ╦ ╦╔═╗╔═╗╔═╗  ╦╔═╦╦  ╦  ╔═╗╦═╗  {green}The {blue}BABA{red}-{cyan}YAGA{yellow} Killer{blue}
                       ║ ╠═╣║╣   ╠╩╗╠═╣╠╩╗╠═╣  ╚╦╝╠═╣║ ╦╠═╣  ╠╩╗║║  ║  ║╣ ╠╦╝    {green}Terminal {red}and {blue}Cmd{red}    
                       ╩ ╩ ╩╚═╝  ╚═╝╩ ╩╚═╝╩ ╩   ╩ ╩ ╩╚═╝╩ ╩  ╩ ╩╩╩═╝╩═╝╚═╝╩╚═      {blue}Version {yellow}0{red}.{green}1

                  ╚╦═══════════════════════════════════════════════════════════════════════════╦╝
             ╔═════╩═══════════════════════════════════════════════════════════════════════════╩═════╗
                
		{red}[{yellow}+{red}]{cyan} clear    {red}:{green} clear page
                {red}[{yellow}+{red}]{cyan} cmd      {red}:{green} show terminal info
                {red}[{yellow}+{red}]{cyan} exit     {red}:{green} exit
                {red}[{yellow}+{red}]{cyan} now      {red}:{green} show date & time
                {red}[{yellow}+{red}]{cyan} ifconfig {red}:{green} ipconfig
		{red}[{yellow}+{red}]{cyan} uname    {red}:{green} show system
		{red}[{yellow}+{red}]{cyan} ls       {red}:{green} show directory
		{red}[{yellow}+{red}]{cyan} ping     {red}:{green} pinging | usage : ping target_ip
		{red}[{yellow}+{red}]{cyan} rm       {red}:{green} remove file | usage : rm filename
		{red}[{yellow}+{red}]{cyan} rmdir    {red}:{green} remove folder | usage : rmdir folder_name
		{red}[{yellow}+{red}]{cyan} mkdir    {red}:{green} create folder | usage : mkdir foldername
		{red}[{yellow}+{red}]{cyan} cat      {red}:{green} show text or ... on screen | usage : cat filename
		{red}[{yellow}+{red}]{cyan} nano     {red}:{green} open notepad for write | usage : filename
                {red}[{yellow}+{red}]{cyan} uname -a {red}:{green} show real system info
                {red}[{yellow}+{red}]{cyan} waf         {red}:{green} detect waf | usage : waf https://target.com
                {red}[{yellow}+{red}]{cyan} and more cmd commands {red}.{yellow}.{blue}.{green}
               
	     ╚═══════════════════════════════════════════════════════════════════════════════════════╝'''
                system('cls' if name == 'nt' else 'clear')
                print(banr)
            elif c2 == 'uname -a':
                print(f'\n  {cyan}{uname()}')
            else:
                system(c2)
        except:
            pass

thr(target=main).start()
