import pandas as pd
import os

folder = "C:/Users/Jerry/Desktop/"

file_cancer = next((f for f in os.listdir(folder) if "cancer" in f.lower() and f.endswith(".csv")), None)
file_heart = next((f for f in os.listdir(folder) if "heart" in f.lower() and f.endswith(".csv")), None)

if file_cancer:
    df_c = pd.read_csv(os.path.join(folder, file_cancer))
    print(f"--- ANALIZA: {file_cancer} ---")
    print(f"Próbki: {df_c.shape[0]}, Kolumny: {df_c.shape[1]}")
    col = 'diagnosis' if 'diagnosis' in df_c.columns else df_c.columns[-1]
    print(f"Klasy w kolumnie '{col}':\n{df_c[col].value_counts()}\n")
else:
    print("Nie znaleziono pliku z 'cancer' w nazwie na Pulpicie!")

if file_heart:
    df_h = pd.read_csv(os.path.join(folder, file_heart))
    print(f"--- ANALIZA: {file_heart} ---")
    print(f"Próbki: {df_h.shape[0]}, Kolumny: {df_h.shape[1]}")
    col_h = 'target' if 'target' in df_h.columns else df_h.columns[-1]
    print(f"Klasy w kolumnie '{col_h}':\n{df_h[col_h].value_counts()}")