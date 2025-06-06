import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for Apple (AAPL)
data = yf.download('AAPL', start='2020-01-01')

# Plot the closing price over time
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'])
plt.title('Apple Stock Price')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()
