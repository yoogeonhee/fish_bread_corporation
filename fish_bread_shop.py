# 주문, 관리자, 종료 ,3가지 선택을 통해 기능이 작동되도록 한다.
#input()을 통해 3가지 중 한가지를 입력받아 작동시킬 수 있다.

while True: 
    mode = input("원하는 모드를 선택하세요(주문,관리자,종료):")
    if mode == "종료":
        break

    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
        