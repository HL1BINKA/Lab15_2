import pandas as pd
import matplotlib.pyplot as plt

# Налаштування стилю для графіків
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 10)

# Шлях до файлу з даними
file_path = r'D:\Zavd2\comptagevelo2011.csv'  # Замініть на свій шлях до файлу

try:
    fixed_df = pd.read_csv(file_path, sep=',', encoding='latin1', header=0, parse_dates=['Date'], dayfirst=True)
except Exception as e:
    print(f"Помилка при читанні файлу: {e}")
    exit()

print("Перші кілька рядків даних:\n", fixed_df.head(3))

fixed_df.set_index('Date', inplace=True)
fixed_df.plot(figsize=(15, 10), title="Використання велодоріжок протягом року")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.legend(title="Локації")
plt.show()

