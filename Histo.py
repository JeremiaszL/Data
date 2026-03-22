import pandas as pd
import matplotlib.pyplot as plt
import os

sciezka = "C:/Users/Jerry/Desktop/cancer.csv"

if not os.path.exists(sciezka):
    print(f"BŁĄD: Dalej nie widzę pliku {sciezka}!")
    print("Pliki CSV na pulpicie to:", [f for f in os.listdir("C:/Users/Jerry/Desktop/") if f.endswith('.csv')])
else:
    df = pd.read_csv(sciezka)

    cechy_numeryczne = df.select_dtypes(include=['float64', 'int64']).columns
    cecha = cechy_numeryczne[1] if len(cechy_numeryczne) > 1 else cechy_numeryczne[0]

    diag_col = 'diagnosis' if 'diagnosis' in df.columns else df.columns[1]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    df[cecha].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram: {cecha}')

    plt.subplot(1, 2, 2)
    df.boxplot(column=cecha, by=diag_col)
    plt.title(f'{cecha} vs {diag_col}')
    plt.suptitle('')

    print("Generuję wykresy... Jeśli nic się nie pojawia, sprawdź czy nie otworzyły się w tle.")
    plt.tight_layout()
    plt.show()