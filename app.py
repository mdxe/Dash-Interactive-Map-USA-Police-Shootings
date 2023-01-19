from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

app = Dash(__name__)

#df2 = pd.read_csv('https://github.com/washingtonpost/data-police-shootings/blob/master/v2/fatal-police-shootings-data.csv?raw=true')
#df2 = df2.astype(str)

con = create_engine('sqlite:///database.sqlite3').connect()
#con2 = create_engine('sqlite:///database2.sqlite3')

df = pd.read_sql_table('locations', con)

app_title = 'Deadly Shootings By Police in the U.S. from 2015-01-01 to ' + df['date'].max()

# Cleanup data
# df = df.astype(str)
# df = df.replace({'race' : {'W' : 'White',
                           # 'B' : 'Black',
                           # 'H' : 'Hispanic',
                           # 'A' : 'Asian',
                           # 'O' : 'Unknown',
                           # 'N' : 'Native American',
                           # 'None' : 'Unknown',
                           # 'nan' : 'Unknown',
                           # 'B;H'  : 'Unknown'},
                # 'gender' : {
                           # 'None' : 'Unknown',
                           # 'nan' : 'Unknown',}})
# df['year'] = pd.to_datetime(df['date']).dt.year
# 
# df.to_sql("locations", con2)

# def generate_table(dataframe, max_rows=10):
    # return html.Table([
        # html.Thead(
            # html.Tr([html.Th(col) for col in dataframe.columns])
        # ),
        # html.Tbody([
            # html.Tr([
                # html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            # ]) for i in range(min(len(dataframe), max_rows))
        # ])
    # ])
    
app.title  = app_title
app.layout = html.Div([
    html.H4(
        children = app_title,
        id = 'dashboard_title',),
    html.Span([
        html.Label(
            children = 'Color by',
            htmlFor = 'scatter_dropdown_cat',
            style = {'width': '48%', 'display': 'inline-block'}
        ),
        html.Label(
            children='Period',
            htmlFor = 'scatter_dropdown_year',
            style = {'width': '48%', 'display': 'inline-block'}
        ),
    ]),
    html.Span(
        dcc.Dropdown(
            options = [
                {'label' : 'race',      'value' : 'race'},
                {'label' : 'gender', 'value' : 'gender'},
            ],            
            value = 'race',
            searchable = False,
            id = 'scatter_dropdown_cat', 
            style = {'width': '48%', 'display': 'inline-block'}),
        ),
    dcc.Dropdown(
        options = ['All'] + df.year.unique().tolist(),
        value = 'All',
        searchable = False,
        id = 'scatter_dropdown_year', 
        style = {'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id = 'scatter_plot'),

#    html.H4(children='death per 100k per state'),
#    generate_table(df)
])

@app.callback(
    Output('scatter_plot', 'figure'),
    Input('scatter_dropdown_cat', 'value'),
    Input('scatter_dropdown_year', 'value')
)

def update_figure(selected_filter, selected_year):
    if selected_year == 'All':
        filtered_df = df
    else:
        filtered_df = df[df.year == selected_year]
        
    fig = px.scatter_geo(filtered_df,
         lat    = 'latitude',
         lon    = 'longitude',
         color  = selected_filter,
         symbol = selected_filter,
         title = str(filtered_df.shape[0]) + " Deaths",
         # basic symbols: circle, square, diamond, cross, x, triangle-up, pentagon, hexagram, star, diamond, hourglass, bowtie, asterisk, hash, y, and line
         symbol_sequence = ['circle','diamond','x','square','triangle-up','star'],
         color_discrete_sequence = ['blue','red','Green','Orange','DarkGray','Black'],
         hover_name = 'gender',
         hover_data = ['armed_with', 'city', 'county', 'state'], # columns added to hover information
         opacity = 0.7,
         scope = 'usa',)
    fig.layout.autosize = True
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)