from bokeh.models import HoverTool
from bokeh.sampledata import us_states
from bokeh.plotting import figure, show, output_file, ColumnDataSource
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def rgb_to_hex(rgb):
    arr=np.round(255*np.array(list(rgb[:3])))
    return '#%02x%02x%02x' % tuple(arr)

us_states = us_states.data.copy()
loan_defs = pd.read_excel("data/peps300.xlsx")
loan_defs['State']=loan_defs['State'].apply(lambda x: x.lower())

blues_grad = plt.get_cmap('Blues')

del us_states["HI"]
del us_states["AK"]

state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

state_colors = []
sld_rate={}

for state_key in us_states:
    sld_rate[state_key] = loan_defs[loan_defs['State'] == state_key.lower()]['Num 1'].sum() / loan_defs[loan_defs['State'] == state_key.lower()]['Denom 1'].sum()

sld_min, sld_max=np.min(sld_rate.values()), np.max(sld_rate.values())

for state_key in us_states:
    col_idx=(sld_rate[state_key]-sld_min)/(sld_max-sld_min)
    state_colors.append(rgb_to_hex(blues_grad(col_idx)))


state_keys=us_states.keys()
state_sld_rates=np.round(np.array(sld_rate.values())*100)

source = ColumnDataSource(data=dict(
    state_key=state_keys,
    sld_rate=state_sld_rates,
))

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="Student Loan Defaults - 2012", toolbar_location="left", tools=TOOLS,
    plot_width=1100, plot_height=700)

p.patches(state_xs, state_ys, fill_color=state_colors, fill_alpha=0.8,
    line_color="navy", line_width=1, source=source)

hover=p.select_one(HoverTool)
hover.point_policy="follow_mouse"
hover.tooltips=[
    ("State", "@state_key"),
    ("Default rate", "@sld_rate%")
]

output_file("sld_rate_map.html", title="Student Default Rates")
show(p)