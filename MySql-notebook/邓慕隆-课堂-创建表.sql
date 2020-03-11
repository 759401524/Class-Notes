-- 1创建数据库dengmulong1,
-- 创建表dmla, 列cola, int类型。
CREATE DATABASE IF NOT EXISTS Dengmulong1;
USE Dengmulong1;
CREATE TABLE Dmla
(
	Cola int
);

-- 2查看数据库dengmulong1中的表。
USE Dengmulong1;
SHOW TABLES;

-- 3查看数据库dengmulong1中的表dmla的结构。
SHOW COLUMNS FROM Dmla FROM Dengmulong1;
SHOW COLUMNS FROM Dengmulong1.Dmla;
DESCRIBE Dmla;

-- 4查看数据库dengmulong1中的表tbldmla中列cola的信息。
DESCRIBE Dmla Cola;

-- 5向表dmla中添加列colb, smallint类型，位于表的第一列,
-- 列colc, varchar(20)类型, 位于表的第二列,
-- cold，DATE类型,位于表的最后-列。
ALTER TABLE Dmla
	ADD Colb smallint FIRST,
	ADD Colc varchar(20) AFTER Colb,
	ADD Cold DATE;

-- 6将表dmla中列colb的名称改为colid,
ALTER TABLE Dmla
	CHANGE COLUMN Colb Colid smallint;

-- 7将表dmla中列colid的数据类型改为tinyint.
ALTER TABLE Dmla
	MODIFY Colid tinyint;

-- 8将表dmla中的列colc删除。
ALTER TABLE Dmla
	DROP Colc;

-- 9将表dmla的表名改为dengmulonga.
ALTER TABLE Dmla RENAME AS Dengmulonga;

-- 10将表dengmulonga的表名改为dmla。
RENAME TABLE Dengmulonga TO Dmla;

-- 11创建表tbla的备份表dmlabak.
CREATE TABLE Dmlabak LIKE Dmla;

-- 12删除表dmla.
DROP TABLE Dmla;
