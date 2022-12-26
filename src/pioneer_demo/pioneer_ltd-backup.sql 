-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: drussellkc.mysql.eu.pythonanywhere-services.com    Database: drussellkc$pioneer_ltd
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (2,1,1,1,'2022-12-23 17:21:12','B11 KED','Lorem Ipsum',4,2);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_note`
--

DROP TABLE IF EXISTS `booking_note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) NOT NULL,
  `time_of_note` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `note` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_note_has_booking_idx` (`booking_id`),
  CONSTRAINT `booking_note_has_booking` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_note`
--

LOCK TABLES `booking_note` WRITE;
/*!40000 ALTER TABLE `booking_note` DISABLE KEYS */;
INSERT INTO `booking_note` VALUES (1,2,'2022-12-23 17:40:03','Donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed velit dignissim sodales ut eu sem integer vitae justo eget magna fermentum iaculis eu'),(6,2,'2022-12-24 06:20:53','Ornare Lectus Sit amet est placerat in egestas erat imperdiet sed euismod nisi porta lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor id eu nisl nunc mi ipsum');
/*!40000 ALTER TABLE `booking_note` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_type`
--

DROP TABLE IF EXISTS `booking_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `problem_has_general_type_idx` (`parent_id`),
  CONSTRAINT `booking_has_general_type` FOREIGN KEY (`parent_id`) REFERENCES `booking_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_type`
--

LOCK TABLES `booking_type` WRITE;
/*!40000 ALTER TABLE `booking_type` DISABLE KEYS */;
INSERT INTO `booking_type` VALUES (1,'engine',NULL),(2,'interior',NULL),(3,'body',NULL),(4,'valet',2);
/*!40000 ALTER TABLE `booking_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `caller_id` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `membership_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `caller_has_jobtitle_idx` (`membership_id`),
  CONSTRAINT `customer_has_membeship` FOREIGN KEY (`membership_id`) REFERENCES `membership` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,1922,'Cecil','Shoreditch',1),(2,2851,'Alimjan Beli','Hampton',2),(3,2851,'Hilary','Rouse',3),(4,3034,'Hilary','Rouse',3),(5,3443,'Gustav','Purpleson',4),(6,3487,'Caspian','Bellevedere',5),(7,4934,'Alicia','Radoslav',6),(8,5287,'Jetinder','Abbas',7),(9,7343,'Gustav','Purpleson',7),(20,0,'Russ','Newrick',6);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership`
--

DROP TABLE IF EXISTS `membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membership` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(90) NOT NULL,
  `level_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobrole_has_department_idx` (`level_id`),
  CONSTRAINT `membership_has_level` FOREIGN KEY (`level_id`) REFERENCES `membership_level` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership`
--

LOCK TABLES `membership` WRITE;
/*!40000 ALTER TABLE `membership` DISABLE KEYS */;
INSERT INTO `membership` VALUES (1,'Finance Director',1),(2,'Property Manager',2),(3,'Administrator',3),(4,'Commerial Property Manager',3),(5,'Leasing Agent',2),(6,'Managing Director',1),(7,'Administrator',2);
/*!40000 ALTER TABLE `membership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership_level`
--

DROP TABLE IF EXISTS `membership_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membership_level` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership_level`
--

LOCK TABLES `membership_level` WRITE;
/*!40000 ALTER TABLE `membership_level` DISABLE KEYS */;
INSERT INTO `membership_level` VALUES (1,'Departmental'),(2,'Residential'),(3,'Commercial');
/*!40000 ALTER TABLE `membership_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'Akram','Hussain'),(2,'Brian','Cummin'),(3,'Jim','Sechen'),(4,'Ruba','Ng'),(5,'Karishma','Khati'),(6,'Gunther','Beard'),(7,'Tatiana','Zellweger'),(8,'Indigo','Violet'),(9,'John','Doe'),(10,'Quiche','Hollandaise');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `urgency`
--

DROP TABLE IF EXISTS `urgency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `urgency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urgency`
--

LOCK TABLES `urgency` WRITE;
/*!40000 ALTER TABLE `urgency` DISABLE KEYS */;
INSERT INTO `urgency` VALUES (1,'Urgent'),(2,'Required Today'),(3,'Minor Issue'),(4,'Can workaround'),(5,'Required next week'),(6,'Effecting everyone i'),(7,'Required this week');
/*!40000 ALTER TABLE `urgency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `registration_no` varchar(10) NOT NULL,
  PRIMARY KEY (`registration_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES ('B11 KED'),('BG11 KES'),('VE16 JED');
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'drussellkc$pioneer_ltd'
--
/*!50003 DROP PROCEDURE IF EXISTS `booking_delete` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_delete`(IN p_id int)
BEGIN
	DELETE FROM booking WHERE id = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_get_all`()
BEGIN
	SELECT 
		b.id, 
        b.time_of_call,
		b.description,
        b.registration_no,
        b.staff_id,
        s.first_name as staff_first_name,
        s.surname as staff_surname,
        b.customer_id,
        c.first_name as customer_first_name,
        c.surname as customer_surname,
        b.urgency_id,
        u.name as urgency_name,
        b.booking_type_id,
        t.name as booking_type_name,
        b.assigned_driver_id,
        d.first_name as driver_first_name,
        d.surname as driver_surname
	FROM booking as b
    INNER JOIN staff as s ON b.staff_id = s.id
    INNER JOIN customer as c ON b.customer_id = c.id
    INNER JOIN urgency as u ON b.urgency_id = u.id
    INNER JOIN booking_type as t ON b.booking_type_id = t.id
    INNER JOIN staff as d ON b.assigned_driver_id = d.id
    ORDER BY b.time_of_call DESC; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_get_byid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_get_byid`(IN p_booking_id int)
BEGIN
	SELECT 
		b.id, 
        b.time_of_call,
		b.description,
        b.registration_no,
        b.staff_id,
        s.first_name as staff_first_name,
        s.surname as staff_surname,
        b.customer_id,
        c.first_name as customer_first_name,
        c.surname as customer_surname,
        b.urgency_id,
        u.name as urgency_name,
        b.booking_type_id,
        t.name as booking_type_name,
        b.assigned_driver_id,
        d.first_name as driver_first_name,
        d.surname as driver_surname
	FROM booking as b
    INNER JOIN staff as s ON b.staff_id = s.id
    INNER JOIN customer as c ON b.customer_id = c.id
    INNER JOIN urgency as u ON b.urgency_id = u.id
    INNER JOIN booking_type as t ON b.booking_type_id = t.id
    INNER JOIN staff as d ON b.assigned_driver_id = d.id
    WHERE b.id = p_booking_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_note_delete` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_note_delete`(IN p_id int)
BEGIN
	DELETE FROM booking_note WHERE id = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_note_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_note_get_all`(IN p_booking_id int)
BEGIN
	SELECT 
		booking_note.id, 
        booking_note.time_of_note,
		booking_note.note,
        booking_note.booking_id,
        booking.time_of_call,
		booking.description,
        booking.registration_no
	FROM booking_note
    INNER JOIN booking ON booking_note.booking_id = booking.id
    WHERE booking.id = p_booking_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_note_get_byid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_note_get_byid`(IN p_booking_note_id int)
BEGIN
	SELECT 
		booking_note.id, 
        booking_note.time_of_note,
		booking_note.note,
        booking_note.booking_id,
        booking.time_of_call,
		booking.description,
        booking.registration_no
	FROM booking_note
    INNER JOIN booking ON booking_note.booking_id = booking.id
    WHERE booking_note.id = p_booking_note_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_note_upsert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_note_upsert`(IN p_id int, IN p_note text, IN p_booking_id int)
BEGIN
	if p_id > 0 then
		update booking_note
        set
			note = p_note
		where id = p_id;

    else
		insert booking_note 
			(note, booking_id)
        values 
			(p_note, p_booking_id);
		
        set p_id = LAST_INSERT_ID();
	
	end if;
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_type_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_type_get_all`()
BEGIN
	SELECT 
		id, 
		name 
	FROM booking_type
    ORDER BY id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `booking_upsert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `booking_upsert`(
	IN p_id int, 
    IN p_description text, 
    IN p_registration_no varchar(10), 
    IN p_staff_id int,
    IN p_customer_id int,
    IN p_urgency_id int,
    IN p_booking_type_id int,
    IN p_assigned_driver_id int
    )
BEGIN
	if p_id > 0 then
		update booking
        set
			registration_no = p_registration_no,
			description = p_description,
            staff_id = p_staff_id,
            customer_id = p_customer_id,
            urgency_id = p_urgency_id,
            booking_type_id = p_booking_type_id,
            assigned_driver_id = p_assigned_driver_id
		where id = p_id;

    else
		insert booking 
			(description, registration_no, staff_id, customer_id, urgency_id, booking_type_id, assigned_driver_id)
        values 
			(p_description, p_registration_no, p_staff_id, p_customer_id, p_urgency_id, p_booking_type_id, p_assigned_driver_id);
		
        set p_id = LAST_INSERT_ID();
	
	end if;
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_delete` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `customer_delete`(IN p_id int)
BEGIN
	DELETE FROM customer WHERE id = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `customer_get_all`()
BEGIN
	SELECT 
		c.id, 
		c.first_name, 
        c.surname, 
        c.membership_id, 
        m.name as membership_name, 
        m.level_id, 
        l.name as membership_level_name
    FROM customer as c
    INNER JOIN membership as m ON m.id = c.membership_id
    INNER JOIN membership_level as l ON l.id = m.level_id
    ORDER BY c.id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_get_byid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `customer_get_byid`(IN p_customer_id int)
BEGIN
	SELECT 
		c.id, 
		c.first_name, 
        c.surname, 
        c.membership_id, 
        m.name as membership_name, 
        m.level_id, 
        l.name as membership_level_name
    FROM customer as c
    INNER JOIN membership as m ON m.id = c.membership_id
    INNER JOIN membership_level as l ON l.id = m.level_id
    WHERE c.id = p_customer_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_upsert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `customer_upsert`(IN p_id int, IN p_first_name varchar(45), IN p_surname varchar(45), IN p_membership_id int)
BEGIN
	if p_id > 0 then
		update customer
        set
			first_name = p_first_name,
            surname = p_surname,
			membership_id = p_membership_id
        where id = p_id;

    else
		insert customer 
			(first_name, surname, membership_id)
        values 
			(p_first_name, p_surname, p_membership_id);
		
        set p_id = LAST_INSERT_ID();
	
	end if;
    

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `membership_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `membership_get_all`()
BEGIN
	SELECT
		m.id,
		m.name,
        m.level_id,
        l.name as level_name
	FROM 
		membership as m
        INNER JOIN membership_level as l ON m.level_id = l.id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `problem_note_get_byid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `problem_note_get_byid`(IN p_problem_note_id int)
BEGIN
	SELECT 
		id, 
		name
	FROM problem_note
    WHERE id = p_problem_note_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `staff_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `staff_get_all`()
BEGIN
	SELECT 
		id, 
		first_name,
        surname
	FROM staff
    ORDER BY surname, first_name;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `urgency_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `urgency_get_all`()
BEGIN
	SELECT 
		id, 
		name 
	FROM urgency
    ORDER BY id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `vehicle_delete` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `vehicle_delete`(IN p_registration_no varchar(10))
BEGIN
	DELETE FROM vehicle WHERE registration_no = p_registration_no;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `vehicle_get_all` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `vehicle_get_all`()
BEGIN
	SELECT 
		v.registration_no
    FROM vehicle as v
    ORDER BY v.registration_no;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `vehicle_get_byid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `vehicle_get_byid`(IN p_registration_no varchar(10))
BEGIN
	SELECT 
		v.chassis_no
    FROM vehicle as v
    WHERE v.registration_no = p_registration_no;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `vehicle_upsert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`drussellkc`@`%` PROCEDURE `vehicle_upsert`(IN p_old_registration_no varchar(10), IN p_registration_no varchar(10))
BEGIN
	if length(p_old_chassis_no) > 0 then
		update vehicle
        set
			registration_no = p_registration_no
        where registration_no = p_old_registration_no;

    else
		insert vehicle 
			(registration_no)
        values 
			(p_registration_no);
			
	end if;
    

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-25 17:37:53
