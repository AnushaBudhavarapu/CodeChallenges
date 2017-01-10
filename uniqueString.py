#with dictionary ds
#FIND IF STRING IS UNIQUE
def UniqueString(string):
    values={}
    for i in string:
        if values.get(i):
            return False
        else:
             values[i]=True
             
    return True

string=raw_input()
print UniqueString(string)
