import os 
import pandas as pd
import matplotlib.pyplot as plt

# beinhaltet: Zeitoperationen; Vorarbeitung; Vorverarbeitung; Imputation;

base_path = r"C:\Users\phili\OneDrive\Dokumente\Uni\Sem_3\Python\prv\ml\ml_beg"
file_name_jena_complete = "jena_climate_complete_hourly.csv"
file_name_jena_temp = "jena_climate_temp_monthly.csv"
file_path = os.path.join(base_path, file_name_jena_complete)


df = pd.DataFrame()
df = pd.read_csv(file_path)
#if jena_complete
df = df[['Date Time', 'p (mbar)', 'T (degC)']]


df['date'] = pd.to_datetime(df['Date Time'])
df.drop(axis=1, columns=['Date Time'], inplace=True)
#df['month'] = df['date'].dt.month


df.set_index('date', inplace=True)


df = df.resample(rule='H').mean()


#df['Lag_1'] = df['T (degC)'].shift(periods=1) --> diff1 --> Value Spalte - Lag_1
df['diff1'] = df['T (degC)'].diff() # --> zyklisch unabhängig


df['diff1'].fillna(method='bfill', inplace=True)


df_C_Plot = df['T (degC)'].rolling(window=1000, center=True).mean() # --> Glättung / --> gute Imputation nächste Zeile:
#df[Spalte mit nans].fillna(Inplace=True, value=df['...'].rolling(window=..., center=...).mean())



#-------------------------------------------------------------------------------------------------------
#print(df)
#print(df.head(5))
#print(df['2010-01-02':'2010-04-02'])
#print(df[df.index.month == 5])
#print(df.index.freq) # ggf. bei resample
#print(df.isna().sum()) #bzw. print(df[df.isna().any(axis=1)])
#-------------------------------------------------------------------------------------------------------


df_C_Plot.plot()
plt.show()