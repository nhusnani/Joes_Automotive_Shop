import Customer_Class
import Car_Class
import ServiceQuote_Class


def main():

    service_dict = {}
    name = input("Enter customer name: ")
    address = input("Enter Address: ")
    phone = int(input("Enter Phone No - without dashes and space: "))
    customer_info = Customer_Class.Customer(name, address, phone)

    make = input("Car Make: ")
    model = input("Car Model: ")
    year = int(input("Car Manufacturing Year: "))
    car_info = Car_Class.Car(make, model, year)

    pcharges = float(input("Parts Charges: "))
    lcharges = float(input("Labor Charges: "))
    taxrate = float(input("Enter Sales Tax Rate: "))
    service_quote = ServiceQuote_Class.ServiceQuote(pcharges, lcharges, taxrate)

    service_dict[customer_info.get_name()] = [
        customer_info.get_address(),
        customer_info.get_phone(),
        car_info.get_make(),
        car_info.get_model(),
        car_info.get_year(),
        service_quote.get_lcharges(),
        service_quote.get_pcharges(),
        service_quote.get_salestax(),
        service_quote.get_totalcharges(),
    ]

    print("Sales Tax:  ", service_quote.get_salestax())
    print("Total Charges (inclusive of tax):  ", service_quote.get_totalcharges())


main()