<?php

// inisialisasi koneksi database
$host = "localhost";
$user = "root";
$pass = "";
$db = "main_data";

$conn = new mysqli($host, $user, $pass, $db);

// menangkap semua request
$nik = $_REQUEST['nik'];
$nama = $_REQUEST['nama'];
$jenis_kelamin = $_REQUEST['jenis_kelamin'];
$tanggal_lahir = $_REQUEST['tanggal_lahir'];
$agama = $_REQUEST['agama'];
$tinggi_badan = $_REQUEST['tinggi_badan'];
// menserialize hobi dikarenakan data banyak
$hobi = @json_encode($_REQUEST['hobi']);
$telepon = $_REQUEST['telepon'];
$email = $_REQUEST['email'];
$alamat = $_REQUEST['alamat'];
$username = $_REQUEST['username'];
// hash password untuk keamanan
$password = md5($_REQUEST['password']);

// insert data ke tabel user
$sql = "INSERT INTO user (nik, nama, jenis_kelamin, tanggal_lahir, agama, tinggi_badan, hobi, telepon, email, alamat, username, password) VALUES ('$nik', '$nama', '$jenis_kelamin', '$tanggal_lahir', '$agama', '$tinggi_badan', '$hobi', '$telepon', '$email', '$alamat', '$username', '$password')";

// buat pesan dengan session
session_start();

// jika query berhasil
if ($conn->query($sql) === TRUE) {
    $_SESSION['insert'] = '1';
} else {
    $_SESSION['insert'] = '0';
}

// mengembalikan ke halaman index
header('Location: index.php');

?>