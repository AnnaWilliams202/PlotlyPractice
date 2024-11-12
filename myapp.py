import pandas as pd
import plotly.express as px

data = pd.read_csv('employees.csv')

fig = px.scatter(data,x= 'PerformanceScore',y="Salary",color="Department",
                 title="Salary vs Performance Score by Department",
                 hover_data=['Name', 'Position'])


fig.show()