import requests
from PIL import Image, ImageDraw, ImageFont
from .. import loader, utils
import io
from asyncio import sleep
@loader.tds
class XuyZnaetMod(loader.Module):
	strings = {"name": "Хуй знает"}
	@loader.owner
	async def xzcmd(self, message):
		text = utils.get_args_raw(message)
		text=text.split(' ')[0]
		if len(text)<=7:
			await message.edit('<code>Качаем...</code>')
			ufr = requests.get("https://github.com/LaciaMemeFrame/FTG-Modules/raw/master/zfont.ttf")
			f = ufr.content
			p = requests.get('https://i.imgur.com/5UDr5Ya.png')
			await message.edit('<code>Открываем...</code>')
			out = open(f"img.jpg", "wb")
			out.write(p.content)
			out.close()
			tatras = Image.open("img.jpg")
			await message.edit('<code>Пишем...</code>')
			idraw = ImageDraw.Draw(tatras)
			font = ImageFont.truetype(io.BytesIO(f), size=30)
			idraw.text((390, 101), text, font=font,fill='black')
			tatras.save('img.webp')
			await message.delete()
			await message.client.send_file(message.to_id,'img.webp')
		else:
			await message.edit('<strong>Не больше 7 букв!</strong>')
	