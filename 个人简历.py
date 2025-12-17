import streamlit as st

# 页面设置：黑色背景+宽屏+隐藏默认样式
st.set_page_config(page_title="个人简历生成器", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    /* 全局样式：黑色背景+白色文字+清除内边距 */
    .stApp {
        background-color: #1E1E1E; 
        color: #FFFFFF; 
        padding: 0 !important;
        margin: 0 !important;
    }
    /* 清除页面默认间距 */
    .main .block-container {
        padding: 1rem 2rem !important;
        max-width: 100% !important;
    }
    /* 所有文本元素强制白色 */
    * {
        color: #FFFFFF !important;
        font-family: "微软雅黑", sans-serif !important;
    }
    /* 输入框/下拉框样式（深色背景+白色文字） */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stNumberInput>div>div>input, 
    .stSlider>div>div,
    .stTextArea>div>div>textarea {
        background-color: #333333 !important; 
        color: #FFFFFF !important; 
        border: none !important;
        font-size: 0.9rem !important;
    }
    /* 按钮样式（红色背景+白色文字） */
    .stButton>button {
        background-color: #E53935 !important; 
        color: #FFFFFF !important; 
        border: none !important;
        font-size: 0.8rem !important;
        padding: 0.3rem 0.8rem !important;
    }
    /* 标题样式（缩小间距） */
    h1, h2, h3, h4, h5, h6 {
        margin: 0.3rem 0 !important;
        padding: 0 !important;
        font-size: 1.2rem !important;
    }
    /* 单选按钮/滑块样式（适配白色文字） */
    .stRadio>div>label, .stSlider>label {
        font-size: 0.9rem !important;
    }
    /* 预览区右侧信息块（右对齐） */
    .preview-right {
        text-align: right !important;
        font-size: 0.85rem !important;
    }
    /* 压缩组件间距 */
    .stTextInput, .stSelectbox, .stNumberInput, .stSlider, .stTextArea, .stFileUploader {
        margin-bottom: 0.5rem !important;
    }
    /* 自定义小字体样式 */
    .small-text {
        font-size: 0.9rem !important;
        margin: 0.2rem 0 !important;
    }
    .tiny-text {
        font-size: 0.85rem !important;
        margin: 0.2rem 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

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
