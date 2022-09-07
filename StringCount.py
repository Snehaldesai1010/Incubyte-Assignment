l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def add(s):
    if(s.isnumeric()):
        sum=0
    else:
        sum=2
    s.lower()
    for i in range(len(l)):
        if l[i] in s:
            s=s.replace(l[i],str(i))
    if(len(s)==0):
        return 0
    m=[int(i) for i in s.split(",")]
    for i in m:
        sum+=i
    return(sum)
    
print(add("c,b"))
