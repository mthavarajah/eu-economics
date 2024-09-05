import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Data
current_account_data = pd.read_csv('datafiles/external/current_account.csv')
current_account_data_x = current_account_data['TIME PERIOD'].apply(lambda x: f"{x[-3:]} {x[:4]}")
current_account_data_y = current_account_data['Current account, Balance (BPS.M.N.I9.W1.S1.S1.T.B.CA._Z._Z._Z.EUR._T._X.N.ALL)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=current_account_data_x, y=current_account_data_y, mode='lines', line=dict(color='#50B7E1')))

# Update Layout
fig.update_layout(title='Current Account',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False),
                  yaxis_tickformat=',.0f')

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('financial_economics/current_account/current_account.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Current Account</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="current_account-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')