#function to scan name fro user
myname=input("please entre your name")
#function to scan age fro user
myage=input("please entre your age")
#function to scan faculty fro user
myfaculty=input("please entre your faculty")
f1=open("file.txt","w")
f1.write(myname)
f1.write("\n")
f1=open("file.txt","a+")
f1.write(myage)
f1.write("\n")
f1=open("file.txt","a+")
f1.write(myfaculty)
f1.write("\n")
