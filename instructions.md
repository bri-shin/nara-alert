# dain_scraper - Slack notification bot for data.go.kr

## Project Overview

We are developing a Slack notification bot for data.go.kr. This bot will send notifications to a Slack channel when new data is available on data.go.kr with a specific keyword.

## Core Functionalities

### 1. Set keyword

- User will be able to set a keyword to search for data.go.kr
- User should be able to set a slack channel to send notifications

### 2. Search data.go.kr

- User will be able to search data.go.kr with the keyword
- User will be able to get the data with the keyword

### 3. Receive notification on Slack

- Whenever there is a new data with the keyword, the bot will send a notification to the slack channel

## API Information

- Base URL: apis.data.go.kr/1230000/BidPublicInfoService05
- GET /getBidPblancListInfoServcPPSSrch02: 조달청의 나라장터에서 제공하는 물품, 용역, 공사, 외자 입찰공고목록, 입찰공고상세정보, 기초금액정보, 면허제한정보, 참가가능지역정보, 입찰공고 변경이력를 제공하며 나라장터 입찰공고 검색조건으로도 업무별 입찰공고 정보를 제공하는 나라장터 입찰공고정보서비스 . 조달청과 연계기관의 입찰공고 정보 또한 제공: 
- Service Key: s1AtlYWjA/vRMLFP7EwfcrStoCJCMGtZkAXtDKmVUQ0EGdNmcZnn8BMpyLd3dTFjf3GIYX5BHW7KQwgyWcQH2Q==

## API Parameters
- numOfRows (required) - 한 페이지 결과 수
- pageNo (required) - 페이지 번호
- ServiceKey (required) - 공공데이터포탈에서 받은 인증키 (s1AtlYWjA/vRMLFP7EwfcrStoCJCMGtZkAXtDKmVUQ0EGdNmcZnn8BMpyLd3dTFjf3GIYX5BHW7KQwgyWcQH2Q==)
- inqryDiv (required) - 검색하고자하는 조회구분 1:공고게시일시, 2:개찰일시 (방위사업청 연계건의 경우 조회구분) 1. 공고게시일시 : 공고일자(pblancDate)
- inqryBgnDt - 검색하고자 하는 조회시작일시
- inqryEndDt - 검색하고자 하는 조회종료일시
- type - 오픈API 리턴 타입을 JSON으로 받고 싶을 경우 'json' 으로 지정