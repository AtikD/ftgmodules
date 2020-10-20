from .. import loader
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from asyncio import sleep
@loader.tds
class UserHistoryMod(loader.Module):
	strings = {"name": "UserHistory"}
	@loader.owner
	async def userhistorycmd(self, message):
		reply=await message.get_reply_message()
		idd=message.id
		if reply:
			if reply.media:
				await message.edit('К сожалению бот не работает с файлами.')
				return
			idd=reply.id
		await message.edit('<code>Жди...</code>')
		async with message.client.conversation('@sangmatainfo_bot') as silent:
			try:
				response = silent.wait_event(events.NewMessage(incoming=True,
				                                             from_users=461843263
				                                             ))
				response2 = silent.wait_event(events.NewMessage(incoming=True,
				                                             from_users=461843263))
				await message.client.forward_messages('sangmatainfo_bot' ,idd,message.to_id)
				response = await response
				if response.message.text =='Forward any message to this chat to see user history.':
					await message.edit('Настройки конфидитиальности пользователя не позволяют узнать историю.')
					return
				response2 = await response2
				await message.client.send_message(message.to_id,f'<b>{response.message.text}</b>',reply_to=reply.id)
				await message.client.send_message(message.to_id,f'<b>{response2.message.text}</b>',reply_to=reply.id)
				await message.delete()
			except YouBlockedUserError:
				await message.edit('<code>Разблокируй </code> @voicybot')
				return