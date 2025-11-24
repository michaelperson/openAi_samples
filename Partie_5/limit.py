import redis
from datetime import datetime, timedelta
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def check_budget_before_call(estimated_cost_usd): 
    today_key = f"api_cost:{datetime.now().strftime('%Y-%m-%d')}" 
    current_daily_cost = float(redis_client.get(today_key) or 0)  
    DAILY_BUDGET_USD = 100.0 
    # Limite quotidienne  
    if current_daily_cost + estimated_cost_usd > DAILY_BUDGET_USD: 
        logger.critical(f"BUDGET EXCEEDED: {current_daily_cost:.2f}$ spent today") 
        raise BudgetExceededException("Daily API budget exceeded")  
    # Incrémenter le compteur 
    redis_client.incrbyfloat(today_key, estimated_cost_usd) 
    redis_client.expire(today_key, timedelta(days=2)) # Expiration après 2 jours




    