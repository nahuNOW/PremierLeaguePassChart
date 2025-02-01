#PremierLeaguePassChart using Python

This Python code visualizes soccer passes using the `pandas`, `mplsoccer`, `matplotlib`, and `seaborn` libraries.

## Step-by-Step Breakdown

1. **Import Libraries**:
   - `import pandas as pd`: Imports the pandas library for data manipulation.
   - `from mplsoccer import *`: Imports functions from the mplsoccer library to create soccer field visuals.
   - `import matplotlib.pyplot as plt`: Imports matplotlib for plotting graphs.
   - `import seaborn as sns`: Imports seaborn for enhanced visualizations (although not used directly in this code).

2. **Load Data**:
   - `df = pd.read_csv("passes.csv")`: Reads a CSV file named "passes.csv" into a DataFrame called `df`.

3. **Adjust Coordinates**:
   - The code adjusts the passing coordinates by scaling:
     - `df['X'] = df['X']*1.2`
     - `df['Y'] = df['Y']*.8`
     - `df['EndX'] = df['EndX']*1.2`
     - `df['EndY'] = df['EndY']*.8`

4. **Create Soccer Field**:
   - `fig, ax = plt.subplots(figsize=(13.5, 0))`: Creates a figure and axes for the plot.
   - `fig.set_facecolor("#22312b")`: Sets the background color of the figure.
   - `pitch = Pitch(...)`: Initializes a soccer pitch with specific colors.
   - `pitch.draw(ax=ax)`: Draws the soccer pitch on the axes.
   - `plt.gca().invert_yaxis()`: Inverts the y-axis for the correct orientation.

5. **Plot Passes**:
   - A loop iterates through the rows in the DataFrame:
     - If the pass is `Successful`, it plots the pass line in green and marks the starting point.
     - If the pass is `Unsuccessful`, it plots the pass line in red and marks the starting point.

6. **Title and Show Plot**:
   - `plt.title(...)`: Adds a title to the plot.
   - `plt.show()`: Displays the final visualization.

## Conclusion

This code provides a clear visual representation of soccer passes, distinguishing between successful and unsuccessful attempts using color coding.
