#R

a=read.table("./a.txt",skip=2)

write.table(x=a,file="./b2.txt",row.names=F,col.names=F,quote=F)

