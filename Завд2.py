import pandas as pd
import matplotlib.pyplot as plt
import calendar

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 10)

file_path = r'D:\Zavd2\comptagevelo2011.csv'  # Замініть на свій шлях до файлу

try:
    fixed_df = pd.read_csv(file_path, sep=',', encoding='latin1', header=0, parse_dates=['Date'], dayfirst=True)
except Exception as e:
    print(f"Помилка при читанні файлу: {e}")
    exit()

print("Інформація про дані:")
print(fixed_df.info())

fixed_df.set_index('Date', inplace=True)

numeric_cols = fixed_df.select_dtypes(include=['number'])
if numeric_cols.empty:
    print("Помилка: У таблиці немає числових даних для аналізу.")
    exit()

fixed_df['Month'] = fixed_df.index.month

monthly_totals = fixed_df.groupby('Month')[numeric_cols.columns].sum().sum(axis=1)

most_popular_month = monthly_totals.idxmax()
most_popular_count = monthly_totals.max()

month_name = calendar.month_name[most_popular_month]

print(f"Найпопулярніший місяць: {month_name} (Місяць №{most_popular_month})")
print(f"Загальна кількість велосипедистів у цьому місяці: {most_popular_count}")

numeric_cols.plot(figsize=(15, 10), title="Використання велодоріжок протягом року")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.legend(title="Локації")
plt.show()
