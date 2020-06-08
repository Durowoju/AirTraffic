from resources.read_data import AirTraffic

use_cols = ['Activity Period', 'Operating Airline', 'GEO Summary', 'GEO Region', 'Price Category Code', 'Passenger Count', 'Year', 'Month']
new_air_traffic =  AirTraffic("Air_Traffic_Passenger_Statistics.csv")
formated_columns = new_air_traffic.read_from_csv(use_cols)
new_air_traffic.visualize_data(formated_columns)
