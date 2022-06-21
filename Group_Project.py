import csv
import statistics
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#######KASIA######
def read_data():
    data = []

    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            data.append(row)


    return data

print(read_data())

#CREATING LIST OF SALES
def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)


    return sales

print(run())


total = sum(run())

#######ELOISE######
max_sales = max(run())
min_sales = min(run())
ave_sales = round(statistics.mean(run()),2)

#TOTAL, MIN, MAX SALES
print(f'Total sales: {total}')
print(f'Highest sales: {max_sales}')
print(f'Lowest sales: {min_sales}')
print(f'Average sales: {ave_sales}')


#CREATE DATAFRAME AND ADD % CHANGE
df = pd.read_csv("sales.csv")

df['sales_pct_change'] = round(df['sales'].pct_change(),4)

#ADD PROFIT COLUMN AND PROFIT % CHANGE
df['profit'] = df['sales'] - df['expenditure']
df['profit_pct_change'] = round(df['profit'].pct_change(),4)

print(df)

#TOTAL, MIN, MAX PROFIT
total_profit = sum(df['profit'])
max_profit = max(df['profit'])
min_profit = min(df['profit'])
ave_profit = round(statistics.mean(df['profit']),2)

print(f'Total profit:{total_profit}')
print(f'Highest profit:{max_profit}')
print(f'Lowest profit:{min_profit}')
print(f'Average profit:{ave_profit}')


#######KIRSTY######
#FORMATTING DF TO SHOW SLS, PROFIT, EXPENDITURE ONLY
new_df = df.drop(['year','sales_pct_change','profit_pct_change'],1)
print(new_df)

#MELTING DATAFRAME TO PREP FOR GRAPH SHOWING SLS, PROFIT AND EXPENDITURE
df_melt = pd.melt(new_df, id_vars=['month'])
print(df_melt)


#PLOTTING SALES AND PROFIT GRAPH
sns.set_theme()

sns.relplot(
    data = df,
    x="month", y="sales", kind="line")

plt.show()

#sns.relplot(
    #data = df,
    #x="month", y="profit", kind="line")

#plt.show()


#PLOTTING MELTED DF OF SLS, PROFIT, EXPENDITURE
sns.relplot(
    data = df_melt, kind="line",
    x="month", y="value", hue="variable")

plt.show()

