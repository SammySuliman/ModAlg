from group import AdditiveIdentity
from group import AdditiveInverse
from group import Group
from abelianGroup import AbelianGroup
import myfunctions
from ring import MultiplicativeIdentity
from ring import Ring

def test_Ring1():
    a = Ring()
    a.addObject(2)
    a.addObject(3)
    a.multiply(2,3)
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', '2', 'Additive inverse of 2', '3', 'Additive inverse of 3', '[(2, 3), (3, 2)]', 'Additive inverse of [(2, 3), (3, 2)]']"
    a.multiply([(2,3),(3,2)], 3)
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', '2', 'Additive inverse of 2', '3', 'Additive inverse of 3', '[(2, 3), (3, 2)]', 'Additive inverse of [(2, 3), (3, 2)]', '[(2, 3, 3), (3, 3, 2)]', 'Additive inverse of [(2, 3, 3), (3, 3, 2)]']"
    
def test_Ring2():
    ''' testing non-commutativity of multiplication '''
    a = Ring()
    b = Ring()
    a.addObject(2)
    a.addObject(3)
    b.addObject(2)
    b.addObject(3)
    a.multiply(2,3)
    b.multiply(3,2)
    assert a.group[7] != b.group[7]

def test_Ring3():
    ''' testing associativity of multiplication '''
    a = Ring()
    b = Ring()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    b.addObject(2)
    b.addObject(3)
    b.addObject(5)
    a.multiply(2,3)
    b.multiply(3,5)
    a.multiply([(2,3),(3,2)], 5)
    b.multiply(2, [(3,5),(5,3)])
    assert a.group[11] == b.group[11]

def test_Ring4():
    ''' testing def of multiplicative and additive inverses '''
    a = Ring()
    a.addObject('apple')
    a.multiply('apple', MultiplicativeIdentity())
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', 'apple', 'Additive inverse of apple']"
    a.multiply('apple', AdditiveIdentity())
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', 'apple', 'Additive inverse of apple']"
    a.multiply('apple', AdditiveInverse('apple'))
    assert a.__str__() == """Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', 'apple', 'Additive inverse of apple', [('apple', 'Additive inverse of apple'), ('Additive inverse of apple', 'apple')], "Additive inverse of [('apple', 'Additive inverse of apple'), ('Additive inverse of apple', 'apple')]"]"""

def test_Ring5():
    a = Ring()
    a.addObject(2)
    a.addObject(3)
    a.multiply(2,3)
    a.multiply([(2,3),(3,2)], 3)
    a.multiply([(2,3),(3,2)], [(2, 3, 3), (3, 3, 2)])
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', '2', 'Additive inverse of 2', '3', 'Additive inverse of 3', '[(2, 3), (3, 2)]', 'Additive inverse of [(2, 3), (3, 2)]', '[(2, 3, 3), (3, 3, 2)]', 'Additive inverse of [(2, 3, 3), (3, 3, 2)]', '[(2, 3, 2, 3, 3), (3, 3, 2, 3, 2)]', 'Additive inverse of [(2, 3, 2, 3, 3), (3, 3, 2, 3, 2)]']"

def test_Ring6():
    ''' testing distributive property '''
    a = Ring()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    a.add(2,3)
    a.multiply({2,3},5)
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', '2', 'Additive inverse of 2', '3', 'Additive inverse of 3', '5', 'Additive inverse of 5', '{2, 3}', 'Additive inverse of {2, 3}', '[(2, 5), (5, 2)]', 'Additive inverse of [(2, 5), (5, 2)]', '[(3, 5), (5, 3)]', 'Additive inverse of [(3, 5), (5, 3)]', '{((2, 5), (5, 2)), ((3, 5), (5, 3))}', 'Additive inverse of {((2, 5), (5, 2)), ((3, 5), (5, 3))}']"

def test_Ring7():
    ''' testing distributive property '''
    a = Ring()
    a.addObject(2)
    a.addObject(3)
    a.addObject(5)
    a.add(2,3)
    a.add(3,5)
    a.multiply({2,3},{5,3})
    assert a.__str__() == "Ring: ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity', '2', 'Additive inverse of 2', '3', 'Additive inverse of 3', '5', 'Additive inverse of 5', '{2, 3}', 'Additive inverse of {2, 3}', '{3, 5}', 'Additive inverse of {3, 5}', '[(2, 3), (3, 2)]', 'Additive inverse of [(2, 3), (3, 2)]', '[(2, 5), (5, 2)]', 'Additive inverse of [(2, 5), (5, 2)]', '{((2, 3), (3, 2)), ((2, 5), (5, 2))}', 'Additive inverse of {((2, 3), (3, 2)), ((2, 5), (5, 2))}', '[(3, 3), (3, 3)]', 'Additive inverse of [(3, 3), (3, 3)]', '[(3, 5), (5, 3)]', 'Additive inverse of [(3, 5), (5, 3)]', '{((2, 3), (3, 2)), ((2, 5), (5, 2)), ((3, 3), (3, 3)), ((3, 5), (5, 3))}', 'Additive inverse of {((2, 3), (3, 2)), ((2, 5), (5, 2)), ((3, 3), (3, 3)), ((3, 5), (5, 3))}', '{((2, 3), (3, 2)), ((2, 5), (5, 2)), ((3, 3), (3, 3)), ((3, 5), (5, 3))}', 'Additive inverse of {((2, 3), (3, 2)), ((2, 5), (5, 2)), ((3, 3), (3, 3)), ((3, 5), (5, 3))}']"
    
test_Ring1()
test_Ring2()
test_Ring3()
test_Ring4()
test_Ring5()
test_Ring6()
test_Ring7()
