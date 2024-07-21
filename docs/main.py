import pandas as pd

# 加載HTML文件
file_path = '/mnt/data/資料庫 - Google 試算表.html'
dfs = pd.read_html(file_path)

# 提取數據框
sheet1 = dfs[0]
sheet2 = dfs[1]

# 清理數據（假設第一行是標題）
sheet1.columns = sheet1.iloc[0]
sheet1 = sheet1.drop(0).reset_index(drop=True)

sheet2.columns = sheet2.iloc[0]
sheet2 = sheet2.drop(0).reset_index(drop=True)

# 將相關列轉換為日期格式（假設A列是日期）
sheet1['A'] = pd.to_datetime(sheet1['A'], errors='coerce')
sheet2['A'] = pd.to_datetime(sheet2['A'], errors='coerce')

# 保存清理後的數據框為CSV文件
sheet1.to_csv('/mnt/data/sheet1.csv', index=False)
sheet2.to_csv('/mnt/data/sheet2.csv', index=False)
