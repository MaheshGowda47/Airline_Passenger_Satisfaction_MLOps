import streamlit as st 
import numpy as np 
import pandas as pd 

data = pd.read_csv(r"/root/MLOPS_PROJEST_WSL/Airline-Passenger-Satisfaction/project/data/01_raw/airline_passenger_satisfaction.csv")

def prediction():
    st.title("Airline Passenger Satisfaction")

    try:

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
        Satisfaction = st.selectbox("Satisfaction", ["Neutral or Dissatisfied", "Satisfied"])

        gender_map = {'Male': 0, 'Female': 1}
        Customer_Type_map = {'First-time':0, 'Returning':1}
        Type_of_Travel_map = {'Business':0, 'Personal':1}
        class_map = {'Business':0, 'Economy':1, 'Personal':2}
        Satisfaction_map = {'Neutral or Dissatisfied':0, 'Satisfied':1}

        Gender = gender_map[Gender]
        Customer_Type = Customer_Type_map[Customer_Type]
        Type_of_Travel = Type_of_Travel_map[Type_of_Travel]
        Class = class_map[Class]
        Satisfaction = Satisfaction_map[Satisfaction]

        flight_service_1 = np.round((Ease_of_Online_Booking + Check_in_Service + Online_Boarding ) / 3)
        flight_service_2 = np.round((On_board_Service + Seat_Comfort + Food_and_Drink + Cleanliness + Leg_Room_Service) / 5)
        flight_service_3 = np.round((In_flight_Service + In_flight_Wifi_Service + In_flight_Entertainment + Baggage_Handling) / 4)


        # Categorizing Flight Distance into bins
        q1, q2, q3 = np.percentile(data["Flight Distance"], [25, 50, 75])
        if Flight_Distance <= q1:
            Flight_Distance = 0
        elif q1 < Flight_Distance <= q2:
            Flight_Distance = 1
        elif q2 < Flight_Distance <= q3:
            Flight_Distance = 2
        else:
            Flight_Distance = 3

        # categorizing arrivaly delay into bins
        q1, q2, q3 = np.percentile(data["Arrival Delay"], [25, 50, 75])
        if Arrival_Delay <= q1:
            Arrival_Delay = 0
        elif Arrival_Delay > q1 and Arrival_Delay <= q2:
            Arrival_Delay = 1
        elif Arrival_Delay > q2 and Arrival_Delay <= q3:
            Arrival_Delay = 2
        else:
            Arrival_Delay = 3

        # categorizing departure delay into bins  
        q1, q2, q3 = np.percentile(data["Departure Delay"], [25, 50, 75])
        if Departure_Delay <= q1:
            Departure_Delay = 0
        elif Departure_Delay > q1 and Departure_Delay <= q2:
            Departure_Delay = 1
        elif Departure_Delay > q2 and Departure_Delay <= q3:
            Departure_Delay = 2
        else:
            Departure_Delay = 3

    except Exception as e:
        st.error(e)

if __name__ == "__main__":
    prediction()
