import streamlit as st 
import pickle 
import pandas as pd 

# 设置页面的标题、图标和布局
st.set_page_config(
    page_title="企鹅分类器",  # 页面标题
    page_icon=":penguin:",    # 页面图标
    layout='wide'
)

# 提前定义英文→中文映射（适配图片命名）
EN_TO_CN = {
    "ADELIE": "阿德利企鹅",
    "CHINSTRAP": "帽带企鹅",
    "GENTOO": "巴布亚企鹅",
    "Adelie": "阿德利企鹅",  # 兼容小写/首字母大写情况
    "Chinstrap": "帽带企鹅",
    "Gentoo": "巴布亚企鹅"
}

# 使用侧边栏实现多页面显示效果
with st.sidebar:
    # 侧边栏logo增加异常处理
    try:
        st.image('images/rigth_logo.png', width=100)
    except:
        st.write("侧边栏logo缺失")
    st.title('请选择页面')
    page = st.selectbox(
        "请选择页面",
        ["简介页面","预测分类页面"],
        label_visibility='collapsed'
    )

if page == "简介页面":
    st.title("企鹅分类器：penguin:")
    st.header('数据集介绍')

    st.markdown("""帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，
也可以作为机器学习入门练习。
以对南极企鹅种类进行分类和研究。
该数据集是由 Gorman 等收集，并发布在一个名为 palmerpenguins 的 R 语言包，
该数据集记录了344行观测数据，包含3个不同物种的企鹅：阿德利企鹅、巴布亚企
鹅和帽带企鹅的各种信息。""")

    st.header('三种企鹅的卡通图像')
    # 简介页图片增加异常处理
    try:
        st.image('images/penguins_all.png')
    except:
        st.warning("未找到企鹅汇总图片：images/penguins_all.png")

elif page == "预测分类页面":
    st.header("预测企鹅分类")
    st.markdown("这个 Web 应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入6个信息，就可以预测企鹅的物种，使用下面的表单开始预测吧！")

    # 该页面是3:1:2的列布局
    col_form, col, col_logo = st.columns([3,1,2])
    
    with col_form:
        # 运用表单和表单提交按钮
        with st.form('user_inputs'):
            island = st.selectbox('企鹅栖息的岛屿', options=['托尔森岛','比斯科群岛','德里姆岛'])
            sex = st.selectbox('性别', options=['雄性','雌性'])
            bill_length = st.number_input('喙长度', min_value=0.0)
            bill_depth = st.number_input('喙深度', min_value=0.0)
            flipper_length = st.number_input('鳍肢长度', min_value=0.0)
            body_mass = st.number_input('体重', min_value=0.0)
            submitted = st.form_submit_button('提交')
        
        # 初始化数据预处理格式中与岛屿相关的变量
        island_biscoe, island_dream, island_torgerson = 0, 0, 0
        # 根据用户输入的岛屿数据更改对应的值
        if island == '比斯科群岛':
            island_biscoe = 1
        elif island == '德里姆岛':
            island_dream = 1
        elif island == '托尔森岛':
            island_torgerson = 1
        
        # 初始化数据预处理格式中与性别相关的变量
        sex_female, sex_male = 0, 0
        # 根据用户输入的性别数据更改对应的值
        if sex == '雌性':
            sex_female = 1
        elif sex == '雄性':
            sex_male = 1
        
        # 整理预测数据
        format_data = [bill_length, bill_depth, flipper_length, body_mass, 
                      island_dream, island_torgerson, island_biscoe, sex_male, sex_female]
        
        # 加载模型增加全局异常捕获
        try:
            # 加载随机森林模型
            with open('rfc_model.pkl','rb') as f:
                rfc_model = pickle.load(f)

            # 加载类别映射对象
            with open('output_uniques.pkl','rb') as f:
                output_uniques_map = pickle.load(f)
        except Exception as e:
            st.error(f"模型加载失败：{str(e)}")
            submitted = False  # 避免后续执行预测逻辑
        
        # 表单提交后执行预测
        if submitted:
            try:
                # 构造模型输入的DataFrame
                format_data_df = pd.DataFrame(
                    data=[format_data], 
                    columns=rfc_model.feature_names_in_
                )
                # 模型预测
                predict_result_code = rfc_model.predict(format_data_df)
                
                # 核心修复：提取numpy数组中的第一个元素（解决不可哈希问题）
                predict_result_code = predict_result_code[0]
                
                # 映射到具体物种名称（英文）
                predict_result_species_en = output_uniques_map[predict_result_code]
                # 转换为中文（适配图片命名）
                predict_result_species = EN_TO_CN.get(predict_result_species_en.upper(), predict_result_species_en)
                
                # 显示预测结果
                st.success(f'根据您输入的数据，预测该企鹅的物种名称是：**{predict_result_species}**')
            except Exception as e:
                st.error(f"预测失败：{str(e)}")
                predict_result_species = None
    
    # 右侧logo列 - 完整的异常兜底
    with col_logo:
        # 统一logo路径（避免拼写错误：rigth→right，可选修改）
        default_logo_path = 'images/rigth_logo.png'
        if not submitted:
            try:
                st.image(default_logo_path, width=300)
            except:
                st.info(f"默认logo缺失：{default_logo_path}")
        else:
            if predict_result_species:
                # 优先尝试中文名称图片
                img_path = f'images/{predict_result_species}.png'
                try:
                    st.image(img_path, width=300)
                except:
                    # 备用：尝试英文名称图片
                    en_name = [k for k, v in EN_TO_CN.items() if v == predict_result_species]
                    if en_name:
                        img_path_en = f'images/{en_name[0]}.png'
                        try:
                            st.image(img_path_en, width=300)
                        except:
                            st.image(default_logo_path, width=300)
                            st.warning(f"物种图片缺失：\n中文路径：{img_path}\n英文路径：{img_path_en}")
                    else:
                        st.image(default_logo_path, width=300)
                        st.warning(f"物种图片缺失：{img_path}")
            else:
                try:
                    st.image(default_logo_path, width=300)
                except:
                    st.info(f"默认logo缺失：{default_logo_path}")
