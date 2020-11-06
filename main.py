from settings import DISCORD_TOKEN, GOOGLE_APP_PASSWORD
from bot import bot


def main():
    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
