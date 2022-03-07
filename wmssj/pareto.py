import matplotlib.pyplot as plt
import pandas as pd
aa=('bl.xlsx')   
df=pd.DataFrame(pd.read_excel(aa))
df1=df.groupby(["线别"])["数量"].sum().reset_index()
df1=df1.set_index("线别")
df1=df1[u"数量"].copy()
df2=df1.sort_values(ascending=False)
plt.rc("font",family="SimHei",size=9)
plt.figure(figsize=(60,6))
df2.plot(kind = 'bar', color = 'c', alpha = 0.9, width = 0.4,rot=0)
plt.ylabel(u"个数")
p=1.0*df2.cumsum()/df2.sum()  
p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2) 
plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9),arrowprops=dict(linestyle="-",alpha=0.8 ,connectionstyle="arc3,rad=.2"))
 
#print(p)

plt.ylabel(u"比例")
plt.title("pareto-chat分析")
plt.show()