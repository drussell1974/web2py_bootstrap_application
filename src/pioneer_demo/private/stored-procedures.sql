DELIMITER $$
CREATE PROCEDURE `booking_delete`(IN p_id int)
BEGIN
	DELETE FROM booking WHERE id = p_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_get_all`()
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
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_get_byid`(IN p_booking_id int)
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
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_note_delete`(IN p_id int)
BEGIN
	DELETE FROM booking_note WHERE id = p_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_note_get_all`(IN p_booking_id int)
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
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_note_get_byid`(IN p_booking_note_id int)
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
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_note_upsert`(IN p_id int, IN p_note text, IN p_booking_id int)
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

END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_type_get_all`()
BEGIN
	SELECT
		id,
		name
	FROM booking_type
    ORDER BY id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `booking_upsert`(
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

END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `customer_delete`(IN p_id int)
BEGIN
	DELETE FROM customer WHERE id = p_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `customer_get_all`()
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
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `customer_get_byid`(IN p_customer_id int)
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
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `customer_upsert`(IN p_id int, IN p_first_name varchar(45), IN p_surname varchar(45), IN p_membership_id int)
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


END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `delete_customer`(IN p_id int)
BEGIN
	DELETE FROM caller WHERE id = p_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `get_customer_all`()
BEGIN
	SELECT
		c.id,
		c.first_name,
        c.surname,
        c.job_role_id,
        jr.job_title,
        jr.department_id,
        d.name as department_name
    FROM caller as c
    INNER JOIN job_role as jr ON c.job_role_id = jr.id
    INNER JOIN department as d ON jr.department_id = d.id
    ORDER BY c.id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `get_customer_byid`(IN p_caller_id int)
BEGIN
	SELECT
		c.id,
		c.first_name,
        c.surname,
        c.job_role_id,
        jr.job_title,
        jr.department_id,
        d.name as department_name
    FROM caller as c
    INNER JOIN job_role as jr ON c.job_role_id = jr.id
    INNER JOIN department as d ON jr.department_id = d.id
    WHERE c.id = p_caller_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `get_membership_all`()
BEGIN
	SELECT
		jr.id,
		jr.job_title,
        jr.department_id,
        d.name as department_name
	FROM
		job_role as jr
        INNER JOIN department as d ON d.id = jr.department_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `membership_get_all`()
BEGIN
	SELECT
		m.id,
		m.name,
        m.level_id,
        l.name as level_name
	FROM
		membership as m
        INNER JOIN membership_level as l ON m.level_id = l.id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `problem_note_get_byid`(IN p_problem_note_id int)
BEGIN
	SELECT
		id,
		name
	FROM problem_note
    WHERE id = p_problem_note_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `staff_get_all`()
BEGIN
	SELECT
		id,
		first_name,
        surname
	FROM staff
    ORDER BY surname, first_name;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `upsert_customer`(IN p_id int, IN p_first_name varchar(45), IN p_surname varchar(45), IN p_membership_id int)
BEGIN
	if p_id > 0 then
		update caller
        set
			first_name = p_first_name,
            surname = p_surname,
			job_role_id = p_membership_id
        where id = p_id;

    else
		insert caller
			(first_name, surname, job_role_id)
        values
			(p_first_name, p_surname, p_membership_id);

        set p_id = LAST_INSERT_ID();

	end if;


END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `urgency_get_all`()
BEGIN
	SELECT
		id,
		name
	FROM urgency
    ORDER BY id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `vehicle_delete`(IN p_registration_no varchar(10))
BEGIN
	DELETE FROM vehicle WHERE registration_no = p_registration_no;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `vehicle_get_all`()
BEGIN
	SELECT
		v.registration_no
    FROM vehicle as v
    ORDER BY v.registration_no;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `vehicle_get_byid`(IN p_registration_no varchar(10))
BEGIN
	SELECT
		v.chassis_no
    FROM vehicle as v
    WHERE v.registration_no = p_registration_no;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `vehicle_upsert`(IN p_old_registration_no varchar(10), IN p_registration_no varchar(10))
BEGIN
	if length(p_old_registration_no) > 0 then
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


END$$
DELIMITER ;


DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_upsert;

CREATE PROCEDURE vehicle_upsert(IN p_old_registration_no varchar(10), IN p_registration_no varchar(10))
BEGIN
	if length(p_old_registration_no) > 0 then
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
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_engine_delete;
CREATE PROCEDURE vehicle_engine_delete(IN p_old_registration_no varchar(10))
BEGIN
    DELETE FROM vehicle_engine 
    WHERE registration_no = p_old_registration_no;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_engine_insert;
CREATE PROCEDURE vehicle_engine_insert(IN p_engine_id INT, IN p_registration_no varchar(10))
BEGIN
    INSERT vehicle_engine (engine_id, registration_no)
    VALUES (p_engine_id, p_registration_no);
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_body_delete;
CREATE PROCEDURE vehicle_body_delete(IN p_old_registration_no varchar(10))
BEGIN
    DELETE FROM vehicle_body 
    WHERE registration_no = p_old_registration_no;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_body_insert;
CREATE PROCEDURE vehicle_body_insert(IN p_body_id INT, IN p_old_registration_no varchar(10))
BEGIN
    INSERT vehicle_body (body_id, registration_no)
    VALUES (p_body_id, p_registration_no);
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_furnishing_delete;
CREATE PROCEDURE vehicle_furnishing_delete(IN p_old_registration_no varchar(10))
BEGIN
    DELETE FROM vehicle_furnishing 
    WHERE registration_no = p_old_registration_no;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS vehicle_furnishing_insert;
CREATE PROCEDURE vehicle_furnishing_insert(IN p_furnishing_id INT, IN p_old_registration_no varchar(10))
BEGIN
    INSERT vehicle_furnishing (furnishing_id, registration_no)
    VALUES (p_furnishing_id, p_registration_no);
END$$
DELIMITER ;
