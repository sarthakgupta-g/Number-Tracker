frequencies={}
n=int(input("how many numbers do you want?"))
i=0

while (i<n):
  temp=int(input("enter data: "))
  if(temp in frequencies):
    frequencies[temp]+=1
  else:
    frequencies[temp]=1
  i+=1

for number in frequencies:
  print(f"{number} is repeated {frequencies[number]}")
