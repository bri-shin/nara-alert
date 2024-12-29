from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from ..models.bid import Bid
from config.config import Config

class SlackNotifier:
    def __init__(self):
        self.client = WebClient(token=Config.SLACK_BOT_TOKEN)
        self.channel = Config.SLACK_CHANNEL

    def send_bid_notification(self, bid: Bid):
        try:
            message = self._format_bid_message(bid)
            response = self.client.chat_postMessage(
                channel=self.channel,
                text=message,
                unfurl_links=True
            )
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")

    def _format_bid_message(self, bid: Bid) -> str:
        return f"""
🔔 *새로운 입찰공고*
*공고명:* {bid.bid_notice_name}
*공고번호:* {bid.bid_notice_no}
*공고종류:* {bid.notice_kind_name}
*공고기관:* {bid.organization_name}
*추정가격:* {bid.estimated_price:,.0f}원
*공고일시:* {bid.bid_notice_date.strftime('%Y-%m-%d %H:%M')}
*상세링크:* {bid.bid_notice_url}
""" 