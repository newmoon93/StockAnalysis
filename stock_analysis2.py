# https://bigdata-doctrine.tistory.com/5
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

samsung = fdr.DataReader("005930")
samsung_first_date = str(samsung.index[0])[:10]  # 삼성의 첫번째 데이터의 날짜, 추후 변동 가능
apple = fdr.DataReader("aapl", samsung_first_date)
print(apple.head())

samsung_isna = samsung.isna().sum()
#apple_isna = apple.isna().sum()
samsung = samsung.fillna(0)

print(samsung.head())
sam_change_cp = ((samsung["Change"]+1).cumprod()-1)
sam_exp = (samsung["Close"] / samsung["Close"][samsung_first_date])
#aapl_change_cp = ((apple["Change"]+1).cumprod()-1)

plt.figure(figsize=(15,10))
plt.plot(sam_change_cp, label="SAMSUNG")
plt.plot(sam_exp, label="SAMSUNG")
#plt.plot(aapl_change_cp, label="APPLE")
plt.legend(fontsize=16)

plt.show()