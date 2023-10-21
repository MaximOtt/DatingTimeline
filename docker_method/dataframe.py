
##### DO NOT RUN THIS IS A TEST. IF RUN IT WILL OVERWRITE THE IMAGE if call uncommented


import pandas as pd

def update_dataframe():
    #  example dataframe from national grid api
    gen = [
        {'fuel': 'biomass', 'perc': 2.0},
        {'fuel': 'coal', 'perc': 1.1},
        {'fuel': 'imports', 'perc': 5.5},
        {'fuel': 'gas', 'perc': 12.3},
        {'fuel': 'nuclear', 'perc': 14.4},
        {'fuel': 'other', 'perc': 0.9},
        {'fuel': 'hydro', 'perc': 1.7},
        {'fuel': 'solar', 'perc': 9.8},
        {'fuel': 'wind', 'perc': 52.3}
    ]

    df = pd.DataFrame(gen)
    df_to_html = df.to_html(index=False)

    # If there is no file named like this, it is created
    with open('data_table.html', 'w') as file:
        file.write(df_to_html)

    return df_to_html


#html_content = update_dataframe()


