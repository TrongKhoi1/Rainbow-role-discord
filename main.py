import discord
import asyncio
import random

token = 'Dán token vào đây'
serverid = 123456789101112
rainbowrolename = "Tên role"
delay = 5 #delay thấp quá đứng hình ráng chịu


client = discord.Client()
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print(f"Đã tìm thấy role {rainbowrolename}")
            print("Bắt đầu đổi màu..."
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("Không thể đổi màu role. Vui lòng kiểm tra role của bot cao hơn role màu hay chưa và bật quyền chỉnh sửa role")
                    pass
                await asyncio.sleep(delay)
    print(f'Không tìm thấy role {rainbowrolename} ')
    print("Tiến hành tạo role")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("Đã tạo role!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("Bật cho bố cái quyền tạo role coi ?")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Vịt ngu dcmm chết đi')
    print('------------')

client.run(token)
