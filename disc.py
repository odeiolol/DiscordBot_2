import discord 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content=='\palmas':
            await message.channel.send(':clap:')
        if message.content=='\cafézinho':
            await message.channel.send(':coffee:')

        if message.content=='\bravo':
            await message.channel.send(':angry:')
        if message.content=='\café da manha':
            await message.channel.send(':coffee: :knife: :bread: ')
        



        if message.content=='\astolfo':
            await message.channel.send('https://tenor.com/view/astolfo-plushy-gif-13306557')
        if message.content=='\horny is back':
            await message.channel.send('https://tenor.com/view/ganyu-horny-is-back-horny_is_back-gif-20085349')

client=MyClient()
client.run('NzYzNzc5MDMyMDE3MjcyODQ0.X38qpw._HYFUwH5TqJ-gDnLtet232gSvB0')
