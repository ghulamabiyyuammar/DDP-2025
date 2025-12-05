import streamlit as st

st.title('Aplikasi Data Diri')
st.header('Biodata Pribadi') 

nama = st.text_input('Nama', max_chars=100)
st.write(f'Nama saya adalah {nama}')

with st.form("biodata"):
        st.write("Masukan biodata")
        nama = st.text_input("nama")
        email = st.text_input("email")
        usia = st.number_input("usia",min_value=0, max_value=100, step=1)
        
    
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f'nama saya adalah {nama}, email saya {email} dan usia saya {usia}')