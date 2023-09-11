class realEstate():
    def __init__(self, location, type, deal_type, price, completion_year) -> None:
        # print("총 3가지의 매물이 있습니다.")
        self.location = location
        self.type = type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


class detail(realEstate):
    def __init__(self, location, type, deal_type, price, completion_year) -> None:
        super().__init__(location, type, deal_type, price, completion_year)
        print(
            f"{self.location} {self.type} {self.deal_type} {self.price} {self.completion_year}")


Estatement = realEstate("강남", "아파트", "매매", "10억원", "2010년")
print(detail("강남", "아파트", "매매", "10억원", "2010년"))
