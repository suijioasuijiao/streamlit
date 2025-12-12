import streamlit as st
st.set_page_config(page_title="相册",page_icon="🐾")
st.title("我的相册")
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {
        'url':"https://img.keaitupian.cn/newupload/10/1666862863215295.jpg",
        'text':"miku"
    },{
        'url':"https://img-baofun.zhhainiao.com/pcwallpaper_ugc/static/53870b0791f3529fb39d04d2b26cd6be.jpg?x-oss-process=image%2fresize%2cm_lfit%2cw_1920%2ch_1080",
        'text':"keqin"
    },{
        'url':"http://img.pconline.com.cn/images/upload/upc/tx/wallpaper/1307/30/c0/23934263_1375169304698.jpg",
        'text':"creed"
    }
]

#url:图片的地址 caption:图片注释介绍
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

#按钮绑定函数
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

#分列容器
c1, c2 = st.columns((1, 1))
with c1:
    st.button("上一张",on_click=nextImg,use_container_width=True)
with c2:
    st.button("下一张",on_click=nextImg,use_container_width=True)
