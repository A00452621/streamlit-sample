import pandas as pd
import sqlite3

con=sqlite3.connect("D:/MSc CDA/Semester 2/3. Data and Text Mining_MCDA5580/Python Workshop/Chinook_Sqlite.sqlite")
cur=con.cursor()

query="select * from Artist"

res=cur.execute(query)
    
artists = []
for result in res:
    print(result)
    artists.append(result)
    
new_df=pd.DataFrame(artists,
columns=["id","artist_name"],
)

new_query = "select * from album"

results=cur.execute(new_query)

albums = [i for i in results]
album_df = pd.DataFrame(albums,
                        columns=["id","album_title","artist_id"])

album_df=album_df.join(new_df, on=["artist_id"], lsuffix='_l')
