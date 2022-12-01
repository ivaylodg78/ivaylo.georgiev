n = input()

if "." not in n and n.isnumeric():
    n = int(n)

def input_nums(n):
    if not isinstance(n, int):
        return [] 

    els = []
    for _ in range(n):
        el = input("Enter a list element: ")
        if el.isnumeric():
            els.append(int(el))
           
    return els

def sum_list(els):
    sum = 0
    for el in els:
        if isinstance(el, float) or isinstance(el, int):
            sum  += el
        elif isinstance(el, str) and el.isnumeric():
            sum += float(el)

    return sum




def max_of_two(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a >= b:
            return a
        
        return b
    elif isinstance(a, (int, float)) and not isinstance(b, (int, float)):
        return a 
    elif not isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return b
    else:
        return











