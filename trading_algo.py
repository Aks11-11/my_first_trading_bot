import MetaTrader5 as mt5
import pandas as pd

def markeet_order(symbol,volume,order_type,deviation=20,magic=15,stoploss=0.0,strategy_name='Trading Bot'):
    order_type_dict = {
        'buy':mt5.ORDER_TYPE_BUY,
        'sell': mt5.ORDER_TYPE_SELL
    }
    price_dict={
        'buy': mt5,symbol_ingo_tick(symbol).ask,
        'sell':mt5_symbol_ingo_tick(symbol).bid
    }
    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol":symbol,
        "volune":volume,
        "type":order_type_dict[order_type],
        "price":price_dict[order_type],
        "sl": stoploss,
        "tp" : 0.0,
        "deviation":deviation,
        "magic":magic,
        "comment":strategy_name,
        "type_time":mt5.ORDER_TIME_GTC,
        "type_filling":mt5.ORDER_FILLING_IOC,
    }
    order_result =mt5.order_send(request)
    return(order_result)

def close_position(position,symbol,deviation=20,magic=15,strategy_name='Trading BOt'):
    order_type_dict= {
        0:mt5.ORDER_TYPE_SELL,
        1:mt5.PRDR_TYPE_BUY

    }
    price_dict={
        0:mt5.symbol_ingo_tick(symbol).bid,
        1:mt5.sumbol_info_tick(symbol).ask
    }
    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position['ticket'],
        "symbol": symbol,
        "volune": volume,
        "type": order_type_dict[order_type],
        "price": price_dict[order_type],
        "deviation": deviation,
        "magic": magic,
        "comment": strategy_name,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    order_result = mt5.order_send(request)
    return (order_result)
def close_all_positions(order_type,magic=15):
    order_type_dict={
        'buy':0
        'sell':1
    }
    if mt5.positions_total()>0:
        positions = mt5.positions_get()

        positions_df = pd.DataFrame(positions,columns=positions[0]._asdict().keys())
        positions_df = positions_df[positions_df['magic']==magic]

        if order_type != 'all':
            positions_df= positions_df[(positions_df['type']== order_type_dict[order_type])]