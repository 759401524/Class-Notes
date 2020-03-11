-- 1创建数据库 dengmulong2
-- 使用数据库 dengmulong2
CREATE DATABASE IF NOT EXISTS `dengmulong2`;
USE `dengmulong2`;

-- 创建仓库列表（仓库号，面积，电话）
CREATE TABLE `warehouse`
(
    `warehouse_id`    INT         NOT NULL AUTO_INCREMENT,
    `warehouse_area`  DECIMAL     NOT NULL,
    `warehouse_phone` VARCHAR(20) NOT NULL,
    PRIMARY KEY (`warehouse_id`)
);


-- 创建零件列表（零件号，名称，规格，单价，描述）
CREATE TABLE `parts`
(
    `parts_id`           INT         NOT NULL AUTO_INCREMENT,
    `parts_name`         TINYTEXT    NOT NULL,
    `part_specification` TINYTEXT    NOT NULL,
    `parts_price`        DECIMAL     NOT NULL,
    `part_description`   VARCHAR(20) NOT NULL,
    PRIMARY KEY (`parts_id`)
);

-- 创建项目列表（项目号，预算，开工日期）
CREATE TABLE `project`
(
    `project_id`         INT     NOT NULL AUTO_INCREMENT,
    `project_budget`     DECIMAL NOT NULL,
    `project_start_date` DATE    NOT NULL,
    PRIMARY KEY (`project_id`)
);

-- 创建供应商表（供应商号，姓名，地址，电话，账号）
CREATE TABLE `supplier`
(
    `supplier_id`      INT         NOT NULL AUTO_INCREMENT,
    `supplier_name`    TINYTEXT    NOT NULL,
    `supplier_address` TEXT        NOT NULL,
    `supplier_phone`   VARCHAR(20) NOT NULL,
    `supplier_account` INT         NOT NULL,
    PRIMARY KEY (`supplier_id`)
);

-- 创建职工列表（职工号，姓名，年龄，仓库号，领导工号）
CREATE TABLE `employee`
(
    `employee_id`   INT        NOT NULL AUTO_INCREMENT,
    `employee_name` TINYTEXT   NOT NULL,
    `employee_age`  VARCHAR(3) NOT NULL,
    `warehouse_id`  INT        NOT NULL,
    `leadership_id` INT        NOT NULL,
    PRIMARY KEY (`employee_id`, `warehouse_id`),
    FOREIGN KEY (`warehouse_id`)
        REFERENCES `warehouse` (`warehouse_id`)
);

-- 创建仓库-零件列表（仓库号，零件号，库存量）
CREATE TABLE `warehouse_parts`
(
    `warehouse_id` INT NOT NULL,
    `parts_id`     INT NOT NULL,
    `inventory`    INT NOT NULL,
    PRIMARY KEY (`warehouse_id`, `parts_id`),
    FOREIGN KEY (`warehouse_id`)
        REFERENCES `warehouse` (`warehouse_id`),
    FOREIGN KEY (`parts_id`)
        REFERENCES `parts` (`parts_id`)
);


-- 创建零件供应列表（项目号，零件号，供应商号，供应量）
CREATE TABLE `parts_supply`
(
    `project_id`  INT NOT NULL,
    `part_id`     INT NOT NULL,
    `supplier_id` INT NOT NULL,
    `supply`      INT NOT NULL,
    PRIMARY KEY (`project_id`, `part_id`, `supplier_id`),
    FOREIGN KEY (`project_id`)
        REFERENCES `project` (`project_id`),
    FOREIGN KEY (`part_id`)
        REFERENCES `parts` (`parts_id`),
    FOREIGN KEY (`supplier_id`)
        REFERENCES `supplier` (`supplier_id`)
);
