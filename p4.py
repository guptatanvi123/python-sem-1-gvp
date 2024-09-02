#(4).Word shuffle using string manipulation.

orgnl="Gujarat Vidyapith Ahmedabad Computer Science"

f1=orgnl[0:7]  #indexing
f2=orgnl[8:17]
f3=orgnl[18:27]
f4=orgnl[28:36]

s1=(f2+" "+f3+" "+f1+" "+f4)  #word manipulation
s2=(f4+" "+f1+" "+f3+" "+f2)   #word manipulation
s3=(f3+" "+ f4+" "+f2+" "+f1)  #word manipulation


print(s1,"\n""\n",s2,"\n""\n",s3,) #output
