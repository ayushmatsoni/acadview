import re
#question1
emails=["zuck26@facebook.com","page23@google.com","jeff42@amazon.com"]
ls=[]
for i in emails:
    x=re.findall("[\w]+",i)
    x=tuple(x)
    ls.append(x)
print(ls)

#question2
text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
b=name=re.findall("[b,B][a-zA-Z]{1,5}",text)
print(b)

#question3
sentence="A, very very; irregular_sentence"
print("")
print(sentence)
x=re.compile("[,; _]")
for i in sentence:
    y=x.sub(" ",sentence)
print(y)
print("")
i=0
tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstat"
reg=re.compile("[!]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[R][T]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[@]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[T][h][e][N][e][x][t][W][e][b][:] ")#/lbwej0pxOd cc: garybernhardt #rstat")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile(" [h][t][t][p][:][/][/][t][.][c][o][/][l][b][w][e][j][p][x][O][d]")
reg=re.compile("")#/lbwej0pxOd cc: garybernhardt #rstat")
for i in sentence:
    tweet=reg.sub("",tweet)
#tweet=re.sub(" ",tweet)
print(tweet)

"""
x=re.compile("[Good advice]^[! RT @TheNextWeb: ]^[http://t.co/lbwej0pxOd cc: @garybernhardt #rstats]")
for i in tweet:
    y=x.sub(" ",tweet)
print(y)
"""