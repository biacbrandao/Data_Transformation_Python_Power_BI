# Example of data transformation using Python in Power BI

## About The Project

### The following project shows how data can be transformed in Power BI by using Python. The library pandas is used to modify the data prior loading into Power BI.

* Futher instructions for this project can be found at the link below
<div>
<a href="https://www.youtube.com/watch?v=QoUDYYGR4Pw" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
</div>

* The csv file is a dataset containing the information regarding the popular tv show FRIENDS.

![image-friends](image-friends.jpeg)

* The file was sourced from the Kaggle comunity and can be found at the link below

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/rezaghari/friends-series-dataset)

### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## Python code

```python 
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
```

### Dashboard
![Dashboard](Dashboard_image.jpg)
