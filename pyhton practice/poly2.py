#Inheritance Class Polymorphism
class transport():
    pass
class car(transport):
    def __init__(self,b,m):
        self.b = b
        self.m = m 
    def move(self):
        print('mei nikla gaddi leke raste par ek mod aya hai mei utthe dil chor aya ')
    def hi(self):
        print("gali gali sim sim gali gali sim sim gali gali sim sim sim sim gali gali sim sim ")
class bus(transport):
    def __init__(se,b,m):
        se.b = b 
        se.m = m 
    def move(se):
         print("ajj kal tere mere pyar ke charche haar jaban par sabko malum hai aur sabko khabar hogai ")
    def hi(se):
        print('zindigi ek safar hai suhana yaha kal kya ho kisne jana ')
class walk(transport):
    def __init__(s,b,m):
        s.b = b
        s.m = m
    def move(s):
        print('bin puche mera naam aur pata rasmo ko rakh ke pare char kadam bus char kadam chal do na saath mere ')
    def hi(s):
        print('jane kaha mera jigar gya ji abhi abhi yehi tha kidhar gya ji kiski adaon pe maar gya ji abhi abhi yehi tha kidhar gya ji')

o1 = car("ferari",'kisawari')
o2 = bus('ashok','mercedes')
o3 = walk('female','korean')

for x in (o1,o2,o3):
    print(x.b)
    print(x.m)
    x.hi()
    x.move()

     