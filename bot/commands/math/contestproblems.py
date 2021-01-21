import json
import random

import discord
import requests
from discord.ext import commands

class Contestproblems(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Contest Math cog has been loaded sucessfully')



    # All Math Commands
    @commands.command()
    async def fetchamc(self, ctx, year=None, contest_id=None, problem_num=None):
        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author

        if year != None and problem_num != None and contest_id != None:
            requested_year = str(year)
            requested_id = str(contest_id.upper())
            requested_problem = str(problem_num)
            emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e"}

            tried = []
            earned_points = []

            def check(reaction, user):
                return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{requested_year}/{requested_id}/{requested_problem}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{requested_year}/{requested_id}/{requested_problem}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    users[str(user.id)]["points"] += 6
                    with open("mathpoints.json", "w") as f:
                        json.dump(users, f)
                    await ctx.send("Correct. You earned 6 points. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}')
                    break    
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You have lost 1 point. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={requested_year}_AMC_{requested_id}_Problems/Problem_{requested_problem}')
                    break
    
    @commands.command()
    async def fetchaime(self, ctx, year=None, problem_num=None):
        if year!=None and problem_num !=None:
            requested_year = str(year)
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AIME/{requested_year}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def fetchusamo(self, ctx, year=None, problem_num=None):
        if year!=None and problem_num!=None:
            requested_year = str(year)
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAMO/{requested_year}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")
    
    @commands.command()
    async def fetchusajmo(self, ctx, year=None, problem_num=None):
        if year!=None and problem_num!=None:
            requested_year = str(year)
            requested_problem = str(problem_num)
            try:
                await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/USAJMO/{requested_year}/{requested_problem}/statement.png')
            except:
                await ctx.send("Sorry there was an error processing this command")

    @commands.command()
    async def last5(self, ctx):
        contestid = ["10A", "10B", "12A", "12B"]
        lastfive = str(int(random.randint(20, 25)))
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(contestid))
        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e"}

        tried = []

        def check(reaction, user):
            return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

        while True:
            url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{lastfive}/sol.txt'
            page = requests.get(url)
            sol = str(page.text)
            question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{lastfive}/statement.png')

            for i in emojis:
                await question.add_reaction(i)

            reaction, user = await self.bot.wait_for('reaction_add', check=check)

            if emojis[reaction.emoji] == sol:
                await ctx.send("Correct. You may want to check against this to get a better understanding")
                await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                break
            else:
                tried.append(user.id)
                await ctx.send("Wrong. You may want to check against this go get a better understanding")
                await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{lastfive}')
                break

    @commands.command()
    async def amc10(self, ctx, difficulty):
        amc10_id = ["10A", "10B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc10_id))
        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e"}

        tried = []

        def check(reaction, user):
            return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried


        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break    


        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break



        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break

    @commands.command()
    async def amc12(self, ctx, difficulty):
        amc12_id = ["12A", "12B"]
        randomyear = str(int(random.randint(2002, 2019)))
        randomcontestid = str(random.choice(amc12_id))
        emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e"}

        tried = []

        def check(reaction, user):
            return user == ctx.message.author and reaction.emoji in emojis and user.id not in tried

        if difficulty == "easy" or difficulty == "e":
            easy= str(int(random.randint(1, 10)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{easy}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{easy}')
                    break


        elif difficulty == "med" or difficulty == "medium" or difficulty == "m":
            med = str(int(random.randint(11,16)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{med}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{med}')
                    break

        elif difficulty == "hard" or difficulty == "h":
            hard = str(int(random.randint(17, 25)))

            while True:
                url = f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/sol.txt'
                page = requests.get(url)
                sol = str(page.text)
                question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{hard}/statement.png')

                for i in emojis:
                    await question.add_reaction(i)

                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if emojis[reaction.emoji] == sol:
                    await ctx.send("Correct. You may want to check against this to get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break
                else:
                    tried.append(user.id)
                    await ctx.send("Wrong. You may want to check against this go get a better understanding")
                    await ctx.send(f'https://artofproblemsolving.com/wiki/index.php?title={randomyear}_AMC_{randomcontestid}_Problems/Problem_{hard}')
                    break
    

    @commands.command()
    async def random(self, ctx, contest_type=None):
        if contest_type == 'amc' or contest_type == 'AMC':
            emojis = {"🇦":"a", "🇧":"b", "🇨":"c", "🇩":"d", "🇪":"e"}
            amc_id = ["10A", "12A", "12A", "12B"]
            randomcontestid = str(random.choice(amc_id))
            randomyear = str(int(random.randint(2002, 2019)))
            problem_num = str(int(random.randint(1, 25)))

            def check(reaction, user):
                return user == ctx.message.author

            sol = open(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{problem_num}/sol.txt', 'r').read()
            question = await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AMC/{randomyear}/{randomcontestid}/{problem_num}/statement.png')
            for i in emojis:
                await question.add_reaction(i)
            reaction, user = await self.bot.wait_for('reaction_add', check=check)
            if reaction == sol:
                await ctx.send("Correct. You may want to check against this to get a better understanding")

        if contest_type == 'aime' or contest_type == 'AIME':
            randomyear = str(int(random.randint(2000, 2019)))
            contest_id = str(int(random.randint(1,2)))
            problem_num = str(int(random.randint(1, 15)))
            await ctx.send(f'https://raw.githubusercontent.com/yak-fumblepack/mathcontests/master/AIME/{randomyear}/{contest_id}/{problem_num}/statement.png')
        if contest_type == 'usamo' or contest_type == 'USAMO':
            randomyear = str(int(random.randint(2000, 2019)))
            contest_id = str(int(random.randint(1,2)))
            problem_num = str(int(random.randint(1, 15)))



    # Ranked Question Answering
    @commands.command()
    async def stats(self, ctx):
        await open_account(self, ctx.author)
        users = await get_points_data(self)
        user = ctx.author
        points_scored = users[str(user.id)]["points"]

        emb = discord.Embed(title=f"{ctx.author.name}'s points", color=discord.Color.blue())
        emb.add_field(name="Points:", value= points_scored)
        await ctx.send(embed=emb)

async def open_account(self, user):
    users = await get_points_data(self)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["points"] = 0
        
    with open("mathpoints.json", "w") as f:
        json.dump(users, f)

    return True

async def get_points_data(self):
    with open("mathpoints.json", "r") as f:
        users = json.load(f)
    
    return users

def setup(bot):
    bot.add_cog(Contestproblems(bot))
