def avg(a,b,c,d,e):
    """creating function for avg result"""
    avg=(a+b+c+d+e/5)
    return avg
def get_marks(a,b,c,d,e):
    a=int(input("enter marks of english"))
    b=int(input("enter marks of nepali"))
    c=int(input("enter marks of math"))
    d=int(input("enter marks of GK"))
    e=int(input("enter marks of moral"))
    return a,b,c,d,e
a,b,c,d,e,= get_marks()
print(f"your marks")
    