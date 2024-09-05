import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Data
realGDP_data = pd.read_csv('datafiles/basics/real_GDP.csv')
realGDP_data_x = realGDP_data['TIME PERIOD'].apply(lambda x: f"{x[-2:]} {x[:4]}")
realGDP_data_y = realGDP_data['Gross domestic product at market prices (MNA.Q.Y.I9.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.LR.N)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=realGDP_data_x, y=realGDP_data_y, mode='lines', line=dict(color='#50B7E1')))

# Update Layout
fig.update_layout(title='Real GDP',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False),
                  yaxis_tickformat=',.0f')

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('macroeconomics/realGDP/realGDP.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Real GDP</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="realGDP-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')