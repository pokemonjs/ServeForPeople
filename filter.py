import sys
import pandas as pd

# setting for conditions
# key:[value,value]
conditions = {}
conditions["政治面貌"]=["中共党员"]
conditions["专业"]=["计算机科学与技术","计算机类"]
conditions["学历"]=["本科及以上","仅限本科","本科或硕士研究生"]
conditions["服务基层项目工作经历"]=["无限制"]
conditions["工作地点"]=["贵州","北京"]

# loading data
df = pd.read_excel("content.xls",sheet_name="sheet0")
for i in range(3):
	df = df.append(pd.read_excel("content.xls",sheet_name=f"sheet{i+1}"))
# into one sheet

# filter result
result = []
for idx,row in df.iterrows():
	# for each row
	all_condition = True
	for key in conditions.keys():
		# for each condition
		content = row[key]
		flag = False
		# for each sub condition
		for condi in conditions[key]:
			if condi in content:
				flag = True
		all_condition = all_condition and flag
		if flag==False:
			break
	if all_condition:
		result.append(row)

# save file
result_df = pd.DataFrame(result)
result_df.to_excel("filter.xlsx",index=False)