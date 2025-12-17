import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

if 'ind' not in st.session_state:
    st.session_state['ind']=0

# 宠物图片数组
images = [
            {'url':'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
             'text':'猫1'
         },{
            'url':'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
            'text':'dog2'
           },{
            'url':'https://images2.alphacoders.com/716/71660.jpg',
            'text':'lion3'
    }]

# st.image()总共两个参数，url：图片地址 caption:图片的备注
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

#下一页 函数
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)

#上一页 函数
def forImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)

#分列容器
c1,c2=st.columns(2)
#c1,c2=st.columns([1,2])

with c1:
    st.button('上一张',on_click=forImg,use_container_width=True)

with c2:
    st.button('下一张',on_click=nextImg,use_container_width=True)





    
