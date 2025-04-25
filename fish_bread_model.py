class BreadShop:
    def __init__(self):
        self.stock = {"팥붕어빵" : 10, "슈크림붕어빵" : 10, "피자붕어빵" : 10}
        self.sales = {"팥붕어빵" : 0, "슈크림붕어빵" : 0, "피자붕어빵" : 0}
        self.price = {"팥붕어빵" : 1000, "슈크림붕어빵" : 1500, "피자붕어빵" : 1500}
        
    
    def order_bread(self):
        while True:
            bread_type = input("주문할 메뉴를 선택해 주세요. (팥붕어빵, 슈크림붕어빵, 피자붕어빵) 뒤로가기를 원하시면 뒤로가기를 눌러주세요.")
            if bread_type == "뒤로가기":
                print("주문을 종료합니다.")
                break
            if bread_type in self.stock:
                bread_count = int(input("주문할 수량을 입력해주세요: "))
                if  self.stock[bread_type] >= bread_count:
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] += bread_count
                    print(f"{bread_type},{bread_count}개가 판매되었습니다.")
                    return
                else: 
                    print(f"재고가 부족합니다. 현재 {self.stock[bread_type]}개만 주문 가능합니다.")
            else:
                print("없는 메뉴 입니다. 다시 주문해 주세요.")



    #붕어빵 admin 기능
    def admin_mode(self):
        while True:
            bread_type = input("추가할 메뉴를 입력해주세요,(팥붕어빵, 슈크림붕어빵, 피자붕어빵) 뒤로가기를 원하시면 뒤로가기를 눌러주세요.")
            if bread_type == "뒤로가기":
                print("관리자 모드를 종료합니다.")
                break
            if bread_type in self.stock:
                bread_count = int(input("추가할 수량을 입력해주세요."))
                self.stock[bread_type] += bread_count
                print(f"{bread_type}이 {bread_count}개 추가되었습니다.")
                print(f"현재{bread_type}의 재고는 {self.stock[bread_type]}개 입니다.")
                return
            else:
                print("없는 메뉴 입니다. 다시 추가해 주세요.")

    def calculation(self):
        total = 0 
        for key in self.sales :
            total += (self.sales[key] * self.price[key])
            print(f"오늘의 매출은{total}원입니다.")
