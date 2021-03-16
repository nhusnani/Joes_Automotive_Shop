class ServiceQuote:
    def __init__(self, pcharges, lcharges):
        self.__pcharges = pcharges
        self.__lcharges = lcharges
        self.__salestax = 0.05
        self.__salestax_amount = 0
        self.__total_charges = 0

    def pcharges(self, pcharges):
        self.__pcharges = pcharges

    def lcharges(self, lcharges):
        self.__lcharges = lcharges

    def get_pcharges(self):
        return self.__pcharges

    def get_lcharges(self):
        return self.__lcharges

    def get_salestax_amount(self):
        self.__salestax_amount = (self.__lcharges + self.__pcharges) * self.__salestax
        return self.__salestax_amount   

    def get_total_charges(self):
        self.__total_charges = (self.__lcharges + self.__pcharges + self.__salestax_amount)
        return self.__total_charges