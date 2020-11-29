#https://pypi.org/project/pytrends/#interest-by-region

import json
import pandas as pd                        
from pytrends.request import TrendReq

class MyTrendReq(TrendReq):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def interest_by_region(self, resolution='DMA', inc_low_vol=False,
                           inc_geo_code=False):
        """Request data from Google's Interest by DMA section and return a dataframe"""

        # make the request
        region_payload = dict()

        if self.geo == '': 
            self.interest_by_region_widget['request']['resolution'] = resolution 
        elif self.geo == 'US' and resolution in ['DMA', 'CITY', 'REGION']: 
            self.interest_by_region_widget['request']['resolution'] = resolution 
        elif len(self.geo) == 2 and resolution in ['CITY', 'REGION']:
            self.interest_by_region_widget['request']['resolution'] = resolution


        self.interest_by_region_widget['request'][
            'includeLowSearchVolumeGeos'] = inc_low_vol

        # convert to string as requests will mangle
        region_payload['req'] = json.dumps(
            self.interest_by_region_widget['request'])
        region_payload['token'] = self.interest_by_region_widget['token']
        region_payload['tz'] = self.tz

        # parse returned json
        req_json = self._get_data(
            url=TrendReq.INTEREST_BY_REGION_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=region_payload,
        )
        df = pd.DataFrame(req_json['default']['geoMapData'])
        if (df.empty):
            return df

        # rename the column with the search keyword
        df = df[['geoName', 'value']].set_index(['geoName']).sort_index()


        # split list columns into seperate ones, remove brackets and split on comma
        result_df = df['value'].apply(lambda x: pd.Series(
            str(x).replace('[', '').replace(']', '').split(',')))
        if inc_geo_code:
            result_df['coordinates'] = df['coordinates']

        # rename each column with its search term
        for idx, kw in enumerate(self.kw_list):
            result_df[kw] = result_df[idx].astype('int')
            del result_df[idx]

        return result_df
#import pytrends

if __name__=="__main__":
    pytrend = MyTrendReq()
    kw_list=['Donald Trump', 'Joe Biden']
    pytrend.build_payload(kw_list,timeframe='2020-03-01 2020-11-02')
    dma_df = pytrend.interest_by_region(resolution='DMA')

dma_df.to_csv ('dma.csv')
