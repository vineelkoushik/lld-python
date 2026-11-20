
# Class named Movie
class Movie:
    def __init__(self, movie_name: str, total_seats_available: int, ticket_price: float):
        # Instance attributes
        self.movie_name: str = movie_name
        self.total_seats_available: int = total_seats_available
        self.ticket_price: float = ticket_price
        self.seats_booked: int = 0
    # Method to book tickets
    def book_tickets(self, no_of_people: int)-> None:
        # Validate ticket quantity
        if no_of_people <= 0:
            print("Please enter a valid number of tickets")
            return
        # Check seat availability
        if no_of_people > self.total_seats_available:
            print(f"Only {self.total_seats_available} seats are available")
            return
        # Update booking details
        self.seats_booked += no_of_people
        self.total_seats_available -= no_of_people
        # Calculate total ticket price
        total_price = self.ticket_price * no_of_people
        print(f"Your {no_of_people} seats are booked successfully")
        print(f"Total Price: ₹{total_price:.2f}")
        print("Thanks for Booking\n")
    # Method to display current movie booking status
    def status_now(self) -> None:
        print(f"Movie: {self.movie_name}")
        print(f"Seats Booked So Far: {self.seats_booked}")
        print(f"Seats Available: {self.total_seats_available} \n")


# Creating objects of the Movie class
m1 = Movie("Abc", 100, 475.33)
m2 = Movie("Xyz", 50, 350.00)

# Booking tickets for different movies
m1.book_tickets(12)
m1.status_now()

m2.book_tickets(14)
m2.status_now()

m1.book_tickets(34)
m1.status_now()

m2.book_tickets(2)
m2.status_now()
