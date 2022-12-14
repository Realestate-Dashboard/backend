import time
import json
import requests
import pandas as pd 

from typing import Dict, Final, Any, List
from kafka import KafkaProducer


UPBIT_API_URL: Final[str] = "https://api.upbit.com/v1"
BITHUM_API_URL: Final[str] = "https://api.bithumb.com/public/ticker"
BIT_TOPIC_NAME: Final[str] = "TRADEBITCOINTOTAL"

COIN_TOTAL: Final[str] = "coin_total"


# bootstrap_server = ["kafka1:19091", "kafka2:29092", "kafka3:39093"]
# producer = KafkaProducer(bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")
"""
업비트 토큰 가격 업데이트 주기 카프카 맞추기
"""


def header_to_json(url: str):
    headers: Dict[str, str] = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    info = response.json()
    
    return info

def data_format(name, open, high, low, present) -> Dict:
    data = {
        "market_name": name,
        "open": open,
        "high": high,
        "low": low,
        "present": present
    }
    return data


def upbit_coin_total_market_json() -> List[Dict[str, str]]:
    url: str = f"{UPBIT_API_URL}/market/all?isDetails=true"
    
    return header_to_json(url)


def bithum_coin_total_market_json() -> List[str]:
    url: str = f"{BITHUM_API_URL}/ALL_KRW"
    data: Dict[Any, Any] = header_to_json(url)
    
    return [i for i in data["data"]]


# 프로세스 나누기 
class UpBitBitcoinAPI:
    def __init__(self) -> None:
        self.up_url = UPBIT_API_URL
    
    def upbit_coin_price_json(self) -> List[Dict[str, str]]:
        url: str = f"{self.up_url}/candles/minutes/1?market=KRW-BTC&count=1"
        return header_to_json(url)
    
    def upbit_bitcoin_present_price(self) -> Dict:
        url: str = f'{self.up_url}/ticker?markets=KRW-BTC'
        data = header_to_json(url)
        for i in data:
            up_bitcoin_pd = data_format(
                name    = "upbit-BTC",
                open    = i["opening_price"],
                high    = i["high_price"],
                low     = i["low_price"],
                present = i["trade_price"]
            )
        return up_bitcoin_pd
    

class BithumAPIBitcoin:
    def __init__(self) -> None:
        self.bit_url = BITHUM_API_URL

    def bithum_bitcoin_present_price(self) -> Dict:
        url: str = f"{self.bit_url}/BTC_KRW"
        data: Dict[str] = header_to_json(url)
        bbitcoin_pd = data_format(
            name    = "bithum-BTC",
            open    = data["data"]["opening_price"],
            high    = data["data"]["max_price"],
            low     = data["data"]["min_price"],
            present = data["data"]["closing_price"]
        )
        return bbitcoin_pd


def concatnate() -> None:
    bit = BithumAPIBitcoin().bithum_bitcoin_present_price()
    upbit = UpBitBitcoinAPI().upbit_bitcoin_present_price()
    
    concat_data_bit: Dict[Any, Any] = {"bitthum": bit,
                                        "upbit": upbit}

    

    while True:
        producer.send(topic=TOPIC_NAME, value=json.dumps(concat_data_bit).encode("utf-8"))
        producer.flush()
        print(concat_data_bit)
        time.sleep(1)



print(bithum_coin_total_market_json())