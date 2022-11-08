a=0b1
b=int(input("Въведете число"))
p=int(input("Въведете позиция за проверка"))
a=a<<p
check=a&b
if(check != 0):
        print("Числото  " + str(b)+" има единица в " )  
else:
        print("Числото " +str(b)+" няма единица")
