import sys
import flightSimulations

'''
By Erik Ayavaca-Tirado
This is the main were the call to the functions in the flightsSimulations class will be made.

Note:
Uncomment the print lines to see testing. 

'''


if __name__ == "__main__":
    flights = flightSimulations.read_file(sys.argv[1])
    # print("Flights from file: Delta 160, UAL 120, Delta 6, Wes 10, Mex, pizza 6 and jet 7")  # Expected read in data
    # print(flights)  # Actual data that is read in from the cvs
    flightSimulations.simulate_airport(flights)
    flightSimulations.takeOffPrint(flights)  # actual output
    # print("order of flights should be: pizza 6, delta 160, Mex 7, jet 7, Wes 10,delta 6 and ual 120")  # Expected
