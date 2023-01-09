from group import AdditiveIdentity
from group import AdditiveInverse
from group import Group

class AbelianGroup(Group):
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
        return 'Abelian Group: {}'.format(rtn_list)
    def add(self, obj1, obj2):
        booler = False
        if ((obj1 in self.group) or (type(obj1) == AdditiveIdentity) or (type(obj1) == AdditiveInverse)) and ((obj2 in self.group) or (type(obj2) == AdditiveIdentity) or (type(obj2) == AdditiveInverse)):
            if (type(obj1) == AdditiveIdentity) or (type(obj2) == AdditiveIdentity):
                booler = True
            if type(obj1) == AdditiveInverse:
                if obj2 == obj1.original:
                    booler = True
            elif type(obj2) == AdditiveInverse:
                if obj1 == obj2.original:
                    booler = True
            if (type(obj1) == set) or (type(obj2) == set):
                new_set = set()
                if type(obj1) == set:
                    for j in obj1:
                        new_set.add(j)
                else:
                    new_set.add(obj1)
                if type(obj2) == set:
                    for k in obj2:
                        new_set.add(k)
                else:
                    new_set.add(obj2)
                self.group.append(new_set)
                self.group.append(AdditiveInverse(new_set))
            else:
                self.group.append({obj1, obj2})
                self.group.append(AdditiveInverse({obj1, obj2}))
        else:
            print('Objects must be members of a group to add')


