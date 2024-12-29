from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Bid(BaseModel):
    # Required fields
    bid_notice_no: str          # 입찰공고번호
    bid_notice_name: str        # 입찰공고명
    notice_kind_name: str       # 공고종류명
    bid_notice_date: datetime   # 입찰공고일시
    organization_name: str      # 공고기관명
    
    # Optional fields
    estimated_price: Optional[float]  # 추정가격
    bid_notice_url: Optional[str]     # 입찰공고 상세 URL

    @classmethod
    def from_api_response(cls, data: dict):
        # Converts API response data into a Bid object
        return cls(
            bid_notice_no=data.get('bidNtceNo', ''),
            bid_notice_name=data.get('bidNtceNm', ''),
            notice_kind_name=data.get('ntceKindNm', ''),
            bid_notice_date=datetime.strptime(data.get('bidNtceDt', ''), '%Y-%m-%d %H:%M:%S'),
            organization_name=data.get('ntceInsttNm', ''),
            estimated_price=float(data.get('presmptPrce', 0)),
            bid_notice_url=data.get('bidNtceDtlUrl', '')
        ) 