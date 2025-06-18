import streamlit as st
import pandas as pd
import plotly.express as px

def get_dataframe_from_excel(file_path):
    """从Excel文件读取数据并返回DataFrame"""
    try:
        df = pd.read_excel(
            file_path,
            sheet_name='销售数据',
            skiprows=1,
            index_col='订单号'
        )
        df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
        return df
    except FileNotFoundError:
        st.error(f"文件未找到: {file_path}")
        return pd.DataFrame()  # 返回空DataFrame
    except Exception as e:
        st.error(f"读取文件时出错: {str(e)}")
        return pd.DataFrame()

def add_sidebar_func(df):
    """添加侧边栏筛选功能并返回筛选后的数据"""
    with st.sidebar:
        st.header("请筛选数据：")
        
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "请选择城市：",
            options=city_unique,
            default=city_unique,
        )

        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,
            default=customer_type_unique,
        )

        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            "请选择性别：",
            options=gender_unique,
            default=gender_unique,
        )

        df_selection = df.query(
            "城市 == @city & 顾客类型 == @customer_type & 性别 == @gender"
        )
    return df_selection

def product_line_chart(df):
    """生成按产品类型划分的销售额图表"""
    sales_by_product_line = df.groupby(by=["产品类型"])[["总价"]].sum().sort_values(by="总价")
    
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
    )
    return fig_product_sales

def hour_chart(df):
    """生成按小时划分的销售额图表"""
    sales_by_hour = df.groupby(by=["小时数"])[["总价"]].sum()
    
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
    )
    return fig_hour_sales

def main_page_demo(df):
    """主界面展示函数"""
    st.title(':bar_chart:销售仪表板')
    
    left_key_col, middle_key_col, right_key_col = st.columns(3)
    
    total_sales = int(df["总价"].sum())
    average_rating = round(df["评分"].mean(), 1)
    star_rating_string = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df["总价"].mean(), 2)
    
    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f"RMB ￥ {total_sales:,}")
        
    with middle_key_col:
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating_string}")
        
    with right_key_col:
        st.subheader("每单的平均销售额：")
        st.subheader(f"RMB ￥ {average_sale_by_transaction}")
    
    st.divider()
    
    left_chart_col, right_chart_col = st.columns(2)
    
    with left_chart_col:
        hour_fig = hour_chart(df)
        st.plotly_chart(hour_fig, use_container_width=True)
        
    with right_chart_col:
        product_fig = product_line_chart(df)
        st.plotly_chart(product_fig, use_container_width=True)

def run_app():
    """启动应用"""
    st.set_page_config(
        page_title="销售仪表板",
        page_icon=":bar_chart:",
        layout="wide"
    )
    
    # 指定文件路径
    file_path = r'C:\Users\Lenovo\Desktop\supermarket_sales.xlsm'
    
    # 读取数据
    sale_df = get_dataframe_from_excel(file_path)
    
    if not sale_df.empty:
        # 添加侧边栏筛选
        df_selection = add_sidebar_func(sale_df)
        
        # 显示主界面
        main_page_demo(df_selection)

# 运行应用
if __name__ == "__main__":
    run_app()
