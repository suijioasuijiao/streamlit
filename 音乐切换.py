import streamlit as st

if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.title("🎵 音乐播放器")
#歌手
songs = [
    {
        'imgurl': 'http://p2.music.126.net/o_OjL_NZNoeog9fIjBXAyw==/18782957139233959.jpg?param=130y130',
        'songurl': 'https://music.163.com/song/media/outer/url?id=65546.mp3',
        'name': '白色球鞋',
        'author': '陈奕迅',
        'time': '4:38'
    },
    {
        'imgurl': 'http://p1.music.126.net/Qs7rthgurYD-OISrms8hng==/109951166050592954.jpg?param=130y130',
        'songurl': 'https://music.163.com/song/media/outer/url?id=64561.mp3',
        'name': '单车',
        'author': '陈奕迅',
        'time': '4:38'
    },
    {
        'imgurl': 'http://p1.music.126.net/F7iOBko9fXjhW-aqJGZseA==/109951171843776354.jpg?param=130y130.jpg?param=130y130',
        'songurl': 'https://music.163.com/song/media/outer/url?id=64797.mp3',
        'name': '歌倒带人生',
        'author': '陈奕迅',
        'time': '4:38'
    }
]


#下一首 函数
def next_songs():
    st.session_state['ind']=(st.session_state['ind']+1)%len(songs)

#上一首 函数
def prev_songs():
    st.session_state['ind']=(st.session_state['ind']-1)%len(songs)


#分列容器
#c1,c2=st.columns(2)
c1,c2=st.columns([1,2])

with c1:
   # st.image()总共两个参数，url：图片地址 caption:图片的备注
    st.image(songs[st.session_state['ind']]['imgurl'],caption="专辑页面")
with c2:
    st.text(songs[st.session_state['ind']]['name'])
    st.text(songs[st.session_state['ind']]['author'])
    st.text(songs[st.session_state['ind']]['time'])
    st.button('上一张',on_click=prev_songs,use_container_width=True)
    st.button('下一张',on_click=next_songs,use_container_width=True)


# 读取音频URL
st.audio(songs[st.session_state['ind']]['songurl'])

#st.audio(audio_file)



    


