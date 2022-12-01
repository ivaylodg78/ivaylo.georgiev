n = int(input())
dictionary = {}
array = []

for i in range(n):
    key = input()
    value = input()
    dictionary[key] = value

m = int(input())

for i in range(m):
    num = input()

    if num in dictionary.keys():
        array.append(dictionary[num])
        del dictionary[num]
    else:
        array.append(num)

print(dictionary)
print(array)

