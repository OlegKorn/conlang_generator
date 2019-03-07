#-*- coding: utf-8 -*-   #letter = random.choice(string.ascii_lowercase)
import random
import string    


VOWS = ['aeyuio']
CONS = ['qzwsxdcrfvtgbhnjmklp']
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
        self.counter = len(graphems_set)
  

    def show_info(self):
        print('graphems_set is {}\n'
          'len(graphems_set) is {}' 
          .format(self.graphems_set, self.counter)            
        )        
  

    '''def generate(self):
        for i in graphems_set:
'''



m = Morphem('vvc')
m1 = Morphem('vvcvc')
m.show_info()
m1.show_info()







