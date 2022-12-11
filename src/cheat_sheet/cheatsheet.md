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
    'ABC'.index('B')  # index of element B in ABC, so = 1
    name.upper()
    name.isUpper()
    name.lower()
    name.isUpper()
    name.startswith('foo')
    name.replace('foo', 'bar')
    len(name)
    line.strip()   # removes spaces at the beg and end
    name.isalpha()  # contains only alphabet chars
    line.split(',')
    line.splitlines()  # split on line breaks
    ','.join(['bob','fred']) # create comma seperated list of items
    eval('6 * 5') # use eval to evaluate a formula in a string

[W3 string functions doc](https://www.w3schools.com/python/python_ref_string.asp)

# Numbers

    int(age)
    age.isNumeric()
    float(weight)

    age, weight = 10, 50

# RegEx


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

[Python if/loops docs](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)

# Lists

    a = [] 
    a = ['foo', 'bar']
    a = list()
    a = list(['foo', 'bar'])
    a.count()
    a.index('foo')

    a.append('foo')
    a.remove('foo')
    a.pop()  # removes the last item, if the element if supplies (e.g. pop(1))
    a.pop(0) # to remove the first item in the last, instead of last
    a.clear()

    a.sort()
    a.sort(reverse = True)
    a.reverse()

    list3 = ['a'] + ['b']

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

[W3 set methods](https://www.w3schools.com/python/python_sets_methods.asp)

# Dicts

Pythons map

    d = { 'name': 'bob', 'age': 2 }
    d['name']
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




# Other collections

    from collections import Counter
    Counter('hello')

    sorted(my_structure) # .sort() only works on lists so need to use this, which also outputs the list sorted 

    zip(['bob','dave'],[10, 15]) # = [('bob',10), ('dave',15)]  like tuples of inputs

# Classes

    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def years_til_eighteen(self):
            return 18-self.age

    bob = Person('bob',2)
