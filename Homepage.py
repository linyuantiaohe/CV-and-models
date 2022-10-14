import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(
    page_title="Dr.Wang Ge's Homepage",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Working hard!"
    }
)

os.system('python initial.py')

st.title("Homepage 王歌")
st.sidebar.markdown("诚招勤奋、好学、踏实的研究生, 急需有编程背景的同学。待遇从优！")
st.sidebar.markdown("E-mail: wangge@ncepu.edu.cn")
st.sidebar.markdown("地址: 北京市昌平区北农路2号")
st.sidebar.map(pd.DataFrame(pd.Series([40.088243727163956,116.30600799534605],index=['lat', 'lon']),columns=['Ncepu']).T)

page1, page2, page3 =st.tabs(["个人简历","科研工作","人才培养"])

#-----------------page1
page1.subheader("个人简历")
page1.markdown("华北电力大学 经济与管理学院 博士, 硕导")

p1tab1, p1tab2, p1tab3 =page1.tabs(["工作和教育经历","研究兴趣","招生方向"])
#tab1.markdown('**工作和教育经历**')

p1tab1.markdown("[1] 2019 至今 华北电力大学 经济与管理学院 讲师")
p1tab1.markdown("[2] 2014-2019 中国石油大学（北京）中国能源战略研究院/经济管理学院 硕博连读")
p1tab1.markdown("[3] 2018-2019 美国加州大学伯克利分校 劳伦斯伯克利国家实验室 联合培养")
p1tab1.markdown("[4] 2009-2013 南京大学 天文与空间科学学院 本科")


#tab2.markdown('**研究兴趣**')

p1tab2.markdown("- 电氢交通耦合系统")
p1tab2.markdown("- 可再生能源经济与政策")
p1tab2.markdown("- 复杂网络与博弈")

#tab3.markdown('**招生方向**')

p1tab3.markdown("- 具有经济学、能源、环境、计算机相关背景")
p1tab3.markdown("- 对能源环境经济和管理具有兴趣")
p1tab3.markdown("- 具备英文论文阅读能力")

#-----------------page2
page2.subheader("科研工作")

papers=pd.read_csv("publications.csv")
projects=pd.read_csv("projects.csv")
rewards=pd.read_csv("rewards.csv")

page2.markdown("- 累计发表论文%d篇"%len(papers))
page2.markdown("- 主持科研项目%d项, 累计承担经费:  %d万元"%(len(projects[projects["参与情况"]=="主持"]),projects["金额"].sum()))
page2.markdown("- 获得各类奖项%d项"%len(rewards))

p2tab1, p2tab2, p2tab3 =page2.tabs(["发表论文","承担项目","获得奖项"])

item=0
year=papers.iloc[0].loc["Year"]
p2tab1.markdown("**%d**"%year)
for i in papers.index:
	if papers.loc[i,'Year']<year:
		year=papers.loc[i,'Year']
		p2tab1.markdown("**%d**"%year)
	p2tab1.markdown("[%d] %s"%(item+1,papers.loc[i,'papers']))
	item+=1

for i in projects[projects["类型"]=="纵向"].index:
	if projects.loc[i,"参与情况"]=="主持":
		p2tab2.markdown("[%d] **%s**, %s, %s, %d 万元。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"金额"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))
	else:
		p2tab2.markdown("[%d] **%s**, %s, %s。%d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))

for i in projects[projects["类型"]=="横向"].index:
	if projects.loc[i,"参与情况"]=="主持":
		p2tab2.markdown("[%d] **%s**, %s, %s, %d 万元。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"金额"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))
	else:
		p2tab2.markdown("[%d] **%s**, %s, %s。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))

for i in rewards.index:
	if rewards.loc[i,'类型'] != "其它":
		p2tab3.markdown("[%d] %s %s. 排名第%d. %d年."%(i+1,rewards.loc[i,'奖项'],rewards.loc[i,'等级'],rewards.loc[i,'排名'],rewards.loc[i,'年']))
	else:
		p2tab3.markdown("[%d] %s. %d年."%(i+1,rewards.loc[i,'奖项'],rewards.loc[i,'年']))

#-----------------page3

page3.subheader('人才培养')

p3tab1, p3tab2, p3tab3 =page3.tabs(["教授课程","研究生培养","本科生培养"])

p3tab1.markdown('**开设课程**')

courses=pd.read_csv("courses.csv")

for i in courses.index:
	p3tab1.markdown("[%d] %s, %d学时, %d-%d学年第%d学期, 选课人数: %d人。"%(i+1,courses.loc[i,"课程名称"],courses.loc[i,"课时"],courses.loc[i,"学年起始"],courses.loc[i,"学年终止"],courses.loc[i,"学期"],courses.loc[i,"选课人数"]))

p3tab2.subheader('在读-2022级')

majors=["工业工程与管理","物流工程与管理"]

p3tab2.markdown('(%s) **程煜, 谭宇璇, 康晓杰, 古明越, 赵铭路, 李梓熙, 周舟.**'%majors[0])
p3tab2.markdown('(%s) **尹亭, 冯楚怡.**'%majors[1])
p3tab2.text('\n')

p3tab2.subheader('在读-2021级')
p3tab2.markdown('(%s) **张禾, 郑越.**'%majors[0])
p3tab2.markdown('(%s) **李智, 毛瑀璇, 钱嘉琪.**'%majors[1])
students2021 = Image.open('photos/研究生/2021.png')
p3tab2.image(students2021, caption='2022年初聚餐')
p3tab2.text('\n')

p3tab2.subheader('在读-2020级')
p3tab2.markdown('(%s) **晏嘉泽, 张祯乾, 纪金杉, 文茜雅, 于垆玥.**'%majors[0])
students2020 = Image.open('photos/研究生/2020.png')
p3tab2.image(students2020, caption='2021年太原参会')

p3tab3.markdown('**指导本科生**')

p3tab3.markdown('(2022届) 周智宇, 李楠')
p3tab3.markdown('(2021届) 王聂娟, 田政昊')
p3tab3.markdown('(2020届) 管宇舟, 郑海涛, 陆永香, 聶志峰, 林嘉琳')

p3tab3.text('\n')

p3tab3.markdown('**本科生获得荣誉**')

p3tab3.markdown('周智宇, 华北电力大学2022届校级优秀毕业生')
p3tab3.markdown('周智宇, 中国学术英语教学研究会“中国大学生 5 分钟科研英语演讲”全国总决赛特等奖')

p3tab3.text('\n')

p3tab3.markdown('**担任班主任**')

p3tab3.markdown('2022.9 至今 营销2101班')
p3tab3.markdown('2021.9-2022.9 工商2104班')
p3tab3.markdown('2019.9-2020.9 工商1908班')