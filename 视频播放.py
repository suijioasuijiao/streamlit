import streamlit as st

# 读取视频数据
video_file = 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4'

video_arr=[{
    'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
    'title':'第一集',
    'nume':1,
    'author':'课堂'
    },{
    'url':'https://cn-gddg-ct-01-12.bilivideo.com/upgcxcode/69/94/34722089469/34722089469-1-192.mp4?e=ig8euxZM2rNcNbR3hWdVhwdlhW41hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=0000c10102932d9d4a7780738700f7ed5ceh&nbs=1&uipk=5&mid=0&deadline=1765766818&oi=1782024106&platform=html5&gen=playurlv3&os=bcache&og=hw&upsig=9978c7628b5a341ce5ed4d97829f99f6&uparams=e,trid,nbs,uipk,mid,deadline,oi,platform,gen,os,og&cdnid=61312&bvc=vod&nettype=0&bw=1450966&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
    'title':'第一集',
    'nume':2,
    'author':'NinthA'
    },{
    'url':'https://cn-gdfs-ct-01-01.bilivideo.com/upgcxcode/85/62/34668416285/34668416285-1-192.mp4?e=ig8euxZM2rNcNbNznwdVhwdlhbh3hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=000017a8cc30d6104b49a4f6018b42bac81h&deadline=1765766953&nbs=1&oi=1782024106&gen=playurlv3&os=bcache&og=cos&uipk=5&mid=0&upsig=3cba4ca678273a49916d5a935a21c0b5&uparams=e,platform,trid,deadline,nbs,oi,gen,os,og,uipk,mid&cdnid=60901&bvc=vod&nettype=0&bw=1917651&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
    'title':'第一集',
    'nume':3,
    'author':'爱丽速子LightSpeed'
    },{
    'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
    'title':'第一集',
    'nume':4,
    'author':'课堂'
    },{
    'url':'https://cn-gddg-ct-01-12.bilivideo.com/upgcxcode/69/94/34722089469/34722089469-1-192.mp4?e=ig8euxZM2rNcNbR3hWdVhwdlhW41hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=0000c10102932d9d4a7780738700f7ed5ceh&nbs=1&uipk=5&mid=0&deadline=1765766818&oi=1782024106&platform=html5&gen=playurlv3&os=bcache&og=hw&upsig=9978c7628b5a341ce5ed4d97829f99f6&uparams=e,trid,nbs,uipk,mid,deadline,oi,platform,gen,os,og&cdnid=61312&bvc=vod&nettype=0&bw=1450966&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
    'title':'第一集',
    'nume':5,
    'author':'NinthA-'
    },{
    'url':'https://cn-gdfs-ct-01-01.bilivideo.com/upgcxcode/85/62/34668416285/34668416285-1-192.mp4?e=ig8euxZM2rNcNbNznwdVhwdlhbh3hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=000017a8cc30d6104b49a4f6018b42bac81h&deadline=1765766953&nbs=1&oi=1782024106&gen=playurlv3&os=bcache&og=cos&uipk=5&mid=0&upsig=3cba4ca678273a49916d5a935a21c0b5&uparams=e,platform,trid,deadline,nbs,oi,gen,os,og,uipk,mid&cdnid=60901&bvc=vod&nettype=0&bw=1917651&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
    'title':'第一集',
    'nume':6,
    'author':'爱丽速子LightSpeed'
    }]

# 判断内存中有没有ind
if 'ind' not in st.session_state:
        st.session_state['ind']=1

# 显示视频
st.subheader("展示视频")


st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

#视频演示函数
def play(i):
    st.session_state['ind']=int(i)


#简介
st.subheader("作者")
st.text(video_arr[st.session_state['ind']]['author'])

st.subheader("选择集数")


# 每行显示的按钮数量
BUTTONS_PER_ROW = 3 

# 按行分组渲染按钮
# 创建对应数量的列（一行BUTTONS_PER_ROW个列）
cols = st.columns(BUTTONS_PER_ROW)

# 遍历视频列表，在列中渲染按钮（一行排满）
for idx, video in enumerate(video_arr):
    with cols[idx % BUTTONS_PER_ROW]:       # 按列取模，循环放入列中
        st.button(
            label=f"第{video['nume']}集",  # 显示集数
            use_container_width=True,      # 按钮填满列宽度
            on_click=play,                 # 点击触发切换
            args=[idx],                    # 传递视频索引
            key=f"video_btn_{idx}"         # 唯一key，避免按钮失效
        )
