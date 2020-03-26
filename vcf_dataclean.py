from numpy import NaN
import pandas as pd
df = pd.read_excel('生产力&孵化器（手机）.xlsx')
# print(df['企业公示的联系电话（更多号码）'])
print(df.columns)
# ['Unnamed: 0', '类型', '评级', '公司名称', '法定代表人', '注册资本', '成立日期', '企业公示的联系电话',
       # '企业公示的联系电话（更多号码）', '企业公示的地址', '企业公示的网址', '企业公示的邮箱'],

df1 = df['企业公示的联系电话（更多号码）'].str.split(';',expand = True)
df1.columns=['电话1','电话2','电话3','电话4','电话5']
# print(df1)
print(df.join(df1))

df2 = df.join(df1).fillna('')
df2.rename(columns={'企业公示的联系电话':'电话0'}, inplace = True)
print(df2.columns)

def phonecheck(s):
    if len(s)==11:
        if '-'in s:
            return ''
        else:
            return s
    else:
        return ''

for i in range(6):
    df2['电话{}'.format(i)]=df2['电话{}'.format(i)].map(lambda x :phonecheck(x),)


print(df2.columns)
df2=df2.dropna(axis=0,subset=['电话0','电话1', '电话2', '电话3','电话4', '电话5'])
print(df2)
# df2.to_excel('test.xlsx')