
import pandas as pd
import numpy as np
import streamlit as st
import joblib

df = pd.read_pickle('df_RFM_final2.pkl')
Merchants_dict = joblib.load('Merchants_dict.pkl')

def Top_3_Merchants(user_id):
    
    ## In Case that User exist in one Cluster
    if np.size(np.unique(df.loc[user_id]['Cluster'])) == 1:
        return Merchants_dict[df.loc[user_id]['Cluster']]
    ## In Case that User exist in the 2 Clusters
    elif np.size(np.unique(df.loc[user_id]['Cluster'])) == 2:
        merchant_list = []
        merchant_list.append(Merchants_dict[np.unique(df.loc[user_id]['Cluster'].values)[0]][0]) ## First Merchant in First cluster
        merchant_list.append(Merchants_dict[np.unique(df.loc[user_id]['Cluster'].values)[0]][1]) ## Second Merchant in First Cluster 
        merchant_list.append(Merchants_dict[np.unique(df.loc[user_id]['Cluster'].values)[1]][0]) ## First Merchant in Second Cluster
        return merchant_list
    ## In Case that User exist in the 3 Clusters
    else:
        merchant_list = []
        merchant_list.append(Merchants_dict[np.unique(df.loc[user_id]['Cluster'].values)[0]][0]) ## First Merchant in First Cluster
        merchant_list.append(Merchants_dict[np.unique(df.loc[user_id]['Cluster'].values)[1]][0]) ## First Merchant in Second Cluster
        merchant_list.append(Merchants_dict[np.unique(df.loc[user_id]['Cluster'].values)[2]][0]) ## First Merchant in Third Cluster
        return merchant_list
            
        
def Main():
    st.title('Customer Segmentation')
    user_id = st.number_input("User ID: ",format="%d", step=1, value=0)
    if st.button('Show Merchants'):
        if user_id in df.index:
            merchants = Top_3_Merchants(user_id)
            st.text(f'The user can spend his/her points in : \n 1- {merchants[0]}\n 2- {merchants[1]}\n 3- {merchants[2]}')
        else:
            st.text("User ID doesn't exist !!")
    
Main()
