import discord
from discord.ext import commands
import time
import os
import asyncio
import random

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def attackpolicy(ctx, policyid):
    name = ctx.author.name
    file=open(".//User info//"+name+".txt","r")
    Save = file.read()
    file.close()
    savedata=Save.split("_")
    if policyid == "1":
        await ctx.send("Policy set to destroy as much as possible when attacking")
    else:
        if policyid == "2":
            await ctx.send("Policy set to leave inf alone but take money")
        else:
            await ctx.send("Use a vaild id")
            policyid = savedata[4]
            
    savedata[4] = policyid
    file=open(".//User info//"+name+".txt","w+")
    Save="_".join(savedata)
    file.write(Save)
    file.close()
    
    

@client.command()

async def create_nation(ctx, nationname , member : discord.Member):
    data=nationname,"has been created if you run this command again your nation will be reset"
    user = str(member)
    name = user.split("#")
    name = name[0]
    file = open(".//User info//"+name+".txt","w+")
    savedata = nationname,"200","10","0","1","0"

    Save = "_".join(savedata)

    file.write(Save)
    file.close()
    await ctx.send(data)

@client.command()
@commands.cooldown(7, 60, commands.BucketType.user)
async def tax(ctx):

    name = ctx.author.name
    file=open(".//User info//"+name+".txt","r")
    Save = file.read()
    savedata = Save.split("_")
    file.close()
    inf = savedata[2]
    inf = int(inf)
    cash = inf/2
    cash = round(cash)
    money = int(savedata[1])
    cashgain = money + cash
    cash = str(cash)
    info= "You have gained ",cash," from taxes"
    Info= "_".join(info)
    await ctx.send(Info)
    
    cashgain=str(cashgain)
    savedata[1] = cashgain
    Save = "_".join(savedata)
    print(savedata)
    print(name,info)
    file = open("./User info//"+name+".txt","w+")
    file.write(Save)
    file.close()


@tax.error
async def tax_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

@client.command()
async def buy_inf(ctx, amount):
    name = ctx.author.name
    file = open(".//User info//"+name+".txt","r")
    Save = file.read()
    savedata = Save.split("_")
    inf=savedata[2]
    inf = int(inf)
    amount=int(amount)
    price = amount*10
    
    file.close()
    prices = str(price)
    data = "it will cost you ",prices," Enter y to agree enter n to disagree"
    data = "".join(data)
    await ctx.send(data)
    msg = await client.wait_for("message")
    
    message = msg.content
    if message == "y":
        money = savedata[1]
        money = int(money)
        if money > price:
            cash = money-price
            cash = str(cash)
            
            savedata[1] = cash
            inf = inf + amount
            inf = str(inf)
            savedata[2] = inf
            savedata = "_".join(savedata)
            file=open(".//User info//"+name+".txt","w")
            file.write(savedata)
            file.close()
            await ctx.send("Success infrastructure bought successfully!")
        else:
            await ctx.send("You cannout afford this")
    else:
        await ctx.send("You either misstyped or typed n, stopping buying infrastructer")
        
@client.command()
async def buy_ships(ctx, amount):
    name = ctx.author.name
    file=open(".//User info//"+name+".txt","r")
    Save = file.read()
    savedata = Save.split("_")
    if savedata[5] == "0":
        await ctx.send("You dont have any shipyards")
    else:
        
        inf = savedata[2]
        amount = int(amount)
        inf = int(inf)
        shipyard = savedata[5]
        shipyard = int(shipyard)

        price = amount*5000
        price = price - shipyard
        if price < 300:
            price = 300
        print(price)
        
        file.close()
        Price = str(price)
        data="It will cost you ",Price," enter y to confirm and n to decline"
        data= "".join(data)
        await ctx.send(data)

        msg = await client.wait_for("message")
        message = msg.content
        if message == "y":
            money = savedata[1]
            tanks = savedata[3]
            money = int(money)
            tanks = int(tanks)

            if money > price:
                money=money-price
                money=str(money)
                savedata[1] = money
                amount = amount*100
                tanks = tanks + amount
                tanks = str(tanks)
                savedata[3] = tanks
                Save = "_".join(savedata)
                file=open(".//User info//"+name+".txt","w")
                file.write(Save)
                file.close()
                await ctx.send("succesfully bought spacecraft")
            else:
                await ctx.send("Not enough money")
        else:
         await ctx.send("User entered no")

            
@client.command()
async def buy_shipyards(ctx, amount):
    name = ctx.author.name
    file=open(".//User info//"+name+".txt","r")
    Save = file.read()
    file.close()
    savedata = Save.split("_")
    shipyards = savedata[5]
    
    amount = int(amount)
    shipyards = int(shipyards)
    if shipyards == 0:
        Shipyards = 5
    else:
        Shipyards = int(shipyards)
    price = amount*5000
    price = price * Shipyards
    Price = str(price)
    Amount = str(amount)
    message = "It will  cost you ",Price," to buy ",Amount," shipyards y/n"
    message = "".join(message)
    await ctx.send(message)
    msg = await client.wait_for("message")
    message = msg.content
    if message == "y":
        money = savedata[1]
        shipyards = savedata[5]
        money = int(money)
        shipyards = int(shipyards)

        if money > price:
            money=money-price
            money=str(money)
            savedata[1] = money
            
            shipyards = shipyards + amount
            shipyards = str(shipyards)
            savedata[5] = shipyards
            Save = "_".join(savedata)
            file=open(".//User info//"+name+".txt","w")
            file.write(Save)
            file.close()
            await ctx.send("succesfully bought shipyards")
        else:
            await ctx.send("Not enough money")
    else:
     await ctx.send("User entered no")






    

@client.command()
async def info(ctx, member : discord.Member):
    name = str(member)
    name = name.split("#")
    name = name[0]
    file=open(".//User info//"+name+".txt","r")
    Save = file.read()
    savedata = Save.split("_")
    file.close()
    name = "Nation Name:",savedata[0]
    name = "".join(name)
    cash = "cash:",savedata[1]
    cash = "".join(cash)
    inf = "inf:",savedata[2]
    inf = "".join(inf)
    tank = "firepower:",savedata[3]
    tank ="".join(tank)
    attackpolicy = "attackpolicy: ",savedata[4]
    attackpolicy = "".join(attackpolicy)
    shipyards = "Shipyards: ",savedata[5]
    shipyards = "".join(shipyards)
    await ctx.send(name)
    await ctx.send(cash)
    await ctx.send(inf)
    await ctx.send(tank)
    await ctx.send(shipyards)
    await ctx.send(attackpolicy)

@client.command()
async def global_info(ctx, name):
    name = str(name)

    file=open(".//User info//"+name+".txt","r")
    Save = file.read()
    savedata = Save.split("_")
    file.close()
    name = "Nation Name:",savedata[0]
    name = "".join(name)
    cash = "cash:",savedata[1]
    cash = "".join(cash)
    inf = "inf:",savedata[2]
    inf = "".join(inf)
    tank = "firepower:",savedata[3]
    tank ="".join(tank)
    attackpolicy = "attackpolicy: ",savedata[4]
    attackpolicy = "".join(attackpolicy)
    shipyards = "Shipyards: ",savedata[5]
    shipyards = "".join(shipyards)
    await ctx.send(name)
    await ctx.send(cash)
    await ctx.send(inf)
    await ctx.send(tank)
    await ctx.send(shipyards)
    await ctx.send(attackpolicy)


@client.command()
async def attack(ctx, target :discord.Member):
    attacker = ctx.author.name
    defender = str(target)
    defender = defender.split("#")
    defender = defender[0]

    file=open(".//User info//"+attacker+".txt","r")
    attacks=file.read()
    attacks=attacks.split("_")
    file.close()
    file=open(".//User info//"+defender+".txt","r")
    defend=file.read()
    defend=defend.split("_")
    file.close()

    att_tanks=attacks[3]
    def_tanks=defend[3]
    att_tanks = int(att_tanks)
    attmin = 0
    if att_tanks > 150:
        attmin=att_tanks/2
        attmin=round(attmin)
    def_tanks = int(def_tanks)
    defmin = 0
    if def_tanks > 150:
        defmin=att_tanks/2
        defmin=round(defmin)
    att_score=random.randrange(attmin,att_tanks)
    
    
    defmin = 0
    if def_tanks > 150:
        defmin=def_tanks/2
        defmin=round(defmin)
    def_score=random.randrange(defmin,def_tanks)
    def_score = def_score
    print(att_score)
    print(def_score)
    if def_score > att_score:
        defmin = 0
        at = random.randrange(attmin,def_tanks)
        de = random.randrange(defmin,att_tanks)

        if de > def_tanks:
            de = def_tanks
        if at > att_tanks:
            at = att_tanks
        
        at = round(at)
        att_tanks = att_tanks - at
        de = de/2
        de = round(de)
        def_tanks = def_tanks - de
        if def_tanks < 1:
            def_tanks = 1
        if att_tanks < 1:
            att_tanks = 1
        def_tanks = str(def_tanks)
        att_tanks = str(att_tanks)
        at = str(at)
        de = str(de)
        
        data=defend[0], "[Defender] won the battle and lost ",de," firepower [Took no infrastructure loses]"
        dataa=attacks[0], "[Attacker] lost the battle and and lost ",at," firepower"

        data="".join(data)
        dataa="".join(dataa)
        await ctx.send(data)
        await ctx.send(dataa)
        

        att_tanks = str(att_tanks)
        def_tanks = str(def_tanks)
        file=open(".//User info//"+attacker+".txt","w+")
        
        attacks[3] = att_tanks
        attacks="_".join(attacks)
        file.write(attacks)
        file.close()
        file=open(".//User info//"+defender+".txt","w+")
        
        defend[3] = def_tanks
        defend="_".join(defend)
        print(defender)
        file.write(defend)
        file.close()
        

    else:
        attmin = 0
        at = random.randrange(attmin,def_tanks)
        de = random.randrange(defmin,att_tanks)

        if de > def_tanks:
            de = def_tanks
        if at > att_tanks:
            at = att_tanks
        at = at/2
        at = round(at)
        att_tanks = att_tanks - at
        def_tanks = def_tanks - de

        policyid = attacks[4]
        if policyid == "2":
            await ctx.send("[Attacker] left inf alone")
            inf_lose = "0"
            shipyardloss = "0"
        else:

            def_lose= defend[2]
            shipyardloss = defend[5]

            shipyardloss = int(shipyardloss)

            
        
            def_lose= int(def_lose)
            inf_loss = random.randrange(defmin,att_tanks)
            if inf_loss > def_lose:
                inf_loss = def_lose
            atta_tank = int(att_tanks)
            atta_tank = atta_tank/5
            atta_tank = round(atta_tank)
            shipyardlos = random.randrange(0,atta_tank)
            if shipyardlos > shipyardloss:
                shipyardlos = shipyardloss

            shipyardloss = shipyardloss - shipyardlos

            shipyardloss = str(shipyardloss)

            def_lose= def_lose - inf_loss
            inf_lose = str(inf_loss)
        at = str(at)
        de = str(de)
        data=defend[0], "[Defender] lost the battle and and lost ",de," firepower [lost ",inf_lose," Infrastructure][lost ",shipyardloss," shipyards"
        dataa=attacks[0], "[Attacker] won the battle and and lost ",at," firepower "

        data="".join(data)
        dataa="".join(dataa)
        await ctx.send(data)
        await ctx.send(dataa)
        inf_lose = int(inf_loss)
        if def_tanks < 1:
            def_tanks = 1
        if def_lose < 1:
            def_lose = 5
            await ctx.send("[Defender] Was destroyed but rebuilt what they could")

        tax = inf_lose*2
        attcoin = tax + int(defend[1])
        attcoin = str(attcoin)
        tax = str(tax)
        send = "[Attacker]Has taken the defenders tax of ",tax
        send = "".join(send)
        await ctx.send(send)

        
        inf_lose = str(inf_loss)
        
        def_lose = str(def_lose)
        att_tanks = str(att_tanks)
        def_tanks = str(def_tanks)
        file=open(".//User info//"+attacker+".txt","w+")

        attacks[1] = attcoin
        attacks[3] = att_tanks
        attacks="_".join(attacks)
        file.write(attacks)
        file.close()
        file=open(".//User info//"+defender+".txt","w+")
        
        defend[3] = def_tanks
        defend[2] = def_lose
        defend[5] = shipyardloss
        defend="_".join(defend)
        file.write(defend)
        file.close()

@client.command()
async def give_cash(ctx, amount, WhoTo:discord.Member):
    name= ctx.author.name
    target=str(WhoTo)
    target=target.split("#")
    target=target[0]
    amount = int(amount)
    if amount < 1:
        await ctx.send("Thats not nice")
    else:
        

        file=open(".//User info//"+name+".txt","r")
        cash = file.read()
        file.close()
        cash = cash.split("_")
        
        cashs= cash[1]
        cashs = int(cashs)
        if cashs > amount:
            file=open(".//User info//"+target+".txt","r")
            tcash = file.read()
            file.close()
            tcash = tcash.split("_")
            tcashs = tcash[1]
            tcashs = int(tcashs)

            tcashs = tcashs + amount


            cashs = cashs - amount
            T = str(tcashs)
            C = str(cashs)
            send= target," now has ",T," And you now have ",C
            send = "".join(send)

            file=open(".//User info//"+name+".txt","w+")
            cashs = str(cashs)
            cash[1] = cashs
            cash="_".join(cash)
            file.write(cash)
            file.close()

            file=open(".//User info//"+target+".txt","w+")
            tcashs=str(tcashs)
            tcash[1] = tcashs
            
            tcash="_".join(tcash)
            file.write(tcash)
            file.close()
            await ctx.send(send)

            
            
        else:
            await ctx.send("You do not have enough cash")
        
    
    
    
@client.command()
async def give_ships(ctx, amount, WhoTo:discord.Member):
    name= ctx.author.name
    target=str(WhoTo)
    target=target.split("#")
    target=target[0]
    amount = int(amount)
    if amount < 1:
        await ctx.send("Thats not nice")
    else:
        

        file=open(".//User info//"+name+".txt","r")
        cash = file.read()
        file.close()
        cash = cash.split("_")
        
        cashs= cash[3]
        cashs = int(cashs)
        if cashs > amount:
            file=open(".//User info//"+target+".txt","r")
            tcash = file.read()
            file.close()
            tcash = tcash.split("_")
            tcashs = tcash[3]
            tcashs = int(tcashs)

            tcashs = tcashs + amount


            cashs = cashs - amount
            T = str(tcashs)
            C = str(cashs)
            send= target," now has ",T," And you now have ",C
            send = "".join(send)

            file=open(".//User info//"+name+".txt","w+")
            cashs = str(cashs)
            cash[3] = cashs
            cash="_".join(cash)
            file.write(cash)
            file.close()

            file=open(".//User info//"+target+".txt","w+")
            tcashs=str(tcashs)
            tcash[3] = tcashs
            
            tcash="_".join(tcash)
            file.write(tcash)
            file.close()
            await ctx.send(send)

            
            
        else:
            ctx.send("You do not have enough cash")
        
    
    
    

@client.command()
async def give_inf(ctx, amount, WhoTo:discord.Member):
    name= ctx.author.name
    target=str(WhoTo)
    target=target.split("#")
    target=target[0]
    amount = int(amount)
    if amount < 1:
        await ctx.send("Thats not nice")
    else:
        

        file=open(".//User info//"+name+".txt","r")
        cash = file.read()
        file.close()
        cash = cash.split("_")
        
        cashs= cash[2]
        cashs = int(cashs)
        if cashs > amount:
            file=open(".//User info//"+target+".txt","r")
            tcash = file.read()
            file.close()
            tcash = tcash.split("_")
            tcashs = tcash[2]
            tcashs = int(tcashs)

            tcashs = tcashs + amount


            cashs = cashs - amount
            T = str(tcashs)
            C = str(cashs)
            send= target," now has ",T," And you now have ",C
            send = "".join(send)

            file=open(".//User info//"+name+".txt","w+")
            cashs = str(cashs)
            cash[2] = cashs
            cash="_".join(cash)
            file.write(cash)
            file.close()

            file=open(".//User info//"+target+".txt","w+")
            tcashs=str(tcashs)
            tcash[2] = tcashs
            
            tcash="_".join(tcash)
            file.write(tcash)
            file.close()
            await ctx.send(send)

            
            
        else:
            ctx.send("You do not have enough cash")
        
    
    

    
    
    
    
    
    


                




client.run("Nzc2ODYxMjY2NDEyODMwNzUw.X67Cbw.1ic6PyXvlLL4NkvvgQulkZ4dv8Y")
