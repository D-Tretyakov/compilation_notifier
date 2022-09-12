from bot import Bot

TOKEN = ''
USER_ID = ''

def main():
    bot = Bot(TOKEN, USER_ID)
    bot.notify()


if __name__ == '__main__':
    main()