def load_italian_data():
    # import italian data
    import pandas as pd
    import numpy as np

    df_IT = pd.read_csv(
        "https://github.com/pcm-dpc/COVID-19/raw/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
    )
    time = [220, 360]

    data_casi = np.array(df_IT["totale_casi"])
    data_inf = np.array(df_IT["totale_positivi"])
    data_rec = np.array(df_IT["dimessi_guariti"])
    data_dec = np.array(df_IT["deceduti"])

    return data_casi, data_inf, data_rec, data_dec
