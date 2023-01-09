from group import AdditiveIdentity
from group import AdditiveInverse
from group import Group
from abelianGroup import AbelianGroup

def test_AbelianGroup1():
    a = AbelianGroup()
    b = AbelianGroup()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    b.addObject(2)
    b.addObject(3)
    b.addObject(5)
    a.add(2,3)
    b.add(3,2)
    assert a.group[7] == b.group[7]

def test_AbelianGroup2():
    a = AbelianGroup()
    b = AbelianGroup()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    b.addObject(2)
    b.addObject(3)
    b.addObject(5)
    a.add(2,3)
    b.add(3,5)
    a.add({2,3}, 5)
    b.add(2, {3,5})
    assert (a.group[9] == b.group[9])

test_AbelianGroup1()
test_AbelianGroup2()
