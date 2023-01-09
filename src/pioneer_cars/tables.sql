CREATE TABLE IF NOT EXISTS `booking_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `parent_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `problem_has_general_type_idx` (`parent_id` ASC),
  CONSTRAINT `booking_has_general_type`
    FOREIGN KEY (`parent_id`)
    REFERENCES `booking_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `staff` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `booking` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `staff_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `urgency_id` INT NULL,
  `time_of_call` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `chassis_no` VARCHAR(20) NOT NULL,
  `description` TEXT NOT NULL,
  `booking_type_id` INT NULL,
  `assigned_driver_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `booking_urgency_idx` (`urgency_id` ASC) ,
  INDEX `booking_has_chassis_nox` (`chassis_no` ASC) ,
  INDEX `booking_has_type_idx` (`booking_type_id` ASC) ,
  INDEX `booking_has_staff_idx` (`staff_id` ASC) ,
  INDEX `booking_has_driver_idx` (`assigned_driver_id` ASC) ,
  INDEX `booking_has_customer_idx` (`customer_id` ASC) ,
  CONSTRAINT `booking_has_staff`
    FOREIGN KEY (`staff_id`)
    REFERENCES `staff` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_urgency`
    FOREIGN KEY (`urgency_id`)
    REFERENCES `urgency` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_vehicle`
    FOREIGN KEY (`chassis_no`)
    REFERENCES `vehicle` (`chassis_no`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_assigned_driver`
    FOREIGN KEY (`assigned_driver_id`)
    REFERENCES `staff` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_type`
    FOREIGN KEY (`booking_type_id`)
    REFERENCES `booking_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `booking_has_customer`
    FOREIGN KEY (`customer_id`)
    REFERENCES `customer` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `booking_note` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `booking_id` INT NOT NULL,
  `date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `note` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `booking_note_has_booking_idx` (`booking_id` ASC),
  CONSTRAINT `booking_note_has_booking`
    FOREIGN KEY (`booking_id`)
    REFERENCES `booking` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
