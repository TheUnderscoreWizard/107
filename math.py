import pandas as pd 
import csv 
import plotly.express as px 
import plotly.graph_objects as go 

df=pd.read_csv("data.csv")


mean=df.groupby(["student_id","level"] ).mean()
fig= px.line(mean,x="student_id",y="level")

    

fig.show()