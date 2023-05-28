from http.server import HTTPServer, BaseHTTPRequestHandler #Mengimport dari modul http.server yaitu HTTPServer dan BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler): #Memegang server kita, dan memakai fungsi dari BaseHTTPRequestHandler

    def do_GET(self): #do_GET adalah bawaan dari Pythonnya sendiri, do_GET adalah permintaan dipetakan ke file lokal dengan menginterpretasikan permintaan sebagai jalur relatif ke direktori kerja saat ini
        if self.path == '/': #Jika kita hanya menuliskan slash(/) di link, maka yang akan keluar adalah HTML index1
            self.path = '/index1.html'
        try:
            file_to_open = open(self.path[1:]).read()#Membuka file html yang ada
            self.send_response(200)#Jika ada, maka akan direspon dengan 200 yang berarti halaman telah berhasil diakses
        except:
            file_to_open = "404 File Not Found" #Jika file tidak ada, maka akan muncul tulisan 404 File Not Found
            self.send_response(404) #Respon statusnya adalah 404 yang berarti file tidak bisa diakses
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8')) #Untuk menulis ke layar kita harus mengkonversikannya ke bytes
        #dan kita mengasumsikan bahwa semua file yang ditulis adalah utf-8 (dan aslinya disimpan dalam utf-8)

httpd = HTTPServer(('localhost', 8080), Serv) #HTTP Server menyimpan alamat server sebagai variabel instan yang sudah disediakan oleh Python 
#localhost adalah host dari server yang kita gunakan dan 8080 adalah nomor port yang kita gunakan.
httpd.serve_forever() #Menutup request