# %%
import pandas as pd
import numpy as np

# %%
papers=pd.read_excel("myworks.xlsx",sheet_name="发表论文")

for i in papers.index:
	year=papers.loc[i,"papers"].split(". ")[0].split(" 20")[-1].strip("abcdefghijklmn")
	papers.loc[i,'Year']="20"+year

papers=papers.sort_values(by="Year",ascending=False)
papers.to_csv("publications.csv")

# %%
projects=pd.read_excel("myworks.xlsx",sheet_name="承担项目").fillna(0)

projects=projects.sort_values(by=["开始年份","类型"],ascending=False)
projects.to_csv("projects.csv")

# %%
courses=pd.read_excel("myworks.xlsx",sheet_name="教授课程").fillna(0)
courses=courses.sort_values(by=["学年起始","学期"],ascending=False)
courses.to_csv("courses.csv")

# %%
rewards=pd.read_excel("myworks.xlsx",sheet_name="获得奖项")
rewards=rewards.sort_values(by=["年","月"],ascending=False)
rewards.to_csv("rewards.csv")


