-- 1 使用 CREATE DATABASE语句创建数据库 dengmulong1。
CREATE DATABASE dengmulong1;

-- 2 使用 CREATE SCHEMA语句创建数据库 dengmulong2。
CREATE SCHEMA dengmulong2;

-- 3 使用 CREATE DATABASE语句创建数据库 dengmulong3，
-- 设置默认字符集为UTF8。
CREATE DATABASE dengmulong3
	CHARACTER SET = utf8;

-- 4 使用 CREATE DATABASE语句创建数据库 dengmulong4，
-- 并在创建前查看是否有同名数据库存在，如果没有则创建，如果有则不创建。
CREATE DATABASE IF NOT EXISTS dengmulong4;

-- 5 使用 SHOW DATABASES 语句查看 MYSQL 服务器中的数据库列表。
SHOW DATABASES;

-- 6 选择数据库 dengmulong1 为当前数据库。
USE dengmulong1;

-- 7 修改数据库 dengmulong1，设置默认字符集为UTF8，
-- 设置校对规则为 utf8_unicode_ci。
ALTER DATABASE dengmulong1
	DEFAULT CHARACTER SET utf8
	DEFAULT COLLATE utf8_unicode_ci;

-- 8 删除数据库 dengmulong4。
DROP DATABASE dengmulong4;
