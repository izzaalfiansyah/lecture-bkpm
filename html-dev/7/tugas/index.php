<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Registrasi</title>
    <style>
        @layer utilities {

            html, body {
                scroll-behavior: smooth;
            }
    
            * {
                font-family: Arial, Helvetica, sans-serif;
            }
    
            .loader {
                animation: fade 2s both;
                pointer-events: none;
            }
            
            @keyframes fade {
                0% {
                    opacity: 100%;
                }
                
                100% {
                    opacity: 0;
                }
            }
            
            .animate-up {
                animation: up .5s;
            }
    
            @keyframes up {
                0% {
                    transform: translateY(100%);
                }
                
                100% {
                    transform: translateY(0);
                }
            }
        }
    </style>
    <link rel="stylesheet" href="tailwind.css">
</head>
<body class="min-h-screen bg-gradient-to-b from-purple-400 to-pink-400 p-4 py-10">
    <div class="flex flex-wrap flex-col items-center justify-center">
        <div class="bg-white p-4 rounded shadow font-semibold text-center w-full lg:w-1/2">
            FORMULIR PENDAFTARAN
        </div>
        <form action="store.php" method="POST" class="bg-white rounded p-4 shadow mt-3 w-full lg:w-1/2 relative animate-up">
            <?php 
                session_start();
                
                if (isset($_SESSION['insert'])) {
                    
                    if ($_SESSION['insert'] == '1') {
                        echo '<div class="mb-2 p-3 border-2 border-green-400 bg-green-100 text-green-400 rounded">Data berhasil disimpan</div>';
                    } else {
                        echo '<div class="mb-2 p-3 border-2 border-red-400 bg-red-100 text-red-400 rounded">Data gagal disimpan</div>';
                    }

                    unset($_SESSION['insert']);
                }
            ?>

            <div class="w-full">
                <div class="mb-3">
                    <label class="mb-2" for="">NIK</label>
                    <span class="text-red-500">*</span>
                    <input type="text" placeholder="350904XXXXXXXXXX" only-number required minlength="16" maxlength="16" class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="nik">
                </div>
                
                <div class="mb-3">
                    <label class="mb-2" for="">Nama</label>
                    <span class="text-red-500">*</span>
                    <input type="text" placeholder="Masukkan Nama" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="nama">
                </div>
                
                <div class="mb-3">
                    <label class="mb-2" for="">Jenis Kelamin</label>
                    <span class="text-red-500">*</span>
                    <div class="p-2 bg-purple-100 rounded">
                        <input type="radio" name="jenis_kelamin" value="1"> Laki-laki <br>
                        <input type="radio" name="jenis_kelamin" value="2"> Perempuan
                    </div>
                </div>
                
                <div class="flex flex-wrap mb-3">
                    <div class="lg:w-1/2 w-full lg:pr-1">
                        <label class="mb-2" for="">Tanggal Lahir</label>
                        <span class="text-red-500">*</span>
                        <input type="date" placeholder="Masukkan Tanggal Lahir" max="" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="tanggal_lahir">
                    </div>
                    <div class="lg:w-1/2 w-full lg:pl-1">
                        <label class="mb-2" for="">Agama</label>
                        <span class="text-red-500">*</span>
                        <select required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="agama">
                            <option value="">Pilih Agama</option>
                            <option value="Islam">Islam</option>
                            <option value="Protestan">Protestan</option>
                            <option value="Katolik">Katolik</option>
                            <option value="Hindu">Hindu</option>
                            <option value="Budha">Budha</option>
                        </select>
                    </div>
                </div>
                
                <div class="mb-3">
                    <label class="mb-2" for="">Tinggi Badan</label>
                    <span class="text-red-500">*</span>
                    <input type="number" placeholder="Masukkan Tinggi Badan" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="tinggi_badan">
                </div>
                
                <div class="mb-3">
                    <label class="mb-2" for="">Hobi</label>
                    <div class="p-2 bg-purple-100 rounded">
                        <input type="checkbox" value="Membaca" name="hobi[]"> Membaca <br>
                        <input type="checkbox" value="Mendaki" name="hobi[]"> Mendaki <br>
                        <input type="checkbox" value="Olahraga" name="hobi[]"> Olahraga
                    </div>
                </div>
                
                <div class="flex flex-wrap mb-3">
                    <div class="lg:w-1/2 w-full lg:pr-1">
                        <label class="mb-2" for="">Telepon</label>
                        <span class="text-red-500">*</span>
                        <input type="tel" only-number placeholder="08XXXXXXXXXX" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="telepon">
                    </div>
                    <div class="lg:w-1/2 w-full lg:pl-1">
                        <label class="mb-2" for="">Email</label>
                        <span class="text-red-500">*</span>
                        <input type="email" placeholder="example@outlook.com" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="email">
                    </div>
                </div>
                
                <div class="mb-3">
                    <label class="mb-2" for="">Alamat</label>
                    <textarea cols="30" rows="4" placeholder="Jalan Mangga Besar III No. 17, RT 06 RW 07, Kelurahan Bedali, Kecamatan Lawang, Kab. Malang, Jawa Timur, 60256" class="w-full rounded p-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="alamat"></textarea>
                </div>
                
                <div class="flex flex-wrap mb-3">
                    <div class="lg:w-1/2 w-full lg:pr-1">
                        <label class="mb-2" for="">Username</label>
                        <span class="text-red-500">*</span>
                        <input type="text" minlength="5" maxlength="20" placeholder="Masukkan Username" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="username">
                    </div>
                    <div class="lg:w-1/2 w-full lg:pl-1">
                        <label class="mb-2" for="">Password</label>
                        <span class="text-red-500">*</span>
                        <input type="password" placeholder="********" required class="w-full rounded h-12 px-2 bg-purple-100 border-2 border-transparent focus:border-purple-500 outline-none transition" name="password">
                        <input type="checkbox" id="show-password" class="mt-2 -translate-y-10 mr-2" style="float: right;">
                    </div>
                </div>
        
                <div class="mt-4">
                    <button type="submit" class="bg-gradient-to-r border border-purple-500 from-purple-500 to-pink-400 hover:bg-opacity-75 mr-2 transition p-2 rounded shadow text-white px-4">SUBMIT</button>
                    <button type="reset" class="border p-2 border-purple-500 hover:bg-purple-100 transition px-4 shadow text-purple-500 rounded">RESET</button>
                </div>
            </div>
        </form>
    </div>
    <div class="bg-gray-800 from-purple-500 z-20 fixed top-0 left-0 right-0 bottom-0 h-full rounded flex items-center justify-center flex-col loader">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Polije.png" class="animate-bounce block" alt="" style="width: 200px; height: 200px;">
    </div>

    <button type="button" onclick="window.scrollTo(0, 0)" class="fixed lg:bottom-10 lg:right-10 bottom-5 right-5 shadow-lg shadow-gray-500 bg-white rounded-full h-14 w-14 z-10 flex justify-center items-center transition hover:bg-gray-100 outline-none">
        &UpArrow;
    </button>

    <script>
        // menghandle inputan untuk nomor
        function onlyNumber(e) {
            if (e.keyCode < 48 || e.keyCode > 57) {
                if (e.keyCode !== 13) {
                    return false;
                }
            }
        }

        // fungsi mengambil tanggal untuk 17 tahun yang lalu
        function cekTanggalLahir() {
            var date = new Date();
            var year = date.getFullYear();
            var month = date.getMonth();
            var day = date.getDate();

            var newDate = new Date(year - 17, month, day);
            
            document.querySelector('[name=tanggal_lahir]').max = newDate.toISOString().substr(0, 10);
        }

        cekTanggalLahir();

        document.querySelectorAll('[only-number]').forEach((el) => {
            el.onkeypress = onlyNumber;
        });

        document.getElementById('show-password').onclick = (e) => {
            if (e.target.checked) {
                document.querySelector('[type=password]').type = 'text-password';
            } else {
                document.querySelector('[type=text-password]').type = 'password';
            }
        }
    </script>
</body>
</html>