import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Data
direct_investment_data = pd.read_csv('datafiles/external/direct_investment.csv')
direct_investment_data_x = direct_investment_data['TIME PERIOD'].apply(lambda x: f"{x[-3:]} {x[:4]}")
direct_investment_data_y = direct_investment_data['Financial account, Direct Investment, Net (BPS.M.N.I9.W1.S1.S1.T.N.FA.D.F._Z.EUR._T._X.N.ALL)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=direct_investment_data_x, y=direct_investment_data_y, mode='lines', line=dict(color='#50B7E1')))

# Update Layout
fig.update_layout(title='Direct Investment',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False),
                  yaxis_tickformat=',.0f')

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('financial_economics/direct_investment/direct_investment.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Direct Investment</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="direct_investment-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')