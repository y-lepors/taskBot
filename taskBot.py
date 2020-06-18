# Create a Task Bot
from typing import Any, Union

import discord

# add a composant from discord.py
from discord.ext import commands

# Define every variables
bot = commands.Bot(command_prefix='!')
taskList = []


# React to the connection
@bot.event
async def on_ready():
    print("Bot ready!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Organise vos tâches"))


# Command
# !taskList
@bot.command()
async def task(ctx):
    print("task ready")

    embed = discord.Embed(
        colour=discord.Color.orange()
    )

    title = "TASK LISTENER"
    taskStr = "__Liste des tâches à réaliser :__"

    for i in range(len(taskList)):
        taskStr = taskStr + "\n " + str(i) + ". " + str(taskList[i])

    embed.add_field(name=title, value=taskStr, inline=True)

    await ctx.send(embed=embed)


# Command
# !addTask
@bot.command()
async def addTask(ctx, *, new_task):
    # Take the message
    the_task = new_task

    print("addTask ready")
    taskList.append(the_task)
    await ctx.send(f"Tâche ajoutée : {the_task}")


# Command
# !removeTask
@bot.command()
async def removeTask(ctx, intTask):
    # Take the message
    numTask = int(intTask)

    print("removeTask ready")
    del taskList[numTask]
    await ctx.send(f"Tâche " + str(numTask) + " supprimée")


jeton = "NzE5NjUwODc3NzI3NzAzMTIw.Xt6hzg.JlgCbKTjup4iONZcmdfeV2MV-Nw"

# Print ez info
print("good execution")
bot.run(jeton)
