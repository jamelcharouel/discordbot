import discord

TOKEN = "YOURTOKENHERE"

client = discord.Client()
realgames = ["tf2", "csgo", "cs", "dunderlords"]


@client.event
async def on_message(message):
        if message.author == client.user:
            return

        # add your guild ID here, there's likely a way to make this more general but I couldn't find it quickly
        guild = client.get_guild(123456)
        channel = message.channel
        print(channel.name)

        if message.content.startswith('!game'):
            game = message.content.split(' ')[1]
            if game_is_real(game):
                for role in message.author.roles:
                    reply = "Who's up for some {} {}?".format(game, role.mention)
                    await channel.send(reply)
            else:
                reply = "That's not a real game silly goose! {}".format(message.author.mention)
                await channel.send(reply)

        if message.content.startswith('!fa'):
            reply = ':100: :100: :100: ey yo friendly armadillo! :100: :100: :100:'
            await channel.send(reply)
        
        if message.content.startswith('!100mention'):
            name = message.content.split(' ')[1]
            reply = ":100: :100: :100: {} :100: :100: :100:".format(name)
            await channel.send(reply)


        if message.content.startswith('!list'):
            mems = list(filter(lambda mem: mem.status == discord.Status.online, guild.members))
            for member in mems:
                if member == message.author:
                    return

                reply = str(member.name)
                await channel.send("{} games???".format(member.mention))
            #members = filter(lambda mem: mem.activity == Game, guild.members)
            #print(list(members))
            #await client.send_message(message.channel, reply)

        if message.content.startswith('!help'):
            reply = """Welcome to Jam's discord bot! Here are the current commands I've decided to program on this thing:
            "!game {game}" -> fill in {game} with a real game and call all your friends to play with you
            "!fa" -> friendly armadillo!
            "!100mention {name}" -> mention your friends!
            "!list" -> mention everyone in the channel who's online and call them for some games
            """

            await channel.send(reply)

def game_is_real(game):
   return game.lower() in realgames 

@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)
    print("---------------")


client.run(TOKEN)
