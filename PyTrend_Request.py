#### https://www.honchosearch.com/blog/seo/how-to-use-python-pytrends-to-automate-google-trends-data/

from abc import ABC, abstractmethod
from pytrends import TrendReq
import pandas as pd
import time
import logging

logger = logging.getLogger(__name__)


class PyTrendExport():
    """ shared behavior for all exports """

    def __init__(self, config, unvalidated_parameters):
        """ initialize with an application config and a set of raw/unvalidated options """
        # timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%m-%s")

        
    def process(self):
        """ PyTrend method for processing """
        
        
    def get_data(self, pytrend):
        """ get data for crosswalk and audience files"""
        startTime = time.time()
        pytrend = TrendReq(hl='en-US', tz=360)
        colnames = ["keywords"]
        df = pd.read_csv("keyword_list.csv", names=colnames)
        df2 = df["keywords"].values.tolist()
        df2.remove("Keywords")
        data = []
        for x in range(0,len(df2)):
            keywords = [df2[x]]
            pytrend.build_payload(
                kw_list=keywords,
                cat=0,
                timeframe='2020-04-01 2020-11-02',
                geo='US-GA',
                youtube = gprop= 'youtube'
                )
            data = pytrend.interest_over_time()
            if not data.empty:
                data = data.drop(labels=['isPartial'],axis='columns')
                data.append(data)
       
            return data

