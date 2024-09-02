price = int(input('Price: ')) 
print("Enter 3 Denomination")
deno1 = int(input('Denomination 1: '))
deno2 = int(input('Denomination 2: '))
deno3 = int(input('Denomination 3: ')) 
if price>0 :
        c=0
        for d1 in range(0, 1 + price // deno1): 
            for d2 in range(0, 1 + price // deno2): 
                for d3 in range(0, 1 + price // deno3): 
                 if d1 * deno1 + d2 * deno2 + d3 * deno3 == price: 
                        print(d1, d2, d3)
                        c+=1
        
        if c==0:
             print("No combination found.")  
        else :            
            print("Total combination : ",c)
else: 
    print('Enter price more than 0')
