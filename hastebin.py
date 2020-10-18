from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
@loader.tds
class HastebinMod(loader.Module):
	strings = {"name": "Hastebin"}
	@loader.owner
	async def hastecmd(self, message):
		media=False
		reply_to=False
		user_msg=f"""{utils.get_args_raw(message)}"""
		reply=await message.get_reply_message()
		if reply:
			if reply.media:
				user_msg=reply.media
				media=True
				reply_to=True
			else:
				user_msg = f"""{reply.text}""" 
				reply_to=True
		else:
			pass
		await message.edit('<code>Ждем...</code>')
		async with message.client.conversation('@hastebin_bbot') as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True,
				                                             from_users=1358418309))
				if media:
					await message.client.send_file('@hastebin_bbot', user_msg)
				else:
					await message.client.send_message('@hastebin_bbot', user_msg)
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Разблокируй </code> @hastebin_bbot')
				return
			await message.delete()
			if reply_to:
				await message.client.send_message(message.to_id,response.message,reply_to=reply.id)
			else:
				await message.client.send_message(message.to_id,response.message)