

def read(n):
    a=[]
    for i in range(0,n):
        try:
            a.append(int(input()))
           
        except:
            print("Invalid type.")
            exit(0)
    return(a);
def min(a):
    min=a[0]
    for i in range(0,len(a)):
        if a[i]<min:
            min=a[i]
    return min
def max(a):
    max=a[0]
    for i in range(0,len(a)):
        if a[i]>max:
            max=a[i]
    return max
def task(min,max,a):
    for i in range(0,n):
        if a[i]>=0:
            a[i]=a[i]*min*min
        else:
            a[i]=a[i]*max*max
    return a;
try:
    n=int(input())
except:
    print("Invalid type.")
    exit(0)
a=read(n);

min=min(a)
max=max(a)
print(min)
a=task(min,max,a)
print(a);