from .. import loader
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from asyncio import sleep
@loader.tds
class VoiceToTextMod(loader.Module):
	strings = {"name": "Voice To Text"}
	@loader.owner
	async def vttcmd(self, message):
		reply=await message.get_reply_message()
		media=''
		if reply:
			if reply.media:
				media=reply.media
			else:
				await message.edit('<strong>Это не войс!</strong>')
				return				
		else:
			await message.edit('<strong>А где войс?</strong>')
			return
		await message.edit('<code>Ждем</code>')
		try:
			await message.client.send_message('@voicybot', '/l ru')
		except YouBlockedUserError:
			await message.edit('<code>Разблокируй </code> @voicybot')
			return
		await message.edit('<code>Ждем.</code>')
		async with message.client.conversation('@voicybot') as silent:
			try:
				sresponse = silent.wait_event(events.NewMessage(incoming=True,
				                                             from_users=259276793))
				await message.client.send_message('@voicybot', '/silent')
				sresponse = await sresponse
				if '😶' in f'{sresponse.message}':
					pass
				else:
					await message.client.send_message('@voicybot', '/silent')
					await sleep(0.5)
			except YouBlockedUserError:
				await message.edit('<code>Разблокируй </code> @voicybot')
				return			
			await message.edit('<code>Ждем..</code>')
		async with message.client.conversation('@voicybot') as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True,
				                                             from_users=259276793))
				if media:
					await message.client.send_file('@voicybot', media)
				else:
					await message.edit('<strong>Неизвестная ошибка!</strong>')
				response = await response
				await message.edit('<code>Ждем...</code>')
				await message.delete()
				await message.client.send_message(message.to_id,response.message,reply_to=reply.id)
			except YouBlockedUserError:
				await message.edit('<code>Разблокируй </code> @voicybot')
				return
