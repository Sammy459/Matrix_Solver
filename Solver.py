def rref(a,n,m):
    columns=0
    for i in range(n):
        if columns>=m:                                                      
            x=a
            return x
            
        j=i                                                            
        while i<=j<n:                                                       
            if a[j][columns]==0:                                           # Chooses row with non zero leading entry
                j=j+1
                if j==n:                                                   # If no such row goes to next column
                    j=i
                    columns=columns+1
                    if columns==m:                                         # If no next column function ends 
                        x=a
                        return x
            else:
                break
            
        a[j],a[i]=a[i],a[j]                                                 # Replaces row with zero entry with first row with non zero entry
        b=a[i][columns]                                                     # Leading entry of the row
        a[i]=[a[i][j]/b for j in range(m)]                                  # Makes leading entry=1
        
        for k in range(n):
            for l in range(m):
                a[k][l]=round(a[k][l],5) 
            
        for j in range(n):
            if j!=i:
                b=a[j][columns]                                             # leading entry of row other than one with pivot
                for k in range(m):
                    a[j][k]=a[j][k]-b*a[i][k]                               # Elemntary row operation rj=rj-a*ri
                        
        for k in range(n):
            for j in range(m):
                a[k][j]=round(a[k][j],5)                                    # Rounds entry to make it better
        
        for k in range(n):
            for j in range(m):
                if abs(a[k][j])<0.0001:
                    a[k][j]=0.0
                    
        columns=columns+1
        if i==n-1:                                                            # For last row gives matrix back
            x=a
            return x

n,m=map(int,input('Enter rows and columns of matrix seperated by a space:').split())

if n==0 or m==0:
    print('Invalid matrix size')

else:
    a=[]
    f=open('Matrix.txt')
    a1=f.readlines()
    for i in range(n):
        a1[i]=a1[i].strip()
        l1=a1[i].split(' ')
        l2=[float(x) for x in l1]
        a.append(l2)
    
    count1=0
    for i in range(n):
        count1=count1+(a[i].count(0.0))
    
    if count1==n*m:
        print('This is zero matrix hence always satisfies Ax=0')
    
    else:
        x=rref(a,n,m)
        for i in range(n):
            for j in range(m):
                if x[i][j]==-0.0:
                    x[i][j]=0.0                                               

        l3=[]
        for i in range(len(x)):
            if x[i].count(0)==len(x[0]):
                l3.append(i)
                n=n-1
        for i in l3[::-1]:
            x.pop(i)
        l1={}
        l2=[]
        c=0
        d=0
        for i in range(n):
            if x[0][0]==0:
                l2.append('x'+str(1))
        
            for j in range(d,m):
                if x[i][j]!=0:
                    c=j
                    break
            
            if c-d>1:
                for k in range(c-d-1):
                    l2.append('x'+str(d+2+k))
            
            d=c
            if i==n-1 and m>n:
                for j in range(d+1,m):
                    l2.append('x'+str(j+1))
        
        y=list(set(l2))
        print('The free variables are:',y)
        
        if len(y)==0:
            print('No free variables hence only trivial solution i.e. X=0')
            
        else:
            y1=[int(y[i][1:]) for i in range(len(y))]
            for i in range(len(y)):
                l6=[]
                l1[y[i]]=l6
                a=int(y[i][1:])
                c=[x[i][a-1] for i in range(n)]
                j=0
                while j<n:
                    for k in range(m):
                        if k+1 in y1 and a==k+1:                   # When free variable itself occurs
                            l6.append(1.0)
                            
                        elif k+1 in y1 and a!=k+1:                 # When other free variable occurs
                            l6.append(0.0)
                            
                        else:
                            l6.append(-c[j])                        # When basic variable occurs
                            j=j+1
                            
                        if k==m-1:                           # When last variable occurs
                            j=n
                            
            a='X='
            for key in l1:
                a=a+(key+'*'+str(l1[key]))+'+'
            print(a[:len(a)-1])
