def func(x,w,b):
    return w*x+b

def grad_desc_dw(y_actual,y_predict,x_actual,w):
    ans=0
    for i in range(0,4):
        ans=ans+(y_predict[i]-y_actual[i])*x_actual[i]
    ans=ans/4
    return (w-0.01*ans)
   
def grad_desc_db(y_actual,y_predict,b):
    ans=0
    for i in range(0,4):
        ans=ans+(y_predict[i]-y_actual[i])
    ans=ans/4
    return (b-0.01*ans)

def loss(y_actual,y_predict):
    ans=0
    for i in range(0,4):
        ans=ans+(y_actual[i]-y_predict[i])**2
    return ans/4


x_actual=[1,2,3,4]
y_actual=[8,11,14,17]
y_predict=[0,0,0,0]
w=0
b=0
s=0


oldloss=loss(y_actual,y_predict)
for i in range(0,1000):
    for j in range(0,4):
        y_predict[j]=func(x_actual[j],w,b)
    loss_var=loss(y_actual,y_predict)

    if(i%100==0):
        print("loss after ",i, "step : ",loss_var)
        if(loss_var-oldloss>0):
            s=1
        oldloss=loss_var

    w=grad_desc_dw(y_actual,y_predict,x_actual,w)
    b=grad_desc_db(y_actual,y_predict,b)

for j in range(0,4):
    y_predict[j]=func(x_actual[j],w,b)

    
if(s==1):
    print("Loss : Fail")
else:
    print("Loss : Pass") 
   
if(abs(w - 3) < 0.1):
    print("w: pass")
else:
    print("w: fail")

if (abs(b - 5) < 0.1):
    print("b: pass")
else:
    print("b: fail")

print("Final prediction :")
print(y_predict)


biggest_error = 0
for i in range(4):
    error = abs(y_predict[i] - y_actual[i])
    if error > biggest_error:
        biggest_error = error

print("Biggest error:", biggest_error)
    
