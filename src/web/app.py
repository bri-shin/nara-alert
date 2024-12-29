from flask import Flask, render_template, request, jsonify, redirect, url_for
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv, set_key
import os
import threading
from ..api.data_go_kr import DataGoKrAPI
from ..slack.client import SlackNotifier
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
scraper_thread = None
is_running = False

def validate_slack_token(token: str) -> bool:
    try:
        client = WebClient(token=token)
        client.auth_test()
        return True
    except SlackApiError:
        return False

def get_slack_channels(token: str) -> list:
    try:
        client = WebClient(token=token)
        response = client.conversations_list(types="public_channel,private_channel")
        return [{"name": channel["name"], "id": channel["id"]} for channel in response["channels"]]
    except SlackApiError:
        return []

def run_scraper():
    global is_running
    api = DataGoKrAPI()
    notifier = SlackNotifier()
    
    while is_running:
        try:
            bids = api.get_recent_bids(hours=1)
            keyword_bids = [
                bid for bid in bids 
                if os.getenv('SEARCH_KEYWORD', '').lower() in bid.bid_notice_name.lower()
            ]
            for bid in keyword_bids:
                notifier.send_bid_notification(bid)
        except Exception as e:
            print(f"Error in scraper: {e}")
        time.sleep(int(os.getenv('CHECK_INTERVAL', '3600')))

@app.route('/api/config', methods=['GET'])
def get_config():
    load_dotenv()
    config = {
        'slack_token': os.getenv('SLACK_BOT_TOKEN', ''),
        'channel': os.getenv('SLACK_CHANNEL', '#general'),
        'keyword': os.getenv('SEARCH_KEYWORD', 'EAP'),
        'check_interval': int(os.getenv('CHECK_INTERVAL', '3600')) // 60,
        'is_running': is_running
    }
    
    channels = []
    if config['slack_token']:
        channels = get_slack_channels(config['slack_token'])
    
    return jsonify({'config': config, 'channels': channels})

@app.route('/api/config', methods=['POST'])
def save_config():
    data = request.form
    
    if not validate_slack_token(data['slack_token']):
        return jsonify({'success': False, 'error': 'Invalid Slack token'})
    
    env_vars = {
        'SLACK_BOT_TOKEN': data['slack_token'],
        'SLACK_CHANNEL': data['channel'],
        'SEARCH_KEYWORD': data['keyword'],
        'CHECK_INTERVAL': str(int(data['check_interval']) * 60)  # Convert minutes to seconds
    }
    
    for key, value in env_vars.items():
        set_key('.env', key, value)
    
    return jsonify({'success': True})

@app.route('/api/toggle', methods=['POST'])
def toggle_scraper():
    global scraper_thread, is_running
    
    if not is_running:
        is_running = True
        scraper_thread = threading.Thread(target=run_scraper)
        scraper_thread.start()
        return jsonify({'success': True, 'status': 'started'})
    else:
        is_running = False
        if scraper_thread:
            scraper_thread.join()
        return jsonify({'success': True, 'status': 'stopped'})

if __name__ == '__main__':
    app.run(debug=True) 