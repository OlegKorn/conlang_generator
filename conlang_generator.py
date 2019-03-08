#-*- coding: utf-8 -*-   #letter = random.choice(string.ascii_lowercase)
import random
import string    


VOWS = ['a','e','y','u','i','o', 'æ', 'è', 'é', 'à', 'ā', 'ī']

CONS = ['q','z','w','s','x','d','c','r',
        'f','v','t','g','b','h','n','j',
        'm','k','l','p','ʧ','θ','ð','z','ň' 
]

output = []

class Morpheme: 
    def __init__(self, data):
        self.data = data
        self.len = len(self.data)

    
    # recognizes a graphem type to generate
    def create_graph(self):
        lexem = ''
        for i in self.data:

            if i == 'v':
                v = random.choice(VOWS)
                lexem += v
            elif i == 'c':
                c = random.choice(CONS)
                lexem += c
    
        output.append(lexem) 

    
    def get_output(self):
        print(output)


    def multiply(self, times:int):
        self.times = times
        m = Morpheme('vcvc')
        
        while self.times > 1:
            
            m.create_graph()
            self.times -= 1

        #m.get_output()
        




m = Morpheme('vcvc')
m.multiply(20)

print(output)


