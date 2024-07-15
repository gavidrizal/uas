-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 15, 2024 at 07:21 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `utang_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `hutang3`
--

CREATE TABLE `hutang3` (
  `id` int(20) NOT NULL,
  `kode` varchar(50) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `harga` double NOT NULL,
  `barang` varchar(100) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `hutang3`
--

INSERT INTO `hutang3` (`id`, `kode`, `nama`, `harga`, `barang`, `tanggal`) VALUES
(1, 'B-04', 'tuti', 9000, 'jan', '2024-07-01'),
(5, 'B-07', 'tuti', 23000, 'jajan', '2024-07-30'),
(5, 'B-08', 'turu', 9000, 'jajan', '2024-07-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hutang3`
--
ALTER TABLE `hutang3`
  ADD PRIMARY KEY (`kode`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
