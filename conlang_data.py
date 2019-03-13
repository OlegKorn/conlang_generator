#-*- coding: utf-8 -*- 
import random
import string 
from conlang_data import *   


'''
 A VERY SIMPLE conlang ver. 1.2
'''

prefixes = ['PREFIXES: ']
roots = ['ROOTS: ']
suffixes = ['SUFFIXES: ']

verbs = ['VERBS: ']

class Prefix:
    
    def __init__(self, amount:int=1):
        self.amount = amount

    def generate_pref(self):
        '''
        This method generates prefixes
        '''
        pref_amount = self.amount
        self.pref = ''
 
        #generate a prefix according to the scheme set in data.PREF_TYPES
        while self.amount != 0:
            for _type in PREF_TYPES:
                for i in _type:
                    if i == 'c':
                        self.pref += random.choice(PVOWS)
                    if i == 'v':
                        self.pref += random.choice(PCONS)
                self.pref += '-'
                prefixes.append(self.pref)
                   
                #null the generated pref after appending it to the [self.prefs] 
                self.pref = ''

                self.amount -= 1
                    
                random.shuffle(ROOT_TYPES)
                random.shuffle(RVOWS)
                random.shuffle(RCONS)

        return prefixes



class Root:
    '''
    Generates a stem by contacenating: ([prefix]+root+[suffix])
    '''
    def __init__(self, amount:int=1):
        self.amount = amount

    def generate_root(self):
        '''
        This method generates roots
        '''
        root_amount = self.amount
        self.root = ''

        #generate a root according to the scheme set in conlang_data.ROOT_TYPES
        while root_amount != 0:
            _type = random.choice(ROOT_TYPES)
            for i in _type:
                if i == 'c': 
                    self.root += random.choice(RVOWS)
                if i == 'v':
                    self.root += random.choice(RCONS)
            roots.append(self.root)
                
            #null the generated root after appending it to the [self.roots] 
            self.root = ''

            root_amount -= 1

            random.shuffle(ROOT_TYPES)
            random.shuffle(RVOWS)
            random.shuffle(RCONS)
       
        return roots



class Suffix:

    def __init__(self, amount:int=1):
        self.amount = amount


    def generate_suff(self, amount=1):
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

        return suffixes



class Verb:
    def __init__(self, amount:int=1):
        self.amount = amount


    def contacenate_verb(self):
        p = Prefix(self.amount)
        p.generate_pref()

        r = Root(self.amount)
        r.generate_root()

        s = Suffix(self.amount)
        s.generate_suff()

        self.verb = ''
        
        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            marker = random.choice(VERB_CONJ_MARKERS)
            self.verb += x
            self.verb += y
            self.verb += z
            self.verb += marker

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            random.shuffle(VERB_CONJ_MARKERS)
            
            verbs.append(self.verb) 
            self.verb = ''

        print(verbs)


v = Verb(4)
v.contacenate_verb()

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
            
