import pickle

import streamlit as st
import pandas as pd
import pickle as pk
import warnings


warnings.filterwarnings('ignore')

model = pickle.load(open('model.pkl', 'rb'))
train_path = "cleaned_data/train.csv"
real = "zingat_house_price_prediction.csv"
mahalle_file = 'mahalle_data.xlsx'


mahalle_data = pd.read_excel(mahalle_file)
def inputsToDummy(df):
   df = pd.get_dummies(df, columns=["MAHALLE","NET","ODA_SAYISI"], dtype=int)
   return df

st.title('House Price Prediction')


MAHALLE = st.selectbox(
    'Mahalle Secin',
    ('İmbatlı',
    'Mavişehir',
    'Goncalar',
    'Bostanlı',
    'Şemikler',
    'Aksoy',
    'Bahriye Üçok',
    'Donanmacı',
    'Demirköprü',
    'İnönü',
    'Bahçelievler',
    'Yalı',
    'Örnekköy',
    'Atakent',
    'Alaybey',
    'Nergiz',
    'Fikri Altay',
    'Tersane',
    'Mustafa Kemal',
    'Dedebaşı',
    'Tuna',
    'Bahariye',
    'Zübeyde Hanım',
    'Latife Hanım',
    'Cumhuriyet')
)

NET = st.number_input('Net metrekare')
ODA_SAYISI = st.number_input('Oda sayisi', min_value=0, max_value=10)

house_data = {
    'Net metrekare': [NET],
    'Oda sayisi': [ODA_SAYISI],
    'Mahalle' : [MAHALLE]
}

df = pd.DataFrame(house_data)
df=inputsToDummy(df)

data_train = pd.read_excel(train_path)
expected_columns_order = data_train.columns
df = df.reindex(columns=expected_columns_order, fill_value=0)

prediction = model.predict(df)
prediction=round(prediction[0],2)
st.write(f"Predicted price: {prediction} TL")