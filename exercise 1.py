#exercise 1
def my_func(x1,x2,x3):
    try:
        if  isinstance(x1,str) or isinstance(x2,str)  or isinstance(x3,str):
            return None
        elif not (isinstance(x1,float) and isinstance(x2,float)  and isinstance(x3,float)):
            return "Error: parameters should be float"
        else:
            answer=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        return answer
    except:
        if x1+x2+x3==0  :
            return "Not a number – denominator equals zero"

print(my_func("j","j","u"))


