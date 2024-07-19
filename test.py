import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

color_scale = [(0, 'orange'), (1,'red')]

fig = px.scatter_mapbox(df, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="neighborhood", 
                        hover_data=["neighborhood", "price"],
                        color="price",
                        color_continuous_scale=color_scale,
                        size="size_in_sqft",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()