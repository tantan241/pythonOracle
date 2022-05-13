import cx_Oracle
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QWidget
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog
from PyQt5 import QtWidgets
from Gui_Lam_Viec import Ui_Form
from Lam_Viec import Ui_Form
from Gui import Ui_MainWindow
from datetime import date,datetime
from Gui_Hoa_Don import Ui_Form as Form_Gui_Hoa_Don

class HoaDon:
    def __init__(self):
        self.third_window = QtWidgets.QMainWindow()
        self.uic2 = Form_Gui_Hoa_Don()
        self.uic2.setupUi((self.third_window))
    def form_Hoa_Don_Click(self):
        self.uic2.cbbtenncc.activated.connect(self.loadComboBoxtensanpham)
        self.uic2.cbbtensanpham.activated.connect(self.hienThiThongTinSanPhamPhieuNhap)
        self.uic2.btnthamchitiet.clicked.connect(self.themChiTietNhapHang)
        self.uic2.btnxoachitiet.clicked.connect(self.xoaChiTietSanPham)
        self.uic2.btnin.clicked.connect(self.InPhieuNhap)
        self.uic2.btnlammoi.clicked.connect(self.lamMoiPhieuNhap)
        self.uic2.cbbtensphoadon.activated.connect(self.hienThiThongTinSanPhamHoaDon)
        self.uic2.btnaddchithiethoadon.clicked.connect(self.themChiTietHoaDon)
        self.uic2.btnxoachitiethoadon.clicked.connect(self.xoaChiTietHoaDon)
        self.uic2.btninhoadon.clicked.connect(self.InHoaDon)
        self.uic2.btnlammoihoadon.clicked.connect(self.lamMoiHoaDon)
        self.uic2.btnthoat.clicked.connect(self.thoat)
    def showMaNhanVien(self):
        self.uic2.lbmanhanvien.setText(self.setmanhanvien)
        self.uic2.lbtennhanvien.setText(self.settennhanvien)
    def hienNgay(self):
        day = date.today()
        self.uic2.lbngay.setText(str(day))
    def loadComboboxncc(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select tennhacungcap,manhacungcap from NHACUNGCAP"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for item in results:
                self.uic2.cbbtenncc.addItem(item[0])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def loadComboBoxtensanpham(self):
        tennhacungcap = self.uic2.cbbtenncc.currentText()
        self.uic2.cbbtenncc.setEnabled(False)
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql1 ="select manhacungcap from nhacungcap where tennhacungcap='"+tennhacungcap+"'"
        sql ="select SANPHAM.tensanpham from NHACUNGCAP join SANPHAM on NHACUNGCAP.manhacungcap=SANPHAM.manhacungcap " \
              "where NHACUNGCAP.tennhacungcap='"+tennhacungcap+"'"
        cursor = con.cursor()
        try:
            cursor.execute(sql1)
            resulte1 =cursor.fetchall()
            self.uic2.lbmanhacungcap.setText(resulte1[0][0])
            cursor.execute(sql)
            results = cursor.fetchall()
            for item in results:
                self.uic2.cbbtensanpham.addItem(str(item[0]))
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def hienThiThongTinSanPhamPhieuNhap(self):
        tensanpham =self.uic2.cbbtensanpham.currentText()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from sanpham where tensanpham ='" + tensanpham + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic2.lbmasp.setText(str(results[0][0]))
            self.uic2.lbdonvi.setText(results[0][3])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def themChiTietNhapHang(self):
        masanpham = self.uic2.lbmasp.text()
        tensanpahm = self.uic2.cbbtensanpham.currentText()
        soluong = self.uic2.txtsoluongphieunhap.text()
        donvi=self.uic2.lbdonvi.text()
        thanhtien1 =self.uic2.txtgianhap.text()

        if (len(masanpham) == 0 or len(tensanpahm) == 0 or len(soluong) == 0 or len(donvi) == 0 or
                len(str(thanhtien1)) == 0):
            self.ThongBaoOk("Mời bạn nhập đủ thông tin")
        else:
            thanhtien = int(self.uic2.txtgianhap.text()) * int(soluong)
            row=(masanpham,tensanpahm,str(soluong),donvi,str(thanhtien))
            countrow = self.uic2.tableWidget.rowCount() + 1
            i=self.uic2.tableWidget.rowCount()
            self.uic2.tableWidget.setRowCount(countrow)
            self.uic2.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.uic2.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.uic2.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.uic2.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.uic2.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
    def xoaChiTietSanPham(self):
        lentable = self.uic2.tableWidget.rowCount()
        if (lentable > 0):
            for item in self.uic2.tableWidget.selectedItems():
                row = item.row()
            self.uic2.tableWidget.removeRow(row)
        else:
            self.ThongBaoOk("Mời bạn nhập đủ thông tin")
    def setMaPhieuNhap(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select count(maphieunhap),max(maphieunhap) from phieunhap "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            soluongphieu = result[0][0]
            taoma=''
            if(soluongphieu==None):
                taoma="PN-00000001"
            elif(soluongphieu>0):
                tachma = result[0][1].split("-")
                firstbill= tachma[0]+"-"
                secondbill=''
                k=int(tachma[1])
                k=k+1
                if(k<10):
                    secondbill=secondbill+"0000000"
                elif(k<100):
                    secondbill=secondbill+"000000"
                elif(k<1000):
                    secondbill=secondbill+"00000"
                elif(k<10000):
                    secondbill=secondbill+"0000"
                elif(k<100000):
                    secondbill=secondbill+"000"
                elif(k<1000000):
                    secondbill=secondbill+"00"
                elif (k < 10000000):
                    secondbill=secondbill+"0"
                taoma=firstbill+secondbill+str(k)
            self.uic2.lbmaphieunhap.setText(taoma)
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def laySoLuongSanPhamCon(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        cursor = con.cursor()
        results=[]
        for i in range(0,self.uic2.tableWidget.rowCount()):
            masanpham = self.uic2.tableWidget.item(i, 0).text()
            soluongnhap = self.uic2.tableWidget.item(i, 2).text()
            item = (masanpham,soluongnhap)
            results.append(item)
        for j in results:
            masanpham=j[0]
            soluongnhapthem=int(j[1])
            sqllaysoluongcon = "select soluongcon from sanpham where masanpham= "+masanpham+""

            try:
                cursor.execute(sqllaysoluongcon)
                result =cursor.fetchall()
                soluongcon= result[0][0]+soluongnhapthem
                sqlupdate = f"""update  sanpham set soluongcon={soluongcon} where masanpham = {masanpham}"""
                cursor.execute(sqlupdate)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
        cursor.close()
        con.close()
    def InPhieuNhap(self):
        lentable = self.uic2.tableWidget.rowCount()
        if (lentable > 0):
            tongtien=0
            result =[]
            maphieunhap=self.uic2.lbmaphieunhap.text()
            manhanvien= self.uic2.lbmanhanvien.text()
            manhacungcap=self.uic2.lbmanhacungcap.text()
            thoigian=self.uic2.lbngay.text()
            for i in range(0,self.uic2.tableWidget.rowCount()):
                masanpham = self.uic2.tableWidget.item(i, 0).text()
                soluongnhap = int(self.uic2.tableWidget.item(i, 2).text())
                thanhtien = float(self.uic2.tableWidget.item(i, 4).text())
                tongtien+=thanhtien
                item = (maphieunhap,masanpham, thanhtien, soluongnhap)
                result.append(item)
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = f"""insert into phieunhap (maphieunhap, manhanvien, manhacungcap, thoigian,tongtien)
                 values ('{maphieunhap}', '{manhanvien}', '{manhacungcap}'
                 ,TO_DATE('{thoigian}','yyyy-mm-dd'),{tongtien})"""

            cursor = con.cursor()
            try:
                cursor.execute(sql)
                con.commit()
                for i in range(0,len(result)):
                    maphieunhapis=result[i][0]
                    masanphamis=result[i][1]
                    thanhtienis = result[i][2]
                    soluongnhapis = result[i][3]
                    sql1 = f"""insert into chitietphieunhap (maphieunhap, masanpham, chitiettien, soluongnhap)
                                 values ('{maphieunhapis}', '{masanphamis}', {thanhtienis},{soluongnhapis})"""
                    cursor.execute(sql1)
                    con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            finally:
                cursor.close()
                con.close()
            self.laySoLuongSanPhamCon()
            self.layDuLieuIn()
            self.PrintPDf()
        else:
            self.ThongBaoOk("Mời bạn điền đầy đủ thông tin")
    def PrintPDf(self):
        printer =  QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.uic2.textEdit.print(printer)
    def layDuLieuIn(self):
        tongtien=0
        self.uic2.textEdit.append("*******************Phiếu nhập hàng*******************")
        self.uic2.textEdit.append("\n")
        self.uic2.textEdit.append("\t"+"\t"+"\t"+"\t"+"  Ngày: "+""+self.uic2.lbngay.text()+"")
        self.uic2.textEdit.append("\n")
        self.uic2.textEdit.append(" Nhân viên thực hiên:"+"\t"+"\t"+""+self.uic2.lbtennhanvien.text()+"")
        self.uic2.textEdit.append(" Tên nhà cung cấp:"+"\t"+"\t"+" "+self.uic2.cbbtenncc.currentText()+"")
        self.uic2.textEdit.append("\n")
        self.uic2.textEdit.append(" Tên sản phẩm"+"\t"+"      "+"Đơn vị"+"\t"+"  "+"Số lượng"+"\t"+"  "+"Tiền")
        self.uic2.textEdit.append("\n")
        results = []
        for i in range(0, self.uic2.tableWidget.rowCount()):
            tensanpham = self.uic2.tableWidget.item(i, 1).text()
            soluongnhap = self.uic2.tableWidget.item(i, 2).text()
            donvi=self.uic2.tableWidget.item(i,3).text()
            thanhtien = self.uic2.tableWidget.item(i, 4).text()
            item = (tensanpham,soluongnhap,donvi,thanhtien )
            tongtien=tongtien+float(thanhtien)
            results.append(item)
        for item in results:
            tensanpham = item[0]
            soluongnhap =item[1]
            donvi = item[2]
            thanhtien = item[3]
            self.uic2.textEdit.append(" "+""+tensanpham+""+"\n"+"\t"+"\t"+"      "+""+donvi+""+"        "+soluongnhap+""+"\t"+thanhtien+"")
            self.uic2.textEdit.append("\n")
            self.uic2.textEdit.append("------------------------------------------------------------------------")
        self.uic2.textEdit.append("Tổng tiền :"+"\t"+"\t"+"\t"+""+str(tongtien)+"")
    def lamMoiPhieuNhap(self):
        self.uic2.cbbtenncc.setEnabled(True)
        lencbbtensanpham=self.uic2.cbbtensanpham.count()
        for i in range(0,lencbbtensanpham):
            self.uic2.cbbtensanpham.removeItem(0)
        self.uic2.lbmanhacungcap.setText("")
        self.uic2.lbmasp.setText("")
        self.uic2.txtsoluongphieunhap.setText("")
        self.uic2.lbdonvi.setText("")
        self.uic2.txtgianhap.setText("")
        lentable=self.uic2.tableWidget.rowCount()
        if(lentable>0):
            i=0
            while (i<=lentable):
                self.uic2.tableWidget.removeRow(0)
                i=i+1
        self.setMaPhieuNhap()
        self.uic2.textEdit.setText("")
    def chiNhapSo(self):
        self.uic2.txtgianhap.setInputMask("99999999999")
        self.uic2.txtsoluongphieunhap.setInputMask("9999999999")
    def load_Form_Hoa_Don(self):
        self.third_window.show()
        self.showMaNhanVien()
        self.chiNhapSo()
        self.loadComboboxncc()
        self.hienNgay()
        self.setMaPhieuNhap()
        self.loadComboboxTenSanPhamHoaDon()
        self.main_win.close()
        self.setMaHoaDon()
        self.setMaKhachHang()
    # ------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------Hóa đơn--------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    def loadComboboxTenSanPhamHoaDon(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select tensanpham from sanpham where soluongcon >0"
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for item in results:
                self.uic2.cbbtensphoadon.addItem(item[0])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def hienThiThongTinSanPhamHoaDon(self):
        tensanpham =self.uic2.cbbtensphoadon.currentText()
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select * from sanpham where tensanpham ='" + tensanpham + "' "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            self.uic2.lbmasphoadon.setText(str(results[0][0]))
            self.uic2.lbdongiahoadon.setText(str(results[0][2]))
            self.uic2.lbdonvihoadon.setText(results[0][3])
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def setMaHoaDon(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select count(mahoadon),max(mahoadon) from hoadon "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            soluonghoadoon = result[0][0]
            taoma=''
            if(soluonghoadoon<=0):
                taoma="HD-00000001"
            elif(soluonghoadoon>0):
                tachma = result[0][1].split("-")
                firstbill= tachma[0]+"-"
                secondbill=''
                k=int(tachma[1])
                k=k+1
                if(k<10):
                    secondbill=secondbill+"0000000"
                elif(k<100):
                    secondbill=secondbill+"000000"
                elif(k<1000):
                    secondbill=secondbill+"00000"
                elif(k<10000):
                    secondbill=secondbill+"0000"
                elif(k<100000):
                    secondbill=secondbill+"000"
                elif(k<1000000):
                    secondbill=secondbill+"00"
                elif (k < 10000000):
                    secondbill=secondbill+"0"
                taoma=firstbill+secondbill+str(k)
            self.uic2.lbmahoadon.setText(taoma)
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def setMaKhachHang(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        sql = "select count(makhachhang),max(makhachhang) from khachhang "
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            soluonghoadoon = result[0][0]
            taoma = ''
            if (soluonghoadoon <= 0):
                taoma = "KH-00000001"
            elif (soluonghoadoon > 0):
                tachma = result[0][1].split("-")
                firstbill = tachma[0] + "-"
                secondbill = ''
                k = int(tachma[1])
                k = k + 1
                if (k < 10):
                    secondbill = secondbill + "0000000"
                elif (k < 100):
                    secondbill = secondbill + "000000"
                elif (k < 1000):
                    secondbill = secondbill + "00000"
                elif (k < 10000):
                    secondbill = secondbill + "0000"
                elif (k < 100000):
                    secondbill = secondbill + "000"
                elif (k < 1000000):
                    secondbill = secondbill + "00"
                elif (k < 10000000):
                    secondbill = secondbill + "0"
                taoma = firstbill + secondbill + str(k)
            self.uic2.lbmakhachhang.setText(taoma)
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
        finally:
            cursor.close()
            con.close()
    def themChiTietHoaDon(self):
        masanpham = self.uic2.lbmasphoadon.text()
        tensanpahm = self.uic2.cbbtensphoadon.currentText()
        soluong = self.uic2.txtsoluonghoadon.text()
        donvi = self.uic2.lbdonvihoadon.text()
        dongia = self.uic2.lbdongiahoadon.text()
        if (len(masanpham) == 0 or len(tensanpahm) == 0 or len(soluong) == 0 or len(donvi) == 0 or
                len(str(dongia)) == 0):
            self.ThongBaoOk("Mời bạn nhập đủ thông tin")
        else:
            tongtien=0
            thanhtien = float(self.uic2.lbdongiahoadon.text()) * int(soluong)
            row = (masanpham, tensanpahm, str(soluong), donvi,dongia, str(thanhtien))
            countrow = self.uic2.tableWidget_2.rowCount() + 1
            i = self.uic2.tableWidget_2.rowCount()
            self.uic2.tableWidget_2.setRowCount(countrow)
            self.uic2.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.uic2.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.uic2.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.uic2.tableWidget_2.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.uic2.tableWidget_2.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.uic2.tableWidget_2.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            tien=self.uic2.tableWidget_2.item(i,5).text()
            tien1=self.uic2.lbtongtien.text().replace(',',"")
            self.uic2.lbtongtien.setText("{:,.1f}".format(float(tien1)+float(tien)))
    def xoaChiTietHoaDon(self):
        lentable = self.uic2.tableWidget_2.rowCount()
        if (lentable > 0):
            for item in self.uic2.tableWidget_2.selectedItems():
                row = item.row()
                thanhtien = self.uic2.tableWidget_2.item(row, 5).text()
                tongtien=self.uic2.lbtongtien.text().replace(',',"")
                tiensaukhixoa= float(tongtien)-float(thanhtien)
                self.uic2.lbtongtien.setText("{:,.1f}".format(tiensaukhixoa))
            self.uic2.tableWidget_2.removeRow(row)
        else:
            self.ThongBaoOk("Mời bạn nhập đủ thông tin")
    def updateSoLuong(self):
        con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
        cursor = con.cursor()
        results=[]
        for i in range(0,self.uic2.tableWidget_2.rowCount()):
            masanpham = self.uic2.tableWidget_2.item(i, 0).text()
            soluongnhap = self.uic2.tableWidget_2.item(i, 2).text()
            item = (masanpham,soluongnhap)
            results.append(item)
        for j in results:
            masanpham=j[0]
            soluongban=int(j[1])
            sqllaysoluongcon = "select soluongcon from sanpham where masanpham= "+masanpham+""

            try:
                cursor.execute(sqllaysoluongcon)
                result =cursor.fetchall()
                soluongcon= result[0][0]-soluongban
                sqlupdate = f"""update  sanpham set soluongcon={soluongcon} where masanpham = {masanpham}"""
                cursor.execute(sqlupdate)
                con.commit()
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
        cursor.close()
        con.close()
    def InHoaDon(self):
        lentable = self.uic2.tableWidget_2.rowCount()
        self.checkKhachHang()
        if (lentable > 0):
            result =[]
            mahoadon=self.uic2.lbmahoadon.text()
            manhanvien= self.uic2.lbmanhanvien.text()
            thoigian=self.uic2.lbngay.text()
            tongtien=float(self.uic2.lbtongtien.text().replace(',',""))
            tienkhachdua=float(self.uic2.txttienkhachdua.text())
            makhachhang = self.uic2.lbmakhachhang.text()
            check= tienkhachdua-tongtien
            if(check<0):
                self.ThongBaoOk("Khách đưa thiếu tiền!")
            else:
                for i in range(0,self.uic2.tableWidget_2.rowCount()):
                    masanpham = self.uic2.tableWidget_2.item(i, 0).text()
                    soluong = int(self.uic2.tableWidget_2.item(i, 2).text())
                    thanhtien = float(self.uic2.tableWidget_2.item(i, 5).text())
                    item = (mahoadon,masanpham, soluong, thanhtien)
                    result.append(item)
                con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
                sql = f"""insert into hoadon (mahoadon, thoigian,tongtien, tienkhachdua, tientralai,makhachhang,manhanvien)
                     values ('{mahoadon}', TO_DATE('{thoigian}','yyyy-mm-dd'), {tongtien},{tienkhachdua}
                     ,{check},'{makhachhang}','{manhanvien}')"""
                cursor = con.cursor()
                try:
                    cursor.execute(sql)
                    con.commit()
                    for i in range(0,len(result)):
                        mahoadon=result[i][0]
                        masanphamis=result[i][1]
                        soluongis = result[i][2]
                        thanhtienis = result[i][3]
                        sql1 = f"""insert into chitiethoadon (mahoadon, masanpham, soluong, thanhtien)
                                     values ('{mahoadon}', '{masanphamis}', {soluongis},{thanhtienis})"""
                        cursor.execute(sql1)
                        con.commit()
                except cx_Oracle.DatabaseError as e:
                    print("There is a problem with Oracle", e)
                finally:
                    cursor.close()
                    con.close()
                self.updateSoLuong()
                self.layDuLieuInHoaDon()
                self.printPdfHoaDon()
        else:
            self.ThongBaoOk("Mời bạn điền đầy đủ thông tin")
    def checkKhachHang(self):
        tenkhachhang=self.uic2.txttenkhachhang.text()
        sodienthoai=self.uic2.txtsodienthoai.text()
        diachi = self.uic2.txtdiachi.toPlainText()
        if(len(tenkhachhang)==0 or len(sodienthoai)==0):
            self.ThongBaoOk("Mời bạn nhập Tên khách hàng ,Số điện thoại")
        else:
            con = cx_Oracle.connect('system/tanvip01@@localhost/XEPDB1')
            sql = "select * from khachhang where tenkhachhang = '"+tenkhachhang+"' and " \
                                                                                "sodienthoai ='"+sodienthoai+"' "
            cursor = con.cursor()
            try:
                cursor.execute(sql)
                result=cursor.fetchall()
                if(len(result)>0):
                    self.uic2.lbcheckkh.setText("KH Cũ")
                    self.uic2.lbmakhachhang.setText(result[0][0])
                else:
                    self.uic2.lbcheckkh.setText("KH Mới")
            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)
            if(self.uic2.lbcheckkh.text()=="KH Mới"):
                sodienthoai = int(sodienthoai)
                makhachhang = self.uic2.lbmakhachhang.text()
                sqladdkhachhang =f"""insert into KHACHHANG (makhachhang,tenkhachhang,sodienthoai,diachi)
                                     values ('{makhachhang}','{tenkhachhang}', {sodienthoai}, '{diachi}')"""
                cursor.execute(sqladdkhachhang)
                con.commit()
            cursor.close()
            con.close()
    def printPdfHoaDon(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.uic2.textEdit_2.print(printer)
    def layDuLieuInHoaDon(self):
        tongtien=0
        self.uic2.textEdit_2.append("***********************Hóa đơn***********************")
        self.uic2.textEdit_2.append("\n")
        self.uic2.textEdit_2.append("\t"+"\t"+"\t"+"\t"+"  Ngày: "+""+self.uic2.lbngay.text()+"")
        self.uic2.textEdit_2.append("\n")
        self.uic2.textEdit_2.append("Nhân viên thực hiên:"+"\t"+"\t"+""+self.uic2.lbtennhanvien.text()+"")
        self.uic2.textEdit_2.append("\n")
        self.uic2.textEdit_2.append("Tên khách hàng:"+"\t"+"\t"+" "+self.uic2.txttenkhachhang.text()+"")
        self.uic2.textEdit_2.append("\n")
        self.uic2.textEdit_2.append("------------------------------------------------------------------------")
        self.uic2.textEdit_2.append("Tên sản phẩm"+"     "+"Số lượng"+"    "+"    "+"Đơn giá"+"          "
                                    +"    "+"Thành tiên")
        self.uic2.textEdit_2.append("------------------------------------------------------------------------")

        results = []
        for i in range(0, self.uic2.tableWidget_2.rowCount()):
            tensanpham = self.uic2.tableWidget_2.item(i, 1).text()
            soluong = self.uic2.tableWidget_2.item(i, 2).text()
            dongia = self.uic2.tableWidget_2.item(i, 4).text()
            thanhtien = self.uic2.tableWidget_2.item(i,5).text()
            item = (tensanpham,soluong,dongia,thanhtien )
            tongtien=tongtien+float(thanhtien)
            results.append(item)
        for item in results:
            tensanpham = item[0]
            soluong =item[1]
            dongia = "{:,.1f}".format(float(item[2]))
            thanhtien = "{:,.1f}".format(float(item[3]))
            self.uic2.textEdit_2.append(""+tensanpham+""+"\n"+"\t"+"         "+""+soluong+""+"\t"+"          "+""+dongia+""+"\t"+"   "+""+thanhtien+"")
            # self.uic2.textEdit_2.append("\n")
            self.uic2.textEdit_2.append("------------------------------------------------------------------------")
        self.uic2.textEdit_2.append("Tổng tiền :"+"\t"+"\t"+"\t"+""+"{:,.1f}".format(tongtien)+" vnđ")
        self.uic2.textEdit_2.append("Mã hóa đơn:"+"\t"+"\t"+"\t"+""+self.uic2.lbmahoadon.text()+"")
        self.uic2.textEdit_2.append("\n")
        self.uic2.textEdit_2.append("***********Cản ơn quý khách đã mua hàng***************")
    def lamMoiHoaDon(self):
        self.uic2.lbcheckkh.setText("")
        self.setMaHoaDon()
        self.setMaKhachHang()
        self.uic2.lbmasphoadon.setText("")
        self.uic2.txtsoluonghoadon.setText("")
        self.uic2.lbdonvihoadon.setText("")
        self.uic2.lbdongiahoadon.setText("")
        self.uic2.lbtongtien.setText("0")
        self.uic2.txttienkhachdua.setText("")
        self.uic2.txttenkhachhang.setText("")
        self.uic2.txtsodienthoai.setText("")
        self.uic2.txtdiachi.setText("")
        lentable=self.uic2.tableWidget_2.rowCount()
        if(lentable>0):
            i=0
            while (i<=lentable):
                self.uic2.tableWidget_2.removeRow(0)
                i=i+1
        self.uic2.textEdit_2.setText("")
    def thoat(self):
        self.third_window.close()
        self.main_win.show()
        self.checkSanPhamConHang()


