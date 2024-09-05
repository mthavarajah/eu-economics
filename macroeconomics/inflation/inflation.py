import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Data
inflation_data = pd.read_csv('datafiles/basics/inflation.csv')
inflation_x = inflation_data['TIME PERIOD'].apply(lambda x: f"{x[-3:]} {x[:4]}")
inflation_y = inflation_data['HICP - Overall index (ICP.M.U2.N.000000.4.ANR)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=inflation_x, y=inflation_y, mode='lines', line=dict(color='#50B7E1')))

# Update Layout
fig.update_layout(title='Inflation',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False))

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('macroeconomics/inflation/inflation.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Inflation</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="inflation-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')