a=[]
b=[]
tup=()
print "Enter the end points of 1st line"
for i in range(2):
    x=input("Enter x co-ordinate of point")
    y=input("Enter y co-ordinate of point")
    tup=(x,y)
    a.append(tup)
print "Enter the end points of 2nd line"
for i in range(2):
    x=input("Enter x co-ordinate of point")
    y=input("Enter y co-ordinate of point")
    tup=(x,y)
    b.append(tup)

A=a[1][1]-a[0][1]

B=a[0][0]-a[1][0]

C= (-(B)*a[0][1])-(A*a[0][0])

A1=b[1][1]-b[0][1]

B1=b[0][0]-b[1][0]

C1= (-(B1)*b[0][1])-(A1*b[0][0])


det=float((A*B1)-(A1*B))

if(det==0):
    print "Parallel"
else:
    print "Intersect"
    
    x=float((C1*B)-(C*B1))/det
    y=float((A1*C)-(A*C1))/det
    
    tup=(x,y)
    print "Point of intersection is: "
    print tup

