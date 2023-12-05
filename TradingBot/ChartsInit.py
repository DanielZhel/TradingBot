import plotly.graph_objects as go
from plotly.subplots import make_subplots
import TradingLogic as tl

def ChartsInit(instData1, instData2, macdValues, emaValues, stochValues):
    # �������� ������
    fig = make_subplots(rows=2,cols=2, shared_xaxes=True,  vertical_spacing=0.01, row_heights=[0.8, 0.2])
    fig.update_layout(bargap=0.2)

    # ������ ��� MACD
    macd_trace = go.Scatter(y = macdValues[0][0], x = instData1['time'], line=dict(color='dodgerblue', width=1))
    macdsignal_trace = go.Scatter(y = macdValues[0][1], x = instData1['time'], line=dict(color='orange', width=1))
    hist_trace = go.Bar(x = instData1['time'], y = macdValues[0][2])

    # ������ ��� ��������
    stochfast_trace = go.Scatter(y= stochValues[0], x=instData2['time'],line=dict(color='dodgerblue', width=1))
    stochslow_trace = go.Scatter(y= stochValues[1], x=instData2['time'], line=dict(color='orange', width=1))

    # ������ ��� ���
    ema_trace = go.Scatter(x=instData1['time'], y=emaValues[0])

    # ������ ���
    fig.add_trace(ema_trace, row =1, col =1)

    # ������ MACD
    fig.add_trace(hist_trace, row=2, col=1)
    fig.add_trace(macd_trace, row=2, col=1)
    fig.add_trace(macdsignal_trace, row=2, col=1)

    # ������ Stoch
    fig.add_trace(stochslow_trace, row=2, col=2)
    fig.add_trace(stochfast_trace, row=2, col=2)
    fig.add_hline(y=80, row=2, col=2, line_width=0.8, line_dash="dash", line_color="red")
    fig.add_hline(y=20, row=2, col=2, line_width=0.8, line_dash="dash", line_color="red")

    #������ ������� ����
    fig.add_trace(
                    go.Ohlc(x=instData1['time'],
                    open=instData1['open'],
                    high=instData1['high'],
                    low=instData1['low'],
                    close=instData1['close']), row=1, col=1
                      ).update_traces(line_width=0.8, 
                      selector=dict(
                          type='ohlc'
                          )
                      )

    # ������ ������� ����
    fig.add_trace(
                    go.Ohlc(x=instData2['time'],
                    open=instData2['open'],
                    high=instData2['high'],
                    low=instData2['low'],
                    close=instData2['close']), 
                    row=1, 
                    col=2
                    ).update_traces(line_width=0.8, 
                      selector=dict(
                          type='ohlc'
                          )
                      )

    # ���������� ����� ���������������
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

    tl.get_short_Signal(instData1, instData2, fig, go)
    tl.get_long_Signal(instData1, instData2, fig, go)
    fig.show()


