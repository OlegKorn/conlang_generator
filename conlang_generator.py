
#-*- coding: utf-8 -*- 
import random
import string 
from conlang_data import *   


'''
 A VERY SIMPLE conlang ver. 1.2
'''

prefixes = []
roots = []
suffixes = []

nouns = []
verb_morphemes = []
infinitives = []
adjectives = []

sentences = []

class Amount:
    def __init__(self, amount:int):
        self.amount = amount + 1
        

class Prefix:
    def __init__(self):
        self.amount = a.amount

    def generate_pref(self):
        '''
        This method generates prefixes
        '''
        #pref_amount = self.amount 
        self.pref = ''
 
        #generate a prefix according to the scheme set in data.PREF_TYPES
        while self.amount != 0:
            _type = random.choice(PREF_TYPES)
            for i in _type:
                
                if i == 'c':
                    self.pref += random.choice(PCONS)
                
                if i == 'v':
                    self.pref += random.choice(PVOWS)
            
            prefixes.append(self.pref)
                    
            #null the generated pref after appending it to the [self.prefs] 
            self.pref = ''
                        
            random.shuffle(PCONS)
            random.shuffle(PVOWS)
            self.amount -= 1


class Root:
    '''
    Generates a stem by contacenating: ([prefix]+root+[suffix])
    '''
    def __init__(self):
        self.amount = a.amount

    def generate_root(self): 
        '''
        This method generates roots
        '''
        self.root = ''

        #generate a root according to the scheme set in conlang_data.ROOT_TYPES
        while self.amount != 0:
            _type = random.choice(ROOT_TYPES)
            for i in _type:
                if i == 'c': 
                    self.root += random.choice(RVOWS)
                if i == 'v':
                    self.root += random.choice(RCONS)
            roots.append(self.root)
                
            #null the generated root after appending it to the [self.roots] 
            self.root = ''

            self.amount -= 1

            random.shuffle(ROOT_TYPES)
            random.shuffle(RVOWS)
            random.shuffle(RCONS)


class Suffix:

    def __init__(self):
        self.amount = a.amount

    def generate_suff(self):
        '''
        This method generates roots
        '''
        self.suff = ''

        #generate a root according to the scheme set in ROOT_TYPES
        while self.amount != 0:
        
            _type = random.choice(SUFF_TYPES)
            
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



class Noun: 

    def contacenate_noun(self):

        self.noun = ''

        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            self.noun += x
            self.noun += y
            self.noun += z

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            
            nouns.append(self.noun) 
            self.noun = ''

        nouns.insert(0, 'NOUNS: ')
        #print(nouns)



class Verb:

    def create_infinitive(self):

        self.inf = ''
        
        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            self.inf += x
            self.inf += y
            self.inf += z
            self.inf += INF_MARKER

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            
            infinitives.append(self.inf) 
            self.inf = ''


    def create_verb_morpheme(self):

        self.v_morpheme = ''
        
        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            self.v_morpheme += x
            self.v_morpheme += y
            self.v_morpheme += z

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            
            verb_morphemes.append(self.v_morpheme) 
            self.v_morpheme = ''





class Adjective:

    def contacenate_adjective(self):

        self.adjective = ''

        for x,y,z in zip(prefixes[1:], roots[1:], suffixes[1:]):
            ending = random.choice(ADJ_ENDINGS)
            self.adjective += x
            self.adjective += y
            self.adjective += z
            self.adjective += ending

            random.shuffle(prefixes)
            random.shuffle(roots)
            random.shuffle(suffixes)
            random.shuffle(ADJ_ENDINGS)
            
            adjectives.append(self.adjective) 
            self.adjective = ''
        
        adjectives.insert(0, 'ADJECTIVES: ')



class Sentence:
    def __init__(self):
        self.amount = a.amount
        self.sent = ''

    #nouns = []
    #verb_morphemes = []
    #infinitives = []
    #adjectives = []
    
    SENT_TYPES = ['declarative', 'question', 'exclamation', 'negative']

    #set schemes of generating of sentences
    def declarative(self): # pronoun + verb conjugated + verb infinitive comma
        self.d_num = self.amount

        sentences.append('DECLARATIVE: ')

        while self.d_num != 0:

            self.pronoun, self.v_conj_ending = random.choice(list(PRON_CONJ.items()))
            self.verb_conjugated = str(random.choice(verb_morphemes)) + self.v_conj_ending.replace('-', '')
            self.verb_infinitive = str(random.choice(infinitives))

            self.sent = self.pronoun + ' ' + self.verb_conjugated + ' ' +  self.verb_infinitive + '.'

            sentences.append(self.sent)

            self.sent = '' 

            self.d_num -= 1



    def question(self):  # verb conjugated + pronoun + a + verb infinitive + ?
        self.q_num = self.amount

        sentences.append('QUESTION: ')

        while self.q_num != 0:

            self.pronoun, self.v_conj_ending = random.choice(list(PRON_CONJ.items()))
            self.verb_conjugated = str(random.choice(verb_morphemes)) + self.v_conj_ending.replace('-', '')
            self.verb_infinitive = str(random.choice(infinitives))

            self.sent = self.verb_conjugated + ' ' + self.pronoun + ' a ' + self.verb_infinitive + '?'

            sentences.append(self.sent)

            self.sent = '' 

            self.q_num -= 1


   
    def exclamation(self):  # pronoun + verb conjugated + verb infinitivew + !
        self.e_num = self.amount

        sentences.append('EXCLAMATION: ')

        while self.e_num != 0:

            self.pronoun, self.v_conj_ending = random.choice(list(PRON_CONJ.items()))
            self.verb_conjugated = str(random.choice(verb_morphemes)) + self.v_conj_ending.replace('-', '')
            self.verb_infinitive = str(random.choice(infinitives))

            self.sent = self.pronoun  + ' ' + self.verb_conjugated + ' ' + self.verb_infinitive + '!'

            sentences.append(self.sent)

            self.sent = '' 

            self.e_num -= 1


    
    def negative(self):  # pronoun + non + verb conjugated + a + verb infinitive
        self.n_num = self.amount
        
        sentences.append('NEGATIVE: ')

        while self.n_num != 0:

            self.pronoun, self.v_conj_ending = random.choice(list(PRON_CONJ.items()))
            self.verb_conjugated = str(random.choice(verb_morphemes)) + self.v_conj_ending.replace('-', '')
            self.verb_infinitive = str(random.choice(infinitives))

            self.sent = self.pronoun  + NEG + self.verb_conjugated + ' a ' + self.verb_infinitive + '.'

            sentences.append(self.sent)

            self.sent = '' 

            self.n_num -= 1

        print(sentences)








#for key, value in PRONOUNS.items():
#    print(key, value)

a = Amount(5)  #задаем количество сущностей для генерации


p = Prefix()
p.generate_pref()

r = Root()
r.generate_root()

s = Suffix()
s.generate_suff()

n = Noun()
n.contacenate_noun()

v = Verb()
v.create_infinitive()
v.create_verb_morpheme()


ad = Adjective()
ad.contacenate_adjective()


se = Sentence()
se.declarative()
se.question()
se.exclamation()
se.negative()


#['DECLARATIVE: ', 'loro eisanno oreisen.', 'tu orrmærruæpi orrmærruæssen.', 'voi ovakakete akakæpen.', 'io eiso ovamen.', 
#'il orrmærruæpa oreisen.', 'lei orfærrrria akakæpen.', 'QUESTION: ', 'eisi tu a færrrrien?', 'ovakaka Lei a orrmærruæssen?', 
#'amo io a akakæpen?', 'orfærrrrio io a oreisen?', 'eisanno loro a akakæpen?', 'orrmærruæpo io a orrmærruæssen?', 
#'EXCLAMATION: ', 'noi amamo færrrrien!', 'tu orfærrrrii oreisen!', 'io orrmærruæpo orrmærruæssen!', 'io eiso ovamen!', 
#'io ovakako akakæpen!', 'tu orrmærruæpi orrmærruæssen!', 'NEGATIVE: ', 'voi nun orfærrrriete a oreisen.', 
#'voi nun orrmærruæpete a færrrrien.', 'noi nun orfærrrriamo a oreisen.', 'Lei nun orfærrrria a orrmærruæssen.', 
#'voi nun eisete a akakæpen.', 'voi nun orrmærruæpete a orrmærruæssen.']
