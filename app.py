# Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the dataset
data = pd.read_csv(r"/root/MLOPS_PROJEST_WSL/Airline-Passenger-Satisfaction/project/data/01_raw/airline_passenger_satisfaction.csv")

# Function to make predictions
def prediction():
    # Set the title for the app
    st.title("Airline Passenger Satisfaction")

    try:
        # User input fields
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Age = st.number_input("Age", min_value=0, max_value=85, key="age_input")
        Customer_Type = st.selectbox("Customer Type", ["First-time", "Returning"])
        Type_of_Travel = st.selectbox("Type of Travel", ["Business", "Personal"])
        Class = st.selectbox("Class", ["Business", "Economy", "Economy Plus"])
        Flight_Distance = st.number_input("Flight Distance", min_value=0, key="flight_distance_input")
        Departure_Delay = st.number_input("Departure Delay", min_value=0, key="departure_delay_input")
        Arrival_Delay = st.number_input("Arrival Delay", min_value=0, key="arrival_delay_input")
        Departure_and_Arrival_Time_Convenience = st.number_input("Departure and Arrival Time Convenience", min_value=0, max_value=5, key="departure_arrival_time_convenience_input")
        Ease_of_Online_Booking = st.number_input("Ease of Online Booking", min_value=0, max_value=5, key="ease_of_online_booking_input")
        Check_in_Service = st.number_input("Check-in Service ", min_value=0, max_value=5, key="check_in_service_input")
        Online_Boarding = st.number_input("Online Boarding", min_value=0, max_value=5, key="online_boarding_input")
        On_board_Service = st.number_input("On-board Service", min_value=0, max_value=5, key="on_board_service_input")
        Seat_Comfort = st.number_input("Seat Comfort", min_value=0, max_value=5, key="seat_comfort_input")
        Leg_Room_Service = st.number_input("Leg Room Service", min_value=0, max_value=5, key="leg_room_service_input")
        Cleanliness = st.number_input("Cleanliness", min_value=0, max_value=5, key="cleanliness_input")
        Food_and_Drink = st.number_input("Food and Drink", min_value=0, max_value=5, key="food_and_drink_input")
        In_flight_Service = st.number_input("In-flight Service", min_value=0, max_value=5, key="in_flight_service_input")
        In_flight_Wifi_Service = st.number_input("In-flight Wifi Service", min_value=0, max_value=5, key="in_flight_wifi_service_input")
        In_flight_Entertainment = st.number_input("In-flight Entertainment", min_value=0, max_value=5, key="in_flight_entertainment_input")
        Baggage_Handling = st.number_input("Baggage Handling", min_value=0, max_value=4, key="baggage_handling_input")
        
        # Mapping categorical input to numerical values
        gender_map = {'Male': 0, 'Female': 1}
        Customer_Type_map = {'First-time': 0, 'Returning': 1}
        Type_of_Travel_map = {'Business': 0, 'Personal': 1}
        class_map = {'Business': 0, 'Economy': 1, 'Economy Plus': 2}

        Gender = gender_map[Gender]
        Customer_Type = Customer_Type_map[Customer_Type]
        Type_of_Travel = Type_of_Travel_map[Type_of_Travel]
        Class = class_map[Class]

        # Calculating average values for certain features
        flight_service_1 = np.round((Ease_of_Online_Booking + Check_in_Service + Online_Boarding) / 3)
        flight_service_2 = np.round((On_board_Service + Seat_Comfort + Food_and_Drink + Cleanliness + Leg_Room_Service) / 5)
        flight_service_3 = np.round((In_flight_Service + In_flight_Wifi_Service + In_flight_Entertainment + Baggage_Handling) / 4)

        # Creating a DataFrame with user inputs
        df = pd.DataFrame({
            'Gender': [Gender],
            'Age': [Age],
            'Customer Type': [Customer_Type],
            'Type of Travel': [Type_of_Travel],
            'Class': [Class],
            'Flight Distance': [Flight_Distance],
            'Departure Delay': [Departure_Delay],
            'Arrival Delay': [Arrival_Delay],
            'Departure and Arrival Time Convenience': [Departure_and_Arrival_Time_Convenience],
            'flight_service_1': [flight_service_1],
            'flight_service_2': [flight_service_2],
            'flight_service_3': [flight_service_3],
        })

        # Perform prediction when the "Predict" button is clicked
        if st.button("Predict"):
            # Load the machine learning model
            model = joblib.load("/root/MLOPS_PROJEST_WSL/Airline-Passenger-Satisfaction/project/data/05_model/model.pkl")
            # Make prediction based on user input
            output = model.predict(df)
            # Determine the satisfaction level based on the prediction result
            result = 'Satisfied' if output[0] == 1 else 'Neutral or Dissatisfied'
            # Display the prediction result
            st.success(f"Passenger is: {result}")

    except Exception as e:
        # Display an error message if an exception occurs
        st.error(e)

# Execute the prediction function
if __name__ == "__main__":
    prediction()
