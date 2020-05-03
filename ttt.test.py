#init
import discord
from tic_tae_toe import *
from discord.ext import commands
import os

ttt = False
in_game = False

#init_dis
token = open('token.txt', 'r')
TOKEN = token.read()
client = commands.Bot(command_prefix = 'j!')
#začne z igro

@client.command()
async def ttt(ctx):
    global in_game
    board = [['7', '8', '9'], ['4', 'o', '6'], ['1', 'x', '3']]
    if in_game:
        if checkWin(getBoard(), False):
            await ctx.send(returnPlayer(whoWin(getBoard())) + ' je zmagal. \n Čestitke! :clap:')
        else:
            doMove(board, 1, False)
            await ctx.send(sendBoard(board))
            await ctx.send(askForMove())

    else:
        client = commands.Bot(command_prefix = '')
        await ctx.send(sendBoard(board))
        await ctx.send(askForMove())
        in_game = True

    print('i am right here' + str(board) + str(in_game))
    # ni prava od tu

    #do tu
    
#@client.event
#async def on_message(message):
#    if 'happy birthday' in message.content.lower():
#        await message.channel.send('Happy Birthday! 🎈🎉')

print('i shouldn\' be there')
#run
client.run(TOKEN)