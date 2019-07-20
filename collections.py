from collections import *

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(lst))

print(Counter('aabsbsbsbhshhbbsbs'))

d  = defaultdict(object)
d['one']
d['two']

for item in d:
    print(item)


print('OrderedDict:')


d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'


for k, v in d.items():
    print(k, v)

Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")
print(sam)