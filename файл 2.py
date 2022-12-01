array = ['4', 1.5, "@7$", 3.5, (1,"hi")]

def list_avg(lst, multiplier = 1):
    for i in range(len(lst)):
        if isinstance(lst[i], str) and lst[i].isnumeric():
            lst[i] = float(lst[i])
        elif type(list[i]) != int and type(lst[i]) != float:
            lst[i] = None
        
    if len(lst) == 0:
        print('Error zero division')
        return

    lst = filter(lambda x: x != None, lst)
    lst = list(map(lambda x: x * multiplier, lst))

    print(sum(lst) / len(lst))
        
list_avg(array)
