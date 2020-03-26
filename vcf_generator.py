#conding=utf-8
import pandas as pd
df = pd.read_excel('chuying.xlsx')
print(df.columns)

#添加联系人前缀
def add_prename (name):
    new_name= 'CY&GX'+name
    return new_name

df['法定代表人']=df['法定代表人'].map(lambda x:add_prename(x))

#空数据用0填充
df = df.fillna('0')
com_names = df['公司名称']
bosses = df['法定代表人']
phone1 = df['联系电话1']
phone2 = df['联系电话2']
phone3 = df['联系电话3']
phone4 = df['联系电话4']
addrs = df['地址']
mails = df['邮箱']

#打开文件写入数据
f = open("contacts_chuying.vcf", 'a', encoding='utf-8')

for key,val in enumerate(com_names):
    f.write('BEGIN:VCARD'+'\n')
    f.write('VERSION:2.1'+'\n')
    f.write('N;CHARSET=UTF-8:'+bosses[key]+';;;'+'\n')
    f.write('FN;CHARSET=UTF-8:'+bosses[key]+'\n')
    if phone1[key]!='0':
            f.write('TEL;CELL:'+str(int(phone1[key]))+'\n')
    if phone2[key]!='0':
            f.write('TEL;CELL:'+str(int(phone2[key]))+'\n')
    if phone3[key]!='0':
            f.write('TEL;CELL:'+str(int(phone3[key]))+'\n')
    if phone4[key]!='0':
            f.write('TEL;CELL:'+str(int(phone4[key]))+'\n')
    if addrs[key] != '0':
        f.write('ADR:;;'+addrs[key]+';;;;\n')
    if mails[key] != '0':
        f.write('EMAIL;WORK:'+mails[key]+'\n')
    f.write('ORG:'+val+'\n')
    f.write('END:VCARD'+'\n')
f.close()
print('完成{}个联系人转换'.format(len(com_names)))