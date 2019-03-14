
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

sent = ''

class Amount:
    def __init__(self, amount:int):
        self.amount = amount + 1
        

class Prefix:
    def __init__(self):
        self.amount = a.amount

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
            
            prefixes.append(self.pref)
                    
            #null the generated pref after appending it to the [self.prefs] 
            self.pref = ''
                        
            random.shuffle(PCONS)
            random.shuffle(PVOWS)
            self.amount -= 1




class Root:
    '''
    Generates a stem by contacenating: ([prefix]+root+[suffix])
    '''
    def __init__(self):
        self.amount = a.amount

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
       



class Suffix:

    def __init__(self):
        self.amount = a.amount

    def generate_suff(self):
        '''
        This method generates roots
        '''
        self.suff = ''

        #generate a root according to the scheme set in ROOT_TYPES
        while self.amount != 0:
        
            _type = random.choice(SUFF_TYPES)
            
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



class Noun: 

    def contacenate_noun(self):

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

        nouns.insert(0, 'NOUNS: ')
        #print(nouns)



class Verb:

    def contacenate_verb(self):

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

        verbs.insert(0, 'VERBS: ')
        #print(verbs)



class Adjective:

    def contacenate_adjective(self):

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
        
        adjectives.insert(0, 'ADJECTIVES: ')
        print(adjectives) 





class Sentence:
    def __init__(self, sentence_length:int=False):
        self.sentence_length = sentence_length
        self.sentence = []

    def create(self):
        
        #define combinations of entities
        #verbs = []
        #nouns = []
        #adjectives = []

        # noun + verb
        noun_verb = random.choice(nouns) + ' ' + random.choice(verbs)
        print(f' V+N: {noun_verb}')


#for key, value in PRONOUNS.items():
#    print(key, value)

a = Amount(105)  #задаем количество сущностей для генерации
print(a.amount)


p = Prefix()
p.generate_pref()

r = Root()
r.generate_root()

s = Suffix()
s.generate_suff()

n = Noun()
n.contacenate_noun()

v = Verb()
v.contacenate_verb()

a = Adjective()
a.contacenate_adjective()

se = Sentence()
se.create()  # N+V: aðāsopāp ðoknumassen
     
