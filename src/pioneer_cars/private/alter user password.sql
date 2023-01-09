ALTER USER '<username>'@'%'
  IDENTIFIED WITH caching_sha2_password BY '<password>'
  PASSWORD EXPIRE INTERVAL 180 DAY
  FAILED_LOGIN_ATTEMPTS 100 PASSWORD_LOCK_TIME 2;
  
grant all privileges on pioneer_cars.* to '<username>'@'%';
