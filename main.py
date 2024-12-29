import time
from src.api.data_go_kr import DataGoKrAPI
from src.slack.client import SlackNotifier
from config.config import Config

def main():
    api = DataGoKrAPI()
    notifier = SlackNotifier()
    
    print(f"Starting dain_scraper with keyword: {Config.SEARCH_KEYWORD}")
    
    while True:
        try:
            # Get recent bids
            bids = api.get_recent_bids(hours=1)
            
            # Filter bids containing the keyword
            keyword_bids = [
                bid for bid in bids 
                if Config.SEARCH_KEYWORD.lower() in bid.bid_notice_name.lower()
            ]
            
            # Send notifications for matching bids
            for bid in keyword_bids:
                notifier.send_bid_notification(bid)
            
            # Wait for next check
            time.sleep(Config.CHECK_INTERVAL)
            
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main() 