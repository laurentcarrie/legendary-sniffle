import argparse
import sys
import util

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-rm-all', '--rm-all',action='store_true',help='remove images and containers')
    parser.add_argument('-rm-cont', '--rm-cont',action='store_true',help='remove containers')
    args = parser.parse_args()

    if args.rm_all:
        print("rm all")
        util.rm_all()
        exit(0)

    if args.rm_cont:
        print("rm containers")
        l = util.Container.all()
        for i in l:
            i.rm()
        exit(0)