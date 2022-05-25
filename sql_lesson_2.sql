-- Задание 1
-- MySQL - установка +
-- my.ini в C:\Program Files\MySQL\MySQL Server 8.0

/* Задание 2
Создайте базу данных example, 
разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
*/ 
-- создание новой БД
create database example;
-- переключение на БД
use example;
-- создание таблицы
create table users(Id INT(5) COMMENT 'ID',User CHAR(20) COMMENT 'User');
-- вывод результата
describe users;


/* Задание 3
Создайте дамп базы данных example из предыдущего задания, 
разверните содержимое дампа в новую базу данных sample.
*/ 
-- создание новой БД в которую будет копироваться example
create database sample;
-- создание дампа в cmd
\! mysqldump example > example.sql
-- разворот в другую БД
\! mysql sample < example.sql

/* Задание 4
(по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. 
Создайте дамп единственной таблицы help_keyword базы данных mysql. 
Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/ 

\! mysqldump mysql help_keyword --where="true limit 100" > mysql_100.sql
-- копирование в новую БД
\! mysql mysql_100 < mysql_100.sql
-- вывод таблицы
describe help_keyword;

/*не смог разобраться: из под администратора в командной строке windows mysqldump работает, 
из под командной строки mysql выдает отказ в доступе... соответственно и высвечивает ошибку в Workbench  */