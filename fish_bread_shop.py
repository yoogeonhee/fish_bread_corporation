from fish_bread_model import BreadShop

shop = BreadShop()

    #붕어빵 메인 화면
while True: 
    mode = input("원하는 모드를 선택하세요(주문,관리자,종료):")
    if mode == "종료":
        shop.calculation()
        print("시스템을 종료합니다.")     
        break
    elif mode == "주문":
        shop.order_bread()
    elif mode == "관리자":
        shop.admin_mode()