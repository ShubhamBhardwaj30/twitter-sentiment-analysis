# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import tweepy as tw
import pandas as pd


# %%
consumer_key=os.environ.get('consumer_key')
consumer_secret= os.environ.get('consumer_secret')
access_token= os.environ.get('access_token')
access_token_secret= os.environ.get('access_token_secret')


# %%
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# %%
search_words = "#neerajchopra"
date_since = "2018-08-01"


# %%
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(100)
df = pd.DataFrame({})
# Iterate and print tweets
for tweet in tweets:
    df = df.append(tweet._json, ignore_index=True)


# %%
df.columns


# %%
display(df)


# %%
df.loc[0].text

