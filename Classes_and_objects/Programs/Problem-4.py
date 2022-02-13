"""Create a class that captures airline tickets.
Each ticket lists the departure and arrival cities, a flight number, and a seat assignment.
A seat assignment has both a row and a letter for the seat within the row (such as 12F). Make two examples of tickets."""
class airticket:
    def ticket(self):
        self.departure=input("Enter Departure City:")
        self.arival=input("Enter Arrival City:")
        self.fnumber=input("Enter Flight Number:")
        self.seat=input("Enter Seat Number:")
    def show(self):
        print("Departure From:",self.departure,"\nArrival To:",self.arival,"\nFlight Number:",self.fnumber,"\nSeat Number:",self.seat)

ob1=airticket()
ob2=airticket()
ob1.ticket()
ob2.ticket()
ob1.show()
ob2.show()
