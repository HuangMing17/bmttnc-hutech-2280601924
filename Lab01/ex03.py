#nhập 1 số nguyên từ người dùng
so = input("Nhập 1 số nguyên: ")
#kiểm tra số đó có phải số chẵn không 
if int(so) % 2 == 0:
    print("Số", so, "là số chẵn")
else:
    print("Số", so, "là số lẻ")
