from django.db import models

from django.utils.timezone import now


TIPOLOGIA_CHOICES = [

    ("SUv", "SUV"),

    ("Wagon", "Wagon"),

]


class CarMake(models.Model):

    Name = models.CharField(null=False, max_length=2000, default="name")

    Description = models.CharField(null=False, max_length=2000, default="mame")


    def __str__(self):

        return "Name: " + self.Name + ", " + "Description: " + self.Description



class CarModel(models.Model):

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    Name = models.CharField(null=False, max_length=2000, default="name")

    Dealerid = models.IntegerField(default=0)

    Type = models.CharField(null=False, max_length=2000, choices=TIPOLOGIA_CHOICES)

    Year = models.DateField(default=now)


    def __str__(self):

        return (

            "Name: "

            + self.Name

            + ", "

            + "Description: "

            + str(self.Dealerid)  # Convert Dealerid to string

            + ", "

            + "Type: "

            + self.Type

        )

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + str(self.full_name)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase,review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name= name
        self.purchase= purchase
        self.review=review
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=year
        self.senti=sentiment
        self.id=id

    def __str__(self):
        return "Dealer review:" +self.review


