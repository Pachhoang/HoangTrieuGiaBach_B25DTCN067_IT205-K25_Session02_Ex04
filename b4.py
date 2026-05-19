age = int(input("Nhập tuổi bệnh nhân: ").strip())
blood = int(input("Nhập huyết áp tâm thu: ").strip())
bloodsugar = int(input("Nhập đường huyết: ").strip())
if age < 0 or blood < 0 or bloodsugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
else:
    if age >= 75:
        print("TỪ CHỐI PHẪU THUẬT - Tuổi vượt ngưỡng an toàn")

    elif blood < 90 or blood > 140:
        print("TỪ CHỐI PHẪU THUẬT - Huyết áp không an toàn")

    elif bloodsugar >= 150:
        print("TỪ CHỐI PHẪU THUẬT - Đường huyết quá cao")

    else:
        print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
