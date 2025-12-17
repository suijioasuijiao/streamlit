import streamlit as st
import pandas as pd   # 导入Pandas并用pd代替

# 全局页面配置（必须放在最前面）
st.set_page_config(page_title="选项卡综合示例", page_icon="📌")

st.title("选项卡简单示例")
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["学生档案", "美食探索", "视频切换", "音乐切换", "视频切换","个人简历"])

# ---------------------- 选项卡1：学生档案 ----------------------
with tab1:
 

    # 标题
    st.title("学生张三-学生档案")
    st.header("🔑  基础信息")

    # 基础信息
    st.text("当前教室：实训楼-108")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("学生ID：1433223-20250-12-11")
    with col2:
        st.text("注册时间：")
        st.text("当前教室：实训楼-108")
    with col3:
        st.caption('2025-12-11')

    # 当前任务进度条
    st.title("当前课程进度：")
    st.progress(0.10)

    # 技能矩阵
    st.title("📊技能矩阵")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("法律", help='民法相关')
        st.markdown('##### 95%')
        st.caption('↑2%')
    with col2:
        st.text("语言艺术", help='律师的表达语言')
        st.markdown('##### 96%')
        st.caption('⬇︎-1%')
    with col3:
        st.text("宪法")
        st.markdown('##### 92%')
        st.caption('⬇︎10%')

    # 任务日志
    st.title("📅任务日志")
    data = {
        '日期': ['2025-12-01', '2025-12-03', '2025-12-06', '2025-12-09', '2025-12-12'],
        '任务': ["宪法学习", '教学', '法制科普', '宪法模拟竞赛', '考试'],
        '状态': ["完成", '进行中', '进行中', '未完成', '未完成'],
        '难度': ['难', '易', '易', '中', '中'],
    }
    index = pd.Series(['01', '02', '03', '04', '05'], name='任务编号')
    df = pd.DataFrame(data, index=index)
    st.subheader('默认显示')
    st.dataframe(df)

    # 最新代码成果
    st.title("🔒最新代码成果")
    st.subheader('Python代码块')
    python_code = '''def hello():
    st.text("Hello World!")
    st.title("这是标题")
    st.header("这是章节")
    st.subheader("这是子章节")
    st.text("Hello World!",help="这是帮助")
    等等
    '''
    st.code(python_code, line_numbers=True)
    st.markdown('##### 系统状态：在线 链接状态：已加密')

# ---------------------- 选项卡2：南宁美食 ----------------------
with tab2:
    st.header("这是第二个选项卡")
    st.markdown("#### 第二个选项卡的内容")
    st.title("南宁美食探索")
    st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

    # 地图
    st.header("南宁美食地图")
    data_map = {
        'latitude': [22.854169, 22.853700, 22.854323, 22.854708, 22.854565],
        'longitude': [108.223035, 108.222531, 108.222751, 108.223867, 108.222917]
    }
    df_map = pd.DataFrame(data_map)
    st.map(df_map, size=1)

    # 美食数据
    data = {
        '价格': [20, 26, 23, 35, 25],
        '高峰时期': [11, 12, 13, 14, 10],
        '评分': ['9.8', '8.6', '8.5', '9.6', '7.3'],
    }
    ind = pd.Series(['沪上阿姨', '华莱士汉堡', '蓝师傅柳州螺蛳粉', '横县鱼生', '燕姐钦州老牌猪脚粉'], name='店家')
    df_food = pd.DataFrame(data, index=ind)
    st.dataframe(df_food)

    st.markdown('***')
    # 条形图（评分）
    df_food['评分'] = df_food['评分'].astype(float)
    st.bar_chart(df_food, x='高峰时期', y='评分')

    st.markdown('***')
    # 折线图（价格）
    st.line_chart(df_food, y='价格')

    st.markdown('***')
    # 面积图（高峰时期）
    st.area_chart(df_food, y='高峰时期')

# ---------------------- 选项卡3：图片切换 ----------------------
with tab3:
    st.header("这是第三个选项卡")
    st.markdown("#### 第三个选项卡的内容")

    # 初始化图片切换的独立状态（避免和其他功能冲突）
    if 'img_ind' not in st.session_state:
        st.session_state['img_ind'] = 0

    # 宠物图片数组
    images = [
        {
            'url': 'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
            'text': '猫1'
        },
        {
            'url': 'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
            'text': 'dog2'
        },
        {
            'url': 'https://images2.alphacoders.com/716/71660.jpg',
            'text': 'lion3'
        }
    ]

    # 图片切换函数
    def nextImg():
        st.session_state['img_ind'] = (st.session_state['img_ind'] + 1) % len(images)

    def forImg():
        st.session_state['img_ind'] = (st.session_state['img_ind'] - 1) % len(images)

    # 显示图片
    st.image(images[st.session_state['img_ind']]['url'], caption=images[st.session_state['img_ind']]['text'])

    # 分列容器（按钮添加唯一key）
    c1, c2 = st.columns(2)
    with c1:
        st.button('上一张', on_click=forImg, use_container_width=True, key='img_prev_btn')
    with c2:
        st.button('下一张', on_click=nextImg, use_container_width=True, key='img_next_btn')

# ---------------------- 选项卡4：音乐播放器 ----------------------
with tab4:
    st.header("这是第四个选项卡")
    st.markdown("#### 第四个选项卡的内容")

    # 初始化音乐切换的独立状态
    if 'song_ind' not in st.session_state:
        st.session_state['song_ind'] = 0

    st.title("🎵 音乐播放器")
    # 歌手/歌曲数据
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
            'imgurl': 'http://p1.music.126.net/F7iOBko9fXjhW-aqJGZseA==/109951171843776354.jpg?param=130y130',
            'songurl': 'https://music.163.com/song/media/outer/url?id=64797.mp3',
            'name': '倒带人生',
            'author': '陈奕迅',
            'time': '4:38'
        }
    ]

    # 音乐切换函数
    def next_songs():
        st.session_state['song_ind'] = (st.session_state['song_ind'] + 1) % len(songs)

    def prev_songs():
        st.session_state['song_ind'] = (st.session_state['song_ind'] - 1) % len(songs)

    # 分列容器
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(songs[st.session_state['song_ind']]['imgurl'], caption="专辑封面")
    with c2:
        st.text(songs[st.session_state['song_ind']]['name'])
        st.text(songs[st.session_state['song_ind']]['author'])
        st.text(songs[st.session_state['song_ind']]['time'])
        # 按钮添加唯一key
        st.button('上一首', on_click=prev_songs, use_container_width=True, key='song_prev_btn')
        st.button('下一首', on_click=next_songs, use_container_width=True, key='song_next_btn')

    # 音频播放
    st.audio(songs[st.session_state['song_ind']]['songurl'])

# ---------------------- 选项卡5：视频播放 ----------------------
with tab5:
    st.header("这是第五个选项卡")
    st.markdown("#### 第五个选项卡的内容")

    # 初始化视频切换的独立状态
    if 'video_ind' not in st.session_state:
        st.session_state['video_ind'] = 0

    # 视频数据
    video_arr = [
        {
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '第一集',
            'nume': 1,
            'author': '课堂'
        },
        {
            'url': 'https://cn-gddg-ct-01-12.bilivideo.com/upgcxcode/69/94/34722089469/34722089469-1-192.mp4?e=ig8euxZM2rNcNbR3hWdVhwdlhW41hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=0000c10102932d9d4a7780738700f7ed5ceh&nbs=1&uipk=5&mid=0&deadline=1765766818&oi=1782024106&platform=html5&gen=playurlv3&os=bcache&og=hw&upsig=9978c7628b5a341ce5ed4d97829f99f6&uparams=e,trid,nbs,uipk,mid,deadline,oi,platform,gen,os,og&cdnid=61312&bvc=vod&nettype=0&bw=1450966&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
            'title': '第二集',
            'nume': 2,
            'author': 'NinthA'
        },
        {
            'url': 'https://cn-gdfs-ct-01-01.bilivideo.com/upgcxcode/85/62/34668416285/34668416285-1-192.mp4?e=ig8euxZM2rNcNbNznwdVhwdlhbh3hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=000017a8cc30d6104b49a4f6018b42bac81h&deadline=1765766953&nbs=1&oi=1782024106&gen=playurlv3&os=bcache&og=cos&uipk=5&mid=0&upsig=3cba4ca678273a49916d5a935a21c0b5&uparams=e,platform,trid,deadline,nbs,oi,gen,os,og,uipk,mid&cdnid=60901&bvc=vod&nettype=0&bw=1917651&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
            'title': '第三集',
            'nume': 3,
            'author': '爱丽速子LightSpeed'
        },
        {
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '第四集',
            'nume': 4,
            'author': '课堂'
        },
        {
            'url': 'https://cn-gddg-ct-01-12.bilivideo.com/upgcxcode/69/94/34722089469/34722089469-1-192.mp4?e=ig8euxZM2rNcNbR3hWdVhwdlhW41hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=0000c10102932d9d4a7780738700f7ed5ceh&nbs=1&uipk=5&mid=0&deadline=1765766818&oi=1782024106&platform=html5&gen=playurlv3&os=bcache&og=hw&upsig=9978c7628b5a341ce5ed4d97829f99f6&uparams=e,trid,nbs,uipk,mid,deadline,oi,platform,gen,os,og&cdnid=61312&bvc=vod&nettype=0&bw=1450966&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
            'title': '第五集',
            'nume': 5,
            'author': 'NinthA-'
        },
        {
            'url': 'https://cn-gdfs-ct-01-01.bilivideo.com/upgcxcode/85/62/34668416285/34668416285-1-192.mp4?e=ig8euxZM2rNcNbNznwdVhwdlhbh3hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=000017a8cc30d6104b49a4f6018b42bac81h&deadline=1765766953&nbs=1&oi=1782024106&gen=playurlv3&os=bcache&og=cos&uipk=5&mid=0&upsig=3cba4ca678273a49916d5a935a21c0b5&uparams=e,platform,trid,deadline,nbs,oi,gen,os,og,uipk,mid&cdnid=60901&bvc=vod&nettype=0&bw=1917651&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
            'title': '第六集',
            'nume': 6,
            'author': '爱丽速子LightSpeed'
        }
    ]

    # 视频切换函数
    def play(video_idx):
        st.session_state['video_ind'] = int(video_idx)

    # 显示视频
    st.subheader("展示视频")
    st.video(video_arr[st.session_state['video_ind']]['url'], autoplay=True)

    # 简介
    st.subheader("作者")
    st.text(video_arr[st.session_state['video_ind']]['author'])

    # 选择集数（按钮添加唯一key）
    st.subheader("选择集数")
    BUTTONS_PER_ROW = 3
    cols = st.columns(BUTTONS_PER_ROW)
    for idx, video in enumerate(video_arr):
        with cols[idx % BUTTONS_PER_ROW]:
            st.button(
                label=f"第{video['nume']}集",
                use_container_width=True,
                on_click=play,
                args=[idx],
                key=f"video_btn_{video['nume']}"  # 用集数做唯一key，更直观
            )
# ---------------------- 选项卡6：个人简历 ----------------------
with tab6:

    # ========== 左右分栏（严格压缩布局） ==========
    col_form, col_preview = st.columns([1, 2], gap="small")  # 缩小分栏间距

    with col_form:
        # 左侧：个人信息表单（压缩组件尺寸）
        st.header("个人信息表单")
        
        # 1. 基本信息字段（缩小输入框高度）
        st.text_input("姓名", key="name", help="", label_visibility="visible")
        st.text_input("昵称", key="nickname")
        st.text_input("求职岗位", key="job")
        st.text_input("电话", key="phone")
        st.text_input("邮箱", key="email")
        st.text_input("地址", key="address")
        st.text_input("身份证号码", key="id_card")
        st.text_input("政治面貌", key="politics")
        
        # 性别选择（紧凑排列）
        st.write("性别")
        gender_col = st.columns(3, gap="small")
        with gender_col[0]: st.radio("", ["男"], key="gender1", horizontal=True)
        with gender_col[1]: st.radio("", ["女"], key="gender2", horizontal=True)
        with gender_col[2]: st.radio("", ["其他"], key="gender3", horizontal=True)
        
        st.text_input("学历", key="edu")
        st.selectbox("毕业学校", ["请选择", "XXX大学"], key="school")
        st.selectbox("专业", ["请选择", "软件测试"], key="major")
        
        # 技能标签（紧凑按钮）
        st.write("技能")
        skill_col = st.columns(4, gap="small")
        with skill_col[0]: st.button("Java", key="skill1")
        with skill_col[1]: st.button("HTML/CSS", key="skill2")
        with skill_col[2]: st.button("计算机学习", key="skill3")
        with skill_col[3]: st.button("Python", key="skill4")
        
        # 滑块（缩小高度）
        st.write("工作年限（年）")
        work_years = st.slider("", 0, 10, 4, label_visibility="collapsed", key="work_years")
        st.write("期望薪资（元）")
        salary_range = st.slider("", 0, 50000, (3212, 23190), label_visibility="collapsed", key="salary")
        
        # 个人简介（缩小文本框高度）
        st.write("个人简介")
        intro = st.text_area("", height=80, label_visibility="collapsed", key="intro")
        
        # 上传头像（缩小区域）
        st.write("上传个人头像")
        avatar_file = st.file_uploader("", type=["jpg", "png"], label_visibility="collapsed", key="avatar")


    with col_preview:
        # 右侧：简历实时预览（紧凑布局）
        st.header("简历实时预览")
        
        # 顶部：姓名+右侧信息（缩小字体）
        preview_top_col = st.columns([2, 1], gap="small")
        with preview_top_col[0]:
            st.subheader(st.session_state.get("name", "陆紫光"))  # 关联输入框
        with preview_top_col[1]:
            st.markdown('<div class="small-text">性别：男</div>', unsafe_allow_html=True)
            st.markdown('<div class="small-text">期望：5年</div>', unsafe_allow_html=True)
            st.markdown('<div class="small-text">工作经验：1年</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="small-text">期望薪资：{salary_range[0]}-{salary_range[1]}元</div>', unsafe_allow_html=True)
            st.markdown('<div class="small-text">最高学历：高中/中专</div>', unsafe_allow_html=True)
            st.markdown('<div class="small-text">语言能力：中文 普通话</div>', unsafe_allow_html=True)
        
        # 头像+基本信息（缩小头像+字体）
        avatar_info_col = st.columns([1, 3], gap="small")
        with avatar_info_col[0]:
            if avatar_file:
                st.image(avatar_file, width=80)  # 缩小头像尺寸
            else:
                st.image("https://via.placeholder.com/80", width=80)
        with avatar_info_col[1]:
            st.markdown(f'<div class="small-text">职位：{st.session_state.get("job", "软件测试")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="small-text">电话：{st.session_state.get("phone", "13777835636")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="small-text">邮箱：{st.session_state.get("email", "23792111@qq.com")}</div>', unsafe_allow_html=True)
            st.markdown('<div class="small-text">出生日期：2005/06/07</div>', unsafe_allow_html=True)
        
        # 个人简介模块（用HTML设置小字体）
        st.write("### 个人简介")
        intro_text = intro if intro else "（请在左侧填写个人简介）"
        st.markdown(f'<div class="small-text">{intro_text}</div>', unsafe_allow_html=True)
        
        # 专业技能模块（紧凑列表+小字体）
        st.write("### 专业技能")
        skill_list = ["Java", "HTML/CSS", "计算机学习", "Python"]
        for skill in skill_list:
            st.markdown(f'<div class="small-text">- {skill}</div>', unsafe_allow_html=True)
        
        # 底部标语（超小字体）
        st.markdown('<div class="tiny-text">“有需要的时候来，但是别白来”</div>', unsafe_allow_html=True)
