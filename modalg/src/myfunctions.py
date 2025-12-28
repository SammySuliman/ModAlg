def flatten(obj):
    return eval('[' + str(obj).replace('[', '').replace(']', '').replace('(','').replace(')','') + ']')

def flatten2(obj): # Rings, Commutative rings
    new_lst = ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity']
    it = iter(obj.group[3:])
    booler2 = False
    for elt in it:
        try:
            if ('AdditiveInverse' in str(elt)) or ('MultiplicativeInverse' in str(elt)):
                new_lst.append([(str(elt[0][0]), str(elt[0][1])), (str(elt[0][1]), str(elt[0][0]))])
                new_lst.append('Additive inverse of {}'.format([(str(elt[0][0]), str(elt[0][1])), (str(elt[0][1]), str(elt[0][0]))]))
                next(it)
            else:
                new_lst.append(str(elt))
        except:
            if type(elt) == set:
                for tup in list(elt):
                    set2 = set()
                    for k in tup:
                        set2.add(str(k))
            if booler2 == False:
                tuple1 = tuple(set2)
                reversed1 = tuple1[::-1]
                new_lst.append({tuple1, reversed1})
                new_lst.append('Additive inverse of {}'.format({tuple1, reversed1}))
                booler2 = True
    return new_lst

def flatten3(obj): # Fields
    new_lst = ['Additive identity', 'Multiplicative identity', 'Additive inverse of Multiplicative identity']
    it = iter(obj.group[3:])
    booler2 = False
    for elt in it:
        try:
            if ('AdditiveInverse' in str(elt)) or ('MultiplicativeInverse' in str(elt)):
                new_lst.append([(str(elt[0][0]), str(elt[0][1])), (str(elt[0][1]), str(elt[0][0]))])
                new_lst.append('Additive inverse of {}'.format([(str(elt[0][0]), str(elt[0][1])), (str(elt[0][1]), str(elt[0][0]))]))
                next(it)
            else:
                new_lst.append(str(elt))
        except:
            if type(elt) == set:
                for tup in list(elt):
                    set2 = set()
                    for k in tup:
                        set2.add(str(k))
            if booler2 == False:
                tuple1 = tuple(set2)
                reversed1 = tuple1[::-1]
                new_lst.append({tuple1, reversed1})
                new_lst.append('Additive inverse of {}'.format({tuple1, reversed1}))
                booler2 = True
                new_lst.append('Multiplicative inverse of {}'.format({tuple1, reversed1}))
    return new_lst

def insert(nested_list):
    nested_list.insert(1, '@%$7h^%')
    return nested_list

def is_nested_list(obj1):
    booler = False
    if (type(obj1) == list) or (type(obj1) == set):
        for i in obj1:
            if (type(i) == list) or (type(i) == tuple):
                booler = True
    return booler
