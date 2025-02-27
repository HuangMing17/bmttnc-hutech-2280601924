#nhập các dòng văn bản từ người dùng
print("Nhập các dòng văn bản(Nhập 'done' để kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
#chuyển các dòng chữ thành in hoa và in ra màn hình
print("\nCác dòng văn bản sau khi chuyển thành in hoa: ") 
for line in lines:
    print(line.upper())
