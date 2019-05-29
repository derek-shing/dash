import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
trace01 = {'x':[1, 2, 3], 'y':[4, 1, 2], 'type': 'bar', 'name' : 'SF'}
trace02 = {'x':[1, 2, 3], 'y':[5, 3, 8], 'type' : 'bar', 'name' : 'LA'}
app.layout = html.Div(children=[
    html.H1("Hello Dash!"),
    dcc.Graph(id = 'example',
              figure = {
               'data' : [trace01,trace02],
               'layout': dict(title='Bar Plot')
              }
              )
])


if __name__ == "__main__":
    app.run_server()