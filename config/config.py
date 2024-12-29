import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Configuration
    DATA_GO_KR_BASE_URL = "http://apis.data.go.kr/1230000/BidPublicInfoService05"
    DATA_GO_KR_SERVICE_KEY = os.getenv('DATA_GO_KR_SERVICE_KEY', 's1AtlYWjA/vRMLFP7EwfcrStoCJCMGtZkAXtDKmVUQ0EGdNmcZnn8BMpyLd3dTFjf3GIYX5BHW7KQwgyWcQH2Q==')
    
    # Slack Configuration
    SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
    SLACK_CHANNEL = os.getenv('SLACK_CHANNEL', '#general')
    
    # Search Configuration
    SEARCH_KEYWORD = os.getenv('SEARCH_KEYWORD', 'EAP')
    CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', '3600'))  # Default 1 hour 