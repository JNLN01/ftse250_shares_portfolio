import yfinance as yf
import pandas as pd
import datetime

# List ftse 250 shares
df = pd.read_csv(r'/Users/jnnorrie/PycharmProjects/ftse250_shares_portfolio/ftse250 components.csv')
print(df)

# Create an empty DataFrame to store results
result_df = pd.DataFrame(columns=['Tickers', '3-Year Average Performance'])

# Define the date range
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=3 * 365)  # 3 years of data

# Iterate through each stock symbol in the DataFrame
for symbol in df['Tickers']:
    try:
        # Fetch historical stock data
        stock_data = yf.download(symbol, start=start_date, end=end_date)

        # Calculate the 3-year average performance
        start_price = stock_data['Adj Close'].iloc[0]
        end_price = stock_data['Adj Close'].iloc[-1]
        average_performance = (end_price / start_price - 1) * 100

        # Append the result to the result DataFrame
        result_df = result_df.append({'Symbol': symbol, '3-Year Average Performance': average_performance},
                                     ignore_index=True)
    except Exception as e:
        print(f"Error fetching data for {symbol}: {str(e)}")

# Print the result DataFrame
print(result_df)

# Sort the DataFrame by '3-Year Average Performance' in descending order
result_df = result_df.sort_values(by='3-Year Average Performance', ascending=False)

# Get the top 10 performing stocks
top_10_stocks = result_df.head(10)

# Print the top 10 performing stocks
print("Top 10 Performing Stocks:")
print(top_10_stocks)

top_10_stocks.to_csv(ftse250_top_10.csv)
# Work out a way to find the top 10 performing over 3 years

# Backtest against previous data

# API with broker to enter trades{

# Work on trade automation of the management

# Diversification specification (Industry)