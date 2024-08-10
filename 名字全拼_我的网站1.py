'我的主页'

import wordcloud
import base64
import streamlit as st
from PIL import Image,ImageEnhance
import io

page = st.sidebar.radio('我的首页',['兴趣推荐','图片处理工具','工具指南','评论区'])
def ciyun(str):
    font = "anna.ttf"
    w = wordcloud.WordCloud(width=600, height=400,font_path=font, max_words=50).generate(str)
    w.to_file("ciyun.png")
    img = Image.open("ciyun.png")
    return img
msg2 = ':blue[大家好]'
def page_1():
    uploaded_file = st.file_uploader("名字全拼_滕王阁序")
    if uploaded_file is not None:
        str_data = uploaded_file.read().decode("utf-8")
        st.image(ciyun(str_data))
    else:
        pass
    st.write( "灾厄mod标题曲The Tale Of A Cruel World (残酷世界的传说出)出自【泰拉瑞亚 灾厄mod】")
    with open("名字全拼_TheTaleofaCruelWorld.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.download_button(label = "下载",data = mymp3,file_name="名字全拼_TheTaleofaCrueWorld.mp3")
    st.write( "神明吞噬者主题曲 ""Scourge of The Universe(寰宇灾劫)""出自【泰拉瑞亚 灾厄mod】")
    with open("名字全拼_ScourgeoftheUniverse.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.download_button(label = "下载",data = mymp3,file_name="名字全拼_ScourgeoftheUniverse.mp3")
    st.write( "至尊灾厄战斗曲Stained Brutal Calamity(玷残之灾)出自【泰拉瑞亚 灾厄mod】")
    with open("名字全拼_StainedBrutalCalamity.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.download_button(label = "下载",data = mymp3,file_name="名字全拼_StainedBrutalCalamity.mp3")
    st.write( " 璀璨华焰——犽戎二形态主题曲 Roar of The Jungle Dragon(丛林龙之吼)出自【泰拉瑞亚 灾厄mod】")
    with open("名字全拼_RoaroftheJungleDragon.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.download_button(label = "下载",data = mymp3,file_name="名字全拼_RoaroftheJungleDragon.mp3")
    st.write("Iron Lotus（铁血莲华）出自【废墟图书馆】")
    with open("名字全拼_IronLoyus.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.download_button(label = "下载",data = mymp3,file_name="名字全拼_IronLoyus.mp3")
    st.image("名字全拼_鬼妖村正.gif")
    st.image("名字全拼_鸿蒙方舟.png")
    st.write("-------------------------------------------------------")
    st.write("非游戏音乐")
    st.write("Take Flight  作者：Lindsey Stirling")
    with open("名字全拼_TakeFlight.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.download_button(label = "下载",data = mymp3,file_name="名字全拼_TakeFlight.mp3")
    st.write("-------------------------------------------------------")
    st.write("                                              你可能想看")
    st.write("如何下载Steam，您只需要打开以下按钮到官网即可")
    st.link_button('Steam官网', 'https://store.steampowered.com/')
    st.write("下载按钮在官网右上角！右上角！！")
    st.write("如果碰到没有出现人机验证的情况就换一台设备，或者换个浏览器")
    st.write("人机认证有耐心就行，等图片完全出现，看仔细了在选")
    

    
def page_2():
    '图片处理工具'
    st.write(":sunglasses:图片处理工具:sunglasses:")
    uploaded_file = st.file_uploader("图来！",type=["png",'jpeg',"jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img  = Image.open(uploaded_file)
        
        tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(["原图","改色1","改色2","改色3","改色4","增强10","增强5"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_ch(img,0,2,1))
        with tab3 :
            st.image(img_ch(img,1,0,2))
        with tab4:
            st.image(img_ch(img,1,2,0))
        with tab5:
            st.image(img_ch(img,2,1,0))
        with tab6:
            st.image(img)
            st.image(zengqing(img,10))
        with tab7:
            st.image(img)
            st.image(zengqing(img,5))
        
#        st.image(img_ch(img,0,1,2))

def page_3():
    '工具指南'
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('名字全拼_words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('名字全拼_check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('名字全拼_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'rest':
            st.code('''
            # 恭喜你触发彩蛋，这是一行地址网站:https://www.bilibili.com/''')       
def page_4():
    '评论区'
    st.balloons()
    st.write("评论区")
    with open("名字全拼_leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split()
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "用户":
            with st.chat_message("☕"):
                st.write(i[1],";",i[2])
        elif i[1] == "管理员":
            with st.chat_message('🔥'):
                st.write(i[1],";",i[2])
    name = st.selectbox("我是......",["用户","管理员"])
    new_message = st.text_input("老登快说！")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("名字全拼_leave_messages.txt","w",encoding="utf-8") as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)
    
def img_ch(img,rc,gc,bc):
    "修图"
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img 

def zengqing(img,b):
    e = ImageEnhance.Contrast(img)
    c = e.enhance(b) 
    return c

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last},base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('名字全拼_天象奇景.jpg')
page_bg('名字全拼_天象奇景.jpg')

if page == '兴趣推荐':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '工具指南':
    st.snow()
    page_3()
elif page == '评论区':
    page_4()

