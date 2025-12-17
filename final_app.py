import streamlit as st
import pandas as pd
import plotly.express as px

#设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width',True)
st.set_page_config(page_title="超市销售分析", page_icon="🛒", layout="wide")

# 此函数用于读取Excel文件的数据
def get_dateframe_from_excel():                 
    df = pd.read_excel(
        'supermarket_sales.xlsx',  # 表示Excel文件的路径
        sheet_name='销售数据',
        skiprows=1,                # 跳过第一行
        index_col='订单号'         # 作为索引
    )
    df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    return df

#创建侧边栏
def add_sidebar_func(df):
    with st.sidebar:
        st.header('请筛选数据：')
        #筛选城市
        city_unique=df['城市'].unique()
        city=st.multiselect(
            "请选择城市：",
            options=city_unique,
            default=city_unique,
            )
        #筛选顾客
        customer_type_unique=df['顾客类型'].unique()
        customer_type=st.multiselect(
            "请选择顾客类型:",
            options=customer_type_unique,
            default=customer_type_unique,
            )
        #筛选性别
        gender_unique=df['性别'].unique()
        gender=st.multiselect(
            "请选择性别：",
            options=gender_unique,
            default=gender_unique,
            )

        df_selection=df.query(
            "城市==@city&顾客类型==@customer_type&性别==@gender"
            )
        return df_selection

#创建可视化横向条形图
def product_line_chart(df):
    sales_by_product_line = (
        df.groupby(by=['产品类型'])[['总价']].sum().sort_values(by="总价").reset_index() 
    )
    
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y="产品类型",
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
    )
    return fig_product_sales

#创建可视化纵向条形图
def hour_chart(df):
    sales_by_hour = (
        df.groupby(by=['小时数'])[['总价']].sum()
    )
    
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
    )
    return fig_hour_sales

# 修正：添加df_selection参数
def main_page_demo(df_selection):
    """主界面函数"""
    #设置标题
    st.title('销售仪表板')
    #创建关键指标信息区，生成3个列容器
    left_key_col,middle_key_col,right_key_col=st.columns(3)

    total_sales=int(df_selection["总价"].sum())
    average_rating=round(df_selection["评分"].mean(),1)
    star_rating_string=":star:"*int(round(average_rating,0))
    average_sale_by_transaction=round(df_selection['总价'].mean(),2)
    
    with left_key_col:
        st.subheader("总销售额：")
        # 修正：移除多余的$
        st.subheader(f"RMB：{total_sales:,}")
        
    with middle_key_col:
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating}\n{star_rating_string}")
        
    with right_key_col:
        st.subheader("每单的平均销售额：")
        # 修正：移除多余的$
        st.subheader(f"RMB：{average_sale_by_transaction}")

    st.divider()#生成一个水平分割线

    #创建图表信息区，生成两个列容器
    left_chart_col,right_chart_col=st.columns(2)
    
    with left_chart_col:
        st.subheader("图表1")
        st.markdown("具体信息图表1")
        # 修正：变量改为df_selection
        hour_fig=hour_chart(df_selection)
        st.plotly_chart(hour_fig,use_container_width=True)
        
    # 修正：改为right_chart_col
    with right_chart_col:
        st.subheader("图表2")
        st.markdown("具体信息图表2")
        # 修正：调用正确的函数+变量改为df_selection
        product_fig=product_line_chart(df_selection)
        st.plotly_chart(product_fig,use_container_width=True)

# 修正：移出嵌套，放到全局作用域
def run_app():
    """启动应用"""
    # 修正：删除重复的st.set_page_config
    sale_df=get_dateframe_from_excel()
    #调用筛选区函数
    df_selection=add_sidebar_func(sale_df)
    #调用主页面函数
    main_page_demo(df_selection)

# 修正：移到全局作用域，作为程序入口
if __name__=="__main__":
    run_app()
