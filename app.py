import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# add page options for overall app
ui.page_opts(title="P1: Brower Interactive App", fillable=True)

# Create a sidebar with slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in a histogram. 
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label ("Num
