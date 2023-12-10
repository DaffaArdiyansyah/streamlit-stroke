# load library
import pickle
import streamlit as st

# load save model/ Model yang telah dibuat sebelumnya
ranFor = pickle.load(open('stroke_RF_Model.sav','rb'))

# judul/Title web
st.title('Prediksi Penyakit Stroke')
st.markdown("""
### ini merupakan aplikasi web berbasis Machine Learning untuk prediksi penyakit stroke dengan random forest
### Dibuat oleh: kelompok 9 
Anggota: 1. Daffa Ardiyansyah
         2. Pramudya Raka Utomo
         3. Alyan Muhammad Dainury Iskandar
            
________________________________________________________________________________________________
            
""")

## Kolom Inputan 

#Inputan untuk feature Gender
optionGender = st.selectbox(        
    'Pilih Jenis Kelamin (Gender) :',
    ('Male/Pria','Female/Wanita'),
    )

if optionGender == 'Male/Pria':
    gender = 1
elif optionGender == 'Female/Wanita':
    gender = 0

#Inputan untuk feature Age
age = st.slider("Inputkan Nilai Umur (Age) :",1,100) 

#Inputan untuk feature hypertension
optionhypertension = st.selectbox(
    'Punya Hipertensi (hypertension) ?:',   
    ('Yes/1','No/0'),
    )
if optionhypertension == 'Yes/1':
    hypertension = 1
elif optionhypertension == 'No/0':
    hypertension = 0

#Inputan untuk feature heart_disease
optionheart_disease = st.selectbox(
    'Punya Penyakit Jantung (heart_disease) ?:',   
    ('Yes/1','No/0'),
    )
if optionheart_disease == 'Yes/1':
    heart_disease = 1
elif optionheart_disease == 'No/0':
    heart_disease = 0

#Inputan untuk feature ever_married
optionever_married = st.selectbox(
    'Pernah Menikah (ever_married) ?:',   
    ('Yes','No'),
    )
if optionever_married == 'Yes':
    ever_married = 1
elif optionever_married == 'No':
    ever_married = 0

#Inputan untuk feature work_type
optionwork_type = st.selectbox(
    'Pilih Tipe Pekerjaan (work_type) :',   
    ('Private','Self-employed','Govt_job','children','Never_worked'),
    )
if optionwork_type == 'Private':
    work_type = 2
elif optionwork_type == 'Self-employed':
    work_type = 3
elif optionwork_type == 'Govt_job':
    work_type = 0
elif optionwork_type == 'children':
    work_type = 4
elif optionwork_type == 'Never_worked':
    work_type = 1

#Inputan untuk feature Residence_type
optionResidence_type = st.selectbox(
    'Pilih Tipe Tempat Tinggal (Residence_type) :',   
    ('Urban','Rural'),
    )
if optionResidence_type == 'Urban':
    Residence_type = 1
elif optionResidence_type == 'Rural':
    Residence_type = 0

#Inputan untuk feature avg_glucose_level dengan st.number
avg_glucose_level = st.number_input("Inputkan Nilai rata-rata kadar glukosa (avg_glucose_level) :")

#Inputan untuk feature bmi dengan st.number
bmi = st.number_input("Inputkan Nilai Body Mass Index (bmi) :")

#Inputan untuk feature smoking_status
optionsmoking_status = st.selectbox(
    'Pilih Status Merokok (smoking_status) :',   
    ('formerly smoked','never smoked','smokes'),
    )
if optionsmoking_status == 'formerly smoked':
    smoking_status = 0
elif optionsmoking_status == 'never smoked':
    smoking_status = 1
elif optionsmoking_status == 'smokes':
    smoking_status = 2


# Variabel untuk menyimpan prediksi
stroke_diagnosis = ''

# Membuat tombol prediksi
if st.button("Prediski Penyakit jantung"):
    # Melakukan prediksi/clasifikasi knn berdasarkan Nilai yang telah di inputkan
    stroke_diagnosis= ranFor.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])

    # statment hasil dari prediksi :
    if (stroke_diagnosis[0]==0):
        st.write(stroke_diagnosis[0])
        heart_diagnosis='Pasien Tidak Terkena Penyakit Stroke'
        st.success(heart_diagnosis) # memberi background warna hijau
    else:
        st.write(stroke_diagnosis[0])
        heart_diagnosis= 'Pasien Terkena Penyakit Stroke'
        st.error(heart_diagnosis) # memberi background warna Merah
