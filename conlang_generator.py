

#-*- coding: utf-8 -*- 
import random
import string 
from conlang_data import *   


'''
 A VERY SIMPLE conlang ver. 1.2
'''

prefixes = []
roots = []
suffixes = []

verbs = []
nouns = []
adjectives = []

pref_null = ''
root_null = ''
suff_null = ''

number = 0

class Amount:
    def __init__(self, amount:int):
        self.amount = amount
        number = self.amount


class Prefix:
    def __init__(self, amount:int):
        self.amount = amount

    def generate_pref(self):
         
        '''
        This method generates prefixes
        '''
        #pref_amount = self.amount 
        self.pref = ''
 
        #generate a prefix according to the scheme set in data.PREF_TYPES
        while self.amount != 0:
            _type = random.choice(PREF_TYPES)
            for i in _type:
                
                if i == 'c':
                    self.pref += random.choice(PCONS)
                
                if i == 'v':
                    self.pref += random.choice(PVOWS)
            
            self.pref += '-'
                
            prefixes.append(self.pref)
                    
            #null the generated pref after appending it to the [self.prefs] 
            self.pref = ''
                        
            random.shuffle(PCONS)
            random.shuffle(PVOWS)
            self.amount -= 1

            
        print(prefixes)



class Root:
    '''
    Generates a stem by contacenating: ([prefix]+root+[suffix])
    '''
    def __init__(self, amount:int):
        self.amount = amount

    def generate_root(self): 
        '''
        This method generates roots
        '''
        self.root = ''

        #generate a root according to the scheme set in conlang_data.ROOT_TYPES
        while self.amount != 0:
            _type = random.choice(ROOT_TYPES)
            for i in _type:
                if i == 'c': 
                    self.root += random.choice(RVOWS)
                if i == 'v':
                    self.root += random.choice(RCONS)
            roots.append(self.root)
                
            #null the generated root after appending it to the [self.roots] 
            self.root = ''

            self.amount -= 1

            random.shuffle(ROOT_TYPES)
            random.shuffle(RVOWS)
            random.shuffle(RCONS)
       
        print(roots)



class Suffix:

    def __init__(self, amount:int):
        self.amount = amount

    def generate_suff(self):
        '''
        This method generates roots
        '''
        self.suff = ''

        #generate a root according to the scheme set in ROOT_TYPES
        while self.amount != 0:
        
            _type = random.choice(SUFF_TYPES)
            self.suff += '-'
            for i in _type:
                if i == 'c': 
                    self.suff += random.choice(SCONS)
                if i == 'v':
                    self.suff += random.choice(SVOWS)
            suffixes.append(self.suff)
                 
            #null the generated root after appending it to the [self.roots] 
            self.suff = ''
            
            self.amount -= 1

            random.shuffle(SUFF_TYPES)
            random.shuffle(SVOWS)
            random.shuffle(SCONS)

        print(suffixes)


class Noun: 

    def contacenate_noun(self):

        self.amount = amount 
        self.noun = ''

        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            self.noun += x
            self.noun += y
            self.noun += z

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            
            nouns.append(self.noun) 
            self.noun = ''

        nouns.insert(0, 'NOUNS:')
        print(nouns)



class Verb:

    def contacenate_verb(self):
        self.amount = amount 
        self.verb = ''
        
        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            self.verb += x
            self.verb += y
            self.verb += z
            self.verb += VERB_INFIN_MARKER

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            random.shuffle(VERB_CONJ_MARKERS)
            
            verbs.append(self.verb) 
            self.verb = ''

        verbs.insert(0, 'VERBS:')
        print(verbs)



class Adjective:

    def contacenate_adjective(self):
        self.amount = amount        
        self.adjective = ''

        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            ending = random.choice(ADJ_ENDINGS)
            self.adjective += x
            self.adjective += y
            self.adjective += z
            self.adjective += ending

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            random.shuffle(ADJ_ENDINGS)
            
            adjectives.append(self.adjective) 
            self.adjective = ''
        
        adjectives.insert(0, 'ADJECTIVES:')
        print(adjectives) 


    
p = Prefix(10)
p.generate_pref()

r = Root(10)
r.generate_root()

s = Suffix(10)
s.generate_suff()

n = Noun()
n.contacenate_noun()

v = Verb()
v.contacenate_verb()

a = Adjective()
a.contacenate_adjective()


#['NOUNS: ', 'am-mpo-ass', 'rra-barrmy-ass', 'að-nefge-ass', 'ra-ym-æp', 'ov-bæ-āss', 'vo-iyrr-að', 'orr-adāð-æss', 'ða-ufp-āp', 'ov-pæ-að']
#['VERBS: ', 'að-iyrr-ass-ed', 'am-pæ-æss-i', 'orr-tkā-að-em', 'ov-mpo-æp-ed', 'rro-barrmy-āp-i', 'ra-ym-að-am', 'ða-ufp-ass-i', 'rra-nefge-āss-and', 'vo-adāð-ass-am']



'''def contacenate_noun(self):
        
        This method contacenates
        
        self.word = '' 
        self.nouns = ['NOUNS: ']

        for x,y,z in zip(self.prefs, self.roots, self.suffs):
            self.word += x
            self.word += y
            self.word += z
            self.word += 'r'

            self.nouns.append(self.word.replace('-', '')) 
            self.word = ''
        print(self.nouns)'''
            
