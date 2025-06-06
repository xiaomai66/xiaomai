import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '月份':['01月', '02月', '03月'],
    '1号门店':[200, 150, 180],
    '2号门店':[120, 160, 123],
    '3号门店':[110, 100, 160],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("门店数据")
# 使用write()方法展示数据框
st.write(df)
st.header("条形图")

st.subheader("设置x参数")
# 通过x指定月份所在这一列为条形图的x轴
st.bar_chart(df, x='月份')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)

st.subheader("设置y参数")
# 通过y参数筛选只显示1号门店的数据
st.bar_chart(df, y='1号门店')
# 通过y参数筛选只显示2、3号门店的数据
st.bar_chart(df, y=['2号门店','3号门店'])

st.subheader("设置width、height和use_container_width参数")
# 通过width、height和use_container_width指定条形图的宽度和高度
st.bar_chart(df, width=400, height=300, use_container_width=False)
