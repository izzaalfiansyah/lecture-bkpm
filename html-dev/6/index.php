<?php

$hostname = 'localhost';
$username = 'root';
$password = '';
$database = 'mydb';

// membuat koneksi database
$conn = new mysqli($hostname, $username, $password, $database);

// membuat tabel jurusan dengan primary key auto increment (kode digenerate otomatis berdasarkan urutan masuknya data)
$sql = "CREATE TABLE jurusan (
    kode INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(30) NOT NULL
)";

// membuat tabel prodi dengan foreign key pada kode jurusan
$sql = "CREATE TABLE prodi (
    kode VARCHAR(5) NOT NULL PRIMARY KEY,
    jurusan_kode INT(5) NOT NULL,
    nama VARCHAR(30) NOT NULL,
    FOREIGN KEY (kode) REFERENCES jurusan(kode)
)";

// menambahkan jurusan
$sql = "INSERT INTO jurusan (nama) VALUES ('Teknologi Informasi')";

// menambahkan prodi
$sql = "INSERT INTO prodi (kode, nama, jurusan_kode) VALUES ('TKK', 'Teknik Komputer', '1')";