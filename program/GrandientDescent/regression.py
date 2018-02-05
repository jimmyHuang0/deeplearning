import matplotlib.pyplot as plt
import random


#原始函数
orgK = 1
orgB = 0
def yOrg(x):
    return orgK*x+orgB

def y(x,K,B):
    return K*x+B

#获取离散噪声点，得到原始数据
parN=100 #离散点个数
xList = []
yList = []
for num in range(parN):
    xList.append(num)
    yList.append(yOrg(num)+random.uniform(-1,1))
   # print(yList[num])

#plt.plot(xList,yList,'ro')
#plt.show()
#写loss Function
#方式一：离散点与拟合点的平方的平均值
def lossFun(dK,dB,dn,xL,yL):
    sum=0
    for num in range(dn):
        sum+=(yL[num]-y(xL[num],dK,dB))*(yL[num]-y(xL[num],dK,dB))
    return sum/dn

print(lossFun(orgK,orgB,parN,xList,yList))


def detaK(xL,yL,K,B):
    sum = 0
    for num in range(len(xL)):
        sum += (xL[num]*(yL[num]-(K*xL[num]+B)))
    return sum*(-2) / len(xL)

def detaB(xL,yL,K,B):
    sum = 0
    for num in range(len(xL)):
        sum += (yL[num]-(K*xL[num]+B))
    return sum*(-2) / len(xL)


#开始做梯度下降
learnRateK=0.00007
learnRateB=0.05
KStart=2
BStart=10

deteKTemp=KStart
detaBTemp=BStart

pNum=[]
pK=[]
pB=[]
for num in range(1000):
    KTemp=deteKTemp
    BTemp=detaBTemp
    deteKTemp = deteKTemp - learnRateK*detaK(xList, yList, KTemp, BTemp)
    detaBTemp = detaBTemp - learnRateB*detaB(xList, yList, KTemp, BTemp)
    print(num,deteKTemp,detaBTemp)
    pNum.append(num)
    pK.append(deteKTemp)
    pB.append(detaBTemp)

plt.plot(pNum,pK)
plt.plot(pNum,pB)
plt.show()
'''
a=1
b=1
n=20

def fun(x,a,b):
    return a*x+b


xList = []
yList = []
for num in range(n):
    xList.append(num)
    yList.append(fun(num,a,b)+random.uniform(-1,1))

plt.plot(xList,yList,'ro')
#plt.show()

def lossFun(da,db):
    sum=0.0
    for num in range(n):
        sum=sum+(yList[num]-fun(xList[num],da,db))*(yList[num]-fun(xList[num],da,db))
    return sum/(n-1)

xListLoss=[]
yListLoss=[]
xListLoss.append(1)
yListLoss.append(lossFun(1,1))

#for num in range(-10,20):
#    xListLoss.append(num/10)
#    yListLoss.append(lossFun(num/10,1))


xLine=[0,n]
yLine=[fun(0,1,1),fun(n,1,1)]

plt.plot(xLine,yLine)
plt.show()
'''
