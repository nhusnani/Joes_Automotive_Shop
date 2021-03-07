class ServiceQuote:
    def __init__(self, pcharges, lcharges, taxrate):
        self.__pcharges = pcharges
        self.__lcharges = lcharges
        self.__taxrate = taxrate

    def pcharges(self, pcharges):
        self.__pcharges = pcharges

    def lcharges(self, lcharges):
        self.__lcharges = lcharges

    def get_salestax(self):
        return self.__taxrate * self.__pcharges

    def get_totalcharges(self):
        return self.__lcharges + self.__pcharges + self.get_salestax()

    def get_pcharges(self):
        return self.__pcharges

    def get_lcharges(self):
        return self.__lcharges