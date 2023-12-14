import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ThreeScreenTradingLogic as tl

def charts_init(inst_data1, 
               inst_data2, 
               macd_values, 
               ema_values, 
               stoch_values,
               i, 
               instruments, 
               tf1, 
               tf2, 
               high_stoch_level, 
               low_stoch_value,
               up_range_ema,
               lo_range_ema,
               risk,
               inst_id,
               high_stop_percent,
               low_stop_percent,
               min_stop_percent):
    # Создание фигуры
    fig = make_subplots(rows=2,cols=2, shared_xaxes=True,  vertical_spacing=0.01, row_heights=[0.8, 0.2],  subplot_titles=(tf1, tf2))
    fig.update_layout(bargap=0.2, title=instruments[i], title_font_size=25, title_font_color = "purple")

    # Трейсы для MACD
    macd_trace = go.Scatter(y = macd_values[0][0], x = inst_data1['time'], line=dict(color='dodgerblue', width=1))
    macdsignal_trace = go.Scatter(y = macd_values[0][1], x = inst_data1['time'], line=dict(color='orange', width=1))
    hist_trace = go.Bar(x = inst_data1['time'], y = macd_values[0][2])

    # Трейсы для стохаста
    stochfast_trace = go.Scatter(y= stoch_values[0], x=inst_data2['time'],line=dict(color='dodgerblue', width=1))
    stochslow_trace = go.Scatter(y= stoch_values[1], x=inst_data2['time'], line=dict(color='orange', width=1))

    # Трейсы для ЕМА
    ema_trace = go.Scatter(x=inst_data1['time'], y=ema_values[0])

    # График ЕМА
    fig.add_trace(ema_trace, row =1, col =1)

    # График MACD
    fig.add_trace(hist_trace, row=2, col=1)
    fig.add_trace(macd_trace, row=2, col=1)
    fig.add_trace(macdsignal_trace, row=2, col=1)

    # График Stoch
    fig.add_trace(stochslow_trace, row=2, col=2)
    fig.add_trace(stochfast_trace, row=2, col=2)
    fig.add_hline(y=high_stoch_level, row=2, col=2, line_width=0.8, line_dash="dash", line_color="red")
    fig.add_hline(y=low_stoch_value, row=2, col=2, line_width=0.8, line_dash="dash", line_color="red")

    #График первого окна
    fig.add_trace(
                    go.Ohlc(x=inst_data1['time'],
                    open=inst_data1['open'],
                    high=inst_data1['high'],
                    low=inst_data1['low'],
                    close=inst_data1['close']), row=1, col=1
                      ).update_traces(line_width=0.8, 
                      selector=dict(
                          type='ohlc'
                          )
                      )

    # График второго окна
    fig.add_trace(
                    go.Ohlc(x=inst_data2['time'],
                    open=inst_data2['open'],
                    high=inst_data2['high'],
                    low=inst_data2['low'],
                    close=inst_data2['close']), 
                    row=1, 
                    col=2
                    ).update_traces(line_width=0.8, 
                      selector=dict(
                          type='ohlc'
                          )
                      )

    # Отключение шкалы масштабирования
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=False
                )
            ),
        xaxis2=dict(
            rangeslider=dict(
                visible=False
                )
            )    
        )

    short_stat=tl.get_short_signal(inst_data2, 
                                   fig, 
                                   go, 
                                   high_stoch_level,
                                   lo_range_ema,
                                   stoch_values, 
                                   macd_values,
                                   ema_values,
                                   risk,
                                   high_stop_percent,
                                   min_stop_percent)
    long_stat=tl.get_long_signal(inst_data2, 
                                 fig, 
                                 go, 
                                 low_stoch_value,
                                 up_range_ema,
                                 stoch_values, 
                                 macd_values,
                                 ema_values,
                                 risk, 
                                 low_stop_percent,
                                 min_stop_percent)
    fig.show()
    return short_stat, long_stat


