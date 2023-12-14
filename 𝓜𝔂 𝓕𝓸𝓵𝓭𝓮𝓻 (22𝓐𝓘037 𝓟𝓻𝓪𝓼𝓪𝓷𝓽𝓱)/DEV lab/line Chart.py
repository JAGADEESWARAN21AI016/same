import datetime
import pandas as pd
import random

def generateData(n):
    listdata = []
    start = datetime.datetime(2019, 8, 1)
    end = datetime.datetime(2019, 8, 30)
    delta = end - start
    for _ in range(n):
        random_days = random.randint(0, delta.days)
        date = (start + datetime.timedelta(days=random_days)).strftime("%y-%m-%d")
        price = round(random.uniform(900, 1000), 4)
        listdata.append([date, price])

    df = pd.DataFrame(listdata, columns=['Date', 'Price'])
    df['Date'] = pd.to_datetime(df['Date'], format='%y-%m-%d')
    df = df.groupby(by='Date').mean()

    return df

data = generateData(10z)  # Replace 10 with the number of data points you want
print(data)




 
