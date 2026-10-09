import streamlit as st
import pandas as pd

st.header("1 Rep Max")

with st.container(border=True):
    gewicht = st.number_input('Gewicht', step=2.5, format="%0.1f")
    reps = st.pills('Reps', options=[1,2,3,4,5,6,8,10,12], key=0)

conversions = {
    1:  1.00,
    2:  0.95,
    3:  0.93,
    4:  0.90,
    5:  0.87,
    6:  0.85,
    8:  0.80,
    10: 0.75,
    12: 0.70   
}

if gewicht!=0 and reps:
    

    one_rep_max = gewicht / conversions[reps]    

    single_convert = lambda x: int(one_rep_max * conversions[x])

    the_dict = {
        1: single_convert(1),
        2: single_convert(2),
        3: single_convert(3),
        4: single_convert(4),
        5: single_convert(5),
        6: single_convert(6),
        8: single_convert(8),
        10: single_convert(10),
        12: single_convert(12),
    }

    df = pd.DataFrame({'Gewicht':the_dict})


    print(df)

    st.table(df)


