import time
from os import system,name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

N = {
    0 : [
        ' __ ',
        '|  |',
        '|__|',
    ],
    1 : [
        '    ',
        '   |',
        '   |',
    ],
    2 : [
        ' __ ',
        ' __|',
        '|__ ',
    ],
    3 : [
        ' __ ',
        ' __|',
        ' __|',
    ],
    4 : [
        '    ',
        '|__|',
        '   |',
    ],
    5 : [
        ' __ ',
        '|__ ',
        ' __|',
    ],
    6 : [
        ' __ ',
        '|__',
        '|__|',
    ],
    7 : [
        ' __ ',
        '   |',
        '   |',
    ],
    8 : [
        ' __ ',
        '|__|',
        '|__|',
    ],
    9 : [
        ' __ ',
        '|__|',
        ' __|',
    ]
}

def printSevenSegTime(t) :
    x = []
    for t in (t//3600, (t%3600)//60, t%60) :
        if t > 9 :
            x.extend([int(e) for e in list(str(t))])
        else :
            x.extend([0,t]) 
    print(N[x[0]][0]+'  '+N[x[1]][0]+'     '+N[x[2]][0]+'  '+N[x[3]][0]+'     '+N[x[4]][0]+'  '+N[x[5]][0])
    print(N[x[0]][1]+'  '+N[x[1]][1]+'  ·  '+N[x[2]][1]+'  '+N[x[3]][1]+'  ·  '+N[x[4]][1]+'  '+N[x[5]][1])
    print(N[x[0]][2]+'  '+N[x[1]][2]+'  ·  '+N[x[2]][2]+'  '+N[x[3]][2]+'  ·  '+N[x[4]][2]+'  '+N[x[5]][2])

def countDown(t) :
    clear()
    while t :
        printSevenSegTime(t)
        time.sleep(1)
        t-=1
        clear()
    printSevenSegTime(t)
    print('\n************Execute Order 77************')

def main() :
    inp = input('Input : ').split(':') #suppose the input will be in xx:xx:xx format only
    T = [int(t) for t in inp]
    if (T[1] <= 59) and (T[2] <= 59) :
        t = (3600*T[0]) + (60*T[1]) + T[2]
        while True :
                is_countdown = input('Countdown? (y/n) : ')
                if is_countdown.lower() == 'y' :
                    countDown(t) #count down
                    return 0
                elif is_countdown.lower() == 'n' :
                    printSevenSegTime(t) #just print
                    return 0
                else :
                    print('please input \'y\' or \'n\'')
        
    else :
        print()
        print('            ·              ·            ')
        print(' __    __   ·   __    __   ·   __    __ ')

main()
    