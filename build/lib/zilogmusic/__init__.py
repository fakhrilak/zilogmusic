import argparse
from zilogmusic.app import app
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("start",type=str,help="to start app")
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        apps = app()
        if args.start == "start":
            print("====================== STARTING APP =======================")
            print("this is start")
        if args.start == "login":
            print("====================== STARTING APP =======================")
            apps.Login()
            print("this is start")
    except BaseException as err:
        print(err)