# Variables

    a = 'foo'
    a, b = 'foo', 'bob'
    a, b = ['foo', 'bar']

    # globals - declare them outside a function, if constant convention is to use upper case
    # if declared within function then need global keyword
    global new_global
    new_global = 12
  

# Maths functions

    a % 3 # modulo
    sum([1,2,3])
    max([1,2,3])

# Strings

    str(name)
    a + b      # concats
    'ABC'.index('B')  # index of element B in ABC, so = 1
    name.upper()
    name.isUpper()
    name.lower()
    name.isUpper()
    name.startswith('foo')
    name.endswith('foo')
    name.replace('foo', 'bar')
    len(name)
    line.strip()   # removes spaces at the beg and end
    name.isalpha()  # contains only alphabet chars
    line.split(',')
    line.splitlines()  # split on line breaks, same as line.split('\n')
    ','.join(['bob','fred']) # create comma seperated list of items
    eval('6 * 5') # use eval to evaluate a formula in a string
    name.find('bob') # returns index of first match, -1 if no match
    name.rfind('bob') # same ss find but for last match
    name.count('b')  # how many times is 'b' in the name

    txt = "My name is {}, good morning"
    txt.format("Bob")    # My name is Bob, good morning

    txt = "My name is {0} and my age is {1}, good morning {0}"
    txt.format("Bob", 12)    # My name is Bob and my age is 12, good morning Bob

-> [W3 string functions doc](https://www.w3schools.com/python/python_ref_string.asp)

# Numbers

    int(age)
    age.isNumeric()
    age.isdigit()
    float(weight)

    age, weight = 10, 50

    x % y   # x mod y
    2 ** 0  # 2^0
    

# Special characters

    \n  # new line
    \'  # single quote
    \t  # tab

# RegEx

    import re
    
    line = '123'
    re.findall( '\d', line )  # ['1','2','3']

    line = '1\n2'
    re.split('\n', line) # ['1', '2']

    line = 'name: bob, age: 3'
    name, age = re.match(r'name: (\D+), age: (\d+)', a).groups()  # name = 'bob', age = '3' |  \D is a string without digits, \d is just digits

    line = 'bob: jones'
    re.search(r'(\w*)', a).groups()[0]  # 'bob' , could have used match

    re.findall()  # list contaiming all matches
    re.match()    # match object (but only at BEGINNING of the string)
    re.fullmatch() # match object (matches the WHOLE string)
    re.search()   # match object (anywhere in the string)
    re.finditer() # to iterate over matches
    re.split()    # split and return as list
    re.sub()      # RegEx find and replace

    .     # any char except a newline
    ^     # start of string
    $     # end of string
    [A-z] # match a char set
    *     # 0 or more (i.e. optional)
    +     # 1 or more
    {2}   # exactly 2
    \D    # string without digits
    (\d)  # capture group, capturing digits
    \w    # alpha-numerics
    \s    # white space
    \S    # string not containing white space

-> [Python re docs](https://docs.python.org/3/library/re.html)

# is Vs. ==
   
## is

Compares if they are the same object, same memory address (same as id(a) == id(b)). Can also do `is not`

    a = None
    if a is None:
        pass

    b = True
    if b is True:
        pass

## ==    

Compares the values

    a == 100                
    name == 'simon'
    list('a') == list('b')   # true

# Ifs / Loops
 
    if b > a:
        pass
    elif a == b:
        pass
    else:
        pass

    score = 3 if condition else 6

    if 'b' in name:
        pass

    if 'b' not in name:
        psdd

    for line in input:
        pass

    for idx, line in enumerate(input):
        pass

    for line in range(5):  # loops 5 times (0-4)
        pass
    
    sum(x+1 for x in input)

    # every 3rd line starting with the first line (same as for(i=0;i<len(input);i+=3)
    for line in range(0, len(input), 3):  
        pass    

    while i < 5:
        pass

    while True:
        pass

-> [Python if/loops docs](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)

# Lists

    a = [] 
    a = ['foo', 'bar']
    a = list()
    a = list(['foo', 'bar'])
    b = copy(a)  # copies it so changing a won't change b 
    len(a)  # size of list
    a.count()
    a.index('foo')

    a.append('foo')    # insert at the end of the list
    a.insert(0, 'foo') # inserts thie element at the beg of the list
    a.remove('foo')
    a.pop()  # removes the last item, if the element if supplies (e.g. pop(1))
    a.pop(0) # to remove the first item in the last, instead of last
    a.clear()

    a.extend(b)  # adds elements in list b, to list a

    a.sort()
    a.sort(reverse = True)
    a.reverse()

    min(a)
    max(a)
    sum(a)
    all(a)  # true if they are all True, else False (False means a 0 or a False in the list)

    a = [int(i) for i in a]  # convert all items in a list to ints

    # map
    a = list(map(int, a))    # map() way of doing the same
    bob_age, mary_age = map(int, ['5', '10'])
    simon, bob = map(str.strip, ['simon ', 'bob ']) # string strip white space around the objects
    
    list3 = ['a'] + ['b']

    for item in a:
        pass

    for idx, item in enumerate(a):
        pass


## Custom sort

    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key = myfunc)

## List comprehension

    new_list = [x+1 for x in fruits]
    new_list = [x for x in fruits if x != 'apple']

## List slicing

    # IDX 0,1,2,3,4,5,6,7,8,9
    a =  [1,2,3,4,5,6,7,8,9,10]
    # [start:end]
    # its basically: a[i >= start : i<end]
    a[-1]  # last element                 = 10
    a[2:]  # item 2 til the end           = [3,4,5,6,7,8,9,10]
    a[:2]  # first 2 elements             = [1, 2]
    a[-3:] # last 3 elements              = [8,9,10]
    a[:-3] # get all but last 3 elements  = [1,2,3,4,5,6,7]
    a[2:5] # get 2nd element til 4th      = [3,4,5] 

# Sets

Duplicates not allowed, unordered

    a = set()
    b = set()
    x = {'foo', 'bar'}
    x.add('zee')
    x.remove('foo')
    
    a.union(b)  # join 2 sets
    a.intersection(b) # return items in both
    a & b             # more simple set intersection syntax
    a.difference(b)
    a.issubset()

    frozenset(a)  # then cannot be changed, immutable

    len(set(my_list))==1 # checks a list contains items of all the same element

-> [W3 set methods](https://www.w3schools.com/python/python_sets_methods.asp)

# Dicts

Pythons map

    d = { 'name': 'bob', 'age': 2 }
    d['name']
    d.get('name', 'default name') # allows you to specify a default if the key does not exist
    d.keys()
    d.values()
    d['age'] = 3  # used for updating and adding new elements
    d.pop('age') # removes age field
    e = d.copy()
    'name' in d  # true, as this key exists in this dict 

    for key, value in d.items():
        pass

    for key in d.keys():
        pass

    for value in d.values():
        pass

# Tuples

Ordered, unchangeable (so think of them as constants), use () syntax. Dupes allowed. Can hold more than 2 values.
If you need to change them, you would need to convert them in a list

    a = (1,2)
    a[0]   # = 1

    a = (1,)  # one item tuple, comma needed

    a.index(1) # 0

    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits


# Range

  range(<start>, <stop>, <step>)  # <step> is optional

      same as in C:  for( i = <start>; i < <stop>; i+=<step>)  - where <step> defaults to 1

      range(1)     # equivalent list of [0]
      range(3)     # equivalent list of [0,1,2]
      range(0,5)   # equivalent list of [0,1,2,3,4]
      range(0,5,2) # equivalent list of [0,2,4]


# Other collections

    from collections import Counter
    Counter('hello')

    sorted(my_structure) # .sort() only works on lists so need to use this, which also outputs the list sorted 

    zip(['bob','dave'],[10, 15]) # = [('bob',10), ('dave',15)]  like tuples of inputs

    import random
    random.randrange(1,10)   # returns a number between 1 and 9 (so no 10)

    from collections import defaultDict  
    authors = defaultdict(list)   # set to default to empty list
    authors['king'] = ['book1']
    authors['simon']  # key doesn't exist so with defaultdict it would return empty list ([])

    from collections import deque       # for efficient append(), appendleft(), pop() and popleft()
    from collections import OrderedDict
    from collections import UserString

# Classes

    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def years_til_eighteen(self):
            return 18-self.age

    bob = Person('bob',2)
