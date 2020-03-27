# coding: utf-8

import itchat, datetime
import pandas as pd
from pandas import DataFrame
from itchat.content import TEXT

itchat.auto_login(hotReload=True)  # 不需要重复扫码登录

qun_name = '12.26京东云（天津）项目路演天津'
Wxm_list = []
Ncm_list = []
city_list = []


class WeChat(object):

    def get_all_info_from_wechat(self):
        # itchat.auto_login(enableCmdQR = False)
        # 获取群
        roomslist = itchat.get_chatrooms()
        # 群名称
        itchat.dump_login_status()  # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
        myroom = itchat.search_chatrooms(name=qun_name)  # 群聊名称
        gsq = itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)
        for i in gsq['MemberList']:
            # f.write('微信名：' + i['NickName'] + '|群昵称：' + i['DisplayName'] + '\n')
            # print('微信名：' + i['NickName'] + '|群昵称：' + i['DisplayName'] + '\n')
            # f.close()

            Wxm_list.append(i['NickName'])
            Ncm_list.append(i['DisplayName'])
            city_list.append(i['City'])

        dic_wxq = {'微信名': Wxm_list, '群昵称': Ncm_list,'城市':city_list}

        df = DataFrame(dic_wxq)
        df.to_excel(qun_name +'.xlsx')


if __name__ == '__main__':
    obj = WeChat()
    obj.get_all_info_from_wechat()
