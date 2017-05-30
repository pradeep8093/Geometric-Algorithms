import math
L=[(377,106),(588,361),(450,261),(377,261),(274,381),(404,342),(150,150)];

def findhull(S,a,b):
    
    if(len(S)>0):
        max=-999999
        pos=-1
        s3=[]
        
        
        for i in range(len(S)):
           
            A=b[0]-a[0]
            B=a[1]-b[1]
            C= (-(B)*S[i][1])-(A*S[i][0])

            d=(A+B+C)/(math.sqrt((A*A)+(B*B)))
            print i
            print d
            if(d>=max):
                max=d
                pos=i
        print pos
        d=S[pos]
        print d
        S.remove(S[pos])

        
        for i in range(len(S)):
            d=((L[i][0]-a[0])*(b[0]-a[0]))-((L[i][1]-a[1])*(b[1]-a[1]))
            
            print d
            if(d<0):
                s3.append(L[i])

        findhull(s3,a,d)




def quickhull(L):
    L.sort()
    a=L[0]
    b=L[len(L)-1]
    print a
    print b
    s1=[]
    s2=[]
    L.remove(a)
    L.remove(b)
    for i in range(len(L)):
        
        d=((L[i][1]-a[1])*(b[0]-a[0]))-((L[i][0]-a[0])*(b[1]-a[1]))
        

        if(d>0):
            s1.append(L[i])
        elif(d<0):
            s2.append(L[i])
        else:
            continue
    print s1
    print s2
    findhull(s1,a,b)
    findhull(s2,b,a)


quickhull(L)

     
        
        
    
