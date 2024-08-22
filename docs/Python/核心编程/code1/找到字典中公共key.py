from random import randint,sample
d1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
d2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
d3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
pub = d1.keys() & d2.keys() & d3.keys()
print(d1)
print(d2)
print(d3)
print(pub)