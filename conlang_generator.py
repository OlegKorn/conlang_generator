#-*- coding: utf-8 -*- 
import random
import string 
from conlang_data import *   


'''
 A VERY SIMPLE conlang ver. 1.2
'''





class Noun:
    '''
    Generates a noun by contacenating: (prefix+root+suffix)
    '''
    def __init__(self, amount:int=1):
        self.amount = amount

    
    def generate_pref(self):
        '''
        This method generates prefixes
        '''
        pref_amount = self.amount
        self.pref = ''
        self.prefs = []
 
        #generate a prefix according to the scheme set in data.PREF_TYPES
        while pref_amount != 0:
            for _type in PREF_TYPES:
                for i in _type:
                    if i == 'c':
                        self.pref += random.choice(PVOWS)
                    if i == 'v':
                        self.pref += random.choice(PCONS)
                self.pref += '-'
                self.prefs.append(self.pref)
                
                #null the generated pref after appending it to the [self.prefs] 
                self.pref = ''

                pref_amount -= 1
                
                random.shuffle(ROOT_TYPES)
                random.shuffle(RVOWS)
                random.shuffle(RCONS)

        return self.prefs

    

    def generate_root(self):
        '''
        This method generates roots
        '''
        root_amount = self.amount
        self.root = ''
        self.roots = []

        #generate a root according to the scheme set in conlang_data.ROOT_TYPES
        while root_amount != 0:
            _type = random.choice(ROOT_TYPES)
            for i in _type:
                if i == 'c': 
                    self.root += random.choice(RVOWS)
                if i == 'v':
                    self.root += random.choice(RCONS)
            self.roots.append(self.root)
                
            #null the generated root after appending it to the [self.roots] 
            self.root = ''

            root_amount -= 1

            random.shuffle(ROOT_TYPES)
            random.shuffle(RVOWS)
            random.shuffle(RCONS)

        return self.roots

        

    def generate_suff(self, suffs_quantity=1):
        '''
        This method generates roots
        '''
        suff_amount = self.amount
        self.suff = ''
        self.suffs = []

        #generate a root according to the scheme set in ROOT_TYPES
        while suff_amount != 0:
        
            _type = random.choice(SUFF_TYPES)
            self.suff += '-'
            for i in _type:
                if i == 'c': 
                    self.suff += random.choice(SCONS)
                if i == 'v':
                    self.suff += random.choice(SVOWS)
            self.suffs.append(self.suff)
                 
            #null the generated root after appending it to the [self.roots] 
            self.suff = ''
            suff_amount -= 1

            random.shuffle(SUFF_TYPES)
            random.shuffle(SVOWS)
            random.shuffle(SCONS)

        return self.suffs

    

    def contacenate_noun(self):
        '''
        This method contacenates
        '''
        self.word = '' 
        self.nouns = ['NOUNS: ']

        for x,y,z in zip(self.prefs, self.roots, self.suffs):
            self.word += x
            self.word += y
            self.word += z
            self.word += 'r'

            self.nouns.append(self.word.replace('-', '')) 
            self.word = ''
        print(self.nouns)
            
       


n = Noun(20)
n.generate_pref()
n.generate_root()
n.generate_suff()
n.contacenate_noun()
