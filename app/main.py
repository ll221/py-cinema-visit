from .cinema.bar import CinemaBar
from .cinema.hall import CinemaHall
from .people.customer import Customer
from .people.cinema_staff import Cleaner


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []

    for data in customers:
        customer = Customer(name=data["name"], food=data["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
