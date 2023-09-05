#assignment 4
#Kendall Starcevich
#I used the covid data by state level that we used in our practice for class


from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import requests
import plotly.express as px

#read the state-level data from the API
response = requests.get("https://api.covid19api.com/live/country/united-states")
DATA = response.json()

#create the initial figure of all the states
#- this will quickly get replaced
fig = px.line(DATA, x="Date", y="Deaths", color="Province", title='COVID Deaths in the US')


state_names_list = []
for state_data in DATA:
    state_names_list.append(state_data["Province"])

app = Dash(__name__)

app.layout = html.Div(children = [
    dcc.Markdown(
        id = "title",
        children = "## COVID Dashboard"
    ),

    dcc.Dropdown(
        id = "state_select_dropdown",
        options = state_names_list,
        value = ["Iowa"],
        multi = True #allows us to select multiple values
    ),

    dcc.Graph(
        id = "state_line_graph",
        figure = fig
    )
])

@app.callback(
    Output("state_line_graph","figure"),
    Input("state_select_dropdown","value"),
)
def update_state_graph(state_names):
    #state_names is a list with the states
    #selected from the dropdown by the user
    records_to_display = [] #for keeping only the selected states
    for curr_state in DATA: #loop through all state records
        if curr_state["Province"] in state_names:
            records_to_display.append(curr_state)
    fig = px.line(records_to_display,x="Date", y="Deaths", color="Province", title='COVID Deaths in the US')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

