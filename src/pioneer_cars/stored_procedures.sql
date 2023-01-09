DELIMITER $$
DROP PROCEDURE if exists `booking_get_all`;

CREATE PROCEDURE `booking_get_all`(IN p_booking_id int)
BEGIN
	SELECT 
		id, 
        time_of_call,
		description
	FROM booking
    WHERE id = p_booking_id
    ORDER BY booking.time_of_call;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE if exists `booking_get_byid`;

CREATE PROCEDURE `booking_get_byid`(IN p_booking_id int)
BEGIN
	SELECT 
		booking.id, 
        booking.time_of_call,
		booking.description
	FROM booking
    WHERE id = p_booking_id;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE if exists `booking_note_upsert`;

CREATE PROCEDURE `booking_note_upsert`(IN p_id int, IN p_note text)
BEGIN
	if p_id > 0 then
		update booking_note
        set
			note = p_note
		where id = p_id;

    else
		insert booking_note 
			(note)
        values 
			(p_note);
		
        set p_id = LAST_INSERT_ID();
	
	end if;
    
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE if exists `booking_delete`;

CREATE PROCEDURE `booking_delete`(IN p_id int)
BEGIN
	DELETE FROM booking WHERE id = p_id;
END$$
DELIMITER ;