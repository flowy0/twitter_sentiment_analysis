# try out twint package

import twint

c = twint.Config()
c.Limit =50
c.Username = "twitter"
c.Pandas = True

twint.run.Search(c)

tweets_df = twint.storage.panda.Tweets_df
print(tweets_df.info())

tweets_df.to_csv("twitter_tweets.csv",index=False)