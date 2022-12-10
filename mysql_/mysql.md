# Mysql

## 一、安装使用搭建



## 二、配置

/etc/mysql/mysql.conf.d//mysqld.cnf 

## 三、Mysql Program

Doc：https://dev.mysql.com/doc/refman/8.0/en/programs.html

### 1. mysqld主程序及启动脚本

1. mysql.server
2. mysqld_safe
3. mysqld_multi
4.  ...

### 2. mysql安装更新时的辅助脚本

1. mysql_secure_installation
2. mysql_upgrade
3.  ...

### 3. Mysql客户端

1. mysql

   启动进入shell

2. mysqladmin

   执行管理操作的客户端程序，可以用来检查服务器的配置和当前状态、创建和删除数据库等

3. mysqldump

   csdn详解：https://blog.csdn.net/carefree2005/article/details/113762170

   用于转存储数据库。产生一个SQL脚本，其中包含重新创建数据库所必需的命令CREATE TABLE INSERT等

   备份原理是通过协议连接到 MySQL 数据库，将需要备份的数据查询出来，将查询出的数据转换成对应的insert 语句，执行这些 insert 语句，即可将对应的数据还原。

4. mysqlcheck

   用来 检查，分析，优化，修复表，需要在数据库运行的状态下才可运行

5. ...

### 4. mysql管理实用程序

1. mysql_config_editor
2. mysql_config
3.  ...

## SQL

什么是SQL

- Structured Query Language：结构化查询语言
- 其实就是定义了操作所有关系型数据库的规则。
- 每一种数据库操作的方式可能会存在一些不一样的地方，我们称为“**方言**”。

SQL通用语法

- SQL 语句可以单行或多行书写，以分号结尾
- 可使用空格和缩进来增强语句的可读性
- MySQL 数据库的 SQL 语句不区分大小写，关键字建议使用大写
- 数据库的注释：
  - 单行注释：-- 注释内容       #注释内容(mysql特有)
  - 多行注释：/* 注释内容 */

SQL分类

- DDL(Data Definition Language)数据定义语言
  - 用来定义数据库对象：数据库，表，列等。关键字：create, drop,alter 等
- DML(Data Manipulation Language)数据操作语言
  - 用来对数据库中表的数据进行增删改。关键字：insert, delete, update 等
- DQL(Data Query Language)数据查询语言
  - 用来查询数据库中表的记录(数据)。关键字：select, where 等
- DCL(Data Control Language)数据控制语言(了解)
  - 用来定义数据库的访问权限和安全级别，及创建用户。关键字：GRANT， REVOKE 等

## 隔离级别
* read-uncommitted(读未提交)   一个事务进行了某个操作，不论是否提交，其他事物都能读到这个操作的结果，即想读取到新的数据
* read-committed(读已提交)     一个事务进行了某个操作，只有提交了，其他事物才能读到这个操作的结果，即想读取到新的数据
* repeatable-read(可重复度)    事务只能读到当前事物范围内的数据，并以当前数据作为参考，其他事物就算更新了数据也不在当前事物的可见范围内，即当前事物不受其他事物影响，不想读到其他事务更改的结果
* serializable(串行)          事务与事务采用串行先后执行，即它们之间互不影响

## 锁
### 全局锁
### 表级锁
### 行级锁


## 优化

doc：https://dev.mysql.com/doc/refman/8.0/en/optimization.html

#### 索引

* 索引机制

   创建索引文件时维护了一个B+树，能更快的比较查询，定位到记录的位置

* 索引优劣
   * 极大提高查询速度
   * 由于增删改时需要维护索引文件，会增加开销，速度也会降低。

#### SQL查询优化

* 避免全表扫描，应考虑在 where 及 order by 经常涉及的列上建立索引；
* 查询时使用select明确指明所要查询的字段，避免使用select *的操作；
* SQL语句尽量大写，减少数据库在解析sql语句时会先转换成大写的过程；
* 避免在 where 子句中使用 != 或 <> 操作符，只有对以下操作符才能利用索引：<，<=，=，>，>=，BETWEEN，IN，以及某些时候的LIKE；
* 避免使用模糊查询，会导致全表扫描，若要提高效率，可以考虑全文检索；
* 遵循最左原则，在where子句有多个查询条件时，把创建了索引的字段放在前面；若多个字段经常一起作为条件，可为它们创建复合索引，且查询时字段的顺序与创建索引时的顺序保持一致(否则无法理由符合索引)；
* 能使用关联查询解决的尽量不要使用子查询；
* 能不使用关联查询的尽量不要使用关联查询；
* 不需要获取全表数据的时候，不要查询全表数据，使用LIMIT来限制数据；


#### 数据库优化

* 在进行表设计时，可适度增加冗余字段(反范式设计)，减少JOIN操作；
* 多字段表可以进行垂直分表优化，多数据表可以进行水平分表优化；
* 选择恰当的数据类型，如整型的选择；
* 对于强调快速读取又无需关心事务的操作，可以考虑使用MyISAM数据库引擎；
* 对频繁作为查询条件的字段创建索引；唯一性太差的字段(如性别)就算频繁地作为查询条件也不适合创建索引；更新非常频繁的字段不适合创建索引；
* 编写SQL时使用上面的方式对SQL语句进行优化；
* 使用慢查询工具找出效率低下的SQL语句进行优化；
* 构建缓存，减少数据库磁盘操作；
* 可以考虑结合使用内在型数据库，如Redis，进行混合存储。比如统计的冗余信息从mysql迁出到redis

## 存储过程

参考：https://blog.csdn.net/weixin_45970271/article/details/124180709

事先经过编译并存储在数据库中的一段SQL语句的集合。调用存储过程可以简化应用开发人员的很多工作，减少数据在数据库和应用服务器之间的传输，对于提高数据处理的效率是很有好处的。

**优点**

- 存储过程是通过处理封装在容易使用的单元中，简化了复杂的操作。

- 存储过程是通过处理封装在容易使用的单元中，简化了复杂的操作。
- 简化对变动的管理。如果表名、列名、或业务逻辑有了变化。只需要更改存储过程的代码。使用它的人不用更改自己的代码。

- 通常存储过程都是有助于提高应用程序的性能。当创建的存储过程被编译之后，就存储在数据库中。

  - 但是，MySQL实现的存储过程略有所不同。
  - MySQL存储过程是按需编译。在编译存储过程之后，MySQL将其放入缓存中。
  - MySQL为每个连接维护自己的存储过程高速缓存。如果应用程序在单个连接中多次使用存储过程，则使用编译版本，否则存储过程的工作方式类似于查询。

- 存储过程有助于减少应用程序和数据库服务器之间的流量。

  - 因为应运程序不必发送多个冗长的SQL语句，只用发送存储过程中的名称和参数即可。

- 存储过程度任何应用程序都是可重用的和透明的。存储过程将数据库接口暴露给所有的应用程序，以方便开发人员不必开发存储过程中已支持的功能。


- 存储的程序是安全的。数据库管理员是可以向访问数据库中存储过程的应用程序授予适当的权限，而不是向基础数据库表提供任何权限。

**缺点**

- 如果使用大量的存储过程，那么使用这些存储过程的每个连接的内存使用量将大大增加。
  - 此外，如果在存储过程中过度使用大量的逻辑操作，那么CPU的使用率也在增加，因为MySQL数据库最初的设计就侧重于高效的查询，而不是逻辑运算。

- 存储过程的构造使得开发具有了复杂的业务逻辑的存储过程变得困难。


- 很难调试存储过程。只有少数数据库管理系统允许调试存储过程。不幸的是，MySQL不提供调试存储过程的功能。


- 开发和维护存储过程都不容易。

  - 开发和维护存储过程通常需要一个不是所有应用程序开发人员拥有的专业技能。这可能导致应用程序开发和维护阶段的问题。

- 对数据库依赖程度较高，移值性差。

### 存储过程的基本语句格式

```mysql
DELIMITER $$

CREATE
    /*[DEFINER = { user | CURRENT_USER }]*/
    PROCEDURE 数据库名.存储过程名([in变量名 类型,out 参数 2，...])
    /*LANGUAGE SQL
    | [NOT] DETERMINISTIC
    | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
    | SQL SECURITY { DEFINER | INVOKER }
    | COMMENT 'string'*/
	BEGIN
		[DECLARE 变量名 类型 [DEFAULT 值];]
		存储过程的语句块;
	END$$

DELIMITER ;

```

存储过程中的参数分别是 in，out，inout三种类型；

- in代表输入参数（默认情况下为in参数），表示该参数的值必须由调用程序指定。

- ou代表输出参数，表示该参数的值经存储过程计算后，将out参数的计算结果返回给调用程序。
- inout代表即时输入参数，又是输出参数，表示该参数的值即可有调用程序制定，又可以将inout参数的计算结果返回给调用程序。

存储过程中的语句必须包含在BEGIN和END之间。

DECLARE中用来声明变量，变量默认赋值使用的DEFAULT，语句块中改变变量值，使用SET 变量=值；





