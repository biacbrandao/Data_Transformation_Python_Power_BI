import pandas as pd
df = pd.read_csv(r'C:\Users\beatr\Desktop\EXERCICIO\friends_episodes_v3.csv', encoding='latin-1')
df.rename(columns={'Episode Number': 'Episode_Number', 'Year_of_prod': 'Year_of_Prod'}, inplace=True)
df['Year_of_Prod'] = pd.to_numeric(df['Year_of_Prod'])
df['Season'] = pd.to_numeric(df['Season'])
df['Episode_Number'] = pd.to_numeric(df['Episode_Number'])
df['Duration'] = pd.to_datetime(df['Duration'], unit='m').dt.time
df['Stars'] = pd.to_numeric(df['Stars'], downcast='float')
df['Votes'] = pd.to_numeric(df['Votes'])
print(df)