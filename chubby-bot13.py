import discord
from discord.ext import commands
import datetime  # Import the datetime module for the !time command
import asyncio
import random
import math  # Import the math module for mathematical calculations
import requests

# Initialize the bot with intents
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def yt(ctx, video_id: str):
    # Construct the YouTube video URL
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    # Create an embed with the YouTube URL
    embed = discord.Embed()
    embed.title = "YouTube Video"
    embed.description = youtube_url

    await ctx.send(embed=embed)

@bot.command()
async def sendadmin(ctx, *options: str):
    message_author = ctx.message.author
    guild_owner = ctx.guild.owner

    # Check if the author is the guild owner or the specified user
    if message_author.id == "1020401896772608020" or message_author.id == 123456789012345678:  # Replace 123456789012345678 with the ID of "chubbyboi_51837"
        # Send the poll and add reactions for voting -- inaccurate - repurposed code
        await ctx.send(options)
        await ctx.message.delete()  # Delete the original command message
    else:
        await ctx.send("You are not authorized to use this command.")
        await ctx.send(guild_owner)




@bot.command()
async def meme(ctx):
    try:
        # Fetch a random meme using an API (e.g., a meme subreddit)
        response = requests.get("https://meme-api.herokuapp.com/gimme")
        data = response.json()

        # Create an embed with the meme's title and image
        embed = discord.Embed(title=data['title'])
        embed.set_image(url=data['url'])

        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")



# Define a command to send messages to a specific channel
@bot.command()
async def send(ctx, channel_id: int, *, message: str):
    try:
        # Get the channel object using the channel_id
        channel = bot.get_channel(channel_id)
        if channel is None:
            await ctx.send("Channel not found.")
        else:
            # Send the message to the specified channel
            await channel.send(message)
            await ctx.send(f"Message sent to channel {channel_id}: {message}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Define a command to get the current time
@bot.command()
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Current time: {current_time}")

# Define a command to roast the user
@bot.command()
async def roastme(ctx):
    # You can add your roast messages here
    roast_messages = [
        "You must be the square root of -1 because you're imaginary.",
        "Is your name Google? Because you have everything I've been searching for... Not.",
        "You're so slow, it takes you two hours to watch '60 Minutes.'",
        "If you were any more inbred, you'd be a sandwich.",
        "Are you made of copper and tellurium? Because you're Cu-Te.",
        "I'd agree with you but then we'd both be wrong.",
        "I've seen smarter people at a petting zoo.",
        "Is your name Wi-Fi? Because I'm not feeling a connection.",
        "You're so old, your birth certificate expired.",
        "You're not stupid; you just have bad luck thinking.",
        "Do you have a map? I keep getting lost in your mediocrity.",
        "I'd roast you, but my mom said I'm not allowed to burn trash.",
        "If you were any less intelligent, we'd have to water you twice a week."
    ]

    roast = random.choice(roast_messages)
    await ctx.send(roast)

# Define a command to play "rock, paper, scissors" with the bot
@bot.command()
async def rps(ctx, choice: str):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    choice = choice.lower()
    if choice not in choices:
        await ctx.send("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
    else:
        if choice == bot_choice:
            result = "It's a tie!"
        elif (
            (choice == "rock" and bot_choice == "scissors")
            or (choice == "paper" and bot_choice == "rock")
            or (choice == "scissors" and bot_choice == "paper")
        ):
            result = f"You win! You chose {choice} and I chose {bot_choice}."
        else:
            result = f"I win! You chose {choice} and I chose {bot_choice}."

        await ctx.send(result)

# Define a command to quote a message by its message ID or the most recent message
@bot.command()
async def quote(ctx, message_id: int = None):
    try:
        if message_id is None:
            # If no message_id is provided, quote the most recent message before the command
            async for message in ctx.channel.history(limit=10):
                if message.author != bot.user and not message.content.startswith('!quote'):
                    await ctx.send(f'"{message.content}" - {message.author.name}')
                    return
            await ctx.send("No recent messages found to quote.")
        else:
            message = await ctx.channel.fetch_message(message_id)
            if message:
                await ctx.send(f'"{message.content}" - {message.author.name}')
            else:
                await ctx.send("Message not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")




# Define a command to get a random joke
@bot.command()
async def joke(ctx):
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you call a fish with no eyes? Fsh!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    ]

    random_joke = random.choice(jokes)
    await ctx.send(random_joke)

# Define a command to make the bot say a message
@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

# Define a command to evaluate a mathematical expression
@bot.command()
async def math(ctx, *, expression: str):
    try:
        result = eval(expression)
        await ctx.send(f"{expression} = {result}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Define a command to write a message to publicfile.txt
@bot.command()
async def write(ctx, *, message: str):
    try:
        with open('publicfile.txt', 'a') as file:
            file.write(f"{message} - {ctx.author.name}\n")
        await ctx.send("Message written to publicfile.txt.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Define a command to read publicfile.txt
@bot.command()
async def publicfile(ctx):
    try:
        with open('publicfile.txt', 'r') as file:
            public_file_content = file.read()
        await ctx.send("Here are the messages from publicfile.txt:\n```\n" + public_file_content + "```")
    except FileNotFoundError:
        await ctx.send("The public file 'publicfile.txt' was not found.")

# Define a command to list available commands from a file
@bot.command()
async def cmds(ctx):
    try:
        with open('commands.txt', 'r') as file:
            commands_text = file.read()
        await ctx.send("Here are the available commands:\n```\n" + commands_text + "```")
    except FileNotFoundError:
        await ctx.send("The commands file 'commands.txt' was not found.")

# Define a command to start a trivia game
@bot.command()
async def trivia(ctx):
    trivia_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris",
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct_answer": "Jupiter",
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "correct_answer": "Carbon Dioxide",
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Giraffe", "Whale Shark", "Blue Whale"],
            "correct_answer": "Blue Whale",
        },
    ]

    # Randomly select a trivia question
    question = random.choice(trivia_questions)

    # Send the question and answer options
    await ctx.send(question["question"])
    for index, option in enumerate(question["options"]):
        await ctx.send(f"{index + 1}. {option}")

    # Function to check the answer
    def check_answer(msg):
        return (
            msg.author == ctx.author
            and msg.channel == ctx.channel
            and msg.content.isdigit()
            and 1 <= int(msg.content) <= len(question["options"])
        )

    try:
        # Wait for the user's answer
        response = await bot.wait_for("message", check=check_answer, timeout=30)

        # Check if the answer is correct
        selected_option = question["options"][int(response.content) - 1]
        if selected_option == question["correct_answer"]:
            await ctx.send(f"Correct! The answer is {selected_option}.")
        else:
            await ctx.send(f"Sorry, the correct answer is {question['correct_answer']}.")

    except asyncio.TimeoutError:
        await ctx.send("Time's up! The correct answer was {question['correct_answer']}.")
		  
		  
# Define a command to flip a coin
@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"The coin landed on {result}!")

# Tic-Tac-Toe Game
import random

# Create an empty Tic-Tac-Toe board
tic_tac_toe_board = [" " for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    separator = "|"
    line = "-----------"
    for row in range(0, 9, 3):
        print(f"{board[row]} {separator} {board[row + 1]} {separator} {board[row + 2]}")
        if row < 6:
            print(line)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if all(board[i:i+3] == [player, player, player]):
            return True
    for i in range(3):
        if all(board[i::3] == [player, player, player]):
            return True
    if all(board[::4] == [player, player, player]) or all(board[2:7:2] == [player, player, player]):
        return True
    return False

# Define a command to play Tic-Tac-Toe
@bot.command()
async def tictactoe(ctx):
    await ctx.send("Let's play Tic-Tac-Toe!")
    await ctx.send("Here's the empty board:")
    display_board(tic_tac_toe_board)
    await ctx.send("Use the commands !place (position) to make your move.")

# Define a command to place a symbol on the Tic-Tac-Toe board
@bot.command()
async def place(ctx, position: int):
    if position < 1 or position > 9 or tic_tac_toe_board[position - 1] != " ":
        await ctx.send("Invalid move! Please choose an empty position (1-9).")
        return

    player = "X" if random.choice([True, False]) else "O"
    tic_tac_toe_board[position - 1] = player
    display_board(tic_tac_toe_board)

    if check_win(tic_tac_toe_board, player):
        await ctx.send(f"{player} wins! Congratulations!")
        tic_tac_toe_board.clear()
        tic_tac_toe_board.extend([" " for _ in range(9)])
    elif " " not in tic_tac_toe_board:
        await ctx.send("It's a tie! The game is over.")
        tic_tac_toe_board.clear()
        tic_tac_toe_board.extend([" " for _ in range(9)])

# End of Tic-Tac-Toe Game


# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Define a command to start the Number Guessing Game
@bot.command()
async def guessgame(ctx):
    await ctx.send("Welcome to the Number Guessing Game!")
    await ctx.send("I've selected a random number between 1 and 100. Try to guess it!")

# Define a command to make a guess in the Number Guessing Game
@bot.command()
async def guess(ctx, number: int):
    if number < 1 or number > 100:
        await ctx.send("Please guess a number between 1 and 100.")
        return

    if number < secret_number:
        await ctx.send("Too low! Try guessing higher.")
    elif number > secret_number:
        await ctx.send("Too high! Try guessing lower.")
    else:
        await ctx.send(f"Congratulations! You guessed the correct number, which was {secret_number}.")
        secret_number = random.randint(1, 100)
        await ctx.send("A new number has been chosen. You can start a new game with !guessgame.")

# End of Number Guessing Game


# Define a command to roll a dice
@bot.command()
async def roll(ctx, dice: str):
    try:
        # Parse the dice notation (e.g., "2d6" means rolling 2 six-sided dice)
        num_dice, num_sides = map(int, dice.split('d'))
        
        if num_dice <= 0 or num_sides <= 0:
            await ctx.send("Invalid dice notation.")
            return
        
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        await ctx.send(f"You rolled {', '.join(map(str, rolls))}. Total: {sum(rolls)}")
    except ValueError:
        await ctx.send("Invalid dice notation. Use the format 'XdY' where X is the number of dice and Y is the number of sides.")


# Define a command to simulate a magic 8-ball
@bot.command()
async def eightball(ctx, *, question: str):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]

    response = random.choice(responses)
    await ctx.send(f"Question: {question}\nAnswer: {response}")


@bot.command()
async def cat(ctx):
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        cat_image_url = data[0]["url"]
        await ctx.send(cat_image_url)
    except requests.exceptions.RequestException as e:
        await ctx.send(f"An error occurred while fetching a cat image: {str(e)}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {str(e)}")




@bot.command()
async def fortunecookie(ctx):
    try:
        response = requests.get("http://yerkee.com/api/fortune")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        fortune_message = data["fortune"]
        await ctx.send(f"🥠 Your fortune cookie message: {fortune_message}")
    except requests.exceptions.RequestException as e:
        await ctx.send(f"An error occurred while fetching a fortune: {str(e)}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {str(e)}")





@bot.command()
async def saul(ctx):
    saul_image_url = "https://static.wikia.nocookie.net/supermarioglitchy4/images/a/a8/Saul.webp/revision/latest?cb=20220811065029"
    
    embed = discord.Embed()
    embed.set_image(url=saul_image_url)
    
    await ctx.send(embed=embed)


@bot.command()
async def admin(ctx):
    message_author = ctx.message.author
    guild_owner = ctx.guild.owner

    # Check if the author is the guild owner or the specified user
    if str(message_author.id) == "1020401896772608020" or message_author.id == 1226124599880712192:  # Replace 123456789012345678 with the ID of "chubbyboi_51837"
        # Send a message confirming the user is authorized
        await ctx.send("You are an admin")
    else:
        # Send a message indicating the user is not authorized
        await ctx.send("You are not authorized to use this command.")
        await ctx.send(f"The guild owner is: {guild_owner}")

import requests

@bot.command()
async def dog(ctx, dog_type: str = None):
    if dog_type:
        # If a specific dog breed is provided, fetch an image of that breed
        response = requests.get(f"https://dog.ceo/api/breed/{dog_type}/images/random")
    else:
        # If no specific breed is provided, fetch a random dog image
        response = requests.get("https://dog.ceo/api/breeds/image/random")

    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]
        await ctx.send(image_url)
    else:
        await ctx.send("Failed to fetch dog image. Please try again later.")


# Event handler to confirm bot login
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Run the bot with your token
bot.run('fortnite')
