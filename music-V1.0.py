# -*- coding: utf-8 -*-
# writer:自游
# date:2024/4/2
# 转载使用请标明出处。
# 严禁用于商业用途。
# 如有侵权行为请联系作者。
import re
import requests


# 声明音乐列表
music_list = []

headers = {
    # 请求头
    # 浏览器的身份证
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS)'
}
def get_music():
    # 输入音乐名
    keyword = input("请输入音乐名:")
    url = ('https://www.kumeiwp.com/index/search/data?page=1&limit=50&word={}&scope=all'.format(keyword))
    # 请求数据
    response = requests.get(url).text
    # 解析数据
    response = eval(response)
    data = response['data']
    for d in data:
        d = str(d)
        # 歌曲ID
        id_list = re.findall(r"file_id': (.*?), 'title",d)
        for i in id_list:
            id = i

        # 歌曲名
        name_list = re.findall(r'title="(.*?)">',d)
        for n in name_list:
            name = n

        # 更新列表
        music_list.append({"name":name,"id":id})


def input_music():
    global name
    nu = 0
    for n in music_list:
        nu += 1
        print(nu,'.',n['name'])
    num = input('请输入序号:')
    num = int(num)
    if num <= 0:
        print('序号错误!')
        exit()
    nu = 0
    for n in music_list:
        nu += 1
        if nu == num:
            name = n['name']
            print('下载:',name)
            break

def download_music():
    for music in music_list:
        if music["name"] == name:
            id = music["id"]
            break
    url = 'https://www.kumeiwp.com/file/{id}.html'
    response = requests.get(url.format(id=id)).text
    cc = re.findall(r'<a href="(.*?)xz=b1" target="_blank" title=', response)
    for c in cc:
        cc = '{}xz=b1'.format(c)
    zz = requests.get(cc,headers=headers).content
    with open(name, 'wb') as f:
        f.write(zz)
        f.close()
    print('{}下载成功!'.format(name))

'''***main***'''
get_music()
input_music()
download_music()
