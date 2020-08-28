num=['1','2','3','4','5','6','7','8','9','0']
row1=['Q','W','E','R','T','Y','U','I','O','P']
row2=['A','S','D','F','G','H','J','K','L']
row3=['Z','X','C','V','B','N','M']
print(" Keyboard ")

print("                        Q W E R T Y U I O P ")
print("                         A S D F G H J K L ")
print("                          Z X C V B N M ")
print("                       1 2 3 4 5 6 7 8 9 0")
q=input("Enter a string without special characters : ")
q=q.upper()
def split(q): 
    return [char for char in q]   
w=split(q)

for v in w:
    i=v
    p=0
    if i in row1:
        for x in row1:
            p+=1
            if x==i:
                    print("Character ",i," is present in position ",p," of ROW-1 in Keyboard")
                    
    elif i in row2:
        for x in row2:
            p+=1
            if x==i:
                    print("Character ",i," is present in position ",p," of ROW-2 in Keyboard")
    elif i in row3:
        for x in row3:
            p+=1
            if x==i:
                    print("Character ",i," is present in position ",p," of ROW-3 in Keyboard")
    elif i in num:
        for x in num:
            p+=1
            if x==i:
                    print("Characater ",i," is present in position ",p," of numbers in Keyboard")
    else:
        print("This Characater is Space character of Qwerty Keyboard")
