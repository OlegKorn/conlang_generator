import random


VOWS = ['a', 'e', 'y', 'u', 'i', 'o']
CONS = ['q','z','w','s','kh','d','c','r',
   'f','v','t','g','b','h','n','j',
   'm','k','l','p','ʧ','θ','ð','z','ň' 
]

#to increase the depth of choice there are more than 2 same entities here
TYPES = ['v','c','v','c','v','c','v','c','v','c','v','c','v','c']
res = []

#

def set_random_len():
    l_min = random.choice(range(2))
    l_max = random.choice(range(2,5))

    m_len = ((l_max - l_min) + 1) 
    return m_len


def generate_morph():
    m_len = set_random_len()
    graphem_type = random.choice(TYPES)
    print(graphem_type) 
    for i in range(m_len):
        print(f'i is {i}; m_len is {m_len}')
    



generate_morph()
