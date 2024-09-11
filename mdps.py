
"""
Created on Friday 12 18:57:07 2024

@author: SHIVAM RAWAT
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# import sklearn
import pickle

st.markdown("""
           <style>
              .st-emotion-cache-10trblm.e1nzilvr1{
                  color:#c72d2d;
                  }
              
              p{
                  font-family: cursive;
                  }
              
              block-container.st-emotion-cache-1y4p8pa.ea3mdgi2{
                  
                  background-image:url("im.jpg")

                  background-size:cover;  
                  }  
           body{
                
               }
           </style>
           
           """,unsafe_allow_html=True)
           

#loading the saved model
diabetes_model = pickle.load(open('Saved Model/trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('Saved Model/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Saved Model/parkinsons_model.sav', 'rb'))

#side bar for navigation

with st.sidebar:
    selected = option_menu('SR_MULTIPLE DISEASE PREDICTION SYSTEM',
                           ['Diabetes Prediction','Heart Disease Prediction','Parkinson Prediction','Contact_Us'],
                           icons = ['activity','heart','person','hospital'],
                           default_index = 0)
    
        
    
if(selected == 'Contact_Us'):
    st.header(":mailbox: Get IN Touch With Me!")
    contact_form ="""
    <form action="https://formsubmit.co/shivam2003golu@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Thanks for feedback"></textarea>
         <button type="submit">Send</button>
       
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    
      
st.markdown("""   
            <style>
input[type=text], input[type=email], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}
  </style>
       """, unsafe_allow_html=True)
       
       

if (selected == 'Diabetes Prediction'):
        
    st.title('Diabetes Disease Prediction using ML')
    
    col1, col2 =st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
          
    with col1:
        BloodPressure = st.text_input('BloodPressure Level')    
        
    with col2:
        SkinThickness = st.text_input('SkinThickness Level')

    with col1:
        Insulin = st.text_input('Insulin Level') 
        
    with col2:
        BMI = st.text_input('BMI Level')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Level')
    with col2:
        Age = st.text_input('Age')
        
    diab_diagnosis = ''
    tru=0;
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if(diab_prediction[0]==1):
            diab_diagnosis ='The person is diabetic '
            tru=1;
            
        else:
            diab_diagnosis='The person is not diabetic'
                

   
    st.success(diab_diagnosis)
    if(tru):
        st.markdown("""
                    #            Some Precautions
                    
                #####     1.Monitor Blood Sugar Levels.
                #####     2.Take medications as prescribed by your healthcare provider.
                 #####    3.Take medications as prescribed by your healthcare providers.
                #####     4.Schedule regular check-ups with your healthcare provider.
                #####     5.Drink an adequate amount of water each day.

                    
                    
                    """)
    

#age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
if selected == 'Heart Disease Prediction':

    # page title
    st.title("Heart's Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''
    htru=0;

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            htru =1
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    if(htru):
        st.markdown("""
                    #            Some Precautions
                    
                #####     1.Medication Adherence.
                #####     2.Limit Alcohol Intake.
                 #####    3.Manage Stress.
                #####     4.Cholesterol Management.
                #####     5.Cholesterol Management.

                    
                    
                    """)
    
    
    
    
    



#MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,status,RPDE,DFA,spread1,spread2,D2,PPE


    
if(selected == 'Parkinson Prediction'):
     
    
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP(Fo(Hz))')

    with col2:
        fhi = st.text_input('MDVP(Fhi(Hz))')

    with col3:
        flo = st.text_input('MDVP(Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP(Jitter(%))')

    with col5:
        Jitter_Abs = st.text_input('MDVP(Jitter(Abs))')

    with col1:
        RAP = st.text_input('MDVP(RAP)')

    with col2:
        PPQ = st.text_input('MDVP(PPQ)')

    with col3:
        DDP = st.text_input('Jitter(DDP)')

    with col4:
        Shimmer = st.text_input('MDVP(Shimmer)')

    with col5:
        Shimmer_dB = st.text_input('MDVP(Shimmer(dB))')

    with col1:
        APQ3 = st.text_input('Shimmer(APQ3)')

    with col2:
        APQ5 = st.text_input('Shimmer(APQ5)')

    with col3:
        APQ = st.text_input('MDVP(APQ)')

    with col4:
        DDA = st.text_input('Shimmer(DDA)')

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

    # code for Prediction
    parkinsons_diagnosis = ''
    ptru=0

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            ptru =1
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    if(ptru):
        st.markdown("""
                    #            Some Precautions
                    
                #####     1.Deep Brain Stimulation (DBS).
                #####     2.Physical Therapy, Occupational Therapy & Speech Therapy.
                 #####    3.Manage Stress.
                #####     4.Medication Adherence.
                #####     5.Cognitive Stimulation.

                    
                    
                    """)
         
   












