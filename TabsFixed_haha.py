from bs4 import BeautifulSoup
import requests
import random

from .. import loader
from asyncio import sleep
@loader.tds
class AtiksDMod(loader.Module):
    strings = {"name": "AtiksD"}
    @loader.owner
    async def spamporncmd(self, message):
        await message.edit('Ку')
        pics=[]
        await message.edit('Ку-Ка')
        for q in range(3):
            w=random.randint(0,10)
            page = requests.get(f'https://pornpic.com/popular?page={w}')
            soup = BeautifulSoup(page.text, 'lxml')
            news = soup.findAll('img')
            for i in news:
                if i['src']!='images/logo.png':
                    pics.append(f"https://pornpic.com/{i['src']}")
                else:
                    pass
        await message.edit('Ку-Ка-Ре')
        for i in pics:
            if i=='https://pornpic.com//images/logo.png':
                pass
            else:
                p = requests.get(i)
                out = open(f"img.jpg", "wb")
                out.write(p.content)
                out.close()    
                await message.client.send_file(message.chat.id, 'img.jpg')    
        await message.edit('Ку-Ка-Ре-Ку')


