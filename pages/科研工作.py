import streamlit as st
import pandas as pd

st.title("科研工作")

tab1, tab2, tab3 =st.tabs(["发表论文","承担项目","获得奖项"])

papers=pd.read_csv("publications.csv")

item=0
year=papers.iloc[0].loc["Year"]
tab1.markdown("**%d**"%year)
for i in papers.index:
	if papers.loc[i,'Year']<year:
		year=papers.loc[i,'Year']
		tab1.markdown("**%d**"%year)
	tab1.markdown("[%d] %s"%(item+1,papers.loc[i,'papers']))
	item+=1

projects=pd.read_csv("projects.csv")

for i in projects[projects["类型"]=="纵向"].index:
	if projects.loc[i,"参与情况"]=="主持":
		tab2.markdown("[%d] **%s**, %s, %s, %d 万元。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"金额"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))
	else:
		tab2.markdown("[%d] **%s**, %s, %s。%d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))

for i in projects[projects["类型"]=="横向"].index:
	if projects.loc[i,"参与情况"]=="主持":
		tab2.markdown("[%d] **%s**, %s, %s, %d 万元。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"金额"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))
	else:
		tab2.markdown("[%d] **%s**, %s, %s。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))

tab2.markdown("***累计承担经费:  %d万元***"%(projects["金额"].sum()))

rewards=pd.read_csv("rewards.csv")

for i in rewards.index:
	if rewards.loc[i,'类型'] != "其它":
		tab3.markdown("[%d] %s %s. 排名第%d. %d年."%(i+1,rewards.loc[i,'奖项'],rewards.loc[i,'等级'],rewards.loc[i,'排名'],rewards.loc[i,'年']))
	else:
		tab3.markdown("[%d] %s. %d年."%(i+1,rewards.loc[i,'奖项'],rewards.loc[i,'年']))

st.sidebar.markdown("累计发表论文%d篇"%item)
st.sidebar.markdown("主持科研项目%d项"%len(projects[projects["参与情况"]=="主持"]))
st.sidebar.markdown("获得各类奖项%d项"%len(rewards))