#-*- coding: utf-8 -*-   #letter = random.choice(string.ascii_lowercase)
import random
import string    


VOWS = ['a','e','y','u','i','o', 'æ', 'ā', 'ī']

CONS = ['q','z','w','s','x','d','c','r',
        'f','v','t','g','b','h','n','j',
        'm','k','l','p','ʧ','θ','ð','z','ň' 
]



class Morpheme:
    '''This class creates a morpheme.

       Morpheme is limited by 3 params:
               -minimum size (2 by default)
               -maximum size (3 by defaut)
               -2 types of grapheme: vowel | consonant 
    '''
    

    def __init__(self, min_size:int=2, max_size:int=3, passed=False):
        self.min_size = min_size
        self.max_size = max_size
        self.passed = passed
        self.morph_output = []

    
    def generate_morph(self):
        s = ''

        for i in self.passed:

            if i == 'c':
                c = random.choice(CONS)
                s += c
            else:
                v = random.choice(VOWS)
                s += v
        self.morph_output.append(s)



    def multiply_morph_output(self, morph_multiply_index:int):
        self.morph_multiply_index = morph_multiply_index

        while self.morph_multiply_index != 0:
           # generate_morph = self.generate_morph()
           # morph = self.return_morph_output()
            input()
            self.morph_output.append(self.generate_morph())
            print(self.morph_output)
            self.morph_multiply_index -= 1







    def return_morph_output(self):
        return self.morph_output



    def show_morph_output(self):
        print(self.morph_output)   




class Prefix:
    '''This class creates a prefix.

       This class is limited by 3 params:
               -minimum size (1 by default)
               -maximum size (3 by defaut)
               -2 types of grapheme: vowel | consonant 
    '''


    def __init__(self, min_size:int=1, max_size:int=3, passed=False):
        self.min_size = min_size
        self.max_size = max_size
        self.passed = passed








m = Morpheme(2, 4, 'cvvvccv')
m.generate_morph()
m.multiply_morph_output(10)
