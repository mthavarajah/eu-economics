import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate data
gov_debt_data = pd.read_csv('datafiles/basics/government_debt.csv')
gov_debt_x = gov_debt_data['TIME PERIOD'].apply(lambda x: f"{x[-2:]} {x[:4]}")
gov_debt_y = gov_debt_data[' Government debt (consolidated) (GFS.Q.N.I9.W0.S13.S1.C.L.LE.GD.T._Z.XDC._T.F.V.N._T)']

# Subplot figure
fig = make_subplots(rows=1, cols=1)

# Traces (lines) to the figure
fig.add_trace(go.Scatter(x=gov_debt_x, y=gov_debt_y, mode='lines', line=dict(color='#50B7E1')))

# Update layout
fig.update_layout(title='Government Debt',
                  title_font_size=23,
                  plot_bgcolor='#083185',
                  paper_bgcolor='#083185',
                  title_font_color='#ffffff',
                  xaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False), 
                  yaxis=dict(tickfont_color='#6f80b5', showline=False, zeroline=False, showgrid=False),
                  yaxis_tickformat=',.0f')

# Save plot as HTML
fig_html = fig.to_html(full_html=False)
with open('macroeconomics/govdebt/govdebt.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Government Debt</title>\n')
    f.write('</head>\n<body>\n')
    f.write('<div id="govdebt-graph">\n')
    f.write(fig_html)
    f.write('\n</div>\n</body>\n</html>')


            
            
    
    