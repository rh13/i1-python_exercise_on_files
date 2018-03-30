authors= ["1,almasud,Abdullah Al Masud","2,rimon,Rimon Ali","3,niloy,Niloy Roy","4,sourov,Sourov De Sharma","5,sathi,Sathi Rani Roy"]
with open('02_basic_write.txt','w') as author:
  for i in authors:
    author.write(i)
    author.write("\n")


