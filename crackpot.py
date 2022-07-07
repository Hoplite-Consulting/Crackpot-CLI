#!/bin/python3

import argparse
from csv import DictWriter
from alive_progress import alive_it
from src import utils
import time
from zxcvbn import zxcvbn

def main(args):
    path_DU = args.domainUsers
    path_ADD = args.activeDirectoryDump
    path_CH = args.crackedHash

    adDump = utils.activeDirClean(path_ADD)
    
    if path_CH:
        crack = utils.cracked(path_CH)
    else:
        crack = []

    crackCount = 0
    bar = alive_it(adDump, title="Finding Cracked Passwords...")
    for acc in bar:
        for hash in crack:
            if acc["hash"] == hash["hash"]:
                acc["password"] = hash["password"]
                if args.verbose or args.veryverbose:
                    print("Found Password for User:", acc["user"])
                    crackCount += 1
        if args.slow_mode:
            time.sleep(.01)
    if args.verbose or args.veryverbose:
        print(crackCount, "passwords found in", path_CH)
    
    userHashPass = adDump

    data = utils.grepClean(path_DU)

    occur = {}

    bar = alive_it(data, title="Adding User Hashpass to Data...")

    # Add User Hash and Password to Data
    for user in bar:
        for u in userHashPass:
            if u['user'] == user['sAMAccountName']:
                if args.veryverbose:
                    print("Added Hashpass to User:", user['sAMAccountName'])
                if args.slow_mode:
                    time.sleep(.01)
                user['hash'] = u['hash']
                user['password'] = u['password']
                try:
                    occur[u['hash']] += 1
                except KeyError:
                    occur[u['hash']] = 1
    
    # Add Password Occurence to Data
    for user in data:
        for pw in occur:
            try:
                if user['hash'] == pw:
                    if pw == None:
                        pass
                    else:
                        user['hash occurence'] = occur[pw]
            except:
                pass

    bar = alive_it(data, title="Calculating Password Scores...")

    # Add User Password Score to Data
    for user in bar:
        try:
            res = zxcvbn(user['password'], user_inputs=[user['name'].split(" ")])
            user['password score'] = res['score']
            user['password feedback'] = res['feedback']
            if args.veryverbose:
                print("Calculating Score for User: ", user['sAMAccountName'])
            if args.slow_mode:
                time.sleep(.01)
        except:
            pass

    keys = []
    bar = alive_it(data, title="Generating Column Titles...")
    for user in bar:
        keyList = list(user.keys())
        for k in keyList:
            if k not in keys:
                if args.veryverbose:
                    print("Column Title '"+str(k)+"' Added")
                if args.slow_mode:
                    time.sleep(.01)
                keys.append(k)
    
    if args.writeFile:
        with open(args.writeFile, "w") as f:
            writer = DictWriter(f, keys)
            writer.writeheader()
            bar = alive_it(data, title="Writing to file...")
            for user in bar:
                if args.verbose or args.veryverbose:
                    print("Writing User:", user["sAMAccountName"])
                if args.slow_mode:
                    time.sleep(.01)
                writer.writerow(user)

if __name__ == "__main__":

    __version__ = "1.4.0"

    parser = argparse.ArgumentParser(description=f"Crackpot CLI Version {__version__}")
    parser.add_argument('domainUsers')
    parser.add_argument('activeDirectoryDump')
    parser.add_argument('-cH', '--crackedHash', metavar='', help='path to file')
    parser.add_argument('-w', '--writeFile', metavar='', help='path to file')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-vv', '--veryverbose', action='store_true')
    parser.add_argument('-s', '--slow-mode', action='store_true')
    args = parser.parse_args()

    main(args)