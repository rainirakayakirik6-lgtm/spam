import time, os, platform, requests
from telethon import TelegramClient, events

green = '\x1b[92m'
yellow = '\x1b[93m'
purple = '\x1b[95m'
off = '\x1b[m'
flag = '\x1b[47;30m'
kd = platform.uname().release

api_id = 24366544
api_hash = '1515d479c1ebc1c8177c39e474f77b95'
	
def run():
...
	 
if __name__ == '__main__':
	os.system('clear')
	hdr = { "User-Agent": "Mozilla/5.0" }
	req = requests.get("https://jiro52.github.io/akseskode/", headers=hdr).content
	if f"x_{kd}" in str(req): 
		print(f"{purple}Masa aktif bot sudah habis\nSilahkan hubungi t.me/adiTekno \nUntuk melakukan perpanjangan")
		exit()
	elif f"k_{kd}" in str(req): 
		os.system('rm -rf bot.py')
	else:
		os.system('clear')
		main()
