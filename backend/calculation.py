from typing import Dict
from .currency_exchange import CurrencyExchange

class PaymentCalculator:
    def __init__(self):
        self.currency_exchange = CurrencyExchange()
    
    def calculate_earnings(self, hourly_rate_usd: float, hours_per_day: float, working_days_per_week: int = 5) -> Dict[str, float]:
        exchange_rate = self.currency_exchange.get_usd_to_inr_rate()
        if exchange_rate is None:
            raise Exception("Could not fetch exchange rate")
        
        # Calculate hourly rate in INR
        hourly_rate_inr = hourly_rate_usd * exchange_rate
        
        # Calculate daily earnings
        daily_earnings = hourly_rate_inr * hours_per_day
        
        # Calculate weekly earnings
        weekly_earnings = daily_earnings * working_days_per_week
        
        # Calculate monthly earnings (assuming 4 weeks per month)
        monthly_earnings = weekly_earnings * 4
        
        return {
            "hourly_rate_inr": round(hourly_rate_inr, 2),
            "daily_earnings": round(daily_earnings, 2),
            "weekly_earnings": round(weekly_earnings, 2),
            "monthly_earnings": round(monthly_earnings, 2)
        } 