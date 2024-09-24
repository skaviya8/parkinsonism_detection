import pickle
import numpy as np
# loading the saved models

loaded_model = pickle.load(open('C:/Users/kaviy/Downloads/parkinson project/parkinsons_model.sav', 'rb'))

input_data = (120.26700,137.24400,114.82000,0.00333,0.00003,0.00155,0.00202,0.00466,0.01608,0.14000,0.00779,0.00937,0.01351,0.02337,0.00607,24.88600,0.596040,0.764112,-5.634322,0.257682,1.854785,0.211756)

input_data_as_numpy_array = np. asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction =loaded_model.predict(input_data_reshaped)
print(prediction)


if (prediction[0] == 0):
    print("The Person does not have Parkinsons Disease")
    
else:
    print("The Person has Parkinsons")