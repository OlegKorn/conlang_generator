#-*- coding: utf-8 -*-   #letter = random.choice(string.ascii_lowercase)
import random
import string    


VOWS = ['a','e','y','u','i','o']
CONS = ['q','z','w','s','x','d','c','r','f','v','t','g','b','h','n','j','m','k','l','p']


class Morphem: 
    '''
    morphem has params:
    --lenght
    --type of letters passed in - for example, v.v.c. 
    '''

    '''
    initialize the class with 1 param that every instance will have
    '''
    def __init__(self, graphems_set, counter=True):
        self.graphems_set = graphems_set
        self.graphems_list = list(self.graphems_set)
        self.counter = len(graphems_set)
  

    def show_info(self):
        print('graphems_set is {}\n'
          'len(graphems_set) is {}' 
          .format(self.graphems_list, self.counter)            
        )        
  
    
    #generate the needed random letters in accordance with the passed in ones
    def generate(self):
        '''
        generates morhpem after checking the type out
        (appends grapheme of needed type to a list * indicator) times     
        '''
        
        self.pre_output = ''
        
        #define the type of each graphem
        while self.counter != 0:

            for i in self.graphems_list:

                #if code == "vowel" 
                if i == 'v':
                    v = random.choice(VOWS)
                    self.pre_output += v

                #if code == "consonant" 
                elif i == 'c':
                    c = random.choice(CONS)
                    self.pre_output += c
                self.counter -= 1

        self.output = list(self.pre_output) 



    def get_output(self):
        print(self.output)
        print(self.graphems_list)


m = Morphem('vcvc')
m.generate()
m.get_output()




