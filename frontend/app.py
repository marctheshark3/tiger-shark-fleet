# app.py
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import json
from py_mini_racer import py_mini_racer
import os

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-text', type='text', value='', placeholder='Enter text'),
    html.Button('Execute', id='execute-button'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input('execute-button', 'n_clicks')],
    [dash.dependencies.State('input-text', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is None:
        return ''
    
    ctx = py_mini_racer.MiniRacer()
    path_to_js = os.path.abspath('../backend/dist/index.js')
    with open(path_to_js, 'r') as f:
        js_code = f.read()
    
    ctx.eval(js_code)
    result = ctx.call("executeTool", value)
    
    return "Result: {}".format(result)

if __name__ == '__main__':
    app.run_server(debug=True)
