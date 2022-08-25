
import pandas as pd 
url="https://www.simplilearn.com/power-bi-interview-questions-and-answers-article"
data=pd.read_html(url)

type(data)
len(data)
print(data[1])