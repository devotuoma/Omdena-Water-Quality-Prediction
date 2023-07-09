import pandas as pd
from glob import glob
import pylab as pl

#%%

# read all files
fn_list=glob("./WQ*/*.csv")


D=[]
C=pd.DataFrame()
for fn in fn_list[::-1]:
    # field visits
    if 'Field' in fn:
        A=pd.read_csv(fn)
        A['Parameter'] = [i.replace('_','').replace('Sp ','') for i in A['Parameter']]
        A['fn']=fn.split('/')[1]
        C=pd.concat([C,A])
        
    else:
        
        # time series
        X=pd.read_csv(fn, header=3, sep=',')
        var = X.iloc[0][0].split(':')[-1].lstrip()#.split(' ')[0]
        var=var.replace('_','').replace('Sp ','')
        print(var)
        #X=pd.read_csv(fn, header=6, sep=',')
        df=pd.DataFrame(X.iloc[3:,:].values, columns=X.iloc[2,:].values,)
        df['Parameter']=var
        a = {x.split(':')[0].replace(' ',''):float(x.split(':')[1].replace(' ','')) for x in X.columns}
        a['fn']=fn.split('/')[1]
        for i in range(len(df)):
            val=df.iloc[i]['Value']
            ts=ts=df.iloc[0]['Timestamp']
            a['Date']=ts
            a['Parameter']=var; a['Value']=val
            D.append(a)        
            
D=pd.DataFrame(D)
 
#%% 
# process filed visits data
F=[]
for x, df1 in C.groupby(['fn', ]):
    print(x)
    for y, df2 in df1.groupby(['Date', ]):
        print(y, df2['Parameter'].unique())
        a=dict(zip(df2['Parameter'], df2['Value']))
        a['Date']=y; a['fn']=x
        F.append(a)

#%% 

# process time series data
G=[]
for x, df1 in D.groupby(['fn', ]):
    print(x)
    for y, df2 in df1.groupby(['Date', ]):
        print(y, df2['Parameter'].unique())
        a=dict(zip(df2['Parameter'], df2['Value']))
        a['Date']=y; a['fn']=x
        G.append(a)

#%% 

# save both to csv
F=pd.DataFrame(F)     
G=pd.DataFrame(G)

F.to_csv('field_visits_raw.csv', index=False)
G.to_csv('time_series_raw.csv', index=False)

#%% 

# get columns with the same name in field visits and time series
cols_same=[]
for i in F.columns:
    if i in G.columns:
        if G[i].count()>10 and F[i].count()>10: # at least 10 samples in each
            cols_same.append(i)
      
# print column names
print(cols_same)
# get shape
print(F[cols_same].shape, G[cols_same].shape)    

M = pd.concat([F[cols_same],G[cols_same]]).dropna().drop_duplicates()
M.to_csv('merged_data_clean.csv', index=False)

#%%
# make barplots couting samples (at least 40)
cols_F = F.columns[F.count()>40]
F = F[cols_F].dropna()
print(cols_F)
F.count().plot(kind='bar', title='Field Visits'); pl.show();

cols_G = G.columns[G.count()>40]
G = G[cols_G].dropna()
print(cols_G)
G.count().plot(kind='bar', title='Time Series'); pl.show();


F.to_csv('field_visits_clean.csv', index=False)
G.to_csv('time_series_clean.csv', index=False)

#%%