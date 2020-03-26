#conding=utf-8
import pandas as pd
df = pd.read_excel('test.xlsx')

#空数据用0填充
df = df.fillna('0')
com_names = df['公司名称']
bosses = df['法定代表人']
phone1 = df['电话1']
phone2 = df['电话2']
phone3 = df['电话3']
phone0 = df['电话0']
phone4 = df['电话4']
phone5 = df['电话5']
addrs = df['企业公示的地址']
# mails = df['企业公示的邮箱']

#打开文件写入数据
f = open("contacts.vcf", 'a', encoding='utf-8')

for key,val in enumerate(com_names):
    f.write('BEGIN:VCARD'+'\n')
    f.write('VERSION:2.1'+'\n')
    f.write('N;CHARSET=UTF-8:'+bosses[key]+';;;'+'\n')
    f.write('FN;CHARSET=UTF-8:'+bosses[key]+'\n')
    if phone0[key]!='0':
            f.write('TEL;CELL:'+str(int(phone0[key]))+'\n')
    if phone1[key]!='0':
            f.write('TEL;CELL:'+str(int(phone1[key]))+'\n')
    if phone2[key]!='0':
            f.write('TEL;CELL:'+str(int(phone2[key]))+'\n')
    if phone3[key]!='0':
            f.write('TEL;CELL:'+str(int(phone3[key]))+'\n')
    if phone4[key]!='0':
            f.write('TEL;CELL:'+str(int(phone4[key]))+'\n')
    if phone5[key]!='0':
            f.write('TEL;CELL:'+str(phone5[key])+'\n')
    f.write('ADR:;;'+addrs[key]+';;;;\n')
    # f.write('EMAIL;WORK:'+mails[key]+'\n')
    f.write('ORG:'+val+'\n')
    f.write('END:VCARD'+'\n')
f.close()
