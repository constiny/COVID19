import folium
import altair as alt
import datetime
import pandas as pd
import numpy as np

def line_vega(UID, panel):
    # create vega object for attaching plot on marker
    data = panel[panel["UID"] == UID].iloc[0, -7:]

    x = [datetime.datetime.strptime(i, '%m/%d/%y') for i in list(data.index)[-7:]]
    x = pd.to_datetime(x).astype(int).astype(int) / 10 ** 6
    y = list(data)
    data2 = pd.DataFrame([x,y],index=["Date", "Confirmed"]).transpose()


    line = alt.Chart(data2).mark_line().encode(
        alt.X('Date:T' , timeUnit='monthdate',axis = alt.Axis(title = 'DATE', format = ("%b %d"))), 
        alt.Y('Confirmed:Q',axis = alt.Axis(title = 'Number of Cases'))
    ).properties(
        title=f'{panel[panel["UID"] == UID].iloc[0, 5]} county has {int(y[-1])} case.',
        # , {int(y[-1]/ panel[panel["UID"] == UID].iloc[0, -8] * 100 - 100)}% increase in 7 days
        width=300,
        height=200
    )

    vega = folium.features.VegaLite(line, width=360, height=250)
    
    return vega


def color_on_quantity(n):
    # color from sharp to pale indicates the sericity
    if n > 10000:
        color="red" 
    elif n > 1000:
        color="#8B0000"   # pale red
    elif n > 100:
        color="#FA8072"# salmon  
    elif n > 10:
        color="#FFCE00"# tangerine        
    else:
        color="#0A8A9F" # teal
    return color

def plot_confirm_counts(data, panel):

    ## Create map

    folium_map = folium.Map(location=[37, -105],
                            zoom_start=5,
                            tiles="CartoDB dark_matter", # alternative "OpenStreetMap"
                            width=960, 
                            height=540)
    
    for index in range(data.shape[0]):   # data.shape[0]
        case_info = data.iloc[index, 5:]
        if case_info[2] > 0:

            county_name = data.iloc[index, 1]
    
            # radius of circles
            radius = np.log10(case_info[2]*10) * 5

            # choose the color of the marker
            color = color_on_quantity(case_info[2])

            marker = folium.CircleMarker(location=(case_info[0],case_info[1]),
                                        radius=radius,
                                        color=color,
                                        fill=True)
            
            vega = line_vega(case_info[-1], df_panel)

            popup = folium.Popup()
            vega.add_to(popup)
            popup.add_to(marker)
            marker.add_to(folium_map)

    
    return folium_map