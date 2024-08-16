price = int(input('Price: ')) 
deno1, deno2, deno3 = map(int, input('Denominations: ').split()) 
print("Can you form", price, "exactly using", deno1, deno2, deno3, "?") 
for d1 in range(0, 1 + price // deno1): 
    for d2 in range(0, 1 + price // deno2): 
         for d3 in range(0, 1 + price // deno3): 
           if d1 * deno1 + d2 * deno2 + d3 * deno3 == price: 
                  print(d1, d2, d3) 
    else: 
       # print('No')
       pass