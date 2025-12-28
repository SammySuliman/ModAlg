class AdditiveIdentity:
    def __init__(self):
        self.identity = 0
    def __str__(self):
        return 'Additive identity'
    
class AdditiveInverse:
    def __init__(self, obj):
        self.original = obj
    def __str__(self):
        return 'Additive inverse of {}'.format(self.original)
    
class Group:
    def __init__(self):
        self.group = [AdditiveIdentity()]
    def getGroup(self):
        return self.group
    def addObject(self, obj):
        if obj not in self.group:
            self.group.append(obj)
            self.group.append(AdditiveInverse(obj))
        else:
            print('Object already contained within')
    def removeObject(self, obj):
        if (obj in self.group) and (obj.__class__ != AdditiveIdentity):
            self.group.remove(self.group[self.group.index(obj)+1])
            self.group.remove(obj)
        elif type(obj) == AdditiveIdentity:
            print('You cannot remove the additive identity from a group')
        elif type(obj) == AdditiveInverse:
            self.group.remove(self.group[self.group.index(obj)-1])
            self.group.remove(obj)
        elif obj not in self.group:
            print('Objects must be members to remove')
    def __str__(self):
        rtn_list = []
        rtn_list2 = []
        for obj in self.group:
            if type(obj) == list:
                for elt in obj:
                    if (type(elt) == AdditiveIdentity) or (type(elt) == AdditiveInverse):
                        rtn_list2.append(elt.__str__())
                    else:
                        rtn_list2.append(elt)
                rtn_list.append(rtn_list2)
                rtn_list2 = []
            else:
                if (type(obj) == AdditiveIdentity) or (type(obj) == AdditiveInverse):
                    rtn_list.append(obj.__str__())
                else:
                    rtn_list.append(obj)
        return 'Group: {}'.format(rtn_list)
    def __eq__(self, obj):
        for (i, val) in enumerate(self.group):
            if len(self.group) == len(obj.group):
                if (type(val) != AdditiveIdentity) and (type(val) != AdditiveInverse):
                    if val != obj.group[i]:
                        return False
                elif type(val) == AdditiveIdentity:
                    if type(obj.group[i]) != AdditiveIdentity:
                        return False
                elif type(val) == AdditiveInverse:
                    if type(obj.group[i]) != AdditiveInverse:
                        return False
                    elif val.original != obj.group[i].original:
                        return False
            else:
                return False
        return True
    def add(self, obj1, obj2):
        booler = False
        if ((obj1 in self.group) or (type(obj1) == AdditiveIdentity) or (type(obj1) == AdditiveInverse)) and ((obj2 in self.group) or (type(obj2) == AdditiveIdentity) or (type(obj2) == AdditiveInverse)):
            if type(obj1) == AdditiveIdentity:
                booler = True
            elif type(obj2) == AdditiveIdentity:
                booler = True
            if type(obj1) == AdditiveInverse:
                if obj2 == obj1.original:
                    booler = True
            elif type(obj2) == AdditiveInverse:
                if obj1 == obj2.original:
                    booler = True
            if ((type(obj1) == list) or (type(obj2) == list)) and booler == False:
                new_list = []
                for x in [obj1, obj2]:
                    if type(x) is list:
                        for y in x:
                            new_list.append(y)
                    else:
                        new_list.append(x)
                self.group.append(new_list)
                self.group.append(AdditiveInverse(new_list))
            else:
                if booler == False:
                    self.group.append([obj1, obj2])
                    self.group.append(AdditiveInverse([obj1, obj2]))
        else:
            print('Objects must be members of a group to add')
