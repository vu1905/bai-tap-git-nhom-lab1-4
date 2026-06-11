def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5:
        return 4.0
    else:
        return round((diem_so / 10) * 4, 2)

print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5))
