from argparse import ArgumentParser

from enotify.bot import Bot
from enotify.config import Config


def notify():
    bot = Bot()
    bot.notify()


def get_id(username):
    bot = Bot()

    print(f'Looking for message from @{username}')
    print('Send any message to bot')
    
    user_id = bot.get_user_id(username)
    if user_id is None:
        print('Couldn\'t find message :(')
        return

    Config.store(user_id=user_id)
    
    print(f'ID is {user_id}')
    print(f'Saved user id to config ({Config.get_path()})')


def setup(token=None, user_id=None):
    Config.store(token, user_id)
    print(f'Saved: {Config.get_path()}')


def main():
    parser = ArgumentParser(
        description='ENofify. Send telegram message when compilation ends.'
    )

    parser.add_argument('-t', '--token', 
        dest='bot_token', 
        action='store',
        help='save bot token to config'
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g', '--get-id', 
        dest='username', 
        action='store',
        help='get user id by telegram username'
    )
    group.add_argument('-i', '--id', 
        dest='user_id', 
        action='store',
        help='save user id to config (if you don\'t know your id use -g flag)'
    )

    args = parser.parse_args()
    if args.username:
        get_id(args.username)
        return

    if args.user_id or args.bot_token:
        setup(args.user_id, args.bot_token)
        return

    notify()