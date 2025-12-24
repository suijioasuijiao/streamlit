import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder  

# ---------------------- 1. 基础配置 ----------------------
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="💯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 中文字体配置（解决乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11


# ---------------------- 2. 数据加载 ----------------------
@st.cache_data
def load_student_data():
    try:
        df = pd.read_csv('student_data_adjusted_rounded.csv', encoding='utf-8-sig')
    except:
        df = pd.read_csv('student_data_adjusted_rounded.csv', encoding='gbk')
    
    required_cols = ['专业', '性别', '每周学习时长（小时）', '期中考试分数', '期末考试分数', '上课出勤率', '作业完成率']
    for col in required_cols:
        if col not in df.columns:
            st.error(f"❌ 缺少必要列：{col}")
            st.stop()
    return df

df = load_student_data()

# 定义特征信息
TARGET_COL = '期末考试分数'
FEATURE_COLS = [col for col in df.columns if col not in ['学号', TARGET_COL] and df[col].dtype in [object, int, float]]
REAL_GENDERS = df['性别'].dropna().unique().tolist() if '性别' in FEATURE_COLS else []
REAL_MAJORS = df['专业'].dropna().unique().tolist() if '专业' in FEATURE_COLS else []


# ---------------------- 3. 模型加载 ----------------------
@st.cache_resource  
def load_model():
    try:
        with open('student_final_score_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except:
        st.error("未找到模型文件，请确保student_final_score_model.pkl存在")
        st.stop()


# ---------------------- 4. 特征编码 ----------------------
def encode_features(gender, major):
    # 性别编码：基于数据中真实性别列表
    gender_le = LabelEncoder()
    gender_le.fit(REAL_GENDERS)
    gender_code = gender_le.transform([gender])[0]
    
    # 专业编码：基于数据中真实专业列表
    major_le = LabelEncoder()
    major_le.fit(REAL_MAJORS)
    major_code = major_le.transform([major])[0]
    
    return gender_code, major_code


# ---------------------- 5. 侧边栏 ----------------------
with st.sidebar:
    st.title("📌 导航菜单")
    st.write("")
    nav_option = st.radio(
        label="",
        options=["项目介绍", "专业成绩分析", "成绩预测"],
        index=0,
        format_func=lambda x: f"• {x}"
    )
    st.write("---")
    st.subheader("专业成绩分析预览")
    st.write("• 各专业学习时长对比图")
    st.write("• 期中/期末成绩趋势图")
    st.write("• 专业出勤率排名")
    st.write("• 大数据管理专业专项分析")


# ---------------------- 6. 页面1：项目介绍页 ----------------------
def show_project_intro():
    st.title("🎓学生成绩分析与预测系统")
    st.write("---")

    # 项目概述
    st.header("📂 项目概述")
    st.write("本项目是一个基于Streamlit的学生成绩分析平台，通过该平台可优化老师教学方式，帮助教育工作者和学生深入了解学生表现，并预测期末考试成绩。")
    
    st.subheader("主要特点：")
    st.markdown("""
    - **📊 数据可视化：** 多维度展示学生学业数据
    - **🔍 专业分析：** 多维度分析的学科统计分析
    - **🤖 智能预测：** 基于机器学习模型的成绩预测
    - **💡 学习建议：** 根据预测结果提供个性化反馈
    """)

    st.write("---")

    # 项目目标
    st.header("🎯 项目目标")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("目标一：分析和调整")
        st.markdown("""
        - 识别关键学习指标
        - 探索成绩相关性
        - 提供态度改进决策
        """)
    with col2:
        st.subheader("目标二：可视化和跟踪")
        st.markdown("""
        - 专业对比分析
        - 追踪学习趋势
        - 学习情况识别
        """)
    with col3:
        st.subheader("目标三：成绩预测")
        st.markdown("""
        - 机器学习模型
        - 个性化预测
        - 及时干预预警
        """)

    st.write("---")

    # 技术架构
    st.header("🔧 技术架构")
    arch_col1, arch_col2, arch_col3, arch_col4 = st.columns(4)
    with arch_col1:
        st.subheader("前端框架")
        st.write("Streamlit")
    with arch_col2:
        st.subheader("数据处理")
        st.write("Pandas\nNumpy")
    with arch_col3:
        st.subheader("可视化")
        st.write("Plotly\nMatplotlib")
    with arch_col4:
        st.subheader("机器学习")
        st.write("Scikit-Learn")


# ---------------------- 7. 页面2：专业成绩分析页 ----------------------
def show_major_analysis():
    st.title("专业成绩分析")
    st.write("---")

    # 第1行：性别比例图表 + 数据表
    st.subheader("一、各专业男女性别比例分析")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        gender_count = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
        # 确保男女性别列存在
        if '男' not in gender_count.columns:
            gender_count['男'] = 0
        if '女' not in gender_count.columns:
            gender_count['女'] = 0
        gender_count = gender_count[['男', '女']]
        
        fig, ax = plt.subplots()
        bar_width = 0.35
        index = np.arange(len(gender_count.index))
        bar1 = ax.bar(index - bar_width/2, gender_count['男'], bar_width, label='男生', color='#3498db', alpha=0.8)
        bar2 = ax.bar(index + bar_width/2, gender_count['女'], bar_width, label='女生', color='#e74c3c', alpha=0.8)
        
        ax.set_xlabel('专业')
        ax.set_ylabel('学生人数')
        ax.set_title('各专业男女性别分布')
        ax.set_xticks(index)
        ax.set_xticklabels(gender_count.index, rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        # 添加数值标签
        for bar in bar1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{int(height)}', ha='center', va='bottom')
        for bar in bar2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        st.pyplot(fig)
    with col2:
        st.subheader("性别比例详细数据表")
        gender_detail = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
        # 确保男女性别列存在
        if '男' not in gender_detail.columns:
            gender_detail['男'] = 0
        if '女' not in gender_detail.columns:
            gender_detail['女'] = 0
        
        gender_detail['总人数'] = gender_detail['男'] + gender_detail['女']
        gender_detail['男生占比(%)'] = (gender_detail['男'] / gender_detail['总人数'] * 100).round(2)
        gender_detail['女生占比(%)'] = (gender_detail['女'] / gender_detail['总人数'] * 100).round(2)
        
        # 添加序号
        gender_detail_df = gender_detail.reset_index()
        gender_detail_df.insert(0, '序号', range(1, len(gender_detail_df)+1))
        st.dataframe(gender_detail_df, use_container_width=True, hide_index=True)

    st.write("---")

    # 第2行：学习指标图表 + 数据表
    st.subheader("二、各专业学习指标分析")
    col3, col4 = st.columns(2, gap="medium")
    with col3:
        st.subheader("期中期末成绩趋势图")
        score_data = df.groupby('专业').agg({
            '期中考试分数': 'mean',
            '期末考试分数': 'mean'
        }).round(2)
        
        fig, ax = plt.subplots()
        ax.plot(score_data.index, score_data['期中考试分数'], marker='o', linewidth=2, label='期中平均分', color='#2ecc71')
        ax.plot(score_data.index, score_data['期末考试分数'], marker='s', linewidth=2, label='期末平均分', color='#f39c12')
        
        ax.set_xlabel('专业')
        ax.set_ylabel('平均分数')
        ax.set_title('各专业期中期末成绩趋势')
        ax.set_xticklabels(score_data.index, rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 添加数值标签
        for i, (mid, final) in enumerate(zip(score_data['期中考试分数'], score_data['期末考试分数'])):
            ax.text(i, mid + 1, f'{mid}', ha='center', va='bottom', fontsize=10)
            ax.text(i, final + 1, f'{final}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig)
    with col4:
        st.subheader("学习指标详细数据表")
        study_detail = df.groupby('专业').agg({
            '每周学习时长（小时）': lambda x: round(x.mean(), 2),
            '期中考试分数': lambda x: round(x.mean(), 2),
            '期末考试分数': lambda x: round(x.mean(), 2)
        }).round(2)
        
        study_detail.columns = ['每周学习时长(小时)', '期中平均分', '期末平均分']
        # 添加序号
        study_detail_df = study_detail.reset_index()
        study_detail_df.insert(0, '序号', range(1, len(study_detail_df)+1))
        st.dataframe(study_detail_df, use_container_width=True, hide_index=True)

    st.write("---")

    # 第3行：出勤率分析图表 + 数据表
    st.subheader("三、各专业出勤率分析")
    col5, col6 = st.columns(2, gap="medium")
    with col5:
        st.subheader("各专业平均出勤率柱状图")
        attendance_data = (df.groupby('专业')['上课出勤率'].mean() * 100).round(2).sort_values(ascending=False)
        
        fig, ax = plt.subplots()
        bars = ax.bar(attendance_data.index, attendance_data.values, color='#9b59b6', alpha=0.8)
        
        ax.set_xlabel('专业')
        ax.set_ylabel('出勤率(%)')
        ax.set_title('各专业平均出勤率排名')
        ax.set_xticklabels(attendance_data.index, rotation=45, ha='right')
        ax.set_ylim(0, 100)
        ax.grid(axis='y', alpha=0.3)
        
        # 添加数值标签
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1, f'{height:.1f}%', ha='center', va='bottom')
        
        plt.tight_layout()
        st.pyplot(fig)
    with col6:
        st.subheader("出勤率排行数据表")
        attendance_detail = (df.groupby('专业')['上课出勤率'].mean() * 100).round(2).reset_index()
        attendance_detail.columns = ['专业', '平均出勤率(%)']
        # 按出勤率降序排序并添加排名
        attendance_detail = attendance_detail.sort_values(by='平均出勤率(%)', ascending=False)
        attendance_detail.insert(0, '排名', range(1, len(attendance_detail)+1))
        
        st.dataframe(attendance_detail, use_container_width=True, hide_index=True)

    st.write("---")

    # 第4行：大数据管理专业专项分析
    st.subheader("四、大数据管理专业专项分析")
    col7 = st.columns(1)[0]
    with col7:
        # 筛选大数据专业数据
        bigdata_df = df[df['专业'] == '大数据管理'].copy()
        if len(bigdata_df) == 0:
            st.warning("⚠️ 未找到'大数据管理'专业，展示所有专业数据替代")
            bigdata_df = df.copy()
            target_major = "所有专业"
        else:
            target_major = "大数据管理专业"
        
        # 核心指标卡片展示
        col7_1, col7_2, col7_3 = st.columns(3)
        with col7_1:
            st.info(f"**分析对象**\n{target_major}")
            st.info(f"**学生总数**\n{len(bigdata_df)} 人")
        with col7_2:
            avg_study_hour = bigdata_df['每周学习时长（小时）'].mean().round(2)
            avg_attendance = (bigdata_df['上课出勤率'].mean() * 100).round(2)
            st.success(f"**每周平均学习时长**\n{avg_study_hour} 小时")
            st.success(f"**平均出勤率**\n{avg_attendance}%")
        with col7_3:
            avg_final_score = bigdata_df['期末考试分数'].mean().round(2)
            min_final_score = bigdata_df['期末考试分数'].min()
            max_final_score = bigdata_df['期末考试分数'].max()
            st.warning(f"**期末平均分**\n{avg_final_score} 分")
            st.warning(f"**期末分数范围**\n{min_final_score} - {max_final_score} 分")
        
        st.write("---")
        
        # 散点图：学习时长与期末成绩关系
        fig, ax = plt.subplots(figsize=(12, 6))
        scatter = ax.scatter(
            bigdata_df['每周学习时长（小时）'],
            bigdata_df['期末考试分数'],
            c=bigdata_df['期末考试分数'],
            cmap='viridis',
            alpha=0.7,
            s=60
        )
        
        # 添加趋势线
        z = np.polyfit(bigdata_df['每周学习时长（小时）'], bigdata_df['期末考试分数'], 1)
        p = np.poly1d(z)
        ax.plot(bigdata_df['每周学习时长（小时）'], p(bigdata_df['每周学习时长（小时）']), 
                "r--", linewidth=2, label=f'趋势线（y={z[0]:.2f}x+{z[1]:.2f}）')
        
        # 图表美化
        ax.set_xlabel('每周学习时长（小时）', fontsize=11)
        ax.set_ylabel('期末考试分数', fontsize=11)
        ax.set_title(f'{target_major}：每周学习时长与期末考试成绩关系', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()
        plt.colorbar(scatter, label='期末考试分数')
        
        plt.tight_layout()
        st.pyplot(fig)


# ---------------------- 8. 页面3：成绩预测页（完善版） ----------------------
def show_score_prediction():
    st.title("成绩预测")
    st.write("---")
    st.markdown(f"基于真实学生数据（共{len(df)}条记录），特征自动匹配数据")
    st.markdown("---")
    
    # 加载模型
    model = load_model()
    
    # 分栏布局
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.subheader("学生信息输入")
        # 1. 学号（仅标识）
        student_id = st.text_input("学号", value="2024001")
        
        # 2. 类别特征输入（适配真实数据中的性别、专业）
        gender = st.selectbox("性别", options=REAL_GENDERS) if '性别' in FEATURE_COLS else st.text_input("性别", value="男")
        major = st.selectbox("专业", options=REAL_MAJORS) if '专业' in FEATURE_COLS else st.text_input("专业", value="信息系统")
        
        # 3. 数值特征输入（基于数据真实范围，自动适配）
        st.markdown("#### 学习特征")
        # 每周学习时长
        study_hours_min = int(df['每周学习时长（小时）'].min()) if '每周学习时长（小时）' in FEATURE_COLS else 0
        study_hours_max = int(df['每周学习时长（小时）'].max()) if '每周学习时长（小时）' in FEATURE_COLS else 50
        study_hours = st.slider("每周学习时长（小时）", min_value=study_hours_min, max_value=study_hours_max, value=int((study_hours_min+study_hours_max)/2))
        
        # 上课出勤率
        attendance_min = round(df['上课出勤率'].min(), 2) if '上课出勤率' in FEATURE_COLS else 0.0
        attendance_max = round(df['上课出勤率'].max(), 2) if '上课出勤率' in FEATURE_COLS else 1.0
        attendance = st.slider("上课出勤率", min_value=attendance_min, max_value=attendance_max, value=round((attendance_min+attendance_max)/2, 2), step=0.01)
        
        # 期中考试分数
        midterm_min = int(df['期中考试分数'].min()) if '期中考试分数' in FEATURE_COLS else 0
        midterm_max = int(df['期中考试分数'].max()) if '期中考试分数' in FEATURE_COLS else 100
        midterm_score = st.slider("期中考试分数", min_value=midterm_min, max_value=midterm_max, value=int((midterm_min+midterm_max)/2))
        
        # 作业完成率
        homework_min = round(df['作业完成率'].min(), 2) if '作业完成率' in FEATURE_COLS else 0.0
        homework_max = round(df['作业完成率'].max(), 2) if '作业完成率' in FEATURE_COLS else 1.0
        homework_rate = st.slider("作业完成率", min_value=homework_min, max_value=homework_max, value=round((homework_min+homework_max)/2, 2), step=0.01)
    
        # 预测按钮
        predict_btn = st.button("预测期末成绩", type="primary")
    
    with col2:
        st.subheader("预测结果")
        if predict_btn:
            # 编码特征
            gender_code, major_code = encode_features(gender, major)
            
            # 构造特征数据
            features = pd.DataFrame({
                "性别": [gender_code],
                "专业": [major_code],
                "每周学习时长（小时）": [study_hours],
                "上课出勤率": [attendance],
                "期中考试分数": [midterm_score],
                "作业完成率": [homework_rate]
            })
            
            # 模型预测
            final_score = model.predict(features)[0]
            final_score = round(final_score, 1)
            
            # 展示结果
            st.success(f"预测期末成绩：{final_score} 分")
            # 根据成绩展示对应图片
            if final_score >= 80:
                st.image("images/优秀.jpg", width=300)
            elif 60 <= final_score < 80:
                st.image("images/恭喜.jpg", width=300)
            else:
                st.image("images/鼓励.jpg", width=300)
            
            st.markdown("---")
            st.subheader("学习建议")
            if final_score >= 80:
                st.markdown("🎉 成绩优秀！建议保持当前的学习节奏，可适当拓展学科相关的实践项目。")
            elif 60 <= final_score < 80:
                st.markdown(f"📖 成绩良好！建议增加每周学习时长（当前：{study_hours}小时），提高作业完成质量。")
            else:
                st.markdown(f"⚠️ 成绩待提升！建议提高上课出勤率（当前：{attendance}），加强期中考试相关知识点的复习。")
        else:
            st.info("请点击左侧的「预测期末成绩」按钮获取结果")


# ---------------------- 9. 导航逻辑 ----------------------
if nav_option == "项目介绍":
    show_project_intro()
elif nav_option == "专业成绩分析":
    show_major_analysis()
elif nav_option == "成绩预测":
    show_score_prediction()