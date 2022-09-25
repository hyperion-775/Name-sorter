numbers1=int(input("How many names need to be sorted?"))
namelist=[]

for n in range(numbers1):
  name1=input("What is name "+ str(n+1)+"? ")
  namelist.append(name1)

for p in range(len(namelist)):
  print(p)
  print(len(namelist))
  for j in range(numbers1-1):
    print("numbers1 "  + str(j) + namelist[j] + " next name " + namelist[j+1])
    if namelist[j]<namelist[j+1]:
      print("Less Than")
    else:
     namelist[j], namelist[j+1] = namelist[j+1], namelist[j]
     print("Greater than, so I swapped the names")
print(namelist)
