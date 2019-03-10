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

#to increase the "depth of choice" there are more than 2 same entities here
TYPES = ['v','c','v','c','v','c','v','c','v','c','v','c','v','c']


morph_res = []


class Morpheme:
    '''This class creates a morpheme.

    Morpheme is limited by 3 params:
        -minimum size (2 by default)
        -maximum size (3 by defaut)
        -2 types of grapheme: vowel | consonant 
    '''
    
     


    def set_random_len(self):
        self.l_min = random.choice(range(2))
        self.l_max = random.choice(range(2,4))

        self.m_len = ((self.l_max - self.l_min) + 1) 
        return self.m_len
        

    def generate_morph(self):
    
        self.generated_type = ''
        self.generated_morph = '' 
        
        self._len = self.set_random_len()
            
        for i in range(self._len):
            self.graphem_type = random.choice(TYPES)
            self.generated_type += self.graphem_type

        for i in self.generated_type:
            if i == 'v':
                self.v_choosen = random.choice(MVOWS)
                self.generated_morph += self.v_choosen
            elif i == 'c':
                self.c_choosen = random.choice(MCONS)
                self.generated_morph += self.c_choosen

        morph_res.append(self.generated_morph)


    def morph_multiply(self, index):
        self.index = index
        while self.index != 0:
            self.generate_morph()
            random.shuffle(MVOWS)
            random.shuffle(MCONS)
            self.index -= 1


    def return_morph_output(self):
        return morph_res



    def show_morph_output(self):
        print(morph_res)   


m = Morpheme()
m.morph_multiply(20) #['khyw', 'āf', 'æt', 'ejc', 'θroe', 'na', 'uar', 'yuuf', 'tqpz', 'īgň', 'zň', 'noʧ', 'cāðy', 'ccvī', 'eīik', 'aw', 'ia', 'tej', 'aī', 'kāky']
m.show_morph_output()
#m.generate_morph()



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
