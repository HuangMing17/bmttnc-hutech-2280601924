from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 ==1):
    print("\nChuong trinh quan ly sinh vien")
    print("************************************************")
    print("1. Thêm sinh vien")
    print("2. Sua sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tìm Kiếm Sinh viên theo tên")
    print("5. Sap xep sinh vien theo điểm trung bình")
    print("6. Sap xep sinh vien theo ten chuyên ngành ")
    print("7. Hien thi danh sach sinh vien")
    print("8. Thoat")
    print("************************************************")

    key = int(input("Nhap lua chon cua ban: "))
    if (key ==1):
       print("\n1. Thêm sinh vien")
       qlsv.nhapSinhVien()
       print("\nThem sinh vien thanh cong")
    elif (key ==2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Sua sinh vien")
            print("Nhap ID cua sinh vien can sua: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien rong")
    elif (key ==3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien")
            print("Nhap ID cua sinh vien can xoa: ")
            ID = int(input())
            if(qlsv.deleteSinhVien(ID)):
                print("\nXoa sinh vien thanh cong")
            else:
                print("\nKhong tim thay sinh vien co ID: ", ID)
        else:
            print("Danh sach sinh vien rong")
    elif (key ==4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm Kiếm Sinh viên theo tên")
            name = input("Nhap ten sinh vien can tim: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien rong")
            
    elif (key ==5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo điểm trung bình")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("Danh sach sinh vien rong")
    elif (key ==6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten chuyên ngành ")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")
    elif (key ==7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")
    elif (key ==8):
        print("\n8. Thoat")
        print("Cam on ban da su dung chuong trinh")
        break
    else:
        print("Lua chon khong hop le")