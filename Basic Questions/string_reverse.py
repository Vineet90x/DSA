#REVERSING A STRING


#Using Slicing
text = "hello"
print(text[::-1]) 

#Using Index 
for i in range(len(text)-1, -1, -1):
    print(text[i],end="")
print()
    
#using variable  
reversed_string = []
for i in range(len(text)-1, -1, -1):
    reversed_string.append(text[i])
reversed_string = "".join(reversed_string)
print(reversed_string)