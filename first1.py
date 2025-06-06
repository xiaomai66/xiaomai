import streamlit as st
import pandas as pd
import numpy as np

# 生成北京市的随机点，其中39.9, 116.4是北京的经纬度
# 首先使用np.random.randn()方法生成1000行2列的符合正态分布的随机点
# 然后在第一列上除以20进行缩小，在第二列上除以50进行缩小
# 最后加上北京市的经纬度。
df = pd.DataFrame(
    np.random.randn(10, 2) / [20, 50] + [22.833840,108.313444],
    columns=['latitude', 'longitude'])
# 设置索引列的名称
df.index.name='序号'

st.subheader('南宁地图')
st.map(df)

st.title('⭐餐厅评分')
# 定义数据,以便创建数据框
data = {
    '门店':['门店1', '门店2', '门店3'],
    '评分':[4.8, 4.5, 4.7],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为条形图的x轴
df_indexed = df.set_index('门店')
st.bar_chart(df_indexed)

st.title('💰不同类型餐厅价格')
# 定义数据,以便创建数据框
data = {
    '餐厅类型':['西餐', '快餐', '日料','火锅'],
    '门店':[20000, 15000, 18000, 99999]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为折线图的x轴
df_indexed = df.set_index('餐厅类型')
st.line_chart(df_indexed)

st.title('🍲用餐高分时段')
# 定义数据,以便创建数据框
data = {
    '时间':['11', '12', '13'],
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

# 通过x指定月份所在这一列为面积图的x轴
df_indexed = df.set_index('时间')
st.area_chart(df_indexed)

st.title('🍽餐厅详情')
with st.expander("好友缘"):
    st.markdown("**注定孤独**")
    st.button("点我点我！！！")
c1, c2= st.columns(2)
c1.markdown('## 好友缘')
c1.markdown('##### 评分')
c1.markdown('# 4.7/5.0')
c1.markdown('#### 人均消费')
c1.markdown('# 3500元')

c2.markdown('**推荐菜品：**')
c2.markdown(' • &#8194;特色套餐')
c2.markdown(' • &#8194;地方小吃')
c2.markdown(' • &#8194;时令蔬菜')


st.subheader('当前拥挤程度')
st.progress(99,text="99%拥挤")


st.title('😍今日午餐推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)
if st.button('点击推荐'):
    st.write('按钮被点击了！')
st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px; background-color:green;'>今日推荐：星艺会七姐螺蛳粉（晚餐）</span>", unsafe_allow_html=True)
# 图片（需在线URL）
st.markdown("![图片](https://ts1.tc.mm.bing.net/th/id/R-C.21d7634b1056afcd04c91f7c86ed7412?rik=LCzkuiIgX%2fIjbQ&riu=http%3a%2f%2fupload.rmlt.com.cn%2f2020%2f1203%2f1606965514840.jpeg&ehk=v1cLqusMPUvjlYjx9Ex%2fwvgGFfG5MUqKk%2fTy%2ff5aEpw%3d&risl=&pid=ImgRaw&r=0)")
# # 超链接
# st.markdown("[Streamlit官网](https://streamlit.io)")

# st.markdown("# 一级标题 (h1)")
# st.markdown("## 二级标题 (h2)")
# st.markdown("### 三级标题 (h3)")
# st.markdown("#### 四级标题 (h4)")
# st.markdown("普通段落文本")

# st.markdown("**粗体文本**")
# st.markdown("*斜体文本*")
# st.markdown("***粗斜体文本***")
# st.markdown("~~删除线文本~~")
# st.markdown("`内联代码样式`")

# # 使用命名颜色
# st.markdown("<span style='color:red;'>红色文本</span>", unsafe_allow_html=True)

# # 使用十六进制颜色
# st.markdown("<span style='color:#3366cc;'>蓝色文本 (#3366cc)</span>", unsafe_allow_html=True)

# # 使用RGB颜色
# st.markdown("<span style='color:rgb(50, 168, 82);'>绿色文本 (rgb(50, 168, 82))</span>", unsafe_allow_html=True)

# # 使用RGBA带透明度
# st.markdown("<span style='color:rgba(255, 165, 0, 0.7);'>半透明橙色</span>", unsafe_allow_html=True)

# # 使用固定大小（像素）
# st.markdown("<p style='font-size:24px;'>24像素大小</p>", unsafe_allow_html=True)

# # 使用相对大小（em）
# st.markdown("<p style='font-size:1.5em;'>1.5em大小（相对于父元素）</p>", unsafe_allow_html=True)

# # 使用百分比
# st.markdown("<p style='font-size:150%;'>150%大小</p>", unsafe_allow_html=True)

# # 使用视口单位（响应式）
# st.markdown("<p style='font-size:3vw;'>响应式文本（3%视口宽度）</p>", unsafe_allow_html=True)

# # 下划线和上划线
# st.markdown("<p style='text-decoration:underline;'>带下划线文本</p>", unsafe_allow_html=True)
# st.markdown("<p style='text-decoration:overline;'>带上划线文本</p>", unsafe_allow_html=True)
# st.markdown("<p style='text-decoration:line-through;'>带删除线文本</p>", unsafe_allow_html=True)

# # 文本大小写
# st.markdown("<p style='text-transform:uppercase;'>全部大写文本</p>", unsafe_allow_html=True)
# st.markdown("<p style='text-transform:lowercase;'>全部小写文本</p>", unsafe_allow_html=True)
# st.markdown("<p style='text-transform:capitalize;'>每个单词首字母大写</p>", un
