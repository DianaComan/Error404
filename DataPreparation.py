import numpy as np
import pandas as pd
          
name_dict=pd.read_csv("Date antrenare (2).csv")
pd.set_option('mode.chained_assignment', None)

df = pd.DataFrame(name_dict)

for ind in df.index: 
  if ((str(df['vârstă'][ind]) in (None, "", "nan",'NaN' )) & 
      (str(df['data rezultat testare'][ind]) in (None, "", "nan", 'NaN'))):
    df.drop(df.index[ind])

for i in  df.index:
   if not (type(df['data rezultat testare'][i]) is str):
     df['data rezultat testare'][i] = '4-4-2020 0:00:00'
   if not ("-" in df['data rezultat testare'][i]):
     df['data rezultat testare'][i] = '5-4-2020 0:00:00'
   if not ("2020" in df['data rezultat testare'][i]):
     df['data rezultat testare'][i] = '3-4-2020 0:00:00'
   elif (not (len(df['data rezultat testare'][i])==19)):
     df['data rezultat testare'][i] = '4-5-2020 0:00:00'
   else:
     m = str(df.loc[i,'data rezultat testare'].split('-')[1])
     y = str(df.loc[i,'data rezultat testare'].split('-')[0])
     d = str(df.loc[i,'data rezultat testare'].split('-')[2].split(' ')[0])
     df['data rezultat testare'][i] = d+'-'+m+'-'+y+ ' 0:00:00'

df['data rezultat testare'] = pd.to_datetime(df['data rezultat testare'], format="%d-%m-%Y %H:%M:%S")


for ind in df.index: 
     df['mijloace de transport folosite'][ind] = str(df['mijloace de transport folosite'][ind])
     df['istoric de călătorie'][ind] = str(df['istoric de călătorie'][ind])
     df['confirmare contact cu o persoană infectată'][ind] = str(df['confirmare contact cu o persoană infectată'][ind])
     df['vârstă'][ind] = str(df['vârstă'][ind])
     df['rezultat testare'][ind] = str(df['rezultat testare'][ind])


for ind in df.index: 
     
     if ((df['sex'][ind] != 'FEMININ') & (df['sex'][ind] != 'MASCULIN')):
       df['sex'][ind] = 'FEMININ'
    # if ((df['dată internare'][ind]['year'] != 2020):
     #  df['dată internare'][ind]['year'] = 2020

     if ((df['mijloace de transport folosite'][ind]=='0')):
        df['mijloace de transport folosite'][ind] = 'NU'
     elif (('nu' in df['mijloace de transport folosite'][ind].lower()) | ('neag' in df['mijloace de transport folosite'][ind].lower())):
        df['mijloace de transport folosite'][ind] = 'NU'
     elif df['mijloace de transport folosite'][ind] in (None, "", "nan"):
        df['mijloace de transport folosite'][ind] = 'NU'
     else:
        df['mijloace de transport folosite'][ind] = 'DA'

     if ((df['istoric de călătorie'][ind]=='0')):
       df['istoric de călătorie'][ind] = 'NU'
     elif (('nu' in df['istoric de călătorie'][ind].lower()) | ('neag' in df['istoric de călătorie'][ind].lower()) | (df['istoric de călătorie'][ind].lower()=='')):
       df['istoric de călătorie'][ind] = 'NU'
     elif df['istoric de călătorie'][ind] in (None, "", "nan"):
        df['istoric de călătorie'][ind] = 'NU'
     else:
       df['istoric de călătorie'][ind] = 'DA'
     
     if ((df['confirmare contact cu o persoană infectată'][ind]=='0')):
       df['confirmare contact cu o persoană infectată'][ind] = 'NU'
     elif (('nu' in df['confirmare contact cu o persoană infectată'][ind].lower()) | ('neag' in df['confirmare contact cu o persoană infectată'][ind].lower()) | (df['confirmare contact cu o persoană infectată'][ind].lower()=='')):
       df['confirmare contact cu o persoană infectată'][ind] = 'NU'
     elif df['confirmare contact cu o persoană infectată'][ind] in (None, "", "nan"):
        df['confirmare contact cu o persoană infectată'][ind] = 'NU'
     else:
       df['confirmare contact cu o persoană infectată'][ind] = 'DA'

     if not (df['vârstă'][ind].isdigit()):
       df['vârstă'][ind] = '45'
     elif not ((int(df['vârstă'][ind])>=0) & (int(df['vârstă'][ind])<101)):
       df['vârstă'][ind] = '45'
     
     df['vârstă'][ind] = int (df['vârstă'][ind])

     
     if not ((df['rezultat testare'][ind].lower()=='pozitiv') | (df['rezultat testare'][ind]=='negativ')):
       df['rezultat testare'][ind] = 'NEGATIV'

     print(df['vârstă'][ind], df['sex'][ind], df['data rezultat testare'][ind], 
           df['mijloace de transport folosite'][ind], df['istoric de călătorie'][ind],
           df['confirmare contact cu o persoană infectată'][ind], df['rezultat testare'][ind])

