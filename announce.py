import discord
import datetime
import asyncio
import time
import os
client = discord.Client()

@client.event
async def on_ready():
    await bt(["저희는"+ str(len(client.guilds)) + "개의 서버와"+ str(len(client.users)) +"명의 유저분들과 함께하고있어요!", '문의는 Miasoul#0811 으로!'])
    global opal
    print("봇 정상 작동")

@client.event
async def bt(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(5)

   

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1:
        return None

    if str(reaction.emoji) == "✅":
        global opal
        role = discord.utils.get(user.guild.roles, name=opal)
        await user.add_roles(role)

       

@client.event
async def on_message(message):
    if message.content.startswith('!!역할'):
        global opal
        opal = message.content[5:]
        i = (message.author.guild_permissions.administrator)
        if i is True:
            embed = discord.Embed(title="역할봇",description="역할!", color=0x00aaaa)
            embed.add_field(name="역할 받기", value= opal + "역할을받으실분들은 아래의 체크 이모지를 눌러주세요", inline=False)
            msg = await message.channel.send(embed=embed)
            await msg.add_reaction("✅")        
        if i is False:
            await message.channel.send("{}님은 관리자가 아닙니다", format(message.author.mention))   
               



    if message.content.startswith ("!!공지"):
        
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content.split(" ")[1]
            chanid = message.content.split(" ")[2]
            channel = client.get_channel(chanid)
            embed = discord.Embed(title="**공지사항 제목 *", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),color=0x00ff00)
            embed.set_footer(text="Bot Made by. Miasoul#0811 | 담당 관리자 : {}".format(message.author))
            
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel(channel.id), message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith ("!!청소"):
        leg = message.content[4:]
        i = (message.author.guild_permissions.administrator)
        if i is True:
            await message.delete()
            await message.channel.purge(limit=int(leg))
            await message.channel.send("메세지 {} 개가 {}님의 요청으로 인해 삭제되었습니다".format(leg, message.author))
            await message.author.send("메세지 삭제완료")
        
        
        if i is False:
            await message.channel.send("{}님은 관리자가 아닙니다".format(message.author.mention))

        
        
        
        
        
        
acces_token = os.environ["BOT_TOKEN"]        

client.run(acces_token)
