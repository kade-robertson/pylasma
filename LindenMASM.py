import os
from sys import *
from turtle import *


def seti(v):
    pu()
    setpos(v[0])
    seth(v[1])
    pd()

def mv(d):
    pu()
    fd(d)
    pd()

def do(n,d,o,x,s,c,r):
    for i in range(n):
        temp = ''
        for j in x:
            try: temp += r[j]
            except: temp += j
        x = temp
    setup(width=1000,height=900,startx=None,starty=None)
    ht()
    tracer(n=len(x))
    for k in x:
        try: exec(c[k])
        except: None
    done()
    

def main():
    iteratns = 0
    distance = 10
    angle    = 90
    axiom    = ''
    saved    = []
    commands = {'-':'lt(o)','+':'rt(o)','[':'s.append([pos(),heading()])',']':'seti(s.pop())'}
    rules    = {}
    if len(argv)>1:
        file = open(argv[1]).read()
        if file[:3]=='STT' and (file[-3:]=='END' or file[-4:]=='END\n'):
            setup = file.split('\n')[1:-1]
            for sett in setup:
                args = sett.split()
                if args[0]=='MOV':
                    try: distance = float(args[1])
                    except: distance = 10
                elif args[0]=='AXI': axiom = args[1]
                elif args[0]=='DEG':
                    try: angle = float(args[1])
                    except: angle = 90
                elif args[0]=='INC':
                    try: iteratns = int(args[1])
                    except: interatns = 0
                elif args[0]=='SET':
                    if args[2]=='0': commands.update({args[1]:'fd(d)'})
                    elif args[2]=='1': commands.update({args[1]:'mv(d)'})
                elif args[0]=='RPL': rules.update({args[1]:args[2]})
            do(iteratns,distance,angle,axiom,saved,commands,rules)
        else:
            print("Error: File does not have appropriate starting or ending identifiers.")
    else:
        print("Usage: python %s <program>"%os.path.basename(__file__))

if __name__=='__main__': main()
