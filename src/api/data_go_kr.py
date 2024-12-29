import requests
from datetime import datetime, timedelta
from typing import List
from ..models.bid import Bid
from config.config import Config

class DataGoKrAPI:
    def __init__(self):
        self.base_url = f"{Config.DATA_GO_KR_BASE_URL}/getBidPblancListInfoServcPPSSrch02"
        self.service_key = Config.DATA_GO_KR_SERVICE_KEY

    def get_recent_bids(self, hours: int = 24) -> List[Bid]:
        end_date = datetime.now()
        start_date = end_date - timedelta(hours=hours)
        
        params = {
            'serviceKey': self.service_key,
            'numOfRows': '100',
            'pageNo': '1',
            'inqryDiv': '1',
            'inqryBgnDt': start_date.strftime("%Y%m%d%H%M"),
            'inqryEndDt': end_date.strftime("%Y%m%d%H%M"),
            'type': 'json'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            items = data['response']['body']['items']
            
            return [Bid.from_api_response(item) for item in items]
            
        except Exception as e:
            print(f"Error fetching bids: {e}")
            return [] 