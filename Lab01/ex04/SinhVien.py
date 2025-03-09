class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocluc = ""  # Học lực mặc định

    def xepLoaiHocLuc(self):
        if self._diemTB >= 8.5:
            self._hocluc = "Giỏi"
        elif self._diemTB >= 7.0:
            self._hocluc = "Khá"
        elif self._diemTB >= 5.0:
            self._hocluc = "Trung bình"
        else:
            self._hocluc = "Yếu"
