import discord
from discord.ext import commands
import random
import os
import time


botToken = "BOT TOKEN"

global file, a, game, winrate, numwins, numlosses, money, tool, \
    ore, dirt, cobblestone, coal, iron, gold, diamond, cooldown, \
    stage, pet
a = 0
numwins = 0
numlosses = 0
money = 0
ore = 0
dirt = 0
cobblestone = 0
coal = 0
iron = 0
gold = 0
diamond = 0


winrate = 0.0
game = False
tool = "beginner"

cooldown = False

stage = 1
pet = 0
def run():

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    def initialize_scores():
        global numwins, numlosses
        file_path = r"C:/Users/maxth/Downloads/scores.txt"

        try:
            file = open(file_path, "r")
            for line in file.readlines():
                if "wins" in line:
                    numwins = int(line.strip().replace("wins", ""))
                elif "losses" in line:
                    numlosses = int(line.strip().replace("losses", ""))
        except FileNotFoundError:
            print("There was an error in retrieving the file!")
        except Exception as e:
            print(f"An error occured: {e}")


    def update_scores():
        global numwins, numlosses
        file_path = r"C:/Users/maxth/Downloads/scores.txt"
        try:
            file = open(file_path, "w")
            file.writelines("wins" + str(numwins) + "\n")
            file.writelines("losses" + str(numlosses) + "\n")
            print("Scores updated successfully.")
        except FileNotFoundError:
            print("There was an error in retrieving the file!")
        except Exception as e:
            print(f"An error occurred while updating the scores: {e}")

    def initialize_mining_scores():
        file_m = r"C:/Users/maxth/Downloads/money.txt"
        global money, dirt, cobblestone, coal, iron, gold, diamond, tool, stage

        try:
            file_mining = open(file_m, "r")
            for line in file_mining.readlines():
                if "dirt" in line:
                    dirt = int(line.strip().replace("dirt", ""))
                elif "cobblestone" in line:
                    cobblestone = int(line.strip().replace("cobblestone", ""))
                elif "coal" in line:
                    coal = int(line.strip().replace("coal", ""))
                elif "iron" in line:
                    iron = int(line.strip().replace("iron", ""))
                elif "gold" in line:
                    gold = int(line.strip().replace("gold", ""))
                elif "diamond" in line:
                    diamond = int(line.strip().replace("diamond", ""))
                if "money" in line:
                    money = int(line.strip().replace("money", ""))
                if "tool" in line:
                    tool = str(line.strip().replace("tool", ""))
                if "stage" in line:
                    stage = int(line.strip().replace("stage", ""))
        except FileNotFoundError:
            print("There was an error in retrieving the mining file!")
        except Exception as e:
            print(f"An error occured: {e}")

    def update_mining_scores():
        global money, dirt, cobblestone, coal, iron, gold, diamond, tool, stage
        file_mining = r"C:/Users/maxth/Downloads/money.txt"
        try:
            file = open(file_mining, "w")
            file.writelines("dirt" + str(dirt) + "\n")
            file.writelines("cobblestone" + str(cobblestone) + "\n")
            file.writelines("coal" + str(coal) + "\n")
            file.writelines("iron" + str(iron) + "\n")
            file.writelines("gold" + str(gold) + "\n")
            file.writelines("diamond" + str(diamond) + "\n")
            file.writelines("money" + str(money) + "\n")
            file.writelines("tool" + str(tool) + "\n")
            file.writelines("stage" + str(stage) + "\n")
            print("Ores, money, tools, and stage have successfully updated.")
        except FileNotFoundError:
            print("There was an error in retrieving the file!")
        except Exception as e:
            print(f"An error occurred while updating the scores: {e}")




    def reset():
        global numwins, numlosses
        file_path = r"C:/Users/maxth/Downloads/scores.txt"
        try:
            file = open(file_path, "w")
            file.writelines("wins" + "0" + "\n")
            file.writelines("losses" + "0" + "\n")
            numwins = 0
            numlosses = 0
        except FileNotFoundError:
            print("There was an error in retrieving the file!")
        except Exception as e:
            print(f"An error occurred while updating the scores: {e}")

    @bot.command()
    async def showcommands(ctx):
        await ctx.send("!rps -> Play rock, paper, scissors \n")
        await ctx.send("    !rock -> Plays rock \n")
        await ctx.send("    !paper -> Plays paper \n")
        await ctx.send("    !scissors -> Plays scissors \n")
        await ctx.send("    !rst -> Resets the rock, paper, scissors game \n")
        await ctx.send("------------------------------------------------------------------------------------------")
        await ctx.send("!mine -> Starts mining \n")
        await ctx.send("    !inv -> Shows mining inventory \n")
        await ctx.send("    !sellall -> Sells all your ores for money! \n")
        await ctx.send("    !shop -> Shows shop offers \n")


    @bot.command()
    async def rps(ctx):
        global a, game
        game = True
        await ctx.send("Pick either: rock, paper, or scissors")

    @bot.command()
    async def rock(ctx):
        global a, game, winrate, numwins, numlosses
        a = random.randint(1, 3)
        file_path = r"C:/Users/maxth/Downloads/scores.txt"
        if game == True:
            if a == 1:
                await ctx.send("The computer picked scissors and you won!")
                numwins += 1
            elif a == 2:
                await ctx.send("The computer picked rock and you tied!")
            elif a == 3:
                await ctx.send("The computer picked paper and you lost!")
                numlosses += 1
            if numwins + numlosses == 0:
                await ctx.send("You have no winrate, you tied")
            else:
                winrate = str(float(numwins/(numwins + numlosses) * 100))
                await ctx.send("Your winrate is: " +winrate +"%!")
            update_scores()
            #game = False
        elif game == False:
            await ctx.send("A game isn't playing right now!")

    @bot.command()
    async def paper(ctx):
        global a, game, winrate, numwins, numlosses
        a = random.randint(1, 3)
        file_path = r"C:/Users/maxth/Downloads/scores.txt"
        if game == True:
            if a == 1:
                await ctx.send("The computer picked rock and you won!")
                numwins += 1
            elif a == 2:
                await ctx.send("The computer picked paper and you tied!")
            elif a == 3:
                await ctx.send("The computer picked scissors and you lost!")
                numlosses += 1
            if numwins + numlosses == 0:
                await ctx.send("You have no winrate, you tied")
            else:
                winrate = str(float(numwins / (numwins + numlosses) * 100))
                await ctx.send("Your winrate is: " + winrate + "%!")
            update_scores()
            #game = False
        elif game == False:
            await ctx.send("A game isn't playing right now!")

    def go_mine():
        global ore, dirt, cobblestone, coal, iron, gold, diamond
        ore = random.randint(1,30)

        if ore in range(1,12):
            dirt += 1
            return "dirt"
        elif ore in range (12,20):
            cobblestone += 1
            return "cobblestone"
        elif ore in range (20,25):
            coal += 1
            return "coal"
        elif ore in range (25,28):
            iron += 1
            return "iron"
        elif ore in range (28,29):
            gold += 1
            return "gold"
        elif ore == 30:
            diamond += 1
            return "diamond"
        else:
            print("There was en error in mining an ore!")




    @bot.command()
    async def scissors(ctx):
        global a, game, winrate, numwins, numlosses
        a = random.randint(1, 3)
        file_path = r"C:/Users/maxth/Downloads/scores.txt"
        if game == True:
            if a == 1:
                await ctx.send("The computer picked paper and you won!")
                numwins += 1
            elif a == 2:
                await ctx.send("The computer picked scissors and you tied!")
            elif a == 3:
                await ctx.send("The computer picked rock and you lost!")
                numlosses += 1
            if numwins + numlosses == 0:
                await ctx.send("You have no winrate, you tied")
            else:
                winrate = str(float(numwins / (numwins + numlosses) * 100))
                await ctx.send("Your winrate is: " + winrate + "%!")
            update_scores()
            #game = False
        elif game == False:
            await ctx.send("A game isn't playing right now!")

    @bot.command()
    async def rst(ctx):
        reset()
        await ctx.send("Scores reset successfully")

    @bot.command()
    async def mine(ctx):
        global tool, ore, cooldown

        if tool == "beginner" and cooldown == False:
            await ctx.send(f"You went mining with a {tool} tool!")
            await ctx.send("Mining...")
            cooldown = True
            time.sleep(3)
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            update_mining_scores()
            cooldown = False
        elif tool == "intermediate" and cooldown == False:
            await ctx.send(f"You went mining with a {tool} tool!")
            await ctx.send("Mining...")
            cooldown = True
            time.sleep(1.5)
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            update_mining_scores()
            cooldown = False
        elif tool == "advanced" and cooldown == False:
            await ctx.send(f"You went mining with a {tool} tool!")
            await ctx.send("Mining...")
            cooldown = True
            time.sleep(0.75)
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            update_mining_scores()
            cooldown = False
        elif tool == "pro" and cooldown == False:
            await ctx.send(f"You went mining with a {tool} tool!")
            await ctx.send("Mining...")
            cooldown = True
            time.sleep(0.375)
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            update_mining_scores()
            cooldown = False
        elif tool == "triple":
            await ctx.send(f"You went mining with a {tool} tool!")
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            ore = go_mine()
            await ctx.send(f"You mined: {ore}")
            update_mining_scores()
        else:
            print("An Error occurred in mining!")
            print(tool)
            await ctx.send("You are on cooldown, you cannot mine.")

    @bot.command()
    async def inv(ctx):
        global money, dirt, cobblestone, coal, iron, gold, diamond
        await ctx.send(f"Your inventory consists of: {dirt} dirt, "
                       f"{cobblestone} cobblestone, "
                       f"{coal} coal, "
                       f"{iron} iron, "
                       f"{gold} gold, "
                       f"{diamond} diamonds.")
        await ctx.send(f"You have: ${money}.")
        await ctx.send(f"You are currently using a {tool} tool.")

    @bot.command()
    async def sellall(ctx):
        global money, dirt, cobblestone, coal, iron, gold, diamond
        file_mining = r"C:/Users/maxth/Downloads/money.txt"

        try:
            money = money + ((dirt * 1) + (cobblestone * 2) + (coal * 5) + (iron * 10) + (gold * 25) + (diamond * 100))

            file = open(file_mining, "w")
            file.writelines("dirt" + "0" + "\n")
            file.writelines("cobblestone" + "0" + "\n")
            file.writelines("coal" + "0" + "\n")
            file.writelines("iron" + "0" + "\n")
            file.writelines("gold" + "0" + "\n")
            file.writelines("diamond" + "0" + "\n")
            file.writelines("money" + str(money) + "\n")

            dirt = 0
            cobblestone = 0
            coal = 0
            iron = 0
            gold = 0
            diamond = 0


            print("All ores have successfully been sold. Money has been updated")
            await ctx.send("All ores have successfully been sold. Money has been updated")

        except FileNotFoundError:
            print("There was an error in retrieving the mining file!")
        except Exception as e:
            print(f"An error occurred while updating the scores: {e}")

    @bot.command()
    async def shop(ctx):
        global stage
        await ctx.send("Welcome to Max's amazing shop! Here we offer new pickaxes and spells!")
        await ctx.send("OFFER 1: INTERMEDIATE PICKAXE ⟹ SELLING FOR 50 DOLLARS")
        await ctx.send("OFFER 2: ADVANCED PICKAXE ⟹ SELLING FOR 125 DOLLARS")
        await ctx.send("OFFER 3: PRO PICKAXE ⟹ SELLING FOR 250 DOLLARS")
        if stage == 2:
            await ctx.send("SECRET OFFER 4: TRIPLE PICKAXE ⟹ SELLING FOR 1000 DOLLARS")
            await ctx.send("SECRET OFFER 5: MINING PET ⟹ SELLING FOR 1000 DOLLARS")
        #await ctx.send("OFFER 4: COOLDOWN SPELL ⟹ SELLING FOR 100 DOLLARS")
        await ctx.send('Type "!buy1" to buy offer1 and etc.')

    @bot.command()
    async def buy1(ctx):
        global money, tool
        if money < 50:
            await ctx.send("You do not have enough money to buy this item!")
        elif money >= 50:
            money = money - 50
            tool = "intermediate"
            update_mining_scores()
            await ctx.send("You have successfully spent $50 to buy an intermediate pickaxe")

    @bot.command()
    async def buy2(ctx):
        global money, tool
        if money < 125:
            await ctx.send("You do not have enough money to buy this item!")
        elif money >= 125:
            money = money - 125
            tool = "advanced"
            update_mining_scores()
            await ctx.send("You have successfully spent $125 to buy an advanced pickaxe")

    @bot.command()
    async def buy3(ctx):
        global money, tool, stage
        if money < 250:
            await ctx.send("You do not have enough money to buy this item!")
        elif money >= 250:
            money = money - 250
            tool = "pro"
            update_mining_scores()
            await ctx.send("You have successfully spent $250 to buy a pro pickaxe")
            stage = 2
            await ctx.send("You have unlocked a new secret item in the shop! Check out the shop!")
            update_mining_scores()

    @bot.command()
    async def buy4(ctx):
        global money, tool, stage
        if stage == 1:
            await ctx.send("You cheater... how'd you find the secret tool? Go back!")
        elif stage == 2:
            if money < 1000:
                await ctx.send("You do not have enough money to buy this item!")
            elif money >= 1000:
                money = money - 1000
                tool = "triple"
                update_mining_scores()
                await ctx.send("You have successfully spent $1000 to buy the secret triple pickaxe!")


    initialize_scores()

    initialize_mining_scores()

    bot.run(botToken, root_logger=True)


if __name__ == "__main__":
    run()