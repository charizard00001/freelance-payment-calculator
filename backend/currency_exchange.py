import requests
from typing import Optional

class CurrencyExchange:
    def __init__(self):
        self.base_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    def get_usd_to_inr_rate(self) -> Optional[float]:
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            data = response.json()
            return data['rates']['INR']
        except Exception as e:
            print(f"Error fetching exchange rate: {str(e)}")
            return None 