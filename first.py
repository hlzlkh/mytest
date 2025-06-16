import streamlit as st

c1,c2=st.columns([1 ,2])
with c1:
    st.subheader("个人信息表单")
    st.markdown('***')
    name = st.text_input('姓名')
    zhiwei = st.text_input('职位')
    dianhua = st.text_input('电话')
    youxiang = st.text_input('邮箱')
    csrq = st.date_input("出生日期", value=None)
    xb = st.radio('性别',['男', '女','其他'],horizontal=True)
    def my_format_func(option):
        return f'{option}'
    st.subheader('学历')
    xueli = st.selectbox('选择你的学历：', ['高中', '专科', '本科','硕士','博士'], format_func=my_format_func, index=2)
    st.subheader('语言能力')
    yuyannl = st.multiselect(
    'choose an option：',
    ['中文', '英文', '日语','法语','德语','西班牙语'],
    format_func=my_format_func,
    )
    st.subheader('技能（可多选）')
    jn = st.multiselect(
    'choose an option：',
    ['Python', 'Java', 'JavaScript','HTML/CSS','SQL','数据分析','机器学习','深度学习','项目管理','UI/UX设计'],
    format_func=my_format_func,
    )
    from datetime import datetime, time
    st.subheader("工作经验")
    age = st.slider('单位（年）', 0, 30, 25)
    values = st.slider(
    '选择一组范围',
    5000.0, 50000.0, (5000.0, 10000.0))
    grjl = st.text_area('个人介绍', placeholder='请简要介绍你的专业背景，职业目标和个人特点')
    
    
with c2:
    st.subheader("简历实时预览")
    st.markdown('***')
    c1,c2=st.columns([1 ,2])
    with c1:
        st.write(f"***职位***：{zhiwei}")
        st.write(f"***电话***：{dianhua}")
        st.write(f"***邮箱***：{youxiang}")
        st.write(f"***出生日期***：{csrq}")
    with c2:
        st.write(f"***性别***：{xb}")
        st.write(f"***学历***：{xueli}")
        st.write(f"***工作经验***：{age}")
        st.write(f"***期望薪资***：{values}")
        st.write(f"***最佳联系时间***：{time}")
        st.write(f"***语言能力***：{yuyannl}")
    st.subheader("个人简历")
    st.write(f"{grjl}")
    st.subheader("专业技能")
    st.write(f"{jn}")
    
