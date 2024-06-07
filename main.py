import MetaTrader5 as mt5
import pandas as pd
from mt5_trade_functions import market_order,close_all_positions

if __name__ ='__main__':
    login = 5632245
    password = 'JPFfsLBB'
    server = 'IC- Markets-Demo'

    mt5.intialize()
    m5.login(login,password,server)

    symbol = 'EURUSD'
    volume = 1.0
    order_type = 'buy'

    market_order(symbol,volume,order_type)
    time.sleep(5)
    close_all_positions('all')