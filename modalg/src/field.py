class MultiplicativeInverse:
    def __init__(self, obj):
        if type(obj) == AdditiveIdentity:
            raise ZeroDivisionError()
        try:
            self.original = obj
        except ZeroDivisionError:
            print('Cannot take multiplicative inverse of additive identity')
    def __str__(self):
        return 'Multiplicative inverse of {}'.format(self.original)
    
class Field(CommutativeRing):
    def addObject(self, obj):
        if obj not in self.group:
            self.group.append(obj)
            self.group.append(AdditiveInverse(obj))
            self.group.append(MultiplicativeInverse(obj))
        else:
            print('Object already contained within')
    def removeObject(self, obj):
        if (obj in self.group) and (type(obj) != AdditiveIdentity) and (type(obj) != AdditiveInverse) and (type(obj) != MultiplicativeIdentity) and (type(obj) != MultiplicativeInverse):
            self.group.remove(self.group[self.group.index(obj)+2])
            self.group.remove(self.group[self.group.index(obj)+1])
            self.group.remove(obj)
        elif type(obj) == AdditiveIdentity:
            print('You cannot remove the additive identity from a group')
        elif type(obj) == AdditiveInverse:
            self.group.remove(self.group[self.group.index(obj)+1])
            self.group.remove(self.group[self.group.index(obj)-1])
            self.group.remove(obj)
        elif type(obj) == MultiplicativeIdentity:
            print('You cannot remove the multiplicative identity from a group')
        elif type(obj) == MultiplicativeInverse:
            self.group.remove(self.group[self.group.index(obj)-2])
            self.group.remove(self.group[self.group.index(obj)-1])
            self.group.remove(obj)
        elif obj not in self.group:
            print('Objects must be members to remove')
    def __str__(self):
        return 'Field: {}'.format(myfunctions.flatten3(self))
    def multiply(self, obj1, obj2):
        booler = False
        if (obj1 in self.group or type(obj1) == MultiplicativeIdentity or type(obj1) == AdditiveIdentity or type(obj1) == AdditiveInverse or type(obj1) == MultiplicativeInverse) and (obj2 in self.group or type(obj2) == MultiplicativeIdentity or type(obj2) == AdditiveIdentity or type(obj2) == AdditiveInverse or type(obj2) == MultiplicativeInverse):
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
            if type(obj1) == MultiplicativeInverse:
                if obj1.original not in self.group:
                    print('Objects must be members of ring to multiply')
                    booler = True
                elif obj1.original == obj2:
                    booler = True
            if type(obj2) == MultiplicativeInverse:
                if obj2.original not in self.group:
                    print('Objects must be members of ring to multiply')
                    booler = True
                elif obj2.original == obj1:
                    booler = True
            if ((type(obj1) == list) or (type(obj1) == set)) and booler == False:
                if is_nested_list(obj1) == True:
                    obj1 = flatten(insert(list(obj1)))
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
                            if is_nested_list(elt) == True:
                                set1.add(tuple(elt))
                    self.group.append(set1)
                    self.group.append(AdditiveInverse(set1))
                    self.group.append(MultiplicativeInverse(set1))
                    booler = True
            if ((type(obj2) == list) or (type(obj2) == set)) and booler == False:
                if is_nested_list(obj2) == True:
                    obj2 = flatten(insert(list(obj2)))
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
                            if is_nested_list(elt) == True:
                                set2.add(tuple(elt))
                    self.group.append(set2)
                    self.group.append(AdditiveInverse(set2))
                    self.group.append(MultiplicativeInverse(set2))
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
                self.group.append(AdditiveInverse({tuple1, reversed1}))
                self.group.append(MultiplicativeInverse({tuple1, reversed1}))
        else:
            print('Objects must be members of ring to multiply')
