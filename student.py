import plotly.express as px
import csv

with open("./data/Student Marks vs Days Present.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
      fig.show()
