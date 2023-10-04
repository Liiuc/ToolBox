import pandas as pd      

def generate_excel(input_file_path, output_file_path):
    df = pd.read_excel(input_file_path)

    # Filtro sull 'Anno' 
    df_2023 = df[df['Anno'] == 2017]

    # Rimuove le colonne con prezzi negativi (prima era >= 0)
    df_2023 = df_2023[df_2023['Prezzo'] > 0]

    # prende solo le righe dove il valore di 'StatoConsegnato' e' diverso da 'A' 
    df_2023 = df_2023[df_2023['StatoConsegnato'] != 'A']

    df_2023 = df_2023[df_2023['TipoVendita'] == 'WINTER SALES']

    df_2023 = df_2023[df_2023['ProductType'].str.contains('SPR')]

    #conta il numero di occorrenze di ogni modello
    modello_counts = df_2023['Modello'].value_counts().reset_index() 
    modello_counts.columns = ['Modello', 'Count']

    #SEZIONE AZIONAMENTO
    adw_counts = df_2023[df_2023['Azionamento'] == 'A/DW'].groupby('Modello').size().reset_index()     # Conta quanti 'A/DW' in 'Azionamento' il tutto diviso per 'Modello'
    adw_counts.columns = ['Modello', 'A/DW']
    result_df = pd.merge(modello_counts, adw_counts, on='Modello', how='left')      # Unisce i due contatori puntando sulla colonna Modello
    result_df['A/DW'].fillna(0, inplace=True)        # Sostituisce i valori nulli (NaN) con il valore 0  

    aid_counts = df_2023[df_2023['Azionamento'] == 'A/ID'].groupby('Modello').size().reset_index()
    aid_counts.columns = ['Modello', 'A/ID']
    result_df = pd.merge(result_df, aid_counts, on='Modello', how='left')
    result_df['A/ID'].fillna(0, inplace=True)

    ad_counts = df_2023[df_2023['Azionamento'] == 'A/D'].groupby('Modello').size().reset_index()
    ad_counts.columns = ['Modello', 'A/D']
    result_df = pd.merge(result_df, ad_counts, on='Modello', how='left')
    result_df['A/D'].fillna(0, inplace=True)

    adf_counts = df_2023[df_2023['Azionamento'] == 'A/D-F'].groupby('Modello').size().reset_index()
    adf_counts.columns = ['Modello', 'A/D-F']
    result_df = pd.merge(result_df, adf_counts, on='Modello', how='left')
    result_df['A/D-F'].fillna(0, inplace=True)

    adr_counts = df_2023[df_2023['Azionamento'] == 'A/D-R'].groupby('Modello').size().reset_index()
    adr_counts.columns = ['Modello', 'A/D-R']
    result_df = pd.merge(result_df, adr_counts, on='Modello', how='left')
    result_df['A/D-R'].fillna(0, inplace=True)

    aho_counts = df_2023[df_2023['Azionamento'] == 'A/HO'].groupby('Modello').size().reset_index()
    aho_counts.columns = ['Modello', 'A/HO']
    result_df = pd.merge(result_df, aho_counts, on='Modello', how='left')
    result_df['A/HO'].fillna(0, inplace=True)

    ahof_counts = df_2023[df_2023['Azionamento'] == 'A/HO-F'].groupby('Modello').size().reset_index()
    ahof_counts.columns = ['Modello', 'A/HO-F']
    result_df = pd.merge(result_df, ahof_counts, on='Modello', how='left')
    result_df['A/HO-F'].fillna(0, inplace=True)

    ahor_counts = df_2023[df_2023['Azionamento'] == 'A/HO-R'].groupby('Modello').size().reset_index()
    ahor_counts.columns = ['Modello', 'A/HO-R']
    result_df = pd.merge(result_df, ahor_counts, on='Modello', how='left')
    result_df['A/HO-R'].fillna(0, inplace=True)

    ae_counts = df_2023[df_2023['Azionamento'] == 'A/E'].groupby('Modello').size().reset_index()
    ae_counts.columns = ['Modello', 'A/E']
    result_df = pd.merge(result_df, ae_counts, on='Modello', how='left')
    result_df['A/E'].fillna(0, inplace=True)

    apf14_counts = df_2023[df_2023['Azionamento'] == 'A/PF14'].groupby('Modello').size().reset_index()
    apf14_counts.columns = ['Modello', 'A/PF14']
    result_df = pd.merge(result_df, apf14_counts, on='Modello', how='left')
    result_df['A/PF14'].fillna(0, inplace=True)

    apf38_counts = df_2023[df_2023['Azionamento'] == 'A/PF38'].groupby('Modello').size().reset_index()
    apf38_counts.columns = ['Modello', 'A/PF38']
    result_df = pd.merge(result_df, apf38_counts, on='Modello', how='left')
    result_df['A/PF38'].fillna(0, inplace=True)  

    #Tramoggia
    m8_counts = df_2023[df_2023['Tramoggia'] == 'M8'].groupby('Modello').size().reset_index()
    m8_counts.columns = ['Modello', 'M8']
    result_df = pd.merge(result_df, m8_counts, on='Modello', how='left')
    result_df['M8'].fillna(0, inplace=True)   

    m15_counts = df_2023[df_2023['Tramoggia'] == 'M15'].groupby('Modello').size().reset_index()
    m15_counts.columns = ['Modello', 'M15']
    result_df = pd.merge(result_df, m15_counts, on='Modello', how='left')
    result_df['M15'].fillna(0, inplace=True) 

    m23_counts = df_2023[df_2023['Tramoggia'] == 'M23'].groupby('Modello').size().reset_index()
    m23_counts.columns = ['Modello', 'M23']
    result_df = pd.merge(result_df, m23_counts, on='Modello', how='left')
    result_df['M23'].fillna(0, inplace=True)
    

    #Umidificatore
    u1_counts = df_2023[df_2023['Umidificatore'] == 'U1'].groupby('Modello').size().reset_index()
    u1_counts.columns = ['Modello', 'U1']
    result_df = pd.merge(result_df, u1_counts, on='Modello', how='left')
    result_df['U1'].fillna(0, inplace=True)   

    u12_counts = df_2023[df_2023['Umidificatore'] == 'U12'].groupby('Modello').size().reset_index()
    u12_counts.columns = ['Modello', 'U12']
    result_df = pd.merge(result_df, u12_counts, on='Modello', how='left')
    result_df['U12'].fillna(0, inplace=True) 

    u2n_counts = df_2023[df_2023['Umidificatore'] == 'U2/N'].groupby('Modello').size().reset_index()
    u2n_counts.columns = ['Modello', 'U2/N']
    result_df = pd.merge(result_df, u2n_counts, on='Modello', how='left')
    result_df['U2/N'].fillna(0, inplace=True)

    #Asimmetria
    c3_counts = df_2023[df_2023['Varie'].str.contains(r'(?i)C3(?!M|P)', na=False, regex=True)].groupby('Modello').size().reset_index()
    c3_counts.columns = ['Modello', 'C3']
    result_df = pd.merge(result_df, c3_counts, on='Modello', how='left')
    result_df['C3'].fillna(0, inplace=True)

    c3m_counts = df_2023[df_2023['Varie'].str.contains('C3M', na=False)].groupby('Modello').size().reset_index()
    c3m_counts.columns = ['Modello', 'C3M']
    result_df = pd.merge(result_df, c3m_counts, on='Modello', how='left')
    result_df['C3M'].fillna(0, inplace=True)

    c3p_counts = df_2023[df_2023['Varie'].str.contains('C3P', na=False)].groupby('Modello').size().reset_index()
    c3p_counts.columns = ['Modello', 'C3P']
    result_df = pd.merge(result_df, c3p_counts, on='Modello', how='left')
    result_df['C3P'].fillna(0, inplace=True)

    #luci L7
    l7_counts = df_2023[df_2023['Varie'].str.contains(r'(?i)L7(?!A|S|^IE/L7$|^IE/L7A$|^IE/L7S$)', na=False, regex=True)].groupby('Modello').size().reset_index()
    l7_counts.columns = ['Modello', 'L7']
    result_df = pd.merge(result_df, l7_counts, on='Modello', how='left')
    result_df['L7'].fillna(0, inplace=True)

    #COMANDI
    c120_counts = df_2023[df_2023['Varie'].str.contains('C1/20', na=False)].groupby('Modello').size().reset_index()
    c120_counts.columns = ['Modello', 'C1/20']
    result_df = pd.merge(result_df, c120_counts, on='Modello', how='left')
    result_df['C1/20'].fillna(0, inplace=True)

    c1620_counts = df_2023[df_2023['Varie'].str.contains('C16/20', na=False)].groupby('Modello').size().reset_index()
    c1620_counts.columns = ['Modello', 'C16/20']
    result_df = pd.merge(result_df, c1620_counts, on='Modello', how='left')
    result_df['C16/20'].fillna(0, inplace=True)

    c1_counts = df_2023[df_2023['Comando'] == 'C1'].groupby('Modello').size().reset_index()
    c1_counts.columns = ['Modello', 'C1']
    result_df = pd.merge(result_df, c1_counts, on='Modello', how='left')
    result_df['C1'].fillna(0, inplace=True)

    c116_counts = df_2023[df_2023['Varie'].str.contains('C1/16', na=False)].groupby('Modello').size().reset_index()
    c116_counts.columns = ['Modello', 'C1/16']
    result_df = pd.merge(result_df, c116_counts, on='Modello', how='left')
    result_df['C1/16'].fillna(0, inplace=True)

    c1le_counts = df_2023[df_2023['Comando'] == 'C1/LE'].groupby('Modello').size().reset_index()
    c1le_counts.columns = ['Modello', 'C1/LE']
    result_df = pd.merge(result_df, c1le_counts, on='Modello', how='left')
    result_df['C1/LE'].fillna(0, inplace=True)

    c16_counts = df_2023[df_2023['Varie'].str.contains(r'(?i)C16(?!/20\s|/P|^C16S$)', na=False, regex=True)].groupby('Modello').size().reset_index()
    c16_counts.columns = ['Modello', 'C16']
    result_df = pd.merge(result_df, c16_counts, on='Modello', how='left')
    result_df['C16'].fillna(0, inplace=True)

    c37_counts = df_2023[df_2023['Comando'] == 'C37'].groupby('Modello').size().reset_index()
    c37_counts.columns = ['Modello', 'C37']
    result_df = pd.merge(result_df, c37_counts, on='Modello', how='left')
    result_df['C37'].fillna(0, inplace=True)

    c19_counts = df_2023[df_2023['Comando'] == 'C19'].groupby('Modello').size().reset_index()
    c19_counts.columns = ['Modello', 'C19']
    result_df = pd.merge(result_df, c19_counts, on='Modello', how='left')
    result_df['C19'].fillna(0, inplace=True)

    c0_counts = df_2023[df_2023['Comando'] == 'C0'].groupby('Modello').size().reset_index()
    c0_counts.columns = ['Modello', 'C0']
    result_df = pd.merge(result_df, c0_counts, on='Modello', how='left')
    result_df['C0'].fillna(0, inplace=True)    

    #SpreadingGroup     
    m28r_counts = df_2023[df_2023['Varie'].str.contains('M28R/', na=False)].groupby('Modello').size().reset_index()
    m28r_counts.columns = ['Modello', 'M28R/']
    result_df = pd.merge(result_df, m28r_counts, on='Modello', how='left')
    result_df['M28R/'].fillna(0, inplace=True)

    m28p_counts = df_2023[df_2023['Varie'].str.contains('M28P/', na=False)].groupby('Modello').size().reset_index()
    m28p_counts.columns = ['Modello', 'M28P/']
    result_df = pd.merge(result_df, m28p_counts, on='Modello', how='left')
    result_df['M28P/'].fillna(0, inplace=True)

    m28_counts = df_2023[df_2023['Varie'].str.contains('M28/', na=False)].groupby('Modello').size().reset_index()
    m28_counts.columns = ['Modello', 'M28/']
    result_df = pd.merge(result_df, m28_counts, on='Modello', how='left')
    result_df['M28/'].fillna(0, inplace=True)

    m28l_counts = df_2023[df_2023['Varie'].str.contains('M28L/', na=False)].groupby('Modello').size().reset_index()
    m28l_counts.columns = ['Modello', 'M28L/']
    result_df = pd.merge(result_df, m28l_counts, on='Modello', how='left')
    result_df['M28L/'].fillna(0, inplace=True)

    #Sensore sale
    c7_counts = df_2023[df_2023['Varie'].str.contains(r'(?i)C7(?!/I)', na=False, regex=True)].groupby('Modello').size().reset_index()
    c7_counts.columns = ['Modello', 'C7']
    result_df = pd.merge(result_df, c7_counts, on='Modello', how='left')
    result_df['C7'].fillna(0, inplace=True)

    c7i_counts = df_2023[df_2023['Varie'].str.contains('C7/I', na=False)].groupby('Modello').size().reset_index()
    c7i_counts.columns = ['Modello', 'C7/I']
    result_df = pd.merge(result_df, c7i_counts, on='Modello', how='left')
    result_df['C7/I'].fillna(0, inplace=True)

    #flashlight
    l6_counts = df_2023[df_2023['Varie'].str.contains('L6', na=False)].groupby('Modello').size().reset_index()
    l6_counts.columns = ['Modello', 'L6']
    result_df = pd.merge(result_df, l6_counts, on='Modello', how='left')
    result_df['L6'].fillna(0, inplace=True)

    #Piedi
    p1_counts = df_2023[df_2023['Piedi'] == 'P1'].groupby('Modello').size().reset_index()
    p1_counts.columns = ['Modello', 'P1']
    result_df = pd.merge(result_df, p1_counts, on='Modello', how='left')
    result_df['P1'].fillna(0, inplace=True)

    p3_counts = df_2023[df_2023['Piedi'] == 'P3'].groupby('Modello').size().reset_index()
    p3_counts.columns = ['Modello', 'P3']
    result_df = pd.merge(result_df, p3_counts, on='Modello', how='left')
    result_df['P3'].fillna(0, inplace=True)

    #Luci L2 e L1(L2 è IN TO DO)
    #l2_counts = df_2023[df_2023['Varie'].str.contains(r'(?i)L2(?!0$|/M|^L20$|^L2/M$|^L20/UK$|^L21$|^L22$|^L25$)', na=False, regex=True)].groupby('Modello').size().reset_index()
    #l2_counts.columns = ['Modello', 'L2']
    #result_df = pd.merge(result_df, l2_counts, on='Modello', how='left')
    #result_df['L2'].fillna(0, inplace=True)
 
    #Tettuccio
    t0_counts = df_2023[df_2023['Tettuccio'] == 'T0'].groupby('Modello').size().reset_index()
    t0_counts.columns = ['Modello', 'T0']
    result_df = pd.merge(result_df, t0_counts, on='Modello', how='left')
    result_df['T0'].fillna(0, inplace=True)

    t1x_counts = df_2023[df_2023['Tettuccio'] == 'T1/X'].groupby('Modello').size().reset_index()
    t1x_counts.columns = ['Modello', 'T1/X']
    result_df = pd.merge(result_df, t1x_counts, on='Modello', how='left')
    result_df['T1/X'].fillna(0, inplace=True)

    #Codici Z
    z4_counts = df_2023[df_2023['Varie'].str.contains('Z4', na=False)].groupby('Modello').size().reset_index()
    z4_counts.columns = ['Modello', 'Z4']
    result_df = pd.merge(result_df, z4_counts, on='Modello', how='left')
    result_df['Z4'].fillna(0, inplace=True)

    z5_counts = df_2023[df_2023['Varie'].str.contains('Z5', na=False)].groupby('Modello').size().reset_index()
    z5_counts.columns = ['Modello', 'Z5']
    result_df = pd.merge(result_df, z5_counts, on='Modello', how='left')
    result_df['Z5'].fillna(0, inplace=True)    

    #Sovrasponde
    t5_counts = df_2023[df_2023['Sovrasponde'] == 'T5'].groupby('Modello').size().reset_index()
    t5_counts.columns = ['Modello', 'T5']
    result_df = pd.merge(result_df, t5_counts, on='Modello', how='left')
    result_df['T5'].fillna(0, inplace=True)

    t52_counts = df_2023[df_2023['Sovrasponde'] == 'T5/2'].groupby('Modello').size().reset_index()
    t52_counts.columns = ['Modello', 'T5/2']
    result_df = pd.merge(result_df, t52_counts, on='Modello', how='left')
    result_df['T5/2'].fillna(0, inplace=True)

    t53_counts = df_2023[df_2023['Sovrasponde'] == 'T5/3'].groupby('Modello').size().reset_index()
    t53_counts.columns = ['Modello', 'T5/3']
    result_df = pd.merge(result_df, t53_counts, on='Modello', how='left')
    result_df['T5/3'].fillna(0, inplace=True)

    t54_counts = df_2023[df_2023['Sovrasponde'] == 'T5/4'].groupby('Modello').size().reset_index()
    t54_counts.columns = ['Modello', 'T5/4']
    result_df = pd.merge(result_df, t54_counts, on='Modello', how='left')
    result_df['T5/4'].fillna(0, inplace=True)

    t55_counts = df_2023[df_2023['Sovrasponde'] == 'T5/5'].groupby('Modello').size().reset_index()
    t55_counts.columns = ['Modello', 'T5/5']
    result_df = pd.merge(result_df, t55_counts, on='Modello', how='left')
    result_df['T5/5'].fillna(0, inplace=True)

    t56_counts = df_2023[df_2023['Sovrasponde'] == 'T5/6'].groupby('Modello').size().reset_index()
    t56_counts.columns = ['Modello', 'T5/6']
    result_df = pd.merge(result_df, t56_counts, on='Modello', how='left')
    result_df['T5/6'].fillna(0, inplace=True)

    t57_counts = df_2023[df_2023['Sovrasponde'] == 'T5/7'].groupby('Modello').size().reset_index()
    t57_counts.columns = ['Modello', 'T5/7']
    result_df = pd.merge(result_df, t57_counts, on='Modello', how='left')
    result_df['T5/7'].fillna(0, inplace=True)

    t58_counts = df_2023[df_2023['Sovrasponde'] == 'T5/8'].groupby('Modello').size().reset_index()
    t58_counts.columns = ['Modello', 'T5/8']
    result_df = pd.merge(result_df, t58_counts, on='Modello', how='left')
    result_df['T5/8'].fillna(0, inplace=True)    

    t59_counts = df_2023[df_2023['Sovrasponde'] == 'T5/9'].groupby('Modello').size().reset_index()
    t59_counts.columns = ['Modello', 'T5/9']
    result_df = pd.merge(result_df, t59_counts, on='Modello', how='left')
    result_df['T5/9'].fillna(0, inplace=True)  

    t511_counts = df_2023[df_2023['Sovrasponde'] == 'T5/11'].groupby('Modello').size().reset_index()
    t511_counts.columns = ['Modello', 'T5/11']
    result_df = pd.merge(result_df, t511_counts, on='Modello', how='left')
    result_df['T5/11'].fillna(0, inplace=True)      

    t512_counts = df_2023[df_2023['Sovrasponde'] == 'T5/12'].groupby('Modello').size().reset_index()
    t512_counts.columns = ['Modello', 'T5/12']
    result_df = pd.merge(result_df, t512_counts, on='Modello', how='left')
    result_df['T5/12'].fillna(0, inplace=True)    

    t516_counts = df_2023[df_2023['Sovrasponde'] == 'T5/16'].groupby('Modello').size().reset_index()
    t516_counts.columns = ['Modello', 'T5/16']
    result_df = pd.merge(result_df, t516_counts, on='Modello', how='left')
    result_df['T5/16'].fillna(0, inplace=True)    

    #crea nuovo file excel e inserisce all'interno il df dei risultati
    result_df.to_excel(output_file_path, index=False)


#Main : 

input_file_path = 'ESTRAPOLAZIONE VENDITE 11.09.2023.xlsx'  
output_file_path = 'Analisi vendite 2017.xlsx'  
generate_excel(input_file_path, output_file_path)

