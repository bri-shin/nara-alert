import requests
from urllib.parse import quote
import json
from datetime import datetime, timedelta

def test_data_go_kr_api():
    # Base configuration
    base_url = "http://apis.data.go.kr/1230000/BidPublicInfoService05/getBidPblancListInfoServcPPSSrch02"
    service_key = "s1AtlYWjA/vRMLFP7EwfcrStoCJCMGtZkAXtDKmVUQ0EGdNmcZnn8BMpyLd3dTFjf3GIYX5BHW7KQwgyWcQH2Q=="
    
    # Get date range (last 7 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Format dates as required by the API (YYYYMMDDHHmm format)
    inqry_bgn_dt = start_date.strftime("%Y%m%d%H%M")
    inqry_end_dt = end_date.strftime("%Y%m%d%H%M")

    # Parameters for the API call
    params = {
        'serviceKey': service_key,
        'numOfRows': '10',
        'pageNo': '1',
        'inqryDiv': '1',  # 1: 공고게시일시
        'inqryBgnDt': inqry_bgn_dt,
        'inqryEndDt': inqry_end_dt,
        'type': 'json'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Print response status and content
        print(f"Status Code: {response.status_code}")
        print("\nResponse Content:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
        # Print the actual URL being called (for debugging)
        print("\nRequest URL:")
        print(response.url)
        
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    test_data_go_kr_api() 