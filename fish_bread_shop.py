# 주문, 관리자, 종료 ,3가지 선택을 통해 기능이 작동되도록 한다.
#input()을 통해 3가지 중 한가지를 입력받아 작동시킬 수 있다.

stock = {
    "팥붕어빵": 10,
    "슈크림붕어빵": 8,
    "피자붕어빵": 5
}

sales =  {
    "팥붕어빵": 0,
    "슈크림붕어빵": 0,
    "피자붕어빵": 0
}

def order_bread():
    while True:
        bread_type = input("주문할 메뉴를 선택해 주세요. (팥붕어빵, 슈크림붕어빵, 피자붕어빵) 뒤로가기를 원하시면 뒤로가기를 눌러주세요.")
        if bread_type == "뒤로가기":
            print("주문을 종료합니다.")
            break
        if bread_type in stock:
            bread_count = int(input("주문할 수량을 입력해주세요: "))
            if  stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f"{bread_type},{bread_count}개가 판매되었습니다.")
                return
            else: 
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
        else:
            print("없는 메뉴 입니다. 다시 주문해 주세요.")

while True: 
    mode = input("원하는 모드를 선택하세요(주문,관리자,종료):")
    if mode == "종료":
        break

    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
        
        