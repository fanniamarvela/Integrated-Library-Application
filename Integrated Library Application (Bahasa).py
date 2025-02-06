listPerpustakaan =[
    {   'ID':'1A',
        'Nama': 'George',
        'Buku': 'A Study in Scarlet',
        'Kategori': 'Mystery',
        'Periode Peminjaman':3
    },
    {   'ID':'2A',
        'Nama': 'Brian',
        'Buku': 'Harry  Potter',
        'Kategori': 'Fantasy',
        'Periode Peminjaman': 10
    },
    {   'ID':'1B',
        'Nama': 'Stephanie',
        'Buku': 'The Little Prince',
        'Kategori': 'Fantasy',
        'Periode Peminjaman': 7
    },
    {   'ID':'3A',
        'Nama': 'Jackson',
        'Buku': 'Atomic Habits',
        'Kategori': 'Psychology',
        'Periode Peminjaman': 5
    },
    {   'ID':'2B',
        'Nama': 'Nicole',
        'Buku': 'Me Before You',
        'Kategori': 'Romance',
        'Periode Peminjaman': 8
    }
]

def Perpustakaan():
    while True :
        pilihanMenu = input('''
        =================================================================================================
                                        SELAMAT DATANG DI PERPUSTAKAAN
        =================================================================================================

            LIST MENU 
            1. Menampilkan Data Perpustakaan
            2. Menambahkan Data Perpustakaan
            3. Mengupdate Data Perpustakaan
            4. Menghapus Data Perpustakaan
            5. Exit Program

            Masukkan Angka Menu yang Ingin Dijalankan : ''')

        if(pilihanMenu == '1') :
            menampilkanlistPerpustakaan()
        elif(pilihanMenu == '2') :
            menambahlistPerpustakaan()
        elif(pilihanMenu == '3') :
            mengupdatelistPerpustakaan()
        elif(pilihanMenu == '4') :
            menghapuslistPerpustakaan()
        elif(pilihanMenu == '5') :
            print('''
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
                                Terima Kasih Sudah Menggunakan Aplikasi Perpustakaan! 
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            ''')
            break
        else:
            print("Maaf, Pilihan Menu yang Anda Masukkan Tidak Ada")

def daftarlistPerpustakaan():
    if len(listPerpustakaan)==0:
        print("Maaf, Tidak Ada Data")
    else: 
        print('''
        ++++++++++++++++++++++++++++++++ DATA PERPUSTAKAAN +++++++++++++++++++++++++++++++++
        ''')
        print("ID \t| NAMA \t \t| BUKU \t \t \t| KATEGORI \t| PERIODE PEMINJAMAN")
        for i in range(len(listPerpustakaan)) :
            print(f"{listPerpustakaan[i]['ID']} \t| {listPerpustakaan[i]['Nama']} \t| {listPerpustakaan[i]['Buku']} \t| {listPerpustakaan[i]['Kategori']} \t| {listPerpustakaan[i]['Periode Peminjaman']}")

def menampilkanlistPerpustakaan():
    while True:
        print('''
        ==================================================================================== 
                                        DAFTAR DATA PERPUSTAKAAN 
        ====================================================================================  

            1. Menampilkan Seluruh Data Perpustakaan
            2. Menampilkan Data Perpustakaan Tertentu
            3. Kembali ke Menu Utama
        ''')
        submenu = int(input("Silahkan Pilih Sub Menu Tampilan Data Perpustakaan : "))
        if submenu==1:
            if len(listPerpustakaan)==0:
                print("Maaf, Tidak Ada Data")
            else:
                daftarlistPerpustakaan()
        elif submenu==2:
            if len(listPerpustakaan)==0:
                print("Maaf, Tidak Ada Data")
            else:
                inputid = input("Masukkan ID Data Yang Ingin Ditampilkan : ")
                hasil=[]
                for i in range(len(listPerpustakaan)):
                    hasil.append(listPerpustakaan[i]['ID'])
                if inputid in hasil:
                    indexsama=hasil.index(inputid)
                    print("ID \t| NAMA \t \t| BUKU\t \t \t| KATEGORI \t| PERIODE PEMINJAMAN")
                    print(f"{listPerpustakaan[indexsama]['ID']} \t| {listPerpustakaan[indexsama]['Nama']} \t| {listPerpustakaan[indexsama]['Buku']} \t| {listPerpustakaan[indexsama]['Kategori']} \t| {listPerpustakaan[indexsama]['Periode Peminjaman']}")
                    hasil=[]
                else:
                    print("Maaf Tidak Ada Data yang Sesuai dengan ID yang Dimasukkan")
        elif submenu==3:
            break
        else:
            print("Maaf Pilihan Sub Menu yang Anda Masukkan Tidak Ada")

def menambahlistPerpustakaan():
    while True: 
        print('''
        ============================================================================================ 
                                        MENAMBAHKAN DATA PERPUSTAKAAN
        ============================================================================================ 

            1. Menambahkan Data Perpustakaan
            2. Kembali Ke Menu Utama
        ''')
        submenu = int(input('Silahkan Pilih Sub Menu Menambahkan Data Perpustakaan : '))
        if submenu==1:
            idbaru = input("Masukkan ID yang Ingin Ditambah : ")
            hasil=[]
            for i in range(len(listPerpustakaan)):
                hasil.append(listPerpustakaan[i]['ID'])
            if idbaru in hasil:
                print("Maaf Data Sudah Ada")
                hasil=[]
            else:
                namabaru = input("Masukkan Nama : ")
                bukubaru = input("Masukkan Buku yang Dipinjam : ")
                kategoribaru = input("Masukkan Kategori Buku yang Dipinjam : ")
                while True:
                    periodebaru = int(input("Masukkan Periode Peminjaman Buku (maksimal 14 hari) : "))
                    if periodebaru>=14:
                        print("Maaf periode peminjaman buku maksimal 14 hari")
                    else:
                        save=input("Apakah Anda Ingin Menyimpan Data? (yes/no)")
                        if save.lower()=='yes':
                            listPerpustakaan.append({
                                'ID' : idbaru,
                                'Nama': namabaru,
                                'Buku': bukubaru,
                                'Kategori': kategoribaru,
                                'Periode Peminjaman': periodebaru
                                })
                            print("Data Telah Tersimpan")
                            daftarlistPerpustakaan()
                            break
                        elif save.lower()=='no':
                            break        
        elif submenu==2:
            break
        else:
            print("Maaf Pilihan Sub Menu yang Anda Masukkan Tidak Ada")

def mengupdatelistPerpustakaan():
    while True: 
        print('''
        =================================================================================================
                                            MENGUPDATE DATA PERPUSTAKAAN 
        =================================================================================================

            1. Mengupdate Data Perpustakaan
            2. Kembali Ke Menu Utama
        ''')
        submenu = int(input("Silahkan Pilih Sub Menu Mengupdate Data Perpustakaan : "))
        if submenu==1:
            inputid = input("Masukkan ID Data yang Ingin Diupdate : ")
            hasil=[]
            for i in range(len(listPerpustakaan)):
                hasil.append(listPerpustakaan[i]['ID'])
            if inputid in hasil:
                indexupdate=hasil.index(inputid)
                print("ID \t| NAMA \t \t| BUKU \t \t \t| KATEGORI \t| PERIODE PEMINJAMAN")
                print(f"{listPerpustakaan[indexupdate]['ID']} \t| {listPerpustakaan[indexupdate]['Nama']} \t| {listPerpustakaan[indexupdate]['Buku']} \t| {listPerpustakaan[indexupdate]['Kategori']} \t| {listPerpustakaan[indexupdate]['Periode Peminjaman']}")
                hasil=[]
                lanjut=input("Apakah Anda Ingin Mengupdate Data Tersebut? (yes/no)")
                if lanjut.lower()=='yes':
                    while True:
                        kolom=input("Masukkan Nama Kolom yang Akan Anda Update (End untuk kembali) : ")
                        if kolom.lower()=='nama':
                            namabaru=input("Masukkan Nama Baru : ")
                            lain=input("Apakah Anda Yakin Ingin Mengubah Kolom Data? (yes/no)")
                            if lain.lower()=='no':
                                continue
                            elif lain.lower()=='yes':
                                listPerpustakaan[indexupdate]['Nama']=namabaru
                                daftarlistPerpustakaan()
                                print("Data Telah Terupdate")
                                mengupdatelistPerpustakaan()
                                break
                        elif kolom.lower()=='buku':
                            bukubaru=input("Masukkan Judul Buku Baru : ")
                            lain=input("Apakah Anda Yakin Ingin Mengubah Kolom Data? (yes/no)")
                            if lain.lower()=='no':
                                continue
                            elif lain.lower()=='yes':
                                listPerpustakaan[indexupdate]['Buku']=bukubaru
                                daftarlistPerpustakaan()
                                print("Data Telah Terupdate")
                                mengupdatelistPerpustakaan()
                                break
                        elif kolom.lower()=='kategori':
                            kategoribaru=input("Masukkan Kategori Baru : ")
                            lain=input("Apakah Anda Yakin Ingin Mengubah Kolom Data? (yes/no)")
                            if lain.lower()=='no':
                                continue
                            elif lain.lower()=='yes':
                                listPerpustakaan[indexupdate]['Kategori']=kategoribaru
                                daftarlistPerpustakaan()
                                print("Data Telah Terupdate")
                                mengupdatelistPerpustakaan()
                                break
                        elif kolom.lower()=='periode' or kolom.lower()=='periode peminjaman':
                            while True:  
                                periodebaru=int(input("Masukkan Periode Peminjaman Baru (maksimal 14 hari): "))
                                if periodebaru>=14:
                                    print("Maaf periode peminjaman buku maksimal 14 hari")
                                    continue
                                else:
                                    listPerpustakaan[indexupdate]['Periode Peminjaman']=periodebaru
                                    lain=input("Apakah Anda Yakin Ingin Mengubah Kolom Data? (yes/no)")
                                    if lain.lower()=='no':
                                        continue
                                    elif lain.lower()=='yes':
                                        listPerpustakaan[indexupdate]['Periode Peminjaman']=periodebaru
                                        daftarlistPerpustakaan()
                                        print("Data Telah Terupdate")
                                        mengupdatelistPerpustakaan()
                                        break
                        elif kolom.lower() == 'end':
                            mengupdatelistPerpustakaan()
                            break
                        break 
                elif lanjut.lower()=='no':
                    continue
            else:
                print("Maaf, Data Yang Ada Cari Tidak Ada")
                hasil=[]
                continue
            break
        elif submenu==2:
            break
        else:
            print("Maaf Pilihan Sub Menu yang Anda Masukkan Tidak Ada")

def menghapuslistPerpustakaan():    
    while True:
        print('''
        ================================================================================================= 
                                            Menghapus Data Perpustakaan 
        ================================================================================================= 

            1. Menghapus Data Perpustakaan Tertentu
            2. Menghapus Semua Data Perpustakaan
            3. Kembali Ke Menu Utama
        ''')
        submenu = int(input("Silahkan Pilih Sub Menu Menghapus Data Perpustakaan : "))
        if submenu==1:  
            daftarlistPerpustakaan()
            hasil=[]
            for i in range(len(listPerpustakaan)):
                hasil.append(listPerpustakaan[i]['ID'])
            idhapus = input("Masukkan ID Peminjam Buku yang Ingin Dihapus : ")
            if idhapus in hasil: 
                indexhapus=hasil.index(idhapus)
                yesno=input(f"Apakah Anda Yakin Akan Menghapus Data Dengan ID {idhapus}? (yes/no)")
                if yesno.lower()=='yes':
                    del listPerpustakaan[indexhapus]
                    daftarlistPerpustakaan()
                    print("Data Telah Dihapus")
                elif yesno.lower()=='no':
                    continue
            else:
                print("Maaf, Data Yang Anda Cari Tidak Ada")
                hasil=[]
        elif submenu==2:
            yesno=input("Apakah Anda Yakin Akan Menghapus Semua Data Perpustakaan? (yes/no)")
            if yesno.lower()=='yes':
                listPerpustakaan.clear()
                print("Semua Data Telah Dihapus")
                daftarlistPerpustakaan()
            elif yesno.lower()=='no':
                continue
        elif submenu==3:
            break
        else:
            print("Maaf Pilihan Sub Menu yang Anda Masukkan Tidak Ada")
     
Perpustakaan()
