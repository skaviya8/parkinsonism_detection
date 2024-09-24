import pickle
import numpy as np
import streamlit as st

# loading the saved models

loaded_model = pickle.load(open('C:/Users/kaviy/Downloads/parkinson project/parkinsons_model.sav', 'rb'))
    
    
def parkinsons_prediction(input_data):
    

    input_data_as_numpy_array = np. asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction =loaded_model.predict(input_data_reshaped)
    return prediction


    

def main():
    #giving tittle
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('RAP')
        
    with col2:
        PPQ = st.text_input('PPQ')
        
    with col3:
        DDP = st.text_input('DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        DB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    # Create a button for prediction
    if st.button("Parkinson's Test Result"):
        try:
            # Convert input values to floats
            fo = float(fo)
            fhi = float(fhi)
            flo=float(flo) 
            Jitter_percent=float(Jitter_percent)
            Jitter_Abs=float(Jitter_Abs)
            RAP=float(RAP)
            PPQ=float(PPQ)
            DDP=float(DDP)
            Shimmer=float(Shimmer)
            DB=float(DB)
            APQ3=float(APQ3)
            APQ5=float(APQ5)
            APQ=float(APQ)
            DDA=float(DDA)
            NHR=float(NHR)
            HNR=float(HNR)
            RPDE=float(RPDE)
            DFA=float(DFA)
            spread1=float(spread1)
            spread2=float(spread2)
            D2=float(D2)
            PPE=float(PPE)
            # Convert other input values similarly...

            # Perform the prediction
            prediction = loaded_model.predict(np.array([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, DB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]).reshape(1, -1))

            if prediction[0] == 0:
                parkinsons_diagnosis = "The Person does not have Parkinsons Disease"
            else:
                parkinsons_diagnosis = "The Person has Parkinsons"
        except ValueError:
            parkinsons_diagnosis = "Please enter valid numerical values for all features."

    st.success(parkinsons_diagnosis)

if __name__ == '__main__':
    main()