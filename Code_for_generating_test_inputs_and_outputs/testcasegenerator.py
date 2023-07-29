import random
inpbbit=""
inpabit=""
d=""
inpa=0
inpb=0
l=""
Fobj=open(r"C:\Users\kakhi\OneDrive\Desktop\IITB\Quartus Projects\vlsidesign_assignment\inp.txt",'w')
for i in range(64):
    for j in range(32):
        a= random.randint(0,1)
        inpa+=(a)*(2**(31-j))
        inpabit+= str(a)
        
        c=random.randint(0,1)
        inpb+=(c)*(2**(31-j))
        inpbbit+=str(c)

        cin=random.randint(0,1)
        
    outsum= inpa + inpb + cin
    h=outsum
    for k in range(33):
        i=h%2
        l+=str(i)
        h=h//2
    outsumbit = l [::-1]
    print(outsumbit,inpabit,inpbbit,cin,outsum)
    temp=outsumbit+inpabit+inpbbit+str(cin)+'\n'
    Fobj.write(temp)
    inpabit=""
    inpbbit=""
    l=""
    inpa=0
    inpb=0
Fobj.close()
