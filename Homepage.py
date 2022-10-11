import streamlit as st
import os

os.system('python initial.py')

st.title("王歌   简历")

st.header("华北电力大学 经济与管理学院 博士, 硕导")

tab1, tab2, tab3 =st.tabs(["工作和教育经历","研究兴趣","招生方向"])


#tab1.markdown('**工作和教育经历**')

tab1.markdown("[1] 2019 至今 华北电力大学 经济与管理学院 讲师")
tab1.markdown("[2] 2014-2019 中国石油大学（北京）中国能源战略研究院/经济管理学院 硕博连读")
tab1.markdown("[3] 2018-2019 美国加州大学伯克利分校 劳伦斯伯克利国家实验室 联合培养")
tab1.markdown("[4] 2009-2013 南京大学 天文与空间科学学院 本科")


#tab2.markdown('**研究兴趣**')

tab2.markdown("- 电氢交通耦合系统")
tab2.markdown("- 可再生能源经济与政策")
tab2.markdown("- 复杂网络与博弈")

#tab3.markdown('**招生方向**')

tab3.markdown("- 具有经济学、能源、环境、计算机相关背景")
tab3.markdown("- 对能源环境经济和管理具有兴趣")
tab3.markdown("- 具备英文论文阅读能力")



st.sidebar.markdown("联系方式:")
st.sidebar.markdown("E-mail: wangge@ncepu.edu.cn")
st.sidebar.markdown("华北电力大学教一楼340")