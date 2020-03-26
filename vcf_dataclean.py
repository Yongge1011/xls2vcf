from numpy import NaN
import pandas as pd
#数据导入
df = pd.read_excel('高新雏鹰（1-150）.xlsx')
df1 = df['企业公示的联系电话（更多号码）'].str.split(';',expand = True)
df2 = df.join(df1).fillna('')

# print(df2.columns)
def phonecheck(s):
    if len(s)==11:
        if '-'in s:
            return NaN
        else:
            return s
    else:
        return NaN

df2['企业公示的联系电话']=df2['企业公示的联系电话'].map(lambda x:phonecheck(x),)
df2[0]=df2[0].map(lambda x :phonecheck(x),)
df2[1]=df2[1].map(lambda x :phonecheck(x),)
df2[2]=df2[2].map(lambda x :phonecheck(x),)


df2 = df2.dropna(subset=[0,1,2,'企业公示的联系电话'],how='all')
df2.to_excel('chuying.xlsx')
