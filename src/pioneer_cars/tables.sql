USE drussellkc$pioneer_cars;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE booking;
DROP TABLE booking_note;
DROP TABLE booking_type;
DROP TABLE caller;
DROP TABLE customer;
DROP TABLE department;
DROP TABLE job_role;
DROP TABLE membership;
DROP TABLE membership_level;
DROP TABLE staff;
DROP TABLE urgency;
DROP TABLE vehicle;

CREATE TABLE `booking` (
  `id` int NOT NULL AUTO_INCREMENT,
  `staff_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `urgency_id` int DEFAULT NULL,
  `time_of_call` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `registration_no` varchar(10) NOT NULL,
  `description` text NOT NULL,
  `booking_type_id` int DEFAULT NULL,
  `assigned_driver_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_urgency_idx` (`urgency_id`),
  KEY `booking_has_type_idx` (`booking_type_id`),
  KEY `booking_has_staff_idx` (`staff_id`),
  KEY `booking_has_driver_idx` (`assigned_driver_id`),
  KEY `booking_has_customer_idx` (`customer_id`),
  KEY `booking_has_vehicle_idx` (`registration_no`),
  CONSTRAINT `booking_has_assigned_driver` FOREIGN KEY (`assigned_driver_id`) REFERENCES `staff` (`id`),
  CONSTRAINT `booking_has_customer` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `booking_has_staff` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`),
  CONSTRAINT `booking_has_type` FOREIGN KEY (`booking_type_id`) REFERENCES `booking_type` (`id`),
  CONSTRAINT `booking_has_urgency` FOREIGN KEY (`urgency_id`) REFERENCES `urgency` (`id`),
  CONSTRAINT `booking_has_vehicle` FOREIGN KEY (`registration_no`) REFERENCES `vehicle` (`registration_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `booking_note` (
  `id` int NOT NULL AUTO_INCREMENT,
  `booking_id` int NOT NULL,
  `time_of_note` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `note` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `booking_note_has_booking_idx` (`booking_id`),
  CONSTRAINT `booking_note_has_booking` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `booking_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `parent_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `problem_has_general_type_idx` (`parent_id`),
  CONSTRAINT `booking_has_general_type` FOREIGN KEY (`parent_id`) REFERENCES `booking_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `caller` (
  `id` int NOT NULL AUTO_INCREMENT,
  `caller_id` int NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `job_role_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `caller_has_jobtitle_idx` (`job_role_id`),
  CONSTRAINT `caller_has_job_role` FOREIGN KEY (`job_role_id`) REFERENCES `job_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `caller_id` int NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `membership_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `caller_has_jobtitle_idx` (`membership_id`),
  CONSTRAINT `customer_has_membeship` FOREIGN KEY (`membership_id`) REFERENCES `membership` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `department` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `job_role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_title` varchar(90) NOT NULL,
  `department_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobrole_has_department_idx` (`department_id`),
  CONSTRAINT `jobrole_has_department` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `membership` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(90) NOT NULL,
  `level_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobrole_has_department_idx` (`level_id`),
  CONSTRAINT `membership_has_level` FOREIGN KEY (`level_id`) REFERENCES `membership_level` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `membership_level` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `staff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `urgency` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `vehicle` (
  `registration_no` varchar(10) NOT NULL,
  PRIMARY KEY (`registration_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE body (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE engine (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE furnishing (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

SET FOREIGN_KEY_CHECKS=0;
