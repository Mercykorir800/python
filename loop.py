#for loop
for i in range (1,11):
    print(f"Welcome to my shop! Customer {i}")
mycustomer=("Mercy","Erick", "Elvis", "Christine", "Bella")

for n in mycustomer:
    print (f"Welcome to my School {n}")
#suppose you buy
#bread ksh130
#milk ksh100
#sugar ksh200
#blueband ksh120
#calculate the total expense

myshopping=[130,100,2000,120]
total=0

for s in myshopping:
    total=total+ s
    print(f"your total expense is {total}")

#while loop
num=0
while num <=8:
    print(f" loops :{num}")
    num+=2
#imagine you start with 0 and
#save 1000 every day until you save 500

money=0
while money<500:
    money=money+100
    print(f"money saved {money}")
print("Congratulations! you reached your target")   

