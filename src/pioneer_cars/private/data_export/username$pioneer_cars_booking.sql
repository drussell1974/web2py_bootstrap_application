-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: <username>.mysql.eu.pythonanywhere-services.com    Database: <username>$pioneer_cars
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `urgency_id` int(11) DEFAULT NULL,
  `time_of_call` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `registration_no` varchar(10) NOT NULL,
  `description` text NOT NULL,
  `booking_type_id` int(11) DEFAULT NULL,
  `assigned_driver_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_urgency_idx` (`urgency_id`),
  KEY `booking_has_type_idx` (`booking_type_id`),
  KEY `booking_has_staff_idx` (`staff_id`),
  KEY `booking_has_driver_idx` (`assigned_driver_id`),
  KEY `booking_has_customer_idx` (`customer_id`),
  KEY `booking_has_vehicle_idx` (`registration_no`),
  CONSTRAINT `booking_has_assigned_driver` FOREIGN KEY (`assigned_driver_id`) REFERENCES `staff` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_customer` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_staff` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_type` FOREIGN KEY (`booking_type_id`) REFERENCES `booking_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_urgency` FOREIGN KEY (`urgency_id`) REFERENCES `urgency` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_vehicle` FOREIGN KEY (`registration_no`) REFERENCES `vehicle` (`registration_no`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (2,1,1,1,'2022-12-23 17:21:12','B11 KED','Lorem Ipsum',4,2),(5,1,8,6,'2022-12-26 08:39:36','BG11 KES','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue ut lectus arcu. Faucibus et molestie ac feugiat. Consequat mauris nunc congue nisi vitae suscipit. Nunc mattis enim ut tellus elementum sagittis vitae. \r\n\r\nOrnare arcu odio ut sem nulla pharetra. Vulputate odio ut enim blandit volutpat. Egestas diam in arcu cursus euismod quis viverra. Mauris pharetra et ultrices neque. Quisque egestas diam in arcu cursus euismod quis viverra nibh.',4,1),(6,10,3,2,'2022-12-26 09:30:28','BG11 KES','Xxx',3,9);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-09 14:05:56
