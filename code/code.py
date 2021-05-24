import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re



res=""
f, (ax1) = plt.subplots(figsize = (6,3),nrows=1)

res=""
with open('data.txt',"r") as fp:
    res+=fp.read()
    fp.close()
    x=np.zeros(60,dtype=int)
    #正则表达式读取
    for k in range(1,61):
        pattern=re.search(r'X{}.*?(\d)'.format(k),res,re.S)
        x[k-1]=pattern.group(1)
    #匹配Y

    x=x.reshape((12,5)).T
    cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
    
    sns.heatmap(pd.DataFrame(x,columns=[i for i in range(1,13)],index=['S1','S2','S3','S4','S5']), 
                linewidths = 0.1, ax = ax1, vmax=3, vmin=0, cmap='gray_r',cbar=False,annot=True)
    
    plt.savefig('pic.jpg')