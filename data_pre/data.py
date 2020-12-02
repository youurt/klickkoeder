import pandas as pd
import sqlite3


cnx = sqlite3.connect('klickscraper.db')


# heftig df
heftig_df = pd.read_sql_query("SELECT * FROM heftig", cnx)
heftig_df["label"] = 1
del heftig_df["news_id"]
del heftig_df["img"]
del heftig_df["date"]
del heftig_df["scraped_at"]
del heftig_df["link"]
heftig_df = heftig_df.rename(columns={"headline": "title"})
# print(heftig_df)


# wiki df
wiki_df = pd.read_sql_query("SELECT * FROM wiki", cnx)
wiki_df = wiki_df[:688]
wiki_df["label"] = 0
del wiki_df["page_id"]
del wiki_df["category"]
del wiki_df["scraped_at"]
# print(wiki_df)


all_df = pd.concat([heftig_df, wiki_df])
all_df = all_df.sample(frac=1)
# all_df = all_df.reset_index()
# del all_df["index"]

# print(all_df)

all_df.to_csv("result.csv", index=False)
