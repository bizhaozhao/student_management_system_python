-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2023 at 11:00 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `manage`
--

CREATE TABLE `manage` (
  `user_name` varchar(20) NOT NULL,
  `user_pwd` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `manage`
--

INSERT INTO `manage` (`user_name`, `user_pwd`) VALUES
('admin', '123456'),
('senioradmin', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `faculty` varchar(20) NOT NULL,
  `SWEN501` varchar(8) NOT NULL,
  `SWEN502` varchar(8) NOT NULL,
  `SWEN504` varchar(8) NOT NULL,
  `SWEN589` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `gender`, `mobile`, `email`, `faculty`, `SWEN501`, `SWEN502`, `SWEN504`, `SWEN589`) VALUES
(1001, 'Sarah', 'F', '55555', '55s@gmail.com', 'eng', 'B', 'D', 'C', 'A+'),
(1002, 'Tommy', 'M', '440232423', 'tommy@hotmail.com', 'Engineering', 'A+', 'B+', 'C', 'PASS'),
(1035, 'Luna', 'F', '23578900', 'luna@qq.com', 'cs', 'B', 'B+', 'A+', 'C+'),
(1036, 'Hunter', 'M', '25645300', 'hhh@qq.com', 'cs', 'B', 'B+', 'E', 'C+'),
(1037, 'Kunning', 'M', '25645300', 'kkk@qq.com', 'cs', 'B', 'B+', '', 'C+'),
(1050, 'Wendy', 'M', '111111', 'wd@qq.com', 'cs', 'A', 'A', 'A', ''),
(1061, 'cindy', 'm', '1111333', 'cc', 'cs', 'A', 'A', 'B', 'A'),
(1065, 'yooy', 'f', '1111', '77', 'cc', 'a', 'a', 'b', 'a');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `manage`
--
ALTER TABLE `manage`
  ADD PRIMARY KEY (`user_name`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1069;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
