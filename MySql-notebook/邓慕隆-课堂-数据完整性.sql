-- 实体完整性

-- 1 创建数据库 dbdml1
-- 创建表 dmla ,列 cola ,int 类型
-- 列 colb ,varchar(10) 类型,列 cola 上有主键
-- 列级完整性约束方式定义主键
CREATE DATABASE `dbdml1`;
USE `dbdml1`;
CREATE TABLE `dmla`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10)
);

-- 表级完整性约束方式定义主键
CREATE TABLE `dmla`
(
    `cola` INT,
    `colb` VARCHAR(10),
    PRIMARY KEY (`cola`)
);

-- 表级完整性约束方式定义主键,并给出主键约束名
CREATE TABLE `dmla`
(
    `cola` INT,
    `colb` VARCHAR(10),
    CONSTRAINT `pkdmla` PRIMARY KEY (`cola`)
);

-- 观察创建主键后,列 cola 是否可以为空.

-- 2 修改表 dmla, 删除表列 cola 上的主键.
ALTER TABLE `dmla`
    DROP PRIMARY KEY;

-- 3 修改表 dmla, 添加表列 cola 和 colb 上的主键.
-- 无约束名
ALTER TABLE `dmla`
    ADD PRIMARY KEY (`cola`, `colb`);

-- 有约束名
ALTER TABLE `dmla`
    ADD CONSTRAINT `pkdmla` PRIMARY KEY (`cola`, `colb`);

-- 4 创建表 dmlb,列 cola, int 类型,
-- 列 colb, varchar(10) 类型, 列 cola 上有主键,
-- 列 colb 上有唯一 约束.
-- 列级完整性约束方式定义唯-约束
CREATE TABLE `dmlb`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10) UNIQUE
);

-- 表级完整性约束方式定义唯一约束
CREATE TABLE `dmlb`
(
    `cola` INT,
    `colb` VARCHAR(10),
    PRIMARY KEY (`cola`),
    UNIQUE (`colb`)
);

-- 表级完整性约束方式定义唯一约束,并给出唯一约束名
CREATE TABLE `dmlb`
(
    `cola` INT,
    `colb` VARCHAR(10),
    CONSTRAINT `pkdmlb` PRIMARY KEY (`cola`),
    CONSTRAINT `undmlb` UNIQUE (`colb`)
);

-- 观察创建唯一约束后,列 colb 是否可以为空.

-- 5修改表 dmlb, 删除主键和唯一约束.
ALTER TABLE `dmlb`
    DROP PRIMARY KEY,
    DROP INDEX `undmlb`;

-- 6修改表 dmlb,分别添加表列 cola 和 colb.上的唯一约束.
ALTER TABLE `dmlb`
    ADD UNIQUE (`cola`),
    ADD UNIQUE (`colb`);

ALTER TABLE `dmlb`
    ADD CONSTRAINT `undmlbcola` UNIQUE (`cola`),
    ADD CONSTRAINT `undmlbcolb` UNIQUE (`colb`);

-- 7创建表 dmlc,列 cola, int 类型,
-- 列 colb, varchar(10)类型, 列 cola 上自增约束.
CREATE TABLE `dmlc`
(
    `cola` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `colb` VARCHAR(10)
);

-- 8修改表 dmlc,删除表列 cola 上的自增约束.
ALTER TABLE `dmlc`
    MODIFY `cola` INT NOT NULL;

-- 9修改表 dmlc,添加表列 cola.上的自增约束,设置自增初始值为100.
ALTER TABLE `dmlc`
    MODIFY `cola` INT NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 100;

-- 参照完整性
-- 10创建表 dmld,列 cola, int 类型,
-- 列 colb, varchar(10)类型, 列 cola 上有主键.
-- 创建表 dmle,列 cola, int 类型, 列 cola 上有主键,
-- 列 colb, varchar(10)类型,
-- 列 colc, int 类型,外键,引用表 dmld 的列 cola 值.
CREATE TABLE `dmld`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10)
);

-- 表级完整性约束方式定义外键
CREATE TABLE `dmle`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10),
    `colc` INT,
    FOREIGN KEY (`colc`)
        REFERENCES `dmld` (`cola`)
);

-- 表级完整性约束方式定义外键,并给出外键约束名
CREATE TABLE `dmle`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10),
    `colc` INT,
    CONSTRAINT `fkcolc` FOREIGN KEY (`colc`)
        REFERENCES `dmld` (`cola`)
);

-- 测试主键表和外键表之间的联系.
-- 11修改表 dmle,删除表列 colc.上的外键.
ALTER TABLE `dmle`
    DROP FOREIGN KEY `fkcolc`;

-- 12修改表 dmle,添加表列 colc.上的外键,
-- 使得外键表随主键表记录的更新而更新,删除而删除.
ALTER TABLE `dmle`
    ADD FOREIGN KEY (`colc`)
        REFERENCES `dmld` (`cola`)
        ON UPDATE CASCADE
        ON DELETE CASCADE;
ALTER TABLE `dmle`
    ADD CONSTRAINT `fkcolc` FOREIGN KEY (`colc`)
        REFERENCES `dmld` (`cola`)
        ON UPDATE CASCADE
        ON DELETE CASCADE;
-- 测试主键表和外键表之间的联系.

-- 用户定义的完整性

-- 13创建表 dmlf,列 cola, int 类型,主键,
-- 列 colb, varchar(10)类型, 非空.
CREATE TABLE `dmlf`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10) NOT NULL
);

-- 14修改表 dmlf,删除表列 colb 上的非空约束.
ALTER TABLE `dmlf`
    MODIFY `colb` VARCHAR(10) NULL;

-- 15修改表 dmlf,添加表列 colb 上的非空约束.
ALTER TABLE `dmlf`
    MODIFY `colb` VARCHAR(10) NOT NULL;

-- 思考:非空约束一 定能添加吗?

-- 16创建表 dmlg, 列 cola, int 类型,主键,
-- 列 colb, varchar(10)类型,默认值为"undefined" .
CREATE TABLE `dmlg`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10) DEFAULT 'undefined'
);

-- 17修改表 dmlg,删除表列 colb 上的默认值约束.
ALTER TABLE `dmlg`
    MODIFY `colb` VARCHAR(10);

-- 18修改表 dmlg, 添加表列 colb 上的默认值约束,
-- 默认值为"defined”.
ALTER TABLE `dmlg`
    MODIFY `colb` VARCHAR(10) DEFAULT 'defined';
-- 思考:已有的非空值被修改了吗?

-- 19创建表 dmlh,列 cola, int 类型,主键,列 colb, varchar(10)类型,要求值为"M"或"F".
-- 列级完整性约束方式定义 CHECK 约束
CREATE TABLE `dmlh`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10) CHECK (`colb` = 'M' OR `colb` = 'F')
);

-- 表级完整性约束方式定义 CHECK 约束
CREATE TABLE `dmlh`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10),
    CHECK (`colb` = 'M' OR `colb` = 'F')
);

-- 表级完整性约束方式定义 CHECK 约束,并给出 CHECK 约束名
CREATE TABLE `dmlh`
(
    `cola` INT PRIMARY KEY,
    `colb` VARCHAR(10),
    CONSTRAINT `ckdmlh` CHECK (`colb` = 'M' OR `colb` = 'F')
);

-- 20修改表 dmlh,删除表列 colb,上的 CHECK 约束.
ALTER TABLE `dmlh`
    DROP CHECK `ckdmlh`;

-- 21修改表 dmlh,添加表列 colb 上的 CHECK 约束,求值为"M"或"F".
-- 无约束名
ALTER TABLE `dmlh`
    ADD CHECK (`colb` = 'M' OR `colb` = 'F');
-- 有约束名
ALTER TABLE `dmlh`
    ADD CONSTRAINT `ckdmlh` CHECK (`colb` = 'M' OR `colb` = 'F');

