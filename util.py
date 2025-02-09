import json
import pickle
import numpy as np  
__locations = None
__data_columns = None
__model = None

def get_location_names():
    global __locations
    return __locations  

def get_estimated_price(location, sqft, bhk, bath):
    global __model, __data_columns
    loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)  

def load_saved_artifacts():
    global __data_columns, __locations, __model
    print("Loading saved artifacts... start")


    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  


    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts... done")


load_saved_artifacts()

if __name__ == "__main__":
    print(get_location_names())  
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))  
