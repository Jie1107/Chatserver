import pandas as pd
from datetime import datetime

# 創建一個空的DataFrame來存儲ETF購買紀錄
columns = ['購買日期', 'ETF代碼', '購買價格', '購買數量']
df = pd.DataFrame(columns=columns)

# 添加一個ETF購買紀錄
buy_date = datetime.now().strftime('%Y-%m-%d')  # 獲取當前日期
etf_code = '0050'
buy_price = 100.0
buy_quantity = 10
df = df.append({'購買日期': buy_date, 'ETF代碼': etf_code, '購買價格': buy_price, '購買數量': buy_quantity}, ignore_index=True)

# 保存ETF購買紀錄到CSV檔案
df.to_csv('etf_purchase_records.csv', index=False, encoding='utf-8')