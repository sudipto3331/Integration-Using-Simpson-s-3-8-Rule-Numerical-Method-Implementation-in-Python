"""
Solve for X^2+5*X-9
"""
def F(x):
    return x**2+5*x+9
def Simpsons_38_interpolation(a,b,n):
    h=(b-a)/n
    integration=0
    for i in range(n):
        x0=a+i*h
        x1=x0+h/3
        x2=x1+h/3
        x3=a+(i+1)*h
        val=(h*(F(x0)+3*F(x1)+3*F(x2)+F(x3)))/8
        integration=integration+val
    return integration
print("____Simpson's 8/3 Rule____")
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
step_size=int(input("Eter the step size: "))
integration=Simpsons_38_interpolation(a, b,step_size+1)
print("\nIntregrated value = %.6f"%(integration))
