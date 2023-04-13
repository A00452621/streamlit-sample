import requests
import pandas as pd

URL='https://data.nasdaq.com/api/v3/datasets/WIKI/FB.json'

params={"api_key":'ike94cV_rNH8zQFwGzzV'}
r = requests.get(URL, params)

results=r.json()
col_name=results["dataset"]["column_names"]
data=results["dataset"]["data"]

df=pd.DataFrame(data,columns=col_name)
df.sort_values("Date", inplace=True)

df.plot("Date", "Close", kind="line")
