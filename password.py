import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
         ,'p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
n_letters=int(input("how many letters you want in your password\n"))
n_numbers=int(input("how many numbers you want in your password\n"))
n_symbols=int(input("how many symbols you want in your password\n"))

length = int(input("enter the length of password:"))

password= []
for i in range(1,n_letters+1):
        char= random.choice(letters)
        password += char
for i in range(1,n_numbers+1):
        char = random.choice(numbers)
        password +=char
for i in range(n_symbols+1):
            char = random.choice(symbols)
            password +=char
            

user = int(n_letters+n_numbers+n_symbols)
minus= length - user
random.shuffle(password)
if user < length:
        all_char = letters+numbers+symbols
        password.extend(random.sample(all_char,minus))    
else:
     password[ :minus]
     
print(f"your generated password is: {password}")