# def avg(a,b,c,d):
#     if (a<b<c and b<c<d)
#         e=(b+c+d)3
#     elif(b<c<d and c<d<a)
#         e=(c+d+a)3
#     elif(d<a<b and a<b<b)
#         e=(d+a+b)3
#     else(print("Error"))
#
# h=2
# g=3
# f=4
# j=5
#
# Average= avg(h,g,f,j)
#
# print("The answer is" Average)


def avg(a,b,c,d):
    num1=min(a,b,c,d)
    num2=(a+b+c+d)-num1
    best_score=num2/3
    return(best_score)
print(avg(4,5,6,7))
