import yfinance as yf
import plotly.graph_objects as go

# Fetch historical data for Apple Inc. (AAPL)
ticker_symbol = "AAPL"
stock_data = yf.Ticker(ticker_symbol)
historical_data = stock_data.history(period="1mo")  # Adjust the period as needed

# Display the historical data
print(historical_data.head())

# Create a Plotly line chart
fig = go.Figure()

# Add the closing prices to the figure
fig.add_trace(go.Scatter(
    x=historical_data.index,  # X-axis: Date
    y=historical_data['Close'],  # Y-axis: Closing Prices
    mode='lines+markers',  # Show lines and markers
    name='Closing Price',  # Legend entry
    line=dict(color='blue')  # Line color
))

# Add titles and labels
fig.update_layout(
    title=f"{ticker_symbol} Closing Prices Over Last 30 Days",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    hovermode='x unified'  # Unified hover effect
)

# Show the interactive plot
fig.show()