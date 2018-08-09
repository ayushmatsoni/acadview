#QUESTION1
def conditionalprob(pA,pB,pAB):
    pA_B=pB*pAB
    pBA=pA_B/pA
    return pBA
print(conditionalprob(11/36,6/36,2/36))

#QUESTION2
w1=4
b1=6
w2=4
b2=3

p=(0.5*(b1/(w1+b1)))/((0.5*(b1/(w1+b1)))+(0.5*(b2/(w2+b2))))
print(p)

#QUESTION3
print(((1/6)*(2/3))+((5/6)*(1/3)))