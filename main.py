import cx_Oracle
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QWidget
# from PyQt5.QtPrintSupport import QPrinter,QPrintDialog
from PyQt5 import QtWidgets
from Gui_Lam_Viec import Ui_Form
from Lam_Viec import Ui_Form
from Gui import Ui_MainWindow
from Hoa_Don import HoaDon
from Lam_Viec import LamViec
from Gui_Lam_Viec import Ui_Form as Form_Gui_Lam_Viec
from Gui_Hoa_Don import Ui_Form as Form_Gui_Hoa_Don
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
class MainWindow(HoaDon,LamViec):
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.btnDangNhap.clicked.connect(self.DangNhap)
        self.uic.btnThoat.clicked.connect(self.Thoat)

    def Thoat(self):
        self.main_win.close()
    def DangNhap(self):
        global setmanhanvien
        global settennhanvien
        global masanphamthongke
        self.Second_window = QtWidgets.QMainWindow()
        self.uic1 = Form_Gui_Lam_Viec()
        self.uic1.setupUi(self.Second_window)

        self.third_window = QtWidgets.QMainWindow()
        self.uic2 = Form_Gui_Hoa_Don()
        self.uic2.setupUi((self.third_window))

        self.form_Lam_Viec_Click()
        self.form_Hoa_Don_Click()
        taikhoan=self.uic.txttaikhoan.text()
        matkhau = self.uic.txtmatkhau.text()
        try:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select * from nhanvien where taikhoan= '"+taikhoan+"' and matkhau= '"+matkhau+"' "
            cursor = con.cursor()
            cursor.execute(sql)
            results= cursor.fetchall()
            cursor.close()
            con.close()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        if(len(results)>0):
            quyen = results[0][8]
            self.setmanhanvien = results[0][0]
            self.settennhanvien = results[0][1]
            if(quyen==0):
                self.load_Form_Lam_Viec()
            elif(quyen==1):
                self.load_Form_Hoa_Don()
        elif(len(results)==0):
            self.ThongBaoOk("Sai thông tin đăng nhập")
    def ThongBaoOk(self,NoiDung):
        QMessageBox.information(QtWidgets.QMessageBox(), "Thông báo", NoiDung,
                                QtWidgets.QMessageBox().Ok)
    def checkSanPhamConHang(self):
        self.uic.textEdit.setText("")
        tensanpham=[]
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from sanpham where soluongcon= 0 "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                tensanpham.append(item[1])
            for i in range(0,len(tensanpham)):
                self.uic.textEdit.append(""+str(i+1)+""+". "+tensanpham[i])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
    def show(self):
        self.main_win.show()
        self.checkSanPhamConHang()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
