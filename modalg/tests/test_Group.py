from group import AdditiveIdentity
from group import AdditiveInverse
from group import Group

def test_Group1():
    ''' testing equality operator '''
    a = Group()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    b = Group()
    b.addObject(2)
    b.addObject(3)
    assert ((a==b) == False)
    b.addObject(5)
    assert (a==b)

def test_Group2():
    ''' testing print operator '''
    a = Group()
    a.addObject(2)
    a.addObject(3)
    a.add(2, 3)
    assert a.__str__() == "Group: ['Additive identity', 2, 'Additive inverse of 2', 3, 'Additive inverse of 3', [2, 3], 'Additive inverse of [2, 3]']"
    a.removeObject(2)
    assert a.__str__() == "Group: ['Additive identity', 3, 'Additive inverse of 3', [2, 3], 'Additive inverse of [2, 3]']"

def test_Group3():
    ''' testing associativity of addition '''
    a = Group()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    b = Group()
    b.addObject(2)
    b.addObject(3)
    b.addObject(5)
    a.add(2,3)
    b.add(3,5)
    a.add([2,3], 5)
    b.add(2, [3,5])
    assert (a.group[9] == b.group[9])
    

test_Group1()
test_Group2()
test_Group3()

