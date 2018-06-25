import steamapi
import time

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

inC = 0
fname = "SAccounts.ini"

with open('apikey.ini', 'r') as myfile:
    apiFile=myfile.read().replace('\n', '')

with open('seconds.ini', 'r') as myfile:
    seconds=myfile.read().replace('\n', '')
    seconds = float(int(seconds))

steamapi.core.APIConnection(api_key=apiFile, validate_key=True)

numOfAccts = file_len(fname)

while(True == True):
    if(numOfAccts == 1):
        f=open(fname)
        lines=f.readlines()
        username=lines[0]
        me = steamapi.user.SteamUser(userurl=username)
        print(username + ": " + str(me.state))
    else:
        while(inC != numOfAccts):
            f=open(fname)
            lines=f.readlines()
            username=lines[inC]
            me = steamapi.user.SteamUser(userurl=username)
            print(username + ": " + str(me.state))
            inC += 1
    time.sleep(seconds)
