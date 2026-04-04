import os
from dotenv import load_dotenv

load_dotenv()


from bot import DebatinatorBot


bot = DebatinatorBot()

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
