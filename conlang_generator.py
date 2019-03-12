#-*- coding: utf-8 -*- 
import random
import string    


'''
Conlang ver 1.1
'''

#define roots types to randomly choice from and generate roots


class Root:

    '''
    Generates a list of roots of сertain type by random choice from ROOTS 
    made of RWOVS and RCONS graphemes 
    '''
    
    def generate_root(self, roots_quantity):
        
        #a number of roots to be generated
        self.roots_quantity = int(roots_quantity)

        self.ROOT_TYPES = [
            'cvvc', 'vcvvc', 'cv', 'cvv', 'vvcv', 
            'cvcv', 'vcvc', 'ccv', 'vvc', 'vc'
        ]

        #graphems to generate roots from
        self.RVOWS = ['a','e','y','u','i','o', 'æ', 'ā', 'ī']
        self.RCONS = [
            'q','z','w','s','kh','d','c','r',
            'f','v','t','g','b','h','n','j',
            'm','k','l','p','ʧ','θ','ð','z','ň' 
        ]
        self.root = ''
        self.roots = []


        #generate a root according to the scheme set in ROOT_TYPES
        while self.roots_quantity != 0:
    
            for _type in self.ROOT_TYPES:
            
                for i in _type:
                    if i == 'c':
                        self.root += random.choice(self.RVOWS)
                    if i == 'v':
                        self.root += random.choice(self.RCONS)

                self.roots.append(self.root)
                
                #null the generated root after appending it to the [self.roots] 
                self.root = ''

                self.roots_quantity -= 1

        return self.roots

    
    def show_roots(self):
        print(self.roots)
            


r = Root()
r.generate_root(33)
r.show_roots()



class Prefix:
    '''
    Generates a list of prefixes of сertain type by random choice from PREFS 
    made of PWOVS and PCONS graphemes 
    '''
    
    def generate_pref(self, prefs_quantity):
        
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
    
#p = Prefix()
#p.generate_pref(50)
#p.show_prefs()
