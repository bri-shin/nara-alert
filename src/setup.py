import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import inquirer
from dotenv import load_dotenv, set_key

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
    except SlackApiError as e:
        print(f"Error fetching channels: {e.response['error']}")
        return []

def setup_configuration():
    print("🔧 dain_scraper Setup Wizard")
    print("============================")
    
    # Load existing configuration
    load_dotenv()
    
    # Get Slack Bot Token
    questions = [
        inquirer.Text(
            'slack_token',
            message="Please enter your Slack Bot Token (starts with xoxb-)",
            default=os.getenv('SLACK_BOT_TOKEN', '')
        )
    ]
    answers = inquirer.prompt(questions)
    
    while not validate_slack_token(answers['slack_token']):
        print("❌ Invalid Slack token. Please check your token and try again.")
        answers = inquirer.prompt(questions)
    
    # Get available Slack channels
    channels = get_slack_channels(answers['slack_token'])
    
    if not channels:
        print("❌ No channels found or error accessing Slack channels.")
        return
    
    # Select Slack channel
    channel_question = [
        inquirer.List(
            'channel',
            message="Select the Slack channel for notifications",
            choices=[f"#{channel['name']}" for channel in channels],
            default=os.getenv('SLACK_CHANNEL', '#general')
        )
    ]
    channel_answer = inquirer.prompt(channel_question)
    
    # Set keyword
    keyword_question = [
        inquirer.Text(
            'keyword',
            message="Enter the keyword to search for in bid notices",
            default=os.getenv('SEARCH_KEYWORD', 'EAP')
        ),
        inquirer.Text(
            'check_interval',
            message="Enter check interval in minutes",
            default=os.getenv('CHECK_INTERVAL', '60')
        )
    ]
    keyword_answer = inquirer.prompt(keyword_question)
    
    # Save configuration to .env file
    env_vars = {
        'SLACK_BOT_TOKEN': answers['slack_token'],
        'SLACK_CHANNEL': channel_answer['channel'],
        'SEARCH_KEYWORD': keyword_answer['keyword'],
        'CHECK_INTERVAL': str(int(keyword_answer['check_interval']) * 60)  # Convert minutes to seconds
    }
    
    for key, value in env_vars.items():
        set_key('.env', key, value)
    
    print("\n✅ Configuration saved successfully!")
    print("\nCurrent settings:")
    print(f"• Slack Channel: {env_vars['SLACK_CHANNEL']}")
    print(f"• Search Keyword: {env_vars['SEARCH_KEYWORD']}")
    print(f"• Check Interval: {keyword_answer['check_interval']} minutes")
    print("\nTo start the scraper, run: python main.py")

if __name__ == "__main__":
    setup_configuration() 