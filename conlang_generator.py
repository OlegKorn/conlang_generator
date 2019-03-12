#-*- coding: utf-8 -*- 
import random
import string    


'''
 A VERY SIMPLE conlang ver. 1.2
'''


class Prefix:
    '''
    Generates a list of prefixes of сertain type by random choice from PREFS 
    made of PWOVS and PCONS graphemes 
    '''
    
    def generate_pref(self, prefs_quantity=1):
        
        #a number of prefs to be generated
        self.prefs_quantity = int(prefs_quantity)

        self.PREF_TYPES = ['vc', 'cv']

        #graphems to generate roots from
        self.PVOWS = ['a','o']
        self.PCONS = ['r','v','rr','m','ð']
        self.pref = ''
        self.prefs = []

        #generate a root according to the scheme set in ROOT_TYPES
        while self.prefs_quantity != 0:
    
            for _type in self.PREF_TYPES:
            
                for i in _type:
                    if i == 'c':
                        self.pref += random.choice(self.PVOWS)
                    if i == 'v':
                        self.pref += random.choice(self.PCONS)
                self.pref += '-'

                self.prefs.append(self.pref)
                
                #null the generated root after appending it to the [self.roots] 
                self.pref = ''

                self.prefs_quantity -= 1

        return self.prefs

    def show_prefs(self):
        print(self.prefs)


class Root:
    '''
    Generates a list of roots of сertain type by random choice from ROOTS 
    made of RWOVS and RCONS graphemes 
    '''
   
    def generate_root(self, roots_quantity=1):
        
        #a number of roots to be generated
        self.roots_quantity = int(roots_quantity)

        self.ROOT_TYPES = [
            'cvvc', 'vcvvc', 'cv', 'cvv', 'vvcv', 
            'cvcv', 'vcvc', 'ccv', 'vvc', 'vc'
        ]

        #graphems to generate roots from
        self.RVOWS = ['a','e','y','u','i','o', 'æ', 'ā', 'ī']

        self.RCONS = [
            's','k','d','rr','n', 
            'g','t','f','rr','b','n',
            'm','k','rr','l','p','ð' 
        ]

        self.root = ''
        self.roots = []


        #generate a root according to the scheme set in ROOT_TYPES
        while self.roots_quantity != 0:
    
            _type = random.choice(self.ROOT_TYPES)
            
            for i in _type:
                if i == 'c': 
                    self.root += random.choice(self.RVOWS)
                if i == 'v':
                    self.root += random.choice(self.RCONS)
            self.roots.append(self.root)
                
            #null the generated root after appending it to the [self.roots] 
            self.root = ''

            self.roots_quantity -= 1
            random.shuffle(self.ROOT_TYPES)
            random.shuffle(self.RVOWS)
            random.shuffle(self.RCONS)

        return self.roots

    
    def show_roots(self):
        print(self.roots)
            



class Suffix:
    '''
    Generates a list of suffixes of сertain type by random choice from SUFFS 
    made of SWOVS and SCONS graphemes 
    '''
   
    def generate_suff(self, suffs_quantity=1):
        
        #a number of suff-s to be generated
        self.suffs_quantity = int(suffs_quantity)

        self.SUFF_TYPES = ['cvc', 'vvc', 'cv', 'vc']

        #graphems to generate roots from
        self.SVOWS = ['a','æ','ā']

        self.SCONS = ['ss','p','ð']

        self.suff = ''
        self.suffs = []


        #generate a root according to the scheme set in ROOT_TYPES
        while self.suffs_quantity != 0:
    
            _type = random.choice(self.SUFF_TYPES)
            self.suff += '-'
            
            for i in _type:
                if i == 'c': 
                    self.suff += random.choice(self.SVOWS)
                if i == 'v':
                    self.suff += random.choice(self.SCONS)
            
            self.suffs.append(self.suff)
                
            #null the generated root after appending it to the [self.roots] 
            self.suff = ''
            self.suffs_quantity -= 1

            random.shuffle(self.SUFF_TYPES)
            random.shuffle(self.SVOWS)
            random.shuffle(self.SCONS)

        return self.suffs

    
    def show_suffs(self):
        print(self.suffs)

#s = Suffix()
#s.generate_suff(20)
#s.show_suffs()


class Noun:
    '''Contacenates a noun from Prefix, Root, Suffix classes output
    '''

    def __init__(self, nouns_amount=10):
        self.nouns_amount = nouns_amount

    def contacenate_noun(self):
        
        p = Prefix()
        p.generate_pref(self.nouns_amount)

        r = Root()
        r.generate_root(self.nouns_amount)

        s = Suffix()
        s.generate_suff(self.nouns_amount)

        self.nouns = []

        for x,y,z in zip(p.prefs, r.roots, s.suffs):
            print(x,y,z) 


n = Noun()
n.contacenate_noun()


