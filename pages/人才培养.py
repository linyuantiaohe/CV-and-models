import streamlit as st
import pandas as pd

st.title('人才培养')

tab1, tab2, tab3 =st.tabs(["教授课程","研究生培养","本科生培养"])

tab1.markdown('**开设课程**')

courses=pd.read_csv("courses.csv")

for i in courses.index:
	tab1.markdown("[%d] %s, %d学时, %d-%d学年第%d学期, 选课人数: %d人。"%(i+1,courses.loc[i,"课程名称"],courses.loc[i,"课时"],courses.loc[i,"学年起始"],courses.loc[i,"学年终止"],courses.loc[i,"学期"],courses.loc[i,"选课人数"]))

tab2.markdown('**指导全日制研究生**')

tab2.markdown('(2022级) 程煜, 谭宇璇, 尹亭, 冯楚怡')
tab2.markdown('(2021级) 张禾, 李智, 毛瑀璇, 钱嘉琪')
tab2.markdown('(2020级) 晏嘉泽, 张祯乾')

tab2.text('\n')

tab2.markdown('**指导非全日制研究生**')

tab2.markdown('(2022级) 康晓杰, 古明越, 赵铭路, 李梓熙, 周舟')
tab2.markdown('(2021级) 郑越')
tab2.markdown('(2020级) 纪金杉, 文茜雅, 于垆玥')

tab3.markdown('**指导本科生**')

tab3.markdown('(2022届) 周智宇, 李楠')
tab3.markdown('(2021届) 王聂娟, 田政昊')
tab3.markdown('(2020届) 管宇舟, 郑海涛, 陆永香, 聶志峰, 林嘉琳')

tab3.text('\n')

tab3.markdown('**本科生获得荣誉**')

tab3.markdown('周智宇, 华北电力大学2022届校级优秀毕业生')
tab3.markdown('周智宇, 中国学术英语教学研究会“中国大学生 5 分钟科研英语演讲”全国总决赛特等奖')

tab3.text('\n')

tab3.markdown('**担任班主任**')

tab3.markdown('2022.9 至今 营销2101班')
tab3.markdown('2021.9-2022.9 工商2104班')
tab3.markdown('2019.9-2020.9 工商1908班')

st.sidebar.markdown("诚招勤奋、好学、踏实的研究生, 急需有编程背景的同学。待遇从优！")