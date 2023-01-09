from group import AdditiveIdentity
from group import AdditiveInverse
from group import Group
from abelianGroup import AbelianGroup
import myfunctions
from ring import MultiplicativeIdentity
from ring import Ring

class CommutativeRing(Ring):
    def multiply(self, obj1, obj2):
        booler = False
        if (obj1 in self.group or type(obj1) == MultiplicativeIdentity or type(obj1) == AdditiveIdentity or type(obj1) == AdditiveInverse) and (obj2 in self.group or type(obj2) == MultiplicativeIdentity or type(obj2) == AdditiveIdentity or type(obj2) == AdditiveInverse):
            if (type(obj1) == MultiplicativeIdentity) or (type(obj1) == AdditiveIdentity):
                booler = True
            if (type(obj2) == MultiplicativeIdentity) or (type(obj2) == AdditiveIdentity):
                booler = True
            if type(obj1) == AdditiveInverse:
                if obj1.original not in self.group:
                    print('Objects must be members of ring to multiply')
                    booler = True
            if type(obj2) == AdditiveInverse:
                if obj2.original not in self.group:
                    print('Objects must be members of ring to multiply')
                    booler = True
            if ((type(obj1) == list) or (type(obj1) == set)) and booler == False:
                if myfunctions.is_nested_list(obj1) == True:
                    obj1 = myfunctions.flatten(myfunctions.insert(list(obj1)))
                    list1 = []
                    for i in obj1:
                        if i != '@%$7h^%':
                            list1.append(i)
                        else:
                            break
                    obj1 = list1
                elif (type(obj1) == set):
                    for i in obj1:
                        self.multiply(i, obj2)
                    set1 = set()
                    for elt in self.group:
                        if type(elt) == list:
                            if myfunctions.is_nested_list(elt) == True:
                                set1.add(tuple(elt))
                    self.group.append(set1)
                    self.group.append(AdditiveInverse(set1))
                    booler = True
            if ((type(obj2) == list) or (type(obj2) == set)) and booler == False:
                if myfunctions.is_nested_list(obj2) == True:
                    obj2 = myfunctions.flatten(myfunctions.insert(list(obj2)))
                    list2 = []
                    for i in obj2:
                        if i != '@%$7h^%':
                            list2.append(i)
                        else:
                            break
                    obj2 = list2
                elif (type(obj2) == set):
                    for j in obj2:
                        self.multiply(obj1, j)
                    set2 = set()
                    for elt in self.group:
                        if type(elt) == list:
                            if myfunctions.is_nested_list(elt) == True:
                                set2.add(tuple(elt))
                    self.group.append(set2)
                    self.group.append(AdditiveInverse(set2))
                    booler = True
            list3 = []
            if ((type(obj1) == list) or (type(obj1) == set)) and booler == False:
                for i in obj1:
                    list3.append(i)
                if (type(obj2) == list) or (type(obj2) == set):
                    for j in obj2:
                        list3.append(j)
                else:
                    list3.append(obj2)
            elif ((type(obj1) != list) or (type(obj1) != set)) and booler == False:
                list3.append(obj1)
                if (type(obj2) == list) or (type(obj2) == set):
                    for k in obj2:
                        list3.append(k)
                else:
                    list3.append(obj2)
            if booler == False:
                tuple1 = tuple(list3)
                reversed1 = tuple1[::-1]
                self.group.append({tuple1, reversed1})
                self.group.append(AdditiveInverse([tuple1, reversed1]))
        else:
            print('Objects must be members of ring to multiply')


