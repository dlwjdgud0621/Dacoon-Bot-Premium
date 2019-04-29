import asyncio
import discord
import time
import random
import datetime
from parser import *
import os
import openpyxl
from turtle import *
import turtle as ttl
import as

app = discord.Client()

access_token = os.environ["BOT_TOKEN"]
token = access_token
@app.event
async def on_ready():
    print("Log in to next : ")
    print(app.user.name) 
    print(app.user.id)
    print("===============")
    await app.change_presence(game=discord.Game(name="v1.1.0(19:26a)|Dacoon Bot Premium", type=0))

@app.event
async def on_message(message):
    
    if message.content == ">안녕":
        await app.send_message(message.channel, message.author.mention+"님, 안녕하세요.")

    elif message.content.startswith(">계산"):
        await app.send_message(message.channel, embed=discord.Embed(description=("`"+message.content[4:]+"`의 계산 결과는 `"+str(eval(message.content[4:]))+"`입니다.")))

    elif message.content == ">시간":
        time = datetime.datetime.now()
        await app.send_message(message.channel, embed=discord.Embed(description=("지금은 `"+str(time.hour)+"`시 `"+str(time.minute)+"`분 `"+str(time.second)+"`초 입니다.")))

    elif message.content == ">임베드":
        embed = discord.Embed(title="이거슨 제목이라 합니다!", description="이거슨 설명이라고 합니다!", color=0x00ff00)
        embed.set_footer(text="이거슨 푸터라고 합니다!")
        embed.set_image(url="https://i.imgur.com/xzPCXp8.jpg")
        await app.send_message(message.channel, embed=embed)

    elif message.content == ">업데이트":
        embed = discord.Embed(title="버전 업그레이드 알림", description="v1.1.0(19:26a)|Dacoon Bot Premium", color=0x00ff00)
        embed.set_footer(text="Dacoon Bot Premium")
        embed.add_field(name='업데이트 소식', value='듀크에 `output`명령어 추가 : 사용법 = `듀크 output.출력할 내용`', inline=False)
        await app.send_message(message.channel, embed=embed)

    elif message.content == ">섬광탄":
        await app.send_message(message.channel, "https://media.discordapp.net/attachments/507167230157520896/558946449753243658/Untitled1.gif")

    elif message.content.startswith(">투표"):
        vote = message.content[4:].split(">")
        await app.send_message(message.channel, embed=discord.Embed(description=("투표 : "+vote[0])))
        He = "투표 / "
        for i in range(1, len(vote)):
            He = He+vote[i]
            choose = await app.send_message(message.channel, "```"+vote[i]+"```")
            await app.add_reaction(choose, '💖')

    elif message.content.startswith(">선택"):
        vote = message.content[4:].split(">")
        await app.send_message(message.channel, embed=discord.Embed(description=(random.choice(vote))))

    elif message.content.startswith(">명령어 집합 만들기"):
        file = open("stu//"+message.content[12:]+".txt", "w")
        dfile = open("stu//명령어집합이름.txt", "a")
        dfile.write("\\"+message.content[12:])
        await app.send_message(message.channel, embed=discord.Embed(description="명령어 집합 만들기에 성공하였습니다."))
        file.close()

    elif message.content.startswith(">>도배1"):
        anum=message.content[5:].split(">")
        for x in range(int(int(anum[1])/200)):
            await app.send_message(message.channel, (anum[0]+"\n")*200)
        await app.send_message(message.channel, (anum[0]+"\n")*int(anum[1])%200)

    elif message.content.startswith(">>도배2"):
        anum = message.content[5:].split(">")
        a=anum[0];
        await app.send_message(message.channel, a*int(anum[1]))

    elif message.content.startswith(">명령어 추가"):
        vote = message.content[8:].split(">")
        file = open("stu//"+vote[0]+".txt", "a")
        file.write("|"+vote[1]+"\\"+vote[2])
        await app.send_message(message.channel, embed=discord.Embed(description="학습에 성공하였습니다."))
        file.close()

    elif message.content.startswith(">명령어 실행"):
        file = open("stu//"+message.content[8:].split(">")[0]+".txt", "r")
        ques = file.read().split("|")
        for x in range(0, len(ques)):
            if message.content[8:].split(">")[1] == ques[x].split("\\")[0]:
                await app.send_message(message.channel, embed=discord.Embed(description=str(ques[x].split("\\")[1])))

    elif message.content.startswith(">명령어 모음"):
        file = open("stu//"+message.content[8:]+".txt", "r")
        txtx = "명령어 집합 : "+message.content[8:]+"\n"
        dff = file.read().split("|")
        for x in range(1, len(dff)):
            txtx = txtx + "```" + (dff[x].split("\\")[0]) + "```\n"
        await app.send_message(message.channel, embed=discord.Embed(description=str(txtx)))

    elif message.content == ">명령어 집합":
        file = open("stu//명령어집합이름.txt", "r")
        txtx = "명령어 집합 이름\n"
        df = file.read().split("\\")
        for x in range(0, len(df)):
            txtx = txtx + "```" + df[x] + "```\n"
        await app.send_message(message.channel, embed=discord.Embed(description=txtx))

    elif message.content.startswith("&"):
        file = open("stu//명령어집합이름.txt", "r")
        txtx = "명령어 집합 이름\n"
        df = file.read().split("\\")
        for x in range(1, len(df)):
            nfile = open("stu//"+df[x]+".txt", "r")
            ques = nfile.read().split("|")
            for y in range(1, len(ques)):
                if message.content[1:] == ques[y].split("\\")[0]:
                    await app.send_message(message.channel, embed=discord.Embed(description=str(ques[y].split("\\")[1])))

    elif message.content.startswith("듀크"):
        progressf = message.content[3:].split(".")

        if progressf[0]=="output":
            await app.send_message(message.channel, progressf[1])

    elif message.content == ">내정보":
        date=datetime.datetime.utcfromtimestamp(((int(message.author.id)>>22)+1420070400000)/1000)
        embed=discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 별명", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month)+"월"+str(date.day)+"일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await app.send_message(message.channel, embed=embed)

app.run(token)
