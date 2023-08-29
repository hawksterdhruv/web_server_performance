# visualization.py

import json
from datetime import datetime

with open('perf_001.json', 'r') as fin:
    data = json.load(fin)

import plotly.express as px

print(data)
for idx, a in enumerate(data):
    a['start_time'] = datetime.fromtimestamp(a['start_time'])
    a['end_time'] = datetime.fromtimestamp(a['end_time'])
    a['index'] = idx
fig = px.timeline(data, x_start="start_time", x_end="end_time", y="index")
print(fig.data)
# fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()