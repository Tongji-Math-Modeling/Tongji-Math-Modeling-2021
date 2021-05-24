# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as npr
class Individual:
    _n=0
    eval=0
    chromsome=None
    def __init__(self):
        #长度为60
        self._n=60
        self.chromsome=np.zeros(60,dtype=int)
        #随机选取12个位置，设置1
        for i in range(12):
            index=npr.randint(0,60)
            self.chromsome[index]=1
 
    def crossover(self,another):
        startPos = npr.randint(self._n) #交叉的起始位置
        jeneLength = npr.randint(self._n)+1 # //交叉的长度
        
        son1 = Individual()
        son2 = Individual()

        son1.chromsome[0:startPos]=self.chromsome[0:startPos]
        son2.chromsome[0:startPos]=another.chromsome[0:startPos]
        
        endpos=startPos+jeneLength
        son1.chromsome[startPos:endpos]=another.chromsome[startPos:endpos]
        son2.chromsome[startPos:endpos]=self.chromsome[startPos:endpos]
        son1.chromsome[endpos:]=self.chromsome[endpos:]
        son2.chromsome[endpos:]=another.chromsome[endpos:]
        return son1,son2
    
    def mutation(self,learnRate):
        son = Individual()
        son.chromsome=self.chromsome.copy()
        mutationPos =npr.randint(self._n)#;//变异的位置
        #产生一个0-2之间的数
        temp = npr.randint(0,3)
        son.chromsome[mutationPos] += learnRate * temp
        return son

result=[]
    
class NGA:
    population=[]
    dimension=1
    bestPos=worstPos=0
    mutationProb=10
    crossoverProb=90
    maxIterTime=10000
    evalFunc=None
    arfa =1.0
    popu=2
    def __init__(self,popuNum, dimension,evalFunc,crossoverProb=10,mutationProb=90,maxIterTime=1000):
        for i in range(popuNum):
            oneInd=Individual()
            oneInd.eval=evalFunc(oneInd.chromsome)
            self.population.append(oneInd)
            print("初始种群",oneInd.eval)
            
        self.crossoverProb=crossoverProb
        self.mutationProb=mutationProb
        self.maxIterTime=maxIterTime
        self.evalFunc=evalFunc
        self.popu=popuNum
        self.dimension=dimension
    
    #找最好的个体位置
    def findBestWorst(self):
        self.population.sort(key=lambda o:o.eval,reverse=True)
        self.bestPos=0
        self.worstPos=self.popu-1
       #交叉操作 
    def crossover(self):
        fatherPos=npr.randint(0,self.popu)
        motherPos=npr.randint(0,self.popu)
        while motherPos == fatherPos:
            motherPos = npr.randint(0,self.popu)
        father = self.population[fatherPos]
        mother = self.population[motherPos]
        son1,son2=father.crossover(mother)
        
        son1.eval = self.evalFunc(son1.chromsome) #;// 评估第一个子代
        son2.eval = self.evalFunc(son2.chromsome)
        self.findBestWorst()
        
        if son1.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son1
        self.findBestWorst()
        if son2.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son2
            
    def mutation(self):
        father = self.population[npr.randint(self.popu)]
        son=father.mutation(self.arfa)
        son.eval = self.evalFunc(son.chromsome)
        self.findBestWorst()
        if son.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son
            
    def solve(self):
        shrinkTimes = self.maxIterTime / 10 
        #//将总迭代代数分成10份
        oneFold = shrinkTimes #;//每份中包含的次数
        i = 0
        while i < self.maxIterTime:
            print(i,"---",self.maxIterTime)
            if i == shrinkTimes:
                self.arfa =self.arfa / 2.0
            #经过一份代数的迭代后，将收敛参数arfa缩小为原来的1/2，以控制mutation
                shrinkTimes += oneFold  #;//下一份到达的位置
            for  j in range(self.crossoverProb):
                self.crossover()
            for  j in range(self.mutationProb):
                self.mutation()
            print("solution:",self.population[self.bestPos].chromsome)
            global result
            result.append(self.population[self.bestPos].chromsome)
            print("func value:",self.population[self.bestPos].eval)
            i=i+1
            
    def getAnswer(self):
        self.findBestWorst()
        return self.population[0].chromsome






#评估函数
def evaluateFunc(x):
    ganshe=0 #定义干涉量
    #约束1:部分书籍无法购买
    if x[15]+x[16]+x[17]+x[35]+x[39]>0:
        ganshe-=10000
    #约束2:每种书买两本
    if x[0]+x[1]+x[2]+x[3]+x[4]+x[45]+x[46]+x[47]+x[48]+x[49]+x[50]+x[51]+x[52]+x[53]+x[54]<2:
        ganshe+=10000
    if x[5]+x[6]+x[7]+x[8]+x[9]+x[10]+x[11]+x[12]+x[13]+x[14]+2*(x[15]+x[16]+x[17]+x[18]+x[19])+x[55]+\
        x[56]+x[57]+x[58]+x[59]<2:
        ganshe+=10000
    if x[20]+x[21]+x[22]+x[23]+x[24]+x[25]+x[26]+x[27]+x[28]+x[29]+x[30]+x[31]+x[32]+x[33]+x[34]+\
        3*(x[35]+x[36]+x[37]+x[38]+x[39])+x[40]+x[41]+x[42]+x[43]+x[44]<2:
        ganshe+=10000
    s1=25*x[0]+19.5*x[5]+22*x[10]+36.1*x[20]+32.5*x[25]+33.6*x[30]+40*x[40]+55*x[45]+30*x[50]+48.5*x[55];
    s2=20*x[1]+19.5*x[6]+22.5*x[11]+39*x[21]+36*x[26]+33*x[31]+100*x[36]+38.8*x[41]+55.5*x[46]+32.5*x[51]+51*x[56];
    s3=19*x[2]+20*x[7]+21.3*x[12]+35.8*x[22]+34*x[27]+32*x[32]+99.9*x[37]+42*x[42]+54*x[47]+29.5*x[52]+49.3*x[57];
    s4=22*x[3]+21*x[8]+20*x[13]+40*x[18]+35.4*x[23]+35.4*x[28]+35*x[33]+102*x[38]+43.5*x[43]+56*x[48]+31*x[53]+50*x[58];
    s5=23*x[4]+19*x[9]+21.5*x[14]+40*x[19]+38.2*x[24]+35.5*x[29]+34*x[34]+46*x[44]+52*x[49]+33*x[54]+48.9*x[59];
    z1=0
    if s1<=1:
        z1=0
    elif s1<60:
        z1=s1+5
    elif s1<100:
        z1=s1
    elif s1<200:
        z1=s1-10
    else:
        z1=s1-25
    z2=0
    if s2<=1:
        z2=0
    elif s2<60:
        z2=s2+5
    elif s2<100:
        z2=s2
    elif s2<200:
        z2=s2-15
    else:
        z2=s2-30
    z3=0.92*s3
    z4=0
    if s4<=1:
        z4=0
    elif s4<60:
        z4=s4+5
    elif s4<130:
        z4=s4
    else:
        chepaest=0 #最便宜的一本书
        if x[13]+x[18]>0:
            cheapest=20
        elif x[8]>0:
            cheapest=21
        elif x[3]>0:
            cheapest=22
        elif x[53]>0:
            cheapest=31
        elif x[33]+x[38]>0:
            cheapest=35
        elif x[28]>0:
            cheapest=35.4
        elif x[23]>0:
            cheapest=35.4
        elif x[43]>0:
            cheapest=43.5
        elif x[58]>0:
            cheapest=50
        elif x[48]>0:
            cheapest=56
        z4=s4-cheapest
    z5=0
    if s5<=1:
        z5=0
    elif s5<60:
        z5=s5+5
    else:
        z5=s5
    #计算总花销
    w=z1+z2+z3+z4+z5
    #约束:总花销需要不超过250
    if w>250: 
        ganshe+=1000
    #计算书本总数
    book=0
    for i in range(60):
        book+=x[i]
    book+=x[18]+x[19]+2*(x[36]+x[37]+x[38])
    #目标函数
    return 100000*book+w-ganshe
    
    


nga=NGA(popuNum=1000,dimension=1,evalFunc=evaluateFunc)
nga.solve()
print(nga.getAnswer())
