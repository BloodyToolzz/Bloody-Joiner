import os
import time
import random
import pystyle
import requests

from pystyle import *
from console.utils import set_title

h_h2 = ["Halal", "Haram"]

banner = '''
 ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄▓██   ██▓    ▄▄▄██▀▀▀▒█████   ██▓ ███▄    █ ▓█████  ██▀███  
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██  ██▒      ▒██  ▒██▒  ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌ ▒██ ██░      ░██  ▒██░  ██▒▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌ ░ ▐██▓░   ▓██▄██▓ ▒██   ██░░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓  ░ ██▒▓░    ▓███▒  ░ ████▓▒░░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒   ██▒▒▒     ▒▓▒▒░  ░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▓██ ░▒░     ▒ ░▒░    ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ▒ ▒ ░░      ░ ░ ░  ░ ░ ░ ▒   ▒ ░   ░   ░ ░    ░     ░░   ░ 
 ░          ░  ░    ░ ░      ░ ░     ░    ░ ░         ░   ░      ░ ░   ░           ░    ░  ░   ░     
      ░                            ░      ░ ░                                                        
Made by Bloody | https://discord.gg/sJTjPzaPT5 | https://github.com/BloodyToolzz
'''

def clear():
    os.system('cls')

def pause():
    os.system('pause >nul')

clear()

set_title("[Bloody Token Joiner] | Made By: Bloody | Loading...")
Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, time=3)
Write.Print(f"This program is:", Colors.purple_to_blue, interval=0)
Write.Print(f" {random.choice(h_h2)}\n", Colors.green_to_white, interval=0)
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

set_title("[Bloody Token Joiner] | Made By: Bloody | Input Server Invite URL")
invite_url = Write.Input("[>] Enter a Discord invite URL:\n", Colors.purple_to_blue, interval=0.008)
invite_code = invite_url.split("/")[-1]

set_title("[Bloody Token Joiner] | Made By: Bloody | Input Discord Token")
authorization_token = Write.Input("[>] Enter your Discord token:\n", Colors.purple_to_blue, interval=0.008)

api_invite_url = "https://discord.com/api/v9/invites/" + invite_code
clear()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

resp = requests.post(api_invite_url, headers={"Authorization": authorization_token})

if resp.ok:
    set_title(f"[Bloody Token Joiner] | Made By: Bloody | Successfully Joined! | discord.gg/{invite_code}")
    Write.Print(f"Bloody | Successfully joined the server, discord.gg/{invite_code}\n", Colors.purple_to_blue, interval=0.008)
    Write.Print("Press any key to continue . . .", Colors.purple_to_blue, interval=0.008)
    pause()
else:
    set_title(f"[Bloody Token Joiner] | Made By: Bloody | Failed To Join Server! | {resp.status_code}, {resp.text}")
    Write.Print(f"Bloody Token Joiner | Error | {resp.status_code}, {resp.text} | Token/Invite Invalid!\n", Colors.red_to_yellow, interval=0.008)
    Write.Print("Press any key to continue . . .", Colors.purple_to_blue, interval=0.008)
    pause()
