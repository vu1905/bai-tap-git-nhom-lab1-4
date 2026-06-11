# test_main.py
import unittest
from main import tinh_diem_gpa

class TestGpaFunctions(unittest.TestCase):

    def test_gpa_he_muoi(self):
        # Kiểm tra xem nhập điểm 8.5 có trả về 4.0 không (Logic của Dev B)
        self.assertEqual(tinh_diem_gpa(8.5), 4.0)

    def test_gpa_tuyen_tinh(self):
        # Kiểm tra nhập điểm 7.0 xem có ra đúng 2.8 không (Logic của Dev A: 7/10 * 4 = 2.8)
        self.assertEqual(tinh_diem_gpa(7.0), 2.8)

if __name__ == '__main__':
    unittest.main()
