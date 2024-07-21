import pandas as pd

# Load the HTML file
file_path = '/mnt/data/資料庫 - Google 試算表.html'
dfs = pd.read_html(file_path, header=None)

# Extract and clean the first dataframe
sheet1 = dfs[0]
sheet2 = dfs[1]

# Clean the data (assuming first row is header)
sheet1.columns = ['Index'] + [f'Col{i}' for i in range(1, len(sheet1.columns))]
sheet1 = sheet1.drop(0).reset_index(drop=True)

# Save cleaned dataframe to CSV for web use
sheet1.to_csv('/mnt/data/sheet1_cleaned.csv', index=False)
sheet2.to_csv('/mnt/data/sheet2_cleaned.csv', index=False)
