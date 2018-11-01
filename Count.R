print("Hello World!")

num <- read.csv("C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 6/num.csv")
num
numbers <- num[order(num),]
numbers

df <- read.table("C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 6/words.txt")
df
length(df)
a = unique(df)

text = scan("C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 6/words.txt", quote=NULL, what="x")
counts = as.data.frame(xtabs(~text))
colnames(counts)
head(counts)
d = sum(counts$Freq)
d
c = nrow(counts)
c

hist(numbers)
