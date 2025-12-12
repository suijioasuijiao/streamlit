import streamlit as st
import pandas as pd


#标题
st.title("南宁美食探索")
st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

#地图
st.header("南宁美食地图")
data_map={
    'latitude':[22.854169,22.853700,22.854323,22.854708,22.854565],
    'longitude':[108.223035,108.222531,108.222751,108.223867,108.222917]
}
df=pd.DataFrame(data_map)
st.map(df,size=1)
       
# 定义数据,以便创建数据框
data = {

    '价格':[20, 26, 23,35,25],
    '高峰时期':[11, 12, 13, 14, 10],
    '评分': ['9.8', '8.6', '8.5', '9.6', '7.3'],  # 注意第三个值有前导空格
}
#新建索引
ind= pd.Series(['沪上阿姨','华莱士汉堡','蓝师傅柳州螺蛳粉','横县鱼生','燕姐钦州老牌猪脚粉'],name='店家')

df=pd.DataFrame(data,index=ind)

#图表
st.dataframe(df)

#折线图
st.line_chart(df,y='价格')

#面积图 高峰时期
st.area_chart(df,y='高峰时期')

#条形图 通过y参数筛选只显示评分的数据
# 1. 构造DataFrame
df = pd.DataFrame(data)

# 数据清洗： 转换为浮点数（核心步骤）
df['评分'] = df['评分'].astype(float)  # 转换为数值类型

# 3. 绘制条形图（可选：指定x轴为高峰时期，让条形更有意义）
st.bar_chart(df, x='高峰时期', y='评分')  # 显式指定x轴，默认x是索引也可



# 通过y参数筛选只显示2、3号门店的数据
#st.bar_chart(df, y=['2号门店','3号门店'])
