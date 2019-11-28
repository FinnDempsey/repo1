res1 = []
res2 = []
allVAT=0
plusVAT=0
total=0

def plusVAT():
    for i in res1:
        global res2
        global allVAT
        res2.append(i*(23/100)+i)
        allVAT = allVAT + (i*(23/100))

    return allVAT

for x in range (1, 100):
   num=int(input('Enter a Sale Figure (Enter -1 to end): '))

   if (num==-1):
       break

   total = num+total

   res1.append(num)

plusVAT()

total = allVAT+total

print('The figure you entered were', res1)
print('These Sales figures including VAT are', res2)
print('The VAT charged in total is', allVAT)
print('The total sales are', total)
