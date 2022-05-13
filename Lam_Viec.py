import cx_Oracle
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QWidget
from PyQt5 import QtWidgets
from Gui_Lam_Viec import Ui_Form
from Lam_Viec import Ui_Form
from Gui import Ui_MainWindow
from Hoa_Don import HoaDon
from datetime import date,datetime
from Gui_Lam_Viec import Ui_Form as Form_Gui_Lam_Viec
from Gui_Hoa_Don import Ui_Form as Form_Gui_Hoa_Don
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import numpy as np
class LamViec():
    def __init__(self):
        self.Second_window = QtWidgets.QMainWindow()
        self.uic1 = Form_Gui_Lam_Viec()
        self.uic1.setupUi(self.Second_window)
    def form_Lam_Viec_Click(self):
        self.uic1.btnnhanvien.clicked.connect(self.ScreenNhanVien)
        self.uic1.btnkhachhang.clicked.connect(self.ScreenKhachHang)
        self.uic1.btnsanpham.clicked.connect(self.ScreenSanPham)
        self.uic1.btnnhacungcap.clicked.connect(self.screenNhaCungcap)
        self.uic1.btnhoadon.clicked.connect(self.screenHoaDon)
        self.uic1.btnphieunhap.clicked.connect(self.screenPhieuNhap)
        self.uic1.btnchitiet.clicked.connect(self.screenChiTiet)
        self.uic1.btnbanhang.clicked.connect(self.banHang)
        self.uic1.btnthongke.clicked.connect(self.screenThongKe)
        self.uic1.btnthoat.clicked.connect(self.thoat1)
        # ----Nhân Viên----
        self.uic1.btnthemnhanvien.clicked.connect(self.ThemNhanVien)
        self.uic1.btnsuanhanvien.clicked.connect(self.SuaNhanVien)
        self.uic1.btnxoanhanvien.clicked.connect(self.XoaNhanVien)
        self.uic1.btntimnhanvien.clicked.connect(self.TimNhanVien)
        self.uic1.btnresetnhanvien.clicked.connect(self.ResetNhanVien)
        self.uic1.tableWidget.clicked.connect(self.TabletoForm)
        ###############################Khách Hàng######################################
        self.uic1.tableWidget_2.clicked.connect(self.TabletoFormKhachHang)
        self.uic1.btntimkhachhang.clicked.connect(self.TimKhachHang)
        self.uic1.btnxoakhcahhang.clicked.connect(self.XoaKhachHang)
        self.uic1.btnthongkekhachhang.clicked.connect(self.thongKeKhachHang)
        ################################Sản Phẩm#######################################
        self.uic1.tablesanpham.clicked.connect(self.TabletoFormSanPham)
        self.uic1.btnthemsanpham.clicked.connect(self.themSanpPham)
        self.uic1.btnsuasanpham.clicked.connect(self.suaSanPham)
        self.uic1.btnxoasanpham.clicked.connect(self.xoaSanPham)
        self.uic1.btntimkiemsanpham.clicked.connect(self.timSanPham)
        self.uic1.btnresetsanpham.clicked.connect(self.resetSanPham)
        ################################Nhà cung cấp#######################################
        self.uic1.tablenhacungcap.clicked.connect(self.TabletoFormNhaCungCap)
        self.uic1.btnthemncc.clicked.connect(self.themNhaCungCap)
        self.uic1.btnsuanhacc.clicked.connect(self.suaNhaCungCap)
        self.uic1.btnxoancc.clicked.connect(self.xoaNhaCungCap)
        self.uic1.btntimkiemncc.clicked.connect(self.timNhaCungcap)
        self.uic1.btnresetncc.clicked.connect(self.resetNhaCungCao)
        ############################Hóa Đơn#########################################
        self.uic1.tablehoadon.clicked.connect(self.tableToFormHoaDon)
        self.uic1.btntimhoadon.clicked.connect(self.timHoaDon)
        self.uic1.btnthongkehoadon.clicked.connect(self.thongKeHoaDon)
        self.uic1.btnxoahoadon.clicked.connect(self.xoaHoaDon)
        ###########################Phiếu nhập#######################################
        self.uic1.btntimphieunhap.clicked.connect(self.timPhieuNhap)
        self.uic1.tablephieunhap.clicked.connect(self.tableToFormPhieuNhap)
        self.uic1.brnxoaphieunhap.clicked.connect(self.xoaPhieuNhap)
        ########################### Chi Tiết#######################################
        self.uic1.btntimcthoadon.clicked.connect(self.timChiTietHoaDon)
        self.uic1.btntimchitietsanpham.clicked.connect(self.timChiTietPhieuNhap)
        ###########################Thống kê######################################
        self.uic1.btnthongke_2.clicked.connect(self.showChart)
        self.uic1.cbbtensanpham.activated.connect(self.hienThiThongTinSanPhamThongKe)

    def load_Form_Lam_Viec(self):
        self.Second_window.show()
        self.ShowTable()
        self.main_win.close()
    def ScreenNhanVien(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_nhanvien)
        self.ShowTable()
    def TabletoForm(self):
        for item in self.uic1.tableWidget.selectedItems():
            row = item.row()
            self.uic1.txtmanhanvien.setText(self.uic1.tableWidget.item(row, 0).text())
            self.uic1.txttennhanvien.setText(self.uic1.tableWidget.item(row, 1).text())
            if(self.uic1.tableWidget.item(row,2).text()== 'Nam'):
                self.uic1.radioButton.click()
            if (self.uic1.tableWidget.item(row, 2).text() == 'Nữ'):
                self.uic1.radioButton_2.click()
            self.uic1.txtsodienthoai.setText(str(self.uic1.tableWidget.item(row, 3).text()))
            self.uic1.txtsocccd.setText(str(self.uic1.tableWidget.item(row, 4).text()))
            self.uic1.txtdiachi.setPlainText(self.uic1.tableWidget.item(row, 5).text())
            self.uic1.txttaikhoan.setText(self.uic1.tableWidget.item(row, 6).text())
            self.uic1.txtmatkhau.setText(self.uic1.tableWidget.item(row, 7).text())
    def ThemNhanVien(self):
        manhanvien = self.uic1.txtmanhanvien.text()
        sodienthoai = self.uic1.txtsodienthoai.text()
        socccd = self.uic1.txtsocccd.text()
        if (len(manhanvien) == 0):
            self.ThongBaoOk("Mời bạn nhập mã nhân viên")
        elif(len(sodienthoai)==0):
            self.ThongBaoOk("Mời bạn nhập số điện thoại")
        elif(len(socccd)==0):
            self.ThongBaoOk("Mời bạn nhập số căn cước công dân")
        else:
            tennhanvien = self.uic1.txttennhanvien.text()

            diachi = self.uic1.txtdiachi.toPlainText()
            taikhoan = self.uic1.txttaikhoan.text()
            matkhau = self.uic1.txtmatkhau.text()
            gioitinh = ''
            quyen = 1
            if (self.uic1.radioButton.isChecked()):
                gioitinh = 'Nam'
            if (self.uic1.radioButton_2.isChecked()):
                gioitinh = 'Nữ'
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""insert into nhanvien (manhanvien, tennhanvien, gioitinh, sodienthoai,socccd, diachi,
                  taikhoan, matkhau,quyen)values ('{manhanvien}', '{tennhanvien}', '{gioitinh}',{sodienthoai},
                  {socccd}, '{diachi}','{taikhoan}', '{matkhau}',{quyen})"""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                self.ThongBaoOk("Thêm thành công")
            except cx_Oracle.DatabaseError as e:
                self.ThongBaoOk("Đã tồn tại mã nhân viên")
            finally:
                cursor.close()
                con.close()
                self.ScreenNhanVien()
    def SuaNhanVien(self):
        manhanvien = self.uic1.txtmanhanvien.text()
        if (len(manhanvien) == 0):
            self.ThongBaoOk("Mời bạn nhập mã nhân viên")
        else:
            tennhanvien = self.uic1.txttennhanvien.text()
            sodienthoai = int(self.uic1.txtsodienthoai.text())
            socccd = int(self.uic1.txtsocccd.text())
            diachi = self.uic1.txtdiachi.toPlainText()
            taikhoan = self.uic1.txttaikhoan.text()
            matkhau = self.uic1.txtmatkhau.text()
            gioitinh = ''
            if (self.uic1.radioButton.isChecked()):
                gioitinh = 'Nam'
            if (self.uic1.radioButton_2.isChecked()):
                gioitinh = 'Nữ'
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""update  nhanvien set tennhanvien='{tennhanvien}', gioitinh='{gioitinh}', sodienthoai={sodienthoai}
            ,socccd={socccd}, diachi='{diachi}', taikhoan='{taikhoan}',matkhau= '{matkhau}'
             where manhanvien ='{manhanvien}'"""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                self.ThongBaoOk("Update thành công")
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
                self.ScreenNhanVien()
    def checkNhanVien(self):
        manhanvien = self.uic1.txtmanhanvien.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select *  from nhanvien where manhanvien='" + manhanvien + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def XoaNhanVien(self):
        manhanvien = self.uic1.txtmanhanvien.text()
        if(len(manhanvien)==0):
            self.ThongBaoOk("Mời bạn nhập mã nhân viên")
        else:
            hoi=QMessageBox.question(QtWidgets.QMessageBox(), "Thông báo", "Bạn muốn xóa thật không",
                                     QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Cancel)
            if(hoi==1024):
                check=self.checkNhanVien()
                if(len(check)>0):
                    self.deletChiTietHoaDonNhanVien()
                    self.deleteHoaDon()
                    self.deletChiTietPhieuMhapNhanVien()
                    self.deletePhieuNhap()
                    con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                    sql = "delete  from NHANVIEN where manhanvien='"+manhanvien+"'"
                    cursor = con.cursor()
                    try:
                        cursor.execute(sql)
                        con.commit()
                        self.ThongBaoOk("Bạn đã xóa thành công")
                    except cx_Oracle.DatabaseError as e:
                        print("There is a problem with Oracle", e)
                    finally:
                        cursor.close()
                        con.close()
                        lentable = self.uic1.tableWidget.rowCount()
                        if (lentable > 0):
                            i = 0
                            while (i <= lentable):
                                self.uic1.tableWidget.removeRow(0)
                                i = i + 1
                        self.ShowTable()
                else:
                    self.ThongBaoOk("Không có nhân viên cần xóa")
    def TimNhanVien(self):
        manhanvien = self.uic1.txtmanhanvien.text()
        if(len(manhanvien)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from NHANVIEN where manhanvien='" +manhanvien+ "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Nhân viên không tồn tại")
                else:
                    self.uic1.tableWidget.setRowCount(1)
                    for row in results:
                        self.uic1.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.uic1.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.uic1.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        self.uic1.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                        self.uic1.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
                        self.uic1.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
                        self.uic1.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập mã nhân viên")
    def ResetNhanVien(self):
        self.uic1.txtmanhanvien.setText("")
        self.uic1.txttennhanvien.setText("")
        self.uic1.txtsocccd.setText("")
        self.uic1.txtsodienthoai.setText("")
        self.uic1.txtdiachi.setPlainText("")
        self.uic1.txttaikhoan.setText("")
        self.uic1.txtmatkhau.setText("")
    def database(self):
        try:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select * from nhanvien  "
            cursor = con.cursor()
            cursor.execute(sql)
            results= cursor.fetchall()
            cursor.close()
            con.close()
            return results
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
    def ShowTable(self):
        data= self.database()
        self.uic1.tableWidget.setRowCount(15)
        i=0
        for row in data:
            self.uic1.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.uic1.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.uic1.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.uic1.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.uic1.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.uic1.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.uic1.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.uic1.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            i+=1
    def banHang(self):
        self.Second_window.close()
        self.load_Form_Hoa_Don()
    def getHoaDonNhanVien(self):
        item = []
        manhanvien = self.uic1.txtmanhanvien.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select  hoadon.mahoadon from hoadon join nhanvien on " \
              "hoadon.manhanvien = nhanvien.manhanvien " \
              " where nhanvien.manhanvien='" + manhanvien + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                item.append(i[0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def deletChiTietHoaDonNhanVien(self):
        mahoadon=self.getHoaDonNhanVien()
        for i in mahoadon:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from chitiethoadon where mahoadon='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def deleteHoaDon(self):
        mahoadon = self.getHoaDonNhanVien()
        for i in mahoadon:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from hoadon where mahoadon='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def getPhieuNhapNhanVien(self):
        item = []
        manhanvien = self.uic1.txtmanhanvien.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select  phieunhap.maphieunhap from phieunhap join nhanvien on " \
              "phieunhap.maphieunhap = nhanvien.manhanvien " \
              " where nhanvien.manhanvien='" + manhanvien + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                item.append(i[0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def deletChiTietPhieuMhapNhanVien(self):
        maphieunhap=self.getPhieuNhapNhanVien()
        for i in maphieunhap:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from chitietphieunhap where maphieunhap='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def deletePhieuNhap(self):
        maphieunhap=self.getPhieuNhapNhanVien()
        for i in maphieunhap:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from phieunhap where maphieunhap='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()

    ############################################################Khách Hàng##########################################
    def loadKhachHang(self):
        self.uic1.tableWidget_2.setColumnWidth(0,150)
        self.uic1.tableWidget_2.setColumnWidth(1, 270)
        self.uic1.tableWidget_2.setColumnWidth(2, 150)
        self.uic1.tableWidget_2.setColumnWidth(3, 400)
    def ScreenKhachHang(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_khachhang)
        self.loadKhachHang()
        self.ShowTableKhachHang()
    def ShowTableKhachHang(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from khachhang  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tableWidget_2.setRowCount(15)
            i=0
            for row in results:
                self.uic1.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.uic1.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.uic1.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic1.tableWidget_2.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
                i+=1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def TabletoFormKhachHang(self):
        for item in self.uic1.tableWidget_2.selectedItems():
            row = item.row()
            self.uic1.txtmakhachhang.setText(self.uic1.tableWidget_2.item(row, 0).text())
    def TimKhachHang(self):
        mankhachhang = self.uic1.txtmakhachhang.text()
        if(len(mankhachhang)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from khachhang where makhachhang='" +mankhachhang+ "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Khách hàng không tồn tại")
                else:
                    self.uic1.tableWidget_2.setRowCount(1)
                    for row in results:
                        self.uic1.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.uic1.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        self.uic1.tableWidget_2.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập mã khách hàng")
    def layMaHoaDon(self):
        makhachhang = self.uic1.txtmakhachhang.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sqllaydu = "select mahoadon from hoadon where makhachhang='" + makhachhang + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sqllaydu)
            results = cursor.fetchall()
            if(not results):
                return
            else:
                return results[0][0]
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def checkKhachHangTonTai(self):
        makhachhang = self.uic1.txtmakhachhang.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select *  from khachhang where makhachhang='" + makhachhang + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def XoaKhachHang(self):
        makhachhang = self.uic1.txtmakhachhang.text()
        if (len(makhachhang) == 0):
            self.ThongBaoOk("Mời bạn nhập mã khách hàng")
        else:
            hoi=QMessageBox.question(QtWidgets.QMessageBox(), "Thông báo", "Bạn có muốn xóa thật không",
                                     QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Cancel)
            if(hoi==1024):
                check=self.checkKhachHangTonTai()
                if(len(check)>0):
                    mahoadon =self.layMaHoaDon()
                    if(not mahoadon):
                        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                        sql ="delete from khachhang where makhachhang = '"+makhachhang+"'"
                        cursor = con.cursor()
                        try:
                            cursor.execute(sql)
                            con.commit()
                            self.ThongBaoOk("Xóa thành công")
                        except cx_Oracle.DatabaseError as e:
                            print("There is a problem with Oracle", e)
                        finally:
                            cursor.close()
                            con.close()
                    else:
                        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                        sqlxoacthd = "delete from chitiethoadon where mahoadon ='" + mahoadon + "'"
                        sqlxoahoadon = "delete from hoadon where mahoadon  ='" + mahoadon + "'"
                        cursor = con.cursor()
                        try:
                            cursor.execute(sqlxoacthd)
                            con.commit()
                            cursor.execute(sqlxoahoadon)
                            con.commit()
                        except cx_Oracle.DatabaseError as e:
                            print("There is a problem with Oracle", e)
                        finally:
                            cursor.close()
                            con.close()
                            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                            sql = "delete from khachhang where makhachhang = '" + makhachhang + "'"
                            cursor = con.cursor()
                            try:
                                cursor.execute(sql)
                                con.commit()
                                self.ThongBaoOk("Xóa thành công")
                            except cx_Oracle.DatabaseError as e:
                                print("There is a problem with Oracle", e)
                            finally:
                                cursor.close()
                                con.close()

                else:
                    self.ThongBaoOk("Không có khách hàng cần xóa")
        lentable = self.uic1.tableWidget_2.rowCount()
        if (lentable > 0):
            i = 0
            while (i <= lentable):
                self.uic1.tableWidget_2.removeRow(0)
                i = i + 1
        self.ShowTableKhachHang()
    def thongKeKhachHang(self):
        ngaybatdau = self.uic1.txtnbdkhchhang.text()
        ngayketthuc=self.uic1.txtnktkhachhang.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select count(makhachhang) from (select MAKHACHHANG from HOADON where " \
              " THOIGIAN between TO_DATE('"+ngaybatdau+"','yyyy-mm-dd') and TO_DATE('"+ngayketthuc+"','yyyy-mm-dd') " \
              "group by MAKHACHHANG )"
        cursor =con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            self.uic1.lbsokhachmua.setText(str(result[0][0]))
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()

    #################################################################Sản phẩm ##########################################
    ##############################################################################################################
    def ScreenSanPham(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_sanpham)
        self.loadsanpham()
        self.showTableSanPham()
        self.loadCbbManhaCungCap()
    def loadsanpham(self):
        self.uic1.tablesanpham.setColumnWidth(0,120)
        self.uic1.tablesanpham.setColumnWidth(1,420)
        self.uic1.tablesanpham.setColumnWidth(2,80)
        self.uic1.tablesanpham.setColumnWidth(3,80)
        self.uic1.tablesanpham.setColumnWidth(4,120)
        self.uic1.tablesanpham.setColumnWidth(5,140)
    def showTableSanPham(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from sanpham  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tablesanpham.setRowCount(15)
            i = 0
            for row in results:
                self.uic1.tablesanpham.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.uic1.tablesanpham.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.uic1.tablesanpham.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic1.tablesanpham.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.uic1.tablesanpham.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.uic1.tablesanpham.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
                i += 1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def loadCbbManhaCungCap(self):
        dem = self.uic1.cbbmanhacungcap.count()
        for i in range(0,dem):
            self.uic1.cbbmanhacungcap.removeItem(0)
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select manhacungcap from nhacungcap  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for item in results:
                self.uic1.cbbmanhacungcap.addItem(item[0])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
    def TabletoFormSanPham(self):
        for item in self.uic1.tablesanpham.selectedItems():
            row = item.row()
            self.uic1.txtmasanpham.setText(self.uic1.tablesanpham.item(row, 0).text())
            self.uic1.txttensanpham.setText(self.uic1.tablesanpham.item(row, 1).text())
            self.uic1.txtdongia.setText(self.uic1.tablesanpham.item(row, 2).text())
            self.uic1.txtdonvi.setText(self.uic1.tablesanpham.item(row, 3).text())
            self.uic1.txtsoluongcon.setText(self.uic1.tablesanpham.item(row, 4).text())
            dem=self.uic1.cbbmanhacungcap.count()
            for i in range(0,dem):
                self.uic1.cbbmanhacungcap.removeItem(0)
            self.uic1.cbbmanhacungcap.addItem(self.uic1.tablesanpham.item(row, 5).text())
    def themSanpPham(self):
        masanpham = self.uic1.txtmasanpham.text()
        tensanpham = self.uic1.txttensanpham.toPlainText()
        dongia = self.uic1.txtdongia.text()
        donvi = self.uic1.txtdonvi.text()
        soluongcon = self.uic1.txtsoluongcon.text()
        if (len(masanpham) == 0):
            self.ThongBaoOk("Mời bạn nhập mã sản phẩm")
        elif (len(tensanpham) == 0):
            self.ThongBaoOk("Mời bạn nhập tên sản phẩm")
        elif (len(dongia) == 0):
            self.ThongBaoOk("Mời bạn nhập đơn giá")
        elif(len(donvi)==0):
            self.ThongBaoOk("Mời bạn nhập đơn vị")
        elif (len(soluongcon) == 0):
            self.ThongBaoOk("Mời bạn nhập số lượng còn")
        else:
            manhacungcap =self.uic1.cbbmanhacungcap.currentText()
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""insert into sanpham (masanpham, tensanpham, dongia, donvi,soluongcon, manhacungcap)
                          values ('{masanpham}', '{tensanpham}', {float(dongia)},'{donvi}',
                          {int(soluongcon)}, '{manhacungcap}')"""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                self.ThongBaoOk("Thêm thành công")
            except cx_Oracle.DatabaseError as e:
                self.ThongBaoOk("Đã tồn tại mã sản phẩm")
            finally:
                cursor.close()
                con.close()
                self.ScreenSanPham()
    def suaSanPham(self):
        masanpham = self.uic1.txtmasanpham.text()
        if (len(masanpham) == 0):
            self.ThongBaoOk("Mời bạn nhập mã nhân viên")
        else:
            tensanpham = self.uic1.txttensanpham.toPlainText()
            dongia = self.uic1.txtdongia.text()
            donvi = self.uic1.txtdonvi.text()
            soluongcon = self.uic1.txtsoluongcon.text()
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""update  sanpham set tensanpham='{tensanpham}', dongia={float(dongia)}, donvi='{donvi}'
               ,soluongcon={int(soluongcon)} where masanpham ='{masanpham}'"""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                self.ThongBaoOk("Update thành công")
            except cx_Oracle.DatabaseError as e:
                   print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
                self.ScreenSanPham()
    def checkSanPham(self):
        masanpham = self.uic1.txtmasanpham.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select *  from sanpham where masanpham='" + masanpham + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaSanPham(self):
        masanpham = self.uic1.txtmasanpham.text()
        if(len(masanpham)==0):
            self.ThongBaoOk("Mời bạn nhập mã sản phẩm")
        else:
            hoi=QMessageBox.question(QtWidgets.QMessageBox(), "Thông báo", "Bạn muốn xóa thật không",
                                     QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Cancel)
            if(hoi==1024):
                check=self.checkSanPham()
                if(len(check)>0):
                    mahoadon= self.getHoaDonSanPham()
                    maphieunhap=self.getPhieuNhapSanPham()
                    self.deleteChiTietHoaDonSanPham(mahoadon)
                    self.deleteChiTietPhieuNhapSanPham(maphieunhap)
                    self.deleteHoaDonSanPham(mahoadon)
                    self.deletePhieuNhapSanPham(maphieunhap)
                    con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                    sql = "delete  from sanpham where masanpham='"+masanpham+"'"
                    cursor = con.cursor()
                    try:
                        cursor.execute(sql)
                        con.commit()
                        self.ThongBaoOk("Bạn đã xóa thành công")
                    except cx_Oracle.DatabaseError as e:
                        print("There is a problem with Oracle", e)
                    finally:
                        cursor.close()
                        con.close()
                        lentable = self.uic1.tablesanpham.rowCount()
                        if (lentable > 0):
                            i = 0
                            while (i <= lentable):
                                self.uic1.tablesanpham.removeRow(0)
                                i = i + 1
                        self.showTableSanPham()
                else:
                    self.ThongBaoOk("Không có sản phẩm cần xóa")
    def timSanPham(self):
        masanpham = self.uic1.txtmasanpham.text()
        if(len(masanpham)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from sanpham where masanpham='" +masanpham+ "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Sản phẩm không tồn tại")
                else:
                    self.uic1.tablesanpham.setRowCount(1)
                    for row in results:
                        self.uic1.tablesanpham.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.uic1.tablesanpham.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.uic1.tablesanpham.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        self.uic1.tablesanpham.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
                        self.uic1.tablesanpham.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                        self.uic1.tablesanpham.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập mã sản phẩm")
    def resetSanPham(self):
        self.uic1.txtmasanpham.setText("")
        self.uic1.txttensanpham.setText("")
        self.uic1.txtdonvi.setText("")
        self.uic1.txtdongia.setText("")
        self.uic1.txtsoluongcon.setText("")
        self.uic1.txttaikhoan.setText("")
        dem = self.uic1.cbbmanhacungcap.count()
        for i in range(0, dem):
            self.uic1.cbbmanhacungcap.removeItem(0)
        self.loadCbbManhaCungCap()
    def getHoaDonSanPham(self):
        item = []
        masanpham = self.uic1.txtmasanpham.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select  mahoadon from chitiethoadon where masanpham='" + masanpham + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                item.append(i[0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def deleteHoaDonSanPham(self,mahoadon):
        for i in mahoadon:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from hoadon where mahoadon='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def deleteChiTietHoaDonSanPham(self,mahoadon):
        mahoadon = self.getHoaDonSanPham()
        for i in mahoadon:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from chitiethoadon where mahoadon='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def getPhieuNhapSanPham(self):
        item = []
        masanpham = self.uic1.txtmasanpham.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select  maphieunhap from chitietphieunhap where masanpham='" + masanpham + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                item.append(i[0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def deletePhieuNhapSanPham(self,maphieunhap):
        for i in maphieunhap:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from phieunhap where maphieunhap='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def deleteChiTietPhieuNhapSanPham(self,maphieunhap):
        for i in maphieunhap:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from chitietphieunhap where maphieunhap='" + i + "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()

    #############################################################Nhà cung cấp ##########################################
    ##############################################################################################################
    def screenNhaCungcap(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_nhacungcap)
        self.uic1.tablenhacungcap.setColumnWidth(0, 150)
        self.uic1.tablenhacungcap.setColumnWidth(1, 380)
        self.uic1.tablenhacungcap.setColumnWidth(2, 100)
        self.uic1.tablenhacungcap.setColumnWidth(3, 320)
        self.showTableNhaCungCap()
    def showTableNhaCungCap(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from nhacungcap  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tablenhacungcap.setRowCount(15)
            i = 0
            for row in results:
                self.uic1.tablenhacungcap.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.uic1.tablenhacungcap.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.uic1.tablenhacungcap.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic1.tablenhacungcap.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
                i += 1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def TabletoFormNhaCungCap(self):
        for item in self.uic1.tablenhacungcap.selectedItems():
            row = item.row()
            self.uic1.txtmancc.setText(self.uic1.tablenhacungcap.item(row, 0).text())
            self.uic1.txttenncc.setText(self.uic1.tablenhacungcap.item(row, 1).text())
            self.uic1.txtsdtncc.setText(self.uic1.tablenhacungcap.item(row, 2).text())
            self.uic1.txtdiachincc.setText(self.uic1.tablenhacungcap.item(row, 3).text())
    def themNhaCungCap(self):
        manhacungcap = self.uic1.txtmancc.text()
        tennhacungcap = self.uic1.txttenncc.toPlainText()
        sodienthoaincc = self.uic1.txtsdtncc.text()
        diachincc = self.uic1.txtdiachincc.toPlainText()
        if (len(manhacungcap) == 0):
            self.ThongBaoOk("Mời bạn nhập mã nhà cung cấp")
        elif(len(tennhacungcap)==0):
            self.ThongBaoOk("Mời bạn nhập tên nhà cung")
        elif(len(sodienthoaincc)==0):
            self.ThongBaoOk("Mời bạn nhập số điện thoại")
        elif (len(diachincc) == 0):
            self.ThongBaoOk("Mời bạn nhập địa chỉ ")
        else:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""insert into nhacungcap (manhacungcap, tennhacungcap, sodienthoai, diachi)
                  values ('{manhacungcap}', '{tennhacungcap}', '{sodienthoaincc}','{diachincc}')"""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                self.ThongBaoOk("Thêm thành công")
            except cx_Oracle.DatabaseError as e:
                self.ThongBaoOk("Đã tồn tại mã nhà cung cấp")
            finally:
                cursor.close()
                con.close()
                self.screenNhaCungcap()
    def suaNhaCungCap(self):
        manhacungcap = self.uic1.txtmancc.text()
        if (len(manhacungcap) == 0):
            self.ThongBaoOk("Mời bạn nhập mã nhà cung cấp")
        else:
            tennhacungcap = self.uic1.txttenncc.toPlainText()
            sodienthoai = int(self.uic1.txtsdtncc.text())
            diachi = self.uic1.txtdiachincc.toPlainText()
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""update  nhacungcap set tennhacungcap='{tennhacungcap}', sodienthoai={sodienthoai}
            , diachi='{diachi}'where manhacungcap ='{manhacungcap}'"""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                self.ThongBaoOk("Update thành công")
            except cx_Oracle.DatabaseError as e:
                self.ThongBaoOk("Update thất bại")
            finally:
                cursor.close()
                con.close()
                self.screenNhaCungcap()
    def getMaPhieuNhap(self):
        manhacungcap = self.uic1.txtmancc.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select maphieunhap  from sanpham where manhacungcap='" + manhacungcap + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result[0][0]
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def getMaSanPhamCTPN(self):
        item=[]
        manhacungcap = self.uic1.txtmancc.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select  SANPHAM.masanpham from SANPHAM join CHITIETPHIEUNHAP on " \
              "CHITIETPHIEUNHAP.masanpham = SANPHAM.masanpham join NHACUNGCAP " \
              "on NHACUNGCAP.manhacungcap = SANPHAM.manhacungcap" \
              " where NHACUNGCAP.MANHACUNGCAP='"+manhacungcap+"' group by SANPHAM.masanpham"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                item.append(i[0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def getMaSanPhamCTHD(self):
        item = []
        manhacungcap = self.uic1.txtmancc.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select  SANPHAM.masanpham from SANPHAM join chitiethoadon on " \
              "chitiethoadon.masanpham = SANPHAM.masanpham join NHACUNGCAP " \
              "on NHACUNGCAP.manhacungcap = SANPHAM.manhacungcap" \
              " where NHACUNGCAP.MANHACUNGCAP='" + manhacungcap + "' group by SANPHAM.masanpham"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                item.append(i[0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaChitietPhieuNhapNhaCungCap1(self):
        maphieunhap= self.getMaPhieuNhap()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "delete from chitietphieunhap where maphieunhap='" + maphieunhap + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaChiTietPhieuNhapNhaCungcap2(self):
        masanpham=self.getMaSanPhamCTPN()
        for i in masanpham:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from chitietphieunhap where masanpham=" + str(i) + ""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def xoaChiTietHoaDonNhaCungcap(self):
        masanpham = self.getMaSanPhamCTHD()
        for i in masanpham:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "delete from chitiethoadon where masanpham=" + str(i) + ""
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
    def xoaPhieuNhapNhaCungCap(self):
        manhacungcap = self.uic1.txtmancc.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "delete  from phieunhap where manhacungcap='" + manhacungcap + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaSanPhamNhaCungCap(self):
        manhacungcap = self.uic1.txtmancc.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "delete  from sanpham where manhacungcap='" + manhacungcap + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def checkNhaCungCap(self):
        manhacungcap = self.uic1.txtmancc.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select *  from nhacungcap where manhacungcap='" + manhacungcap + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaNhaCungCap(self):
        manhacungcap = self.uic1.txtmancc.text()
        if(len(manhacungcap)==0):
            self.ThongBaoOk("Mời bạn nhập mã nha cung cấp")
        else:
            hoi=QMessageBox.question(QtWidgets.QMessageBox(), "Thông báo", "Hành động này sẽ xóa dữ liệu Hóa Đơn,"
                                                                           "Phiếu Nhập,Sản Phẩm."
                                                                           "Bạn vẫn muốn xóa chứ?",
                                     QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Cancel)
            if(hoi==1024):
                check = self.checkNhaCungCap()
                if(len(check)>0):
                    self.xoaChiTietHoaDonNhaCungcap()
                    self.xoaChiTietPhieuNhapNhaCungcap2()
                    self.xoaSanPhamNhaCungCap()
                    self.xoaPhieuNhapNhaCungCap()
                    con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                    sql = "delete  from nhacungcap where manhacungcap='"+manhacungcap+"'"
                    cursor = con.cursor()
                    try:
                        cursor.execute(sql)
                        con.commit()
                        self.ThongBaoOk("Bạn đã xóa thành công")
                    except cx_Oracle.DatabaseError as e:
                        print("There is a problem with Oracle", e)
                    finally:
                        cursor.close()
                        con.close()
                        lentable = self.uic1.tablenhacungcap.rowCount()
                        if (lentable > 0):
                            i = 0
                            while (i <= lentable):
                                self.uic1.tablenhacungcap.removeRow(0)
                                i = i + 1
                        self.showTableNhaCungCap()
                else:
                    self.ThongBaoOk("Không có nhà cung cấp cần xóa")
    def timNhaCungcap(self):
        manhacungcap = self.uic1.txtmancc.text()
        if(len(manhacungcap)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from nhacungcap where manhacungcap='" +manhacungcap+ "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("nhà cung cấp  không tồn tại")
                else:
                    self.uic1.tablenhacungcap.setRowCount(1)
                    for row in results:
                        self.uic1.tablenhacungcap.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tablenhacungcap.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.uic1.tablenhacungcap.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        self.uic1.tablenhacungcap.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập mã nhà cung cấp")
    def resetNhaCungCao(self):
        self.uic1.txtmancc.setText("")
        self.uic1.txtsdtncc.setText("")
        self.uic1.txttenncc.setText("")
        self.uic1.txtdiachincc.setText("")

    #############################################################Hóa đơn ##########################################
    ##############################################################################################################
    def screenHoaDon(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_hoadon)
        self.uic1.tablehoadon.setColumnWidth(0, 120)
        self.uic1.tablehoadon.setColumnWidth(1, 150)
        self.uic1.tablehoadon.setColumnWidth(2, 150)
        self.uic1.tablehoadon.setColumnWidth(3, 150)
        self.uic1.tablehoadon.setColumnWidth(4, 150)
        self.uic1.tablehoadon.setColumnWidth(5, 150)
        self.uic1.tablehoadon.setColumnWidth(6, 120)
        self.showTableHoaDon()
    def showTableHoaDon(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from hoadon  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tablehoadon.setRowCount(15)
            i=0
            for row in results:
                self.uic1.tablehoadon.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.uic1.tablehoadon.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.uic1.tablehoadon.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic1.tablehoadon.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.uic1.tablehoadon.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.uic1.tablehoadon.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
                self.uic1.tablehoadon.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
                i+=1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def tableToFormHoaDon(self):
        for item in self.uic1.tablehoadon.selectedItems():
            row = item.row()
            self.uic1.txtmahoadon.setText(self.uic1.tablehoadon.item(row, 0).text())
    def timHoaDon(self):
        mahoadon = self.uic1.txtmahoadon.text()
        if(len(mahoadon)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from hoadon where mahoadon='" +mahoadon+ "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Hóa đơn không tồn tại")
                else:
                    self.uic1.tablehoadon.setRowCount(1)
                    for row in results:
                        self.uic1.tablehoadon.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tablehoadon.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                        self.uic1.tablehoadon.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        self.uic1.tablehoadon.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        self.uic1.tablehoadon.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                        self.uic1.tablehoadon.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
                        self.uic1.tablehoadon.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập mã hóa đơn")
    def thongKeHoaDon(self):
        ngaybatdau = self.uic1.txtnbdhoadon.text()
        ngayketthuc=self.uic1.txtngaykthoadon.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select count(mahoadon) from HOADON where " \
              " THOIGIAN between TO_DATE('"+ngaybatdau+"','yyyy-mm-dd') and TO_DATE('"+ngayketthuc+"','yyyy-mm-dd') "
        cursor =con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            self.uic1.lbsohoadon.setText(str(result[0][0]))
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def checkHoaDon(self):
        mahoadon = self.uic1.txtmahoadon.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select *  from hoadon where mahoadon='" + mahoadon + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaChiTietHoaDon1(self):
        mahoadon= self.uic1.txtmahoadon.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql ="delete from chitiethoadon where mahoadon ='"+mahoadon+"'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaHoaDon(self):
        mahoadon = self.uic1.txtmahoadon.text()
        if (len(mahoadon) == 0):
            self.ThongBaoOk("Mời bạn nhập mã hóa đơn")
        else:
            hoi = QMessageBox.question(QtWidgets.QMessageBox(), "Thông báo", "Bạn muốn xóa thật không",
                                       QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if (hoi == 1024):
                check = self.checkHoaDon()
                if(len(check)>0):
                    self.xoaChiTietHoaDon1()
                    con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                    sql = "delete  from hoadon where mahoadon='" + mahoadon + "'"
                    cursor = con.cursor()
                    try:
                        cursor.execute(sql)
                        con.commit()
                        self.ThongBaoOk("Bạn đã xóa thành công")
                    except cx_Oracle.DatabaseError as e:
                        print("There is a problem with Oracle", e)
                    finally:
                        cursor.close()
                        con.close()
                    lentable = self.uic1.tablehoadon.rowCount()
                    if (lentable > 0):
                        i = 0
                        while (i <= lentable):
                            self.uic1.tablehoadon.removeRow(0)
                            i = i + 1
                    self.showTableHoaDon()
                else:
                    self.ThongBaoOk("Không có hóa đơn cần xóa")

    #############################################################Hóa đơn ##########################################
    ##############################################################################################################
    def screenPhieuNhap(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_phieunhap)
        self.uic1.tablephieunhap.setColumnWidth(0, 180)
        self.uic1.tablephieunhap.setColumnWidth(1, 180)
        self.uic1.tablephieunhap.setColumnWidth(2, 180)
        self.uic1.tablephieunhap.setColumnWidth(3, 180)
        self.uic1.tablephieunhap.setColumnWidth(4, 180)
        self.showTablePhieuNhap()
    def showTablePhieuNhap(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from phieunhap  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tablephieunhap.setRowCount(15)
            i=0
            for row in results:
                self.uic1.tablephieunhap.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.uic1.tablephieunhap.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.uic1.tablephieunhap.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.uic1.tablephieunhap.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.uic1.tablephieunhap.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                i+=1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def tableToFormPhieuNhap(self):
        for item in self.uic1.tablephieunhap.selectedItems():
            row = item.row()
            self.uic1.txtmaphieunhap.setText(self.uic1.tablephieunhap.item(row, 0).text())
    def timPhieuNhap(self):
        maphieunhap = self.uic1.txtmaphieunhap.text()
        if(len(maphieunhap)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from phieunhap where maphieunhap='" +maphieunhap+ "'"
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Phiếu nhập không tồn tại")
                else:
                    self.uic1.tablephieunhap.setRowCount(1)
                    for row in results:
                        self.uic1.tablephieunhap.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tablephieunhap.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.uic1.tablephieunhap.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.uic1.tablephieunhap.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        self.uic1.tablephieunhap.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập mã phiếu nhập")
    def checkPhieuNhap(self):
        maphieunhap = self.uic1.txtmaphieunhap.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select *  from phieunhap where maphieunhap='" + maphieunhap + "'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaChiTietPhieuNhap(self):
        maphieunhap= self.uic1.txtmaphieunhap.text()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql ="delete from chitietphieunhap where maphieunhap ='"+maphieunhap+"'"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def xoaPhieuNhap(self):
        maphieunhap = self.uic1.txtmaphieunhap.text()
        if (len(maphieunhap) == 0):
            self.ThongBaoOk("Mời bạn nhập mã phiếu nhập")
        else:
            hoi = QMessageBox.question(QtWidgets.QMessageBox(), "Thông báo", "Bạn muốn xóa thật không",
                                       QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if (hoi == 1024):
                check = self.checkPhieuNhap()
                if(len(check)>0):
                    self.xoaChiTietPhieuNhap()
                    con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                    sql = "delete  from phieunhap where maphieunhap='" + maphieunhap + "'"
                    cursor = con.cursor()
                    try:
                        cursor.execute(sql)
                        con.commit()
                        self.ThongBaoOk("Bạn đã xóa thành công")
                    except cx_Oracle.DatabaseError as e:
                        print("There is a problem with Oracle", e)
                    finally:
                        cursor.close()
                        con.close()
                    lentable = self.uic1.tablephieunhap.rowCount()
                    if (lentable > 0):
                        i = 0
                        while (i <= lentable):
                            self.uic1.tablephieunhap.removeRow(0)
                            i = i + 1
                    self.showTablePhieuNhap()
                else:
                    self.ThongBaoOk("Không có phiếu nhập cần xóa")

    #############################################################Chi Tiết ##########################################
    ##############################################################################################################
    def screenChiTiet(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_chitiet)
        self.showTableChiTietHoaDon()
        self.showTableChiTietPhieuNhap()
    def showTableChiTietHoaDon(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from chitiethoadon  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tableWidget_3.setRowCount(15)
            i=0
            for row in results:
                self.uic1.tableWidget_3.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.uic1.tableWidget_3.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.uic1.tableWidget_3.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic1.tableWidget_3.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                i+=1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def showTableChiTietPhieuNhap(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from chitietphieunhap  "
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic1.tableWidget_4.setRowCount(15)
            i=0
            for row in results:
                self.uic1.tableWidget_4.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.uic1.tableWidget_4.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.uic1.tableWidget_4.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic1.tableWidget_4.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                i+=1
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def timChiTietHoaDon(self):
        mahoadon = self.uic1.txtmahoadonchitiet.text()
        if( len(mahoadon)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from chitiethoadon where mahoadon='" +mahoadon+ "' "
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Chi tiết hóa đơn không tồn tại")
                else:
                    self.uic1.tableWidget_3.setRowCount(len(results))
                    for row in results:
                        self.uic1.tableWidget_3.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tableWidget_3.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                        self.uic1.tableWidget_3.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        self.uic1.tableWidget_3.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập đủ thông tin")
    def timChiTietPhieuNhap(self):
        maphieunhap = self.uic1.txtmaphieunhapchitiet.text()
        if( len(maphieunhap)>0):
            i=0
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select *  from chitietphieunhap where maphieunhap='" +maphieunhap+ "' "
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if(not results):
                    self.ThongBaoOk("Chi tiết phiếu nhập không tồn tại")
                else:
                    self.uic1.tableWidget_4.setRowCount(len(results))
                    for row in results:
                        self.uic1.tableWidget_4.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.uic1.tableWidget_4.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                        self.uic1.tableWidget_4.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        self.uic1.tableWidget_4.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        i += 1
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
        else:
            self.ThongBaoOk("Mời bạn nhập đủ thông tin")

    #############################################################Chi Tiết ##########################################
    ##############################################################################################################
    def screenThongKe(self):
        self.uic1.stackedWidget.setCurrentWidget(self.uic1.screen_thongke)
        self.loadCbbTenSanPham()
    def showChart(self):
        self.uic1.screen.addWidget(show_chart())
    def loadCbbTenSanPham(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select tensanpham from sanpham"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for item in results:
                self.uic1.cbbtensanpham.addItem(item[0])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def hienThiThongTinSanPhamThongKe(self):
        global test1
        tensanpham = self.uic1.cbbtensanpham.currentText()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from sanpham where tensanpham ='" + tensanpham + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            test1 = results[0][0]
            self.uic1.lbmasanphamtk.setText(str(results[0][0]))
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def thoat1(self):
        self.Second_window.close()
        self.main_win.show()
class show_chart(FigureCanvasQTAgg,LamViec):
    def __init__(self):
        self.fig, self.ax =plt.subplots()
        super().__init__(self.fig)

        self.Second_window = QtWidgets.QMainWindow()
        self.uic1 = Form_Gui_Lam_Viec()
        self.uic1.setupUi(self.Second_window)

        soluong =self.laySoLuong(test1)
        self.veChart(soluong)
    def veChart(self,soluong):
        name=('1 tháng trước', '2 tháng trước', '3 tháng trước')
        N = len(name)
        ind = np.arange(N)
        width = 0.35
        p1 = self.ax.bar(ind, soluong, width, label='Số lượng')

        self.ax.axhline(0, color='grey', linewidth=0.8)
        self.ax.set_ylabel('Số lượng bán ra')
        self.ax.set_title('Số lượng bán ra trong 3 tháng gần nhất')
        self.ax.set_xticks(ind)
        self.ax.set_xticklabels(name)
        self.ax.legend()
        self.ax.bar_label(p1, label_type='center')
    def laySoLuong(self,masanpham):
        sql = f"""select sum(a.SOLUONG) soluong from CHITIETHOADON a join HOADON b on a.MAHOADON=b.MAHOADON
             where b.THOIGIAN <=current_date and a.MASANPHAM={masanpham} union all 
             select sum(a.SOLUONG) soluong from CHITIETHOADON a join HOADON b on a.MAHOADON=b.MAHOADON 
             where b.THOIGIAN <=(current_date-30) and a.MASANPHAM={masanpham} union  all 
             select sum(a.SOLUONG) soluong from CHITIETHOADON a join HOADON b on a.MAHOADON=b.MAHOADON 
             where b.THOIGIAN <=(current_date-60) and a.MASANPHAM={masanpham}"""
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if((results[0][0]==None and results[1][0]==None and results[2][0]==None) ):
                item=(0,0,0)
            if (results[0][0] == None and results[1][0] != None and results[2][0] == None):
                item = (0, results[1][0], 0)
            if (results[0][0] == None and results[1][0] == None and results[2][0] != None):
                item = (0, 0, results[2][0])
            if (results[0][0] != None and results[1][0] == None and results[2][0] == None):
                item=(results[0][0],0,0)
            if (results[0][0] != None and results[1][0] != None and results[2][0] == None):
                item=(results[0][0],results[1][0],0)
            if (results[0][0] != None and results[1][0] != None and results[2][0] != None):
                item=(results[0][0],results[1][0],results[2][0])
            return item
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()

