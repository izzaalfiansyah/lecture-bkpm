<?php

$host = 'localhost';
$user = 'root';
$password = '';
$database = 'main_data';

$conn = mysqli_connect($host, $user, $password, $database) or die('Koneksi error');

$nama = $_REQUEST['nama'];
$alamat = $_REQUEST['alamat'];
$telepon = $_REQUEST['telepon'];

$sql = "INSERT INTO mahasiswa (nama, alamat, telepon) VALUES ('$nama', '$alamat', '$telepon')";

$result = mysqli_query($conn, $sql);

if ($result) {
    echo "Input berhasil";
} else {
    echo "Input gagal";
}

mysqli_close($conn);

?>  