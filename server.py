import argparse
from datetime import datetime

from tinydb import TinyDB

from worker import run as download_data
from magi import run as top_five_predict
from addon import run as draw_magi_ui
from addon import post as tweet_n_ig

def main(args):
    with TinyDB('db.json') as db:
        config = db.table('config')
        config.insert({'url': 'https://twitter.com/i/flow/login', 'user': args.tw, 'pass': args.tw_pw})

    flag = True
    while flag:
        if args.engine.upper() == 'NLTK' or args.engine.upper() == 'HUGGINGFACE':
            download_data(args.engine.upper())
        else:
            raise NotImplementedError

        top5 = top_five_predict()
        print('===== Most popular candidates =====')
        for p in top5:
            print(p[0], f'{p[2]}%')
        print(f'===== {str(datetime.now().date())} =====')

        draw_magi_ui()

        tweet_n_ig(f'{top5[0][0]}.png')

        flag = args.loop
        if datetime.now().date() < datetime.strptime('05/09/2022', '%d/%m/%Y').date():
            flag = False

    with TinyDB('db.json') as db:
        db.drop_table('config')

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='#MAGI_SYS challenge UK Politics')
    parser.add_argument('--engine', type=str,
                        default='NLTK', choices=['HUGGINGFACE', 'NLTK'],
                        help='Engine to be used in sentiment analysis')
    parser.add_argument('--tw', help='Twitter username')
    parser.add_argument('--tw-pw', help='Twitter password')
    parser.add_argument('--loop', action='store_true',
                        help='Sleep 20 hours & loop until Sep 4th 2022')

    main(parser.parse_args())
