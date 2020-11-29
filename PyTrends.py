#### https://www.honchosearch.com/blog/seo/how-to-use-python-pytrends-to-automate-google-trends-data/

from pytrends.request import TrendReq
import pandas as pd
import time
startTime = time.time()
pytrend = TrendReq(hl='en-US', tz=360)

colnames = ["keywords"]
df = pd.read_csv("keyword_list.csv", names=colnames)
df2 = df["keywords"].values.tolist()
df2.remove("Keywords")

dataset1 = []
dataset2 = []
dataset3 = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2020-04-01 2020-11-02',
     geo='US-GA',         
     gprop='youtube'
     )
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset1.append(data)
          
result = pd.concat(dataset1, axis=1)
result.to_csv('youtube_trends.csv')

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2020-04-01 2020-11-02',
     geo='US-GA',         
     gprop='news'
     )
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset2.append(data)

result = pd.concat(dataset2, axis=1)
result.to_csv('news_trends.csv')

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2020-04-01 2020-11-02',
     geo='US-GA',         
     gprop='images'
     )
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset3.append(data)

result = pd.concat(dataset3, axis=1)
result.to_csv('images_trends.csv')

executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))