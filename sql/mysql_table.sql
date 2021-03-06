SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `mydb` ;
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`game_db`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`game_db` ;

CREATE TABLE IF NOT EXISTS `mydb`.`game_db` (
  `game` INT NOT NULL AUTO_INCREMENT,
  `win` TINYINT(1) NOT NULL,
  `turn_1` INT(11) NULL,
  `turn_2` INT(11) NULL,
  `turn_3` INT(11) NULL,
  `turn_4` INT(11) NULL,
  `turn_5` INT(11) NULL,
   PRIMARY KEY (`game`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
