# PROGRAM hitung-nilai.py
import os

# main method
if __name__ == "__main__":

    os.system("cls")

    # Input program
    print("------------------------------------")
    print("Input program")
    print("------------------------------------")
    mata_kuliah = input("Masukan mata kuliah : ")
    nilai_akhir = input("Masukan nilai akhir : ")
    print("------------------------------------")

    # proses program
    if int(nilai_akhir) >= 80:
      nilai_huruf = "A"       # output nilai huruf
    elif int(nilai_akhir) >= 70:
      nilai_huruf = "B"       # output nilai huruf
    elif int(nilai_akhir) >= 60:
      nilai_huruf = "C"       # output nilai huruf
    elif int(nilai_akhir) >= 50:
      nilai_huruf = "D"       # output nilai huruf
    else:
      nilai_huruf = "E"       # output nilai huruf

    # Output Program
    print("------------------------------------")
    print("Output Program")
    print("------------------------------------")
    print("Mata Kuliah : "+str(mata_kuliah))
    print("Nilai Akhir : "+str(nilai_akhir))
    print("Nilai Huruf : "+str(nilai_huruf))
    print("------------------------------------")