from matplotlib import pyplot as plt
import numpy as np

print("The quadratic expression is in type of y=ax^2+bx+c")
print("Please enter the values of a, b, and c")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def discriminant(p,q,r):
    d=float(q**2-4*p*r)
    
    
    if d>0:
        print("The equation has two real roots")
    elif d==0:
        print("The equation has one real root")
    else:
        print("The equation has no real roots")
    return d
def roots(m,n,o):
    j=((-n+(o)**0.5)/(2*m))
    k=((-n-(o)**0.5)/(2*m))

    print("One root is:",j)
    print("Another root is:",k)
    return j , k 

d1=discriminant(a,b,c)


# Making the graph plotting for the quadratic given:
(x1,y1)=roots(a,b,d1)
x=np.linspace(-20,20,10000)
y=a*(x**2)+b*(x)+c

plt.plot(x,y)
plt.xlim(y1-5,x1+5)
plt.plot(x1,0,'x')
plt.plot(y1,0,'x')
if x1!=y1:
    plt.annotate("Root 1",xy=(x1,0),xytext=(x1-2,2),arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.annotate("Root 2",xy=(y1,0),xytext=(y1+2,2),arrowprops=dict(facecolor='black', arrowstyle='->'))
else:
    plt.annotate("Root  ",xy=(x1,0),xytext=(x1+1,1),arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.grid(True)
print("To see the plot , save it")
z=input("wanna save it? (yes/no)")

if z=="yes":
    u=input("Name of your file with proper extension ie. .png,.jpg,.pdf etc: ")
    plt.savefig(u)
elif z=="no":
    print("No plot was saved!")
else:
    print("Enter a valid response")



print("Thanks for using quadratic.py, HAVE A GREAT DAY! :)")