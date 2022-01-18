import discord
import asyncio
import random
TOKEN = ''


client = discord.Client()

@client.event
async def on_ready():
    print('Вошли на аккаунт {0.user}'.format(client))
    # activity = discord.Activity(type=discord.ActivityType.watching, name="github.com/BazZziliuS")
    # await client.change_presence(status=discord.Status.online, activity=activity)
    hannel = client.get_channel(921014066724626452)
    await hannel.connect(reconnect=True)


async def ch_pr():
 await client.wait_until_ready()
 statuses = ["github.com/BazZziliuS",f"на {len(client.guilds)} сервера","на тебя!"]
 while not client.is_closed():
   status = random.choice(statuses)
   await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching,name=status))
   await asyncio.sleep(10)
client.loop.create_task(ch_pr())


@client.event
async def on_message(message):
    if message.author == client.user:
       return

    if message.content.startswith('!anubis'):
        await message.channel.send('Дай мне свой дискордик д-дискордик я хочу тебе помурчать так спокойно а может мы вместе помурчим п-помурчим вот так мур мур мур мур мяу мяу', delete_after=10.0)
        await asyncio.sleep(10)

    if message.content.startswith('!FN'):
        await asyncio.sleep(1)
        await message.author.send('**Лучший канал с новостями : https://t.me/FreekNews**', delete_after=10.0)

    if message.content.startswith('!Привет'):
        await asyncio.sleep(1)
        await message.channel.send('Привет {}'.format(message.author.name), delete_after=5.0)
        await message.author.send('👋', delete_after=10.0)

    if message.content.startswith('!OneBlock'):
        embed=discord.Embed(title="OneBlock", description="==============================\n\nКогда открытие? -  После открытия серверов 1.7.10\nКакие там моды? - Список модов можно узнать на форуме https://forum.centurymine.net/index.php?/topic/796-описание-сервера-oneblock/\nКакая версия? - **1.16.5**\n\n==============================\n\n**Список администрации сервера:**\nКуратор - BazZziliuS\nМодератор - RainbowBear\nМодератор - YatochiKun\nПомощник - Odaaw\n\n==============================", color=0xffa033)
        embed.set_thumbnail(url="https://i.imgur.com/OwYDA2b.jpeg")
        embed.set_footer(text="ЧаВо | OneBlock")
        await asyncio.sleep(2)
        await message.channel.send(embed=embed, delete_after=30.0)

    if message.content.startswith('!Java'):
        await asyncio.sleep(1)
        await message.channel.send('Скачать 64 битную джаву можно по ссылке:\nhttps://javadl.oracle.com/webapps/download/AutoDL?BundleId=244584_d7fc238d0cbf4b0dac67be84580cfb4b', delete_after=30.0)
        
    if message.content.startswith('!Memory'):
        await asyncio.sleep(1)
        await message.channel.send('Чтобы выделить нужное количество оперативной памяти:\n1) Запустите лаунчер\n2) Выберите сервер\n3) В правом верхнем углу нажмите на кнопку настроек\n4) Ползунком выберите нужное количество оперативной памяти\n5) Нажмите Сохранить', delete_after=30.0)

    # if message.content.startswith('!OneBlock'):
    #     embed=discord.Embed(title="OneBlock", description="==============================\n**Общая Информация:**\nДата последнего вайпа - **01.01.2025**\nРазмер региона острова: **12х12 чанков , или 192x192 блоков**\nВерсия - **1.16.5**\n\n==============================\n**Список администрации сервера:**\nКуратор - BazZziliuS\nМодератор - RainbowBear\nМодератор - YatochiKun\nПомощник - Odaaw", color=0xffa033)
    #     embed.set_thumbnail(url="https://i.imgur.com/OwYDA2b.jpeg")
    #     embed.set_footer(text="ЧаВо | OneBlock")
    #     await asyncio.sleep(2)
    #     await message.channel.send(embed=embed, delete_after=30.0)

    # if message.content.startswith('!Кабанчик'):
    #     msg = await message.channel.send('Иду к тебе {}'.format(message.author.name))
    #     await asyncio.sleep(5)
    #     await msg.delete()
    #     await message.author.voice.channel.connect(reconnect=True)
    
    # if message.content.startswith('!d1'):
    #     hannel = client.get_channel(915685953455136768)
    #     await hannel.connect(reconnect=True)

    # if message.content.startswith('!d2'):
    #     hannel = client.get_channel(911171824593813535)
    #     await hannel.connect(reconnect=True)

    # if message.content.startswith('!d3'):
    #     hannel = client.get_channel(911555304787963924)
    #     await hannel.connect(reconnect=True)

    if message.content.startswith('!Discord'):
        await message.author.send('Дай мне свой дискордик', delete_after=10.0)
        await asyncio.sleep(1)
        await message.author.send('д-дискордик я хочу тебе', delete_after=9.0)
        await asyncio.sleep(1)
        await message.author.send('помурчать так спокойно', delete_after=8.0)
        await asyncio.sleep(1)
        await message.author.send('а может мы вместе помурчим', delete_after=7.0)
        await asyncio.sleep(1)
        await message.author.send('п-помурчим вот так', delete_after=6.0)
        await asyncio.sleep(1)
        await message.author.send('мур мур мур мур мяу мяу', delete_after=5.0)

client.run(TOKEN)
