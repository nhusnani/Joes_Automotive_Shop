import Customer_Class
import Car_Class
import ServiceQuote_Class


def main():

    service_dict = {}
    name = input("Enter customer name: ")
    address = input("Enter Address: ")
    phone = int(input("Enter Phone No - without dashes and space: "))
    customer = Customer_Class.Customer(name, address, phone)

    make = input("Car Make: ")
    model = input("Car Model: ")
    year = int(input("Car Manufacturing Year: "))
    car = Car_Class.Car(make, model, year)

    pcharges = float(input("Parts Charges: "))
    lcharges = float(input("Labor Charges: "))
    service_quote = ServiceQuote_Class.ServiceQuote(pcharges, lcharges)

    service_dict[customer.get_name()] = [
        customer.get_address(),
        customer.get_phone(),
        car.get_make(),
        car.get_model(),
        car.get_year(),
        service_quote.get_lcharges(),
        service_quote.get_pcharges(),
        service_quote.get_salestax_amount(),
        service_quote.get_total_charges()]

    print("Sales Tax:  ", format(service_quote.get_salestax_amount(), ".2f"))
    print("Total Charges (inclusive of tax):  ", format(service_quote.get_total_charges(), ".2f"))


main()