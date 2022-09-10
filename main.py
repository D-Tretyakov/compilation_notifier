from bot import Bot

TOKEN = 'TOKEN'
USER_ID = "12345"

def main():
    bot = Bot(TOKEN, USER_ID)
    bot.notify()
    # bot.get_update()


if __name__ == '__main__':
    main()