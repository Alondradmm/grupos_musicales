-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Oct 01, 2025 at 05:22 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gruposmusicales`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumno`
--

CREATE TABLE `alumno` (
  `id_alumno` int(11) NOT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Apellido` varchar(50) DEFAULT NULL,
  `Correo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grupo`
--

CREATE TABLE `grupo` (
  `id_grupo` int(11) NOT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Horario` varchar(150) DEFAULT NULL,
  `CupoMinimo` int(11) DEFAULT NULL,
  `CupoMaximo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grupo`
--

INSERT INTO `grupo` (`id_grupo`, `Nombre`, `Horario`, `CupoMinimo`, `CupoMaximo`) VALUES
(1, 'Piano Vespertino', 'Martes a Jueves de 5:00p.m. a 7:00p.m.', 3, 12),
(2, 'Piano Matutino', 'Sábados de 8:00a.m. a 1:00p.m.', 3, 12),
(3, 'Guitarra Vespertino', 'Martes a Jueves de 5:00p.m. a 7:00p.m.', 5, 12),
(4, 'Guitarra Matutino', 'Sábados de 8:00a.m. a 1:00p.m.', 5, 12),
(5, 'Violín Vespertino', 'Martes a Jueves de 5:00p.m. a 7:00p.m.', 5, 12),
(6, 'Violín Matutino', 'Sábados de 8:00a.m. a 1:00p.m.', 5, 12);

-- --------------------------------------------------------

--
-- Table structure for table `inscripciones`
--

CREATE TABLE `inscripciones` (
  `id_inscripcion` int(11) NOT NULL,
  `id_alumno` int(11) DEFAULT NULL,
  `id_grupo` int(11) DEFAULT NULL,
  `FechaInscripcion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `inscripciones`
--
DELIMITER $$
CREATE TRIGGER `cancelar_inscripcion` BEFORE DELETE ON `inscripciones` FOR EACH ROW UPDATE grupo SET CupoMaximo = CupoMaximo+1 WHERE id_grupo = old.id_grupo
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `disminuir_cupo` AFTER INSERT ON `inscripciones` FOR EACH ROW UPDATE grupo SET CupoMaximo  = CupoMaximo - 1 WHERE id_grupo = new.id_grupo
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumno`
--
ALTER TABLE `alumno`
  ADD PRIMARY KEY (`id_alumno`),
  ADD KEY `id_alumno` (`id_alumno`);

--
-- Indexes for table `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`id_grupo`),
  ADD KEY `id_grupo` (`id_grupo`);

--
-- Indexes for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`id_inscripcion`),
  ADD KEY `id_alumno` (`id_alumno`,`id_grupo`),
  ADD KEY `id_grupo` (`id_grupo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumno`
--
ALTER TABLE `alumno`
  MODIFY `id_alumno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `grupo`
--
ALTER TABLE `grupo`
  MODIFY `id_grupo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `id_inscripcion` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id_alumno`),
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id_grupo`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
