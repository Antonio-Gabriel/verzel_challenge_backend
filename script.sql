--
-- Create model Module
--
CREATE TABLE `module` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL);
--
-- Create model User
--
CREATE TABLE `user` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_at` datetime(6) NOT NULL, `updated_at` datetime(6) NOT NULL, `state` bool NOT NULL, `username` varchar(80) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `password` varchar(128) NOT NULL);
--
-- Create model Lesson
--
CREATE TABLE `lesson` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL, `start_date` date NOT NULL, `module_id` bigint NOT NULL);
ALTER TABLE `user` ADD CONSTRAINT `user_email_54dc62b2_uniq` UNIQUE (`email`);
ALTER TABLE `lesson` ADD CONSTRAINT `lesson_module_id_8d37da49_fk_module_id` FOREIGN KEY (`module_id`) REFERENCES `module` (`id`);