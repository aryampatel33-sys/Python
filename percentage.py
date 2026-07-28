print("Enter Marks obtained in 4 subjects: ")
maths= int(input("maths :"))
science= int(input("science :"))
english= int(input("science :"))
SST= int(input("sst :"))
sum = maths+science+english+SST
print("The sum of maths, science, english and sst is: ", sum)
perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)     