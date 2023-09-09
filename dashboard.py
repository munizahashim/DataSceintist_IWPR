import pandas as pd
import plotly.express as px

# Load the data from Excel
data = pd.read_excel("C:/Users/UCA/Documents/summers 2023/IWPR internship/building/Final Project/Bishkek_data.xlsx")

# Create a 3D bar chart-like visualization using Plotly Express
fig = px.scatter_3d(data,
                    x=data.index,
                    y='No. of Buildings',
                    z='No. of Floors',
                    color='No. of Floors',  # Map the number of floors to bar color intensity
                    opacity=0.7,  # Set opacity for bars
                    color_continuous_scale='Blues'  # Use the 'Blues' colormap
                    )

# Update the layout of the figure
fig.update_layout(scene=dict(
                          xaxis_title='Bishkek',
                          yaxis_title='No. of Buildings',
                          zaxis_title='No. of Floors'),
                  scene_camera=dict(eye=dict(x=1.4, y=-1.4, z=0.5)),  # Adjust camera position for better view
                  title='Bishkek 3D Building Visualization',  # Set title for the figure
)

# Show the interactive 3D bar chart dashboard
fig.show(renderer="browser", port=8050)
