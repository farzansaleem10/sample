c=2024
y=int(input("enter the future year :"))

for i in range (c,y):
    
        if (i%4==0 and i%100!=0) or i%400==0:
            print(i)
            i=+1
       
