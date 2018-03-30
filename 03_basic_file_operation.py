h=open("03_basic_read.txt","r")

with open('03_basic_file_operation.txt','w') as author:
  for i in h:
    a,b,c=i.split(",")
    s="-".join((a,c))
    author.write(s)

