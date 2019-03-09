#-*- coding: utf-8 -*-   #letter = random.choice(string.ascii_lowercase)
import random
import string    


MVOWS = ['a','e','y','u','i','o', 'æ', 'ā', 'ī']
MCONS = ['q','z','w','s','kh','d','c','r',
   'f','v','t','g','b','h','n','j',
   'm','k','l','p','ʧ','θ','ð','z','ň' 
]

PVOWS = ['e','i','o','æ']
PCONS = ['q','w','s','kh','r',
   'f','v','t','g','b','h','n','j',
   'l','p'
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


    
    def generate_morph(self, counter):
        '''counter = number of needed morphems * 5
        '''
        self.counter = counter
        while self.counter > 1:
            s = ''
            for i in self.passed:

                if i == 'c':
                    c = random.choice(MCONS)
                    s += c
                else:
                    v = random.choice(MVOWS)
                    s += v
            self.counter -= 1
            self.morph_output.append(s)



    def return_morph_output(self):
        return self.morph_output



    def show_morph_output(self):
        print(self.morph_output)   


m = Morpheme(2, 4, 'cvccv')
m.generate_morph(10)
m.show_morph_output() 

#o@pc:~/python/conlang$ python3 conlang_generator.py
#['θugzā', 'zyðza', 'zubfo', 'baqðe', 'ňermu', 'datqe', 'līfňa', 'pyθhā', 'tuckha']




class Prefix(Morpheme):
    '''This class creates a prefix.

       This class is limited by 3 params:
               -minimum size (1 by default)
               -maximum size (3 by defaut)
               -2 types of grapheme: vowel | consonant 
    '''
    
    def set_pref_output(self, pref_output = []):
        self.pref_output = pref_output


    def show_info(self):
        print(self.min_size, 
              self.max_size,
              self.passed
        )


    def generate_pref(self, counter):
        '''counter = number of needed morphems * 5
        '''
        self.counter = counter
        while self.counter > 1:
            s = ''
            for i in self.passed:

                if i == 'c':
                    c = random.choice(PCONS)
                    s += c 
                else:
                    v = random.choice(PVOWS)
                    s += v
            s += '-' 
            self.counter -= 1
            self.pref_output.append(s)



    def return_pref_output(self):
        return self.pref_output



    def show_pref_output(self):
        print(self.pref_output)   



p = Prefix(1,2,'cv')
p.set_pref_output()
p.generate_pref(10)
p.show_pref_output()


#https://www.geeksforgeeks.org/python-concatenate-two-lists-element-wise/
res = [i + j for i, j in zip(p.pref_output, m.morph_output)]


print(res)

#['syvðæ', 'lāzræ', 'wībma', 'ʧīcra', 'zāvða', 'highī', 'vīnza', 'θivmī', 'lījfa']
#['le-', 'wi-', 'qæ-', 'fi-', 'ti-', 'væ-', 'to-', 'gi-', 'be-']
#['le-syvðæ', 'wi-lāzræ', 'qæ-wībma', 'fi-ʧīcra', 'ti-zāvða', 'væ-highī', 
#'to-vīnza', 'gi-θivmī', 'be-lījfa']

#

