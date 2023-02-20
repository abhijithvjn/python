# co2 8. Accept a list of words and return length of longest word
def long(get_name):
    length=0
    get_name=get_name.split(" ")
    for i in get_name:
        if len(i)>length:
            length=len(i)
    return length
s=str(input("enter the string:"))
w=long(s)
print(w)      
