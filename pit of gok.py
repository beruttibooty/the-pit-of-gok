import random

#strength, size, agility, speed, coolness, intelligence, experience
#    0      1       2        3     4            5            6
fighters = {
    'dwayne':(100, 1.96, 75, 60, 95, 75, 100),
    'wayne':(90, 2.2, 80, 63, 90, 76, 75),
    'curtis jackson':(105, 1.83, 65, 55, 93, 83, 80),
    'jackie chan':(80, 1.74, 90, 90, 90, 80, 100),
    'lightning mcqueen':(50, 1.45, 125, 125, 90, 60, 50),
    'iron giant':(10000, 18.3, 5, 70, 40, 40, 40),
    'hulk':(2000, 3, 30, 50, 65, 40, 80), 
    'marty mcfly':(65, 1.75, 80, 90, 90, 90, 75),
    'malcolm in the middle':(),
    'malcolm x':(),
    'shia labeouf':(70, 1.76, 85, 77, 80, 80, 80),
    'stanley yelnats':(60, 1.56, 95, 90, 85, 90, 85),
    'martin luther king junior':(),
    'pupienus':(85, 1.8, 80, 80, 100, 65, 100),
    'shitulus maximus':(random.randrange(1,100),random.randrange(100,200)/100,random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100)),
    'michelin man':(90, 2.2, 60, 65, 85, 75, 40),
    'sonic':(60, 1.2, 150, 150, 100, 40, 80),
    'po':(95, 2.1, 90, 60, 70, 60, 100),
    'general grevious':(),
    'tupac':(),
    'biggie smalls':(),
    'drake':(),
    'the bloods':(),
    'timmy turner':(),
    'hugh neutron':(),
    'dinkelberg':(),
    'cal':(80, 1.85, 80, 80, 100, 100, 80),
    'black cal':(125, 2.5, 100, 100, 150, 150, 100),
    'stubby':(),
    'irene':(),
    'stefania':(),
    'dumbledore':(),
    'tony the tiger':(100, 2.2, 85, 70, 105, 80, 30),
    'tigress':(80, 2.2, 100, 100, 80, 85, 100),
    'master oogway':(150, 2, 10, 10, 100, 250, 100),
    'spirit oogway':(150, 2, 50, 50, 100, 260, 100),
    'wise turtle':(10, .15, 5, 5, 35, 250, 25),
    'pigeon':(3, .15, 150, 150, 10, 10, 10), 
    'tigger':(90, 2.3, 95, 80, 100, 40, 75),
    'mount vesuvius':(500000, 1281, 0, 0, 90, 0, 7980),
    'alma mater':(),
    'the green giant':(),
    'lovie smith':(),
    'snap':(),
    'crackle':(),
    'pop':(),
    'italian stallion':(),
    'bruce lee':(),
    'schwarzeneger':(),
    'john cena':(),
    'vasco rossi':(),
    'anakin skywalker':(),
    'shrek':(),
    'kevin':(60, 1.75, 40, 40, 10, 50, 0),
    'gok':(90, 1.75, 10, 9, 0, 1, 0),
    'michael':(70, 1.85, 80, 75, 78, 98, 50),
    'tyler':(73, 1.9, 80, 80, 80, 90, 75),
    'nick':(70, 1.85, 82, 80, 75, 85, 78),
    'ethan':(65, 1.83, 75, 80, 100, 95, 45),
    'jack':(),
    'max':(),
    'ian':(),
    'elanor':(30, 1.65, 80, 40, 0, 50, 2),
    'kaliroe':(40, 1.65, 60, 60, 60, 60, 0),
    'rachel':(),
    'taylor':(),
    'scooby doo':(),
    'melvin doo':(),
    'fred':(),
    'shaggy':(),
    'elmer fudd':(),
    'sylvester the cat':(),
    'mr incredible':(),
    'mr coffee':(70, .25, 20, 90, 70, 75, 5),
    'hulk hogan':(95,2.01, ),
    'the undertaker':(100,2.08),
    'kimbo slice from drake and josh':(),
    'drake bell':(),
    'josh peck':(),
    'youngling':(),
    'andre':(65, 1.78, 85, 80, 95, 80, 40),
    'andre 3000':(3000, 1.78, 85, 80, 95, 80, 40),
    'pepsicita':(50, 1.6, 70, 75, 90, 95, 25),
    'helen keller':(),
    'anne frank':(),
    'hitler':(),
    'bruce genner':(),
    'caitlyn genner':(),
    'pokemon kid':(25, 1.6, 35, 45, 10, 10, 30),
    'sean paul':(),
    'big sean':(75, 1.73, 75, 80, 80, 50, 60),
    'steve martin':(),
    'steve martin the actor':(),
    'dracula':(),
    'jimi hendrix':(),
    'subway guy':(),
    'jared from subway':(),
    'jake from state farm':(),
    'sienna pizza guy':(),
    'fry guy':(),
    'wine amica':(),
    'the pope':(),
    'gazelle':(),
    'donkey':(),
    'lord farquad':(),
    'feona':(),
    'owen wilson':(),
    'owen wilson as a mini cowboy':(),
    'mini cowboy as owen wilson':(),
    'owen wilson as drillbit taylor':(),
    'donkey kong':(),
    'drift king':(),
    'kangaroo jack':(90, 2.3, 95, 150, 80, 50, 30),
    'santa claus':(75, 1.9, 69, 69, 110, 120, 100),
    }
prefix = {
    'deca': 10,
    'hecto': 100,
    'kilo': 1000,
    'mega': 1000000,
    'giga': 1000000000,
    'tera': 1000000000000,
    'peta': 1000000000000000,
    'exa': 1000000000000000000,
    'lil': .75,
    'big': 1.5,
    'large': 5,
    'XL': 40,
    'deci': .1,
    'centi': .01,
    'milli': .001,
    'micro': .000001,
    'nano': .000000001,
    'pico': .000000000001,
    'femto': .000000000000001,
    'atto': .000000000000000001,
    'planck': .00000000000000000000000000000000001,
    }
items = {
    'infinity gauntlet':(),
    'fedora':(1,0, 1,0, 1,0, 1,0, .3,0, 1,10, 1,0),
    'iron man suit':(1,150, 1,0, 1,-10, 0,120, 1.1,10, 1,0, 1,0),
    'black panther suit':(1,100, 1,.2, 1.7,0, 1.5,0, 1.3,5, 1,0, 1,0),
    'retardation':(1.4,0, 1,0, 1,0, 1,0, .7,0, .1,0, 1,0),
    'fighter jet':(1.01,2000, 0,4, 0,200, 0,600, 1.2,0, 1,0, 1,0),
    'gok':(1,90, 1,-30, 1,-20, 1,9, 1,0, 1,-10, 1,0),
    'glock':(1,100, 1,0, 1,0, 1,0, 1,0, 1,0, 1,0),
    'the juice':(1.3,0, 1.3,0, 1.3,0, 1.3,0, 1.3,0, 1.3,0, 1.3,0,),
    'the sauce':(1.5,0, 1.5,0, 1.5,0, 1.5,0, 1.5,0, 1.5,0, 1.5,0,),
    }

print("today's lucky numbers are: {}".format(fighters['shitulus maximus']))

def fm(strang, trials=100000):
    strang = strang.split(' vs ')
    name1=strang[0]
    if strang[0][0].isnumeric():
        n1=''
        name1=''
        for char in strang[0]:
            if char.isnumeric(): n1+=char
            else: name1 += char
        name1 = name1[1:]
        n1=int(n1)
    else: n1 = 1
    name2=strang[1]
    if strang[1][0].isnumeric():
        n2=''
        name2=''
        for char in strang[1]:
            if char.isnumeric(): n2+=char
            else: name2 += char
        name2 = name2[1:]
        n2=int(n2)
    else:
        n2 = 1
    try:
        ni1 = name1.split(' with ')
        name1 = ni1[0]
        ni1 = items[ni1[1]]
    except: ni1 = []
    try:
        ni2 = name2.split(' with ')
        name2 = ni2[0]
        ni2 = items[ni2[1]]
    except: ni2 = []
    try:
        f1=list(fighters[name1])
        rname1=name1
    except:
        prefix1 = prefix[name1.split(' ',1)[0]]
        f1=list(fighters[name1.split(' ',1)[1]])
        rname1=name1.split(' ',1)[1]
        f1[1]=f1[1]*prefix1
        f1[0]=f1[0]*prefix1
    try:
        f2=list(fighters[name2])
        rname2=name2
    except:
        prefix2 = prefix[name2.split(' ',1)[0]]
        f2=list(fighters[name2.split(' ',1)[1]])
        rname2=fighters[name2.split(' ',1)[1]]
        f2[1]=f2[1]*prefix2
        f2[0]=f2[0]*prefix2
    try:
        for i1 in range(0,7):
            f1[i1]*=ni1[2*i1]
            f1[i1]+=ni1[2*i1+1]
    except: ni1 = []
    try:
        for i2 in range(0,7):
            f2[i2]*=ni2[2*i2]
            f2[i2]+=ni2[2*i2+1]
    except: ni2 = []
    f1 = [name1] + f1
    f2 = [name2] + f2
    winner = fight(n1,f1,n2,f2,trials)
    if trials is 0:
        return winner

def fight(n1, dude1, n2, dude2, trials=100000):
    prt = True
    if trials is 0:
        trials = 1
        prt = False
    if type(dude1) != list:
        d1o = list(fighters[str(dude1)])    
        d2o = list(fighters[str(dude2)])
    else:
        d1o=dude1[1:]
        d2o=dude2[1:]
        dude1=dude1[0]
        dude2=dude2[0]
    if(n1>1): d1o[0] = d1o[0]+d1o[0]*(n1-1)*(d1o[5]/100)**(1/2)*3
    if(n2>1): d2o[0] = d2o[0]+d2o[0]*(n2-1)*(d2o[5]/100)**(1/2)*3

    d1w = 0
    d2w = 0

    i = trials
    while i >= 1:
        i-=1

        d1s = d1o[0]*2 + d1o[1]*105 + d1o[2]*1.2 + d1o[3]*1.2 + d1o[4]/2 + d1o[5]*1.3 + d1o[6]*1.4
        if prt: d1s = d1s*random.randrange(90,110)/100
        d2s = d2o[0]*2 + d2o[1]*105 + d2o[2]*1.2 + d2o[3]*1.2 + d2o[4]/2 + d2o[5]*1.3 + d2o[6]*1.4
        if prt: d2s = d2s*random.randrange(90,110)/100

        if d1s>d2s: d1w +=1
        else: d2w +=1

    
    if prt: print((d1w,d2w))
    if(d1w>d2w):
        if prt:
            if(n1>1): print('the {}s win!'.format(dude1))
            else: print('{} wins!'.format(dude1))
            print('{}% win rate'.format(d1w/trials*100))
        return (True,dude1)
    else:
        if prt:
            if(n2>1): print('the {}s win!'.format(dude2))
            else: print('{} wins!'.format(dude2))
            print('{}% win rate'.format(d2w/trials*100))
        return (False,dude2)

def hm(sent):
    '''one = fm('1 '+sent,0)
    if one[0] is True:
        print('it takes only one {} to win.'.format(one[1]))
        return'''
    i = 1
    while(True):
        #try:
        result = fm(str(i)+' '+sent,0)
        #except:
        #    print('not going to happen')
        #    return
        if result[0] is True:
            break
        i*=10
    i/=10
    out = list(str(int(i)))
    for j in range(0,len(out)):
        while(True):
            result = fm(''.join(out)+' '+sent,0)
            if result[0] is True:
                out[j]=str(int(out[j])-1) 
                break
            out[j]=str(int(out[j])+1)
    out[-1]=str(int(out[-1])+1)
    if out == ['0']: print('{} always wins'.format(result[1]))
    else: print('it takes {} {}s to win.'.format(''.join(out),result[1]))
    








