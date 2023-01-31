str1 = input("Please Enter a sentence: ")
total = 1

for i in range(len(str1)):
    if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
        total = total + 1

print("Total Number of Words in the sentence = ", total)




