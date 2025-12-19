import streamlit as st
import  pickle
import pandas as pd


def introduce_page():
    """当选择简介页面时，将呈现该函数的内容"""
    st.write("# 欢迎使用！")
    st.sidebar.success("单击 预测医疗费用")

    st.markdown(
        """
        #医疗费用预测应用
        """
        )
    
def predict_page():
    
    """当选择预测费用页面时，将呈现该函数的内容"""

    st.markdown("""
    
    """)

    #运用表单和表单提交按键
    with st.form('user_inputs'):
        age=st.number_input('年龄',min_value=0)
        sex=st.radio('性别',options=['男性','女性'])
        bmi=st.number_input('BMI',min_value=0.0)

        children=st.number_input("子女数量:,",step=1,min_value=0)
        
        smoke=st.radio('是否吸烟',('是','否'))
        region=st.selectbox('区域',('东南部','西南部','东北部','西北部'))
        submitted=st.form_submit_button('预测费用')

    if submitted:
        format_data=[age,sex,bmi,children,smoke,region]
        st.write("用户输入的数据是：")
        st.text(format_data)

        #初始化数据预处理格式中与岛屿相关的变量
        sex_formale,sex_male=0,0
        #根据用户输入的性别数据更改对应的值
        if sex == '女性':
            sex_formale=1
        elif sex == '男性':
            sex_male=1

        smoke_yes,smoke_no=0,0
        #根据用户输入的吸烟数据更改对应的值
        if smoke == '是':
            smoke_yes=1
        elif smoke == '否':
            smoke_no=1

        region_northeast,region_southeast,region_northwest,region_southwest=0,0,0,0

        #根据用户输入的岛屿数据更改对应的值
        if region == '东北部':
            region_northeast=1
        elif region == '东南部':
            region_southeast=1
        elif region == '西北部':
            region_northwest=1
        elif region == '西南部':
            region_southwest=1

        st.write('转换为数据预处理形式：')
        format_data=[age,bmi,children,sex_formale,sex_male,smoke_yes,smoke_no,
                     region_northeast,region_southeast,region_northwest,region_southwest
                     ]
        st.text(format_data)


    #使用pickle的load方法加载之前的回归模型
    with open('rfr_model.pkl','rb') as f:
        rfr_model=pickle.load(f)

    if submitted:
        format_data_df=pd.DataFrame(data=[format_data],columns=rfr_model.feature_names_in_)

        #使用模型对格式化后的数据format_data进行预测，返回预测的医疗费用
        predict_result=rfr_model.predict(format_data_df)[0]

        st.write('根据你输入的数据，预测该用户的医疗费用是：',round(predict_result,2))

st.write("技术支持0")
st.set_page_config(
    page_title="医疗费用预测",
    #page_icon="",
    )
#在左侧添加侧边栏并设置单选按键
nav=st.sidebar.radio("导航",["简介","预测医疗费用"])
#根据选择结果，展示不同的页面
if nav == '简介':
    introduce_page()
else :
    predict_page()
    
