def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# sử dụng hàm và in ra kết quả
input_string = input("Nhập 1 chuỗi: ")
print("Chuỗi sau khi đảo ngược là: ", dao_nguoc_chuoi(input_string))