print("PROGRAM PERKIRAAN WAKTU NABUNG MASA DEPAN")
print()

try:
	hasil = 0
	i = 1
	jumlah_bulan = 0
	kondisi_looping = True
	
	tabungan_tiap_bulan = int(input("Masukan jumlah tabungan tiap bulan "))
	target_uang_tercapai = int(input("Masukan jumlah uang yang di inginkan "))
	while(kondisi_looping):
		hasil = tabungan_tiap_bulan * i
		if target_uang_tercapai == hasil or hasil >= target_uang_tercapai:
			jumlah_bulan = i
			break
		i += 1
	print("Estimasi ", jumlah_bulan, " bulan")
except ValueError:
	print("Yang anda inputkan bukan angka!")