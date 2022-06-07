import requests
import pystyle
import time
import os
from pystyle import *
from console.utils import set_title

banner = '''
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗         ██╗ ██████╗ ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝         ██║██╔═══██╗██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝          ██║██║   ██║██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝      ██   ██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║       ╚█████╔╝╚██████╔╝██║██║ ╚████║███████╗██║  ██║
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝        ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

Made by Bloody | https://discord.gg/sJTjPzaPT5 | https://youtube.com/c/ScriptHubRoblox
'''
set_title("Bloody Token Joiner | Made by Bloody | Loading...")
Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, enter=True)
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

set_title("Bloody Token Joiner | Made by Bloody | Input Server Invite URL")
invite_url = Write.Input("[>] Enter a Discord invite URL:\n", Colors.purple_to_blue, interval=0.008)
invite_code = invite_url.split("/")[-1]

set_title("Bloody Token Joiner | Made by Bloody | Input Discord Token")
authorization_token = Write.Input("[>] Enter your Discord token:\n", Colors.purple_to_blue, interval=0.008)

api_invite_url = "https://discord.com/api/v9/invites/" + invite_code
time.sleep(2)
os.system('cls')

resp = requests.post(api_invite_url, headers={"Authorization": authorization_token})

if resp.ok:
    set_title("Bloody Token Joiner | Made by Bloody | Successfully Joined!")
    Write.Print("Bloody | Successfully joined the server\n", Colors.purple_to_blue, interval=0.008)
    os.system('pause >nul')
else:
    set_title("Bloody Token Joiner | Made by Bloody | Failed To Join Server!")
    Write.Print(f"{resp.status_code}, {resp.text} | Token/Invite Invalid!\n", Colors.purple_to_blue, interval=0.008)
    Write.Print("Press any key to continue . . .", Colors.purple_to_blue, interval=0.008)
    os.system('pause >nul')
