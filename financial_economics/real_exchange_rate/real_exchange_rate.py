import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Data
real_exchange_rate_data = pd.read_csv('datafiles/external/real_exchange_rate.csv')
real_exchange_rate_data_x = real_exchange_rate_data['TIME PERIOD'].apply(lambda x: f"{x[-3:]} {x[:4]}")
real_exchange_rate_data_y = real_exchange_rate_data['CPI deflated EER-41/Euro (EXR.M.E03.EUR.ERC0.A)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=real_exchange_rate_data_x, y=real_exchange_rate_data_y, mode='lines', line=dict(color='#50B7E1')))

# Update Layout
fig.update_layout(title='Real Exchange Rate',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False),
                  yaxis_tickformat=',.0f')

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('financial_economics/real_exchange_rate/real_exchange_rate.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Real Exchange Rate</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="real_exchange_rate-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')