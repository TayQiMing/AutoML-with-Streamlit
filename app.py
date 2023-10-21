from operator import index
import streamlit as st
import plotly.express as px
from pycaret.classification import setup, compare_models, pull, save_model, load_model
# import pandas_profiling
from ydata_profiling import ProfileReport
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoNickML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    # profile_df = df.profile_report()
    profile_df = ProfileReport(df)
    st_profile_report(profile_df)

if choice == "Modelling": 
    st.title("Machine Learning Modeling")
    chosen_target = st.selectbox('Choose the Target Column', df.columns)
    if st.button('Run Modelling'): 
        # setup(df, target=chosen_target, silent=True)
        setup(df, target=chosen_target, verbose=False)
        setup_df = pull()
        st.info('The ML settings is:')
        st.dataframe(setup_df)
        best_model = compare_models()   # Problem at modeling as the compare model and each model score didnt shown in table, return as empty result
        compare_df = pull()             # Maybe due to different version of libraries
        st.info('The best model is:')
        st.dataframe(compare_df)
        best_model
        save_model(best_model, 'best_model')

if choice == "Download": 
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")
