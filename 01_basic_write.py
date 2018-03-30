with open("01_basic_write.txt","w") as author:
 author1="1,almasud,Abdullah Al Masud"
 author2="2,rimon,Rimon Ali"
 author3="3,niloy,Niloy Roy"
 author4="4,sourov,Sourov De Sharma"
 author5="5,sathi,Sathi Rani Roy"
 author.write('{}\n{}\n{}\n{}\n{}\n'. format(author1, author2,author3,author4,author5))