
import numpy as np
import pandas as pd

price = pd.read_csv("data/airbnb_price.csv")
#print(price.head())
room_type = pd.read_excel("data/airbnb_room_type.xlsx")
#print(room_type)
review = pd.read_csv("data/airbnb_last_review.tsv",sep="\t")
#print(review)

df = price.merge(room_type,on="listing_id").merge(review,on="listing_id")
print(df.info())
df['last_review'] = pd.to_datetime(df['last_review'])

earliest_review = df['last_review'].dt.date.min()
recent_review = df['last_review'].dt.date.max()
df['room_type'] = df['room_type'].str.lower()
numberOfPrivateRoom = df[df['room_type']=='private room'].shape[0]
print(df['room_type'].head(10))
print(numberOfPrivateRoom)
df['price'] = df['price'].str.replace(" dollars","")
df['price'] = df['price'].astype(float)
averagePrice = df['price'].mean()

review_dates = pd.DataFrame({'first_reviewed': [earliest_review],'last_reviewed': [recent_review],'nb_private_rooms':[numberOfPrivateRoom],'avg_price':[round(averagePrice,2)] })

print(review_dates)