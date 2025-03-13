USE blockchain_program;
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `name` VARCHAR(255),
    `user_name` VARCHAR(255) UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `id` INT PRIMARY KEY AUTO_INCREMENT
);