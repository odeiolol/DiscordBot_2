import discord 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content=='ping':
            await message.channel.send('pong')
        if message.content=='café':
            await message.channel.send(':coffee:')

client=MyClient()
client.run('NzYzNzc5MDMyMDE3MjcyODQ0.X38qpw.0fJuwMSI920jaRR0CST4LnQaIEk')