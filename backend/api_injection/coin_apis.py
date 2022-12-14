import sys
import requests
from typing import Dict, Final, List, Any, Optional


UPBIT_API_URL: Final[str] = "https://api.upbit.com/v1"
BITHUM_API_URL: Final[str] = "https://api.bithumb.com/public/ticker"


def header_to_json(url: str):
    headers: Dict[str, str] = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    info = response.json()
    
    return info


class CoinMarketBitCoinPresentPrice:
    def __init__(self) -> None:
        self.upbit_bitcoin_present_price = header_to_json(f"{UPBIT_API_URL}/ticker?markets=KRW-BTC")[0]
        self.bithum_bitcoin_present_price = header_to_json(f"{BITHUM_API_URL}/BTC_KRW")["data"]
           
               
class UpbitAPI:
    def __init__(self, name: Optional[str] = None) -> None:
        super().__init__()
        self.name = name
        self.up_url = UPBIT_API_URL
        self.upbit_market = header_to_json(f"{self.up_url}/market/all?isDetails=true")
        self.upbit_present_url = f'ticker?markets=KRW-{self.name}'
        self.upbit_coin_present_price = header_to_json(f'{self.up_url}/{self.upbit_present_url}')     

    def upbit_market_list(self) -> List[str]:
        return [data["market"].split("-")[1] for data in self.upbit_market]

    def __getitem__(self, index: int) -> Dict:
        return self.upbit_coin_present_price[index]
     
    def __sizeof__(self) -> int:
        return sys.getsizeof(self.upbit_coin_present_price)   
    
    def __namesplit__(self) -> str:
        return f"{self.up_url}/{self.upbit_present_url}".split("-")[1]
    
    
class BithumAPI:
    def __init__(self, name: Optional[str] = None) -> None:
        super().__init__()
        self.name = name
        self.bit_url = BITHUM_API_URL
        self.bithum_market = header_to_json(f"{self.bit_url}/ALL_KRW")
        self.bithum_present_price = header_to_json(f"{self.bit_url}/{name}_KRW")

    def bithum_market_list(self) -> List[Any]:
        a = [coin for coin in self.bithum_market["data"]]
        del a[-1]
        return a
        
    def __index__(self, index) -> dict:
        return self.bithum_market_list[index]

    def __getitem__(self, index: str) -> Dict:
        return self.bithum_present_price[index]
    
    def __sizeof__(self) -> int:
        return sys.getsizeof(self.bithum_present_price)
    
    def __namesplit__(self) -> str:
        return f"{self.bit_url}/{self.name}".split("/")[5]
    
    
class TotalCoinMarketListConcatnate(UpbitAPI, BithumAPI):
    def __init__(self) -> None:
        super().__init__()
    
    def coin_total_preprecessing(self) -> dict[str]:
        """
        ?????? ????????? ?????? ?????? ?????? 
        """
        up = self.upbit_market_list()
        bit = self.bithum_market_list()        
        up.extend(bit)
        
        return set(up)

