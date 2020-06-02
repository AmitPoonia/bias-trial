from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("bar_nested_colormapped.html")

intents = [
    'ShareCurrentLocation',
    'ComparePlaces',
    'GetPlaceDetails',
    'SearchPlace',
    'BookRestaurant',
    'RequestRide',
    'GetDirections',
    'ShareETA',
    'GetTrafficInformation',
    'GetWeather'
]

gender = ['male', 'female']

data = {
    'intents': intents,
    'male': [2, 1, 4, 3, 2, 4, 8, 3, 7, 4],
    'female': [5, 3, 3, 2, 4, 6, 8, 9, 9, 5]
}

palette = ["#718dbf", "#e84d60"]

x = [ (i, g) for i in intents for g in gender ]

counts = sum(zip(data['male'], data['female']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=350, title="Intent counts by gender",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=gender, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
