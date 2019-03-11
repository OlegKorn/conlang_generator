#-*- coding: utf-8 -*- 
import random
import string    


'''
Conlang ver 1.1
'''

#define roots types to randomly choice from and generate roots


class Root:

    '''
    Generates a root of сertain type by random choice from ROOTS 
    made of RWOVS and RCONS graphemes 
    '''
    
    def generate_root(self):
        
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
        for _type in self.ROOT_TYPES:
            
            for i in _type:
                if i == 'c':
                    self.root += random.choice(self.RVOWS)
                if i == 'v':
                    self.root += random.choice(self.RCONS)

            self.roots.append(self.root)
            #null the generated root after appending it to the [self.roots] 
            self.root = ''

        return self.roots

    
    def show_roots(self):
        print(self.roots)
            


r = Root()
r.generate_root()
r.show_roots()
