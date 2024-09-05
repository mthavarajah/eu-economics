import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Data
portfolio_investment_balance_data = pd.read_csv('datafiles/external/portfolio_investment_balance.csv')
portfolio_investment_balance_data_x = portfolio_investment_balance_data['TIME PERIOD'].apply(lambda x: f"{x[-3:]} {x[:4]}")
portfolio_investment_balance_data_y = portfolio_investment_balance_data['Financial account, Portfolio Investment, Net (BPS.M.N.I9.W1.S1.S1.T.N.FA.P.F._Z.EUR._T.M.N.ALL)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=portfolio_investment_balance_data_x, y=portfolio_investment_balance_data_y, mode='lines', line=dict(color='#50B7E1')))

# Update Layout
fig.update_layout(title='Portfolio Investment Balance',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False),
                  yaxis_tickformat=',.0f')

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('financial_economics/portfolio_investment_balance/portfolio_investment_balance.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Portfolio Investment Balance</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="portfolio_investment_balance-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')