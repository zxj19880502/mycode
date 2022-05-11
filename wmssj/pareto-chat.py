import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'Arial Unicode MS'##防止在matplotlib中中文不显示

df = pd.read_excel('bl.xlsx')

data = pd.Series(df['Fail_QTY'].values,index = df['PD_LINE'])##将目标数据导入为series元组

data.sort_values(ascending = False,inplace = True )#对数组进行排序,ascending 升序,inplace代表行和列的排序

p=1.0*data.cumsum()/data.sum() 

key = p[p>0.8].index[0]

key_num = data.index.tolist().index(key)

plt.figure(figsize=(80,6))

data.plot(kind = 'bar', color = 'm', alpha = 0.9, width = 0.4,rot=0)

plt.ylabel('数量（个）')

p.plot(style = '--ko',secondary_y = True)

plt.axvline(key_num,color='r',linestyle=":",alpha=0.8)  

plt.text(key_num+0.2,p[key]-0.05,'累计占比:%.3f%%' % (p[key]*100), color = 'r') 

plt.ylabel('累计百分比')

plt.title("pareto-chat分析")

print('超过80%占比的节点值索引：',key)

print('超过80%占比的节点值索引位置：',key_num)

key_product = data.loc[:key]

print('线别：')

print(key_product)

#plt.savefig('帕累托分布练习1.png')

plt.show()