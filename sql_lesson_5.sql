-- 
-- Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение”

-- Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.

-- если считать что данные поля существуют, то:  
UPDATE users SET created_at = NOW(), update_at = NOW();

-- Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.

ALTER TABLE users MODIFY COLUMN created_at datetime; 
ALTER TABLE users MODIFY COLUMN update_at datetime;

-- В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
-- 
SELECT * FROM storehouses_products  WHERE value>0 ORDER BY value
UNION 
SELECT * FROM storehouses_products  WHERE value=0;

-- (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий ('may', 'august')

SELECT * FROM users WHERE birthday LIKE '%may%' OR birthday LIKE '%august%'

-- (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
-- 
SELECT * FROM catalogs WHERE id=5
UNION 
SELECT * FROM catalogs WHERE id=1
UNION 
SELECT * FROM catalogs WHERE id=2





-- Практическое задание теме “Агрегация данных”
-- Подсчитайте средний возраст пользователей в таблице users

SELECT SUM(YEAR(now())-YEAR(birthday))/COUNT(birthday)  FROM users; -- variant 1

SELECT SUM(DATEDIFF(now(),birthday)/365,25)/COUNT(birthday)  FROM users; -- variant 2

-- Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.

-- SELECT COUNT(*)  FROM users GROUP BY DAYNAME(birthday); -- это по дате рождения

SELECT COUNT(*) FROM users GROUP BY DAYNAME(MAKEDATE(YEAR(NOW()),DAYOFYEAR(birthday))) ; 


-- (по желанию) Подсчитайте произведение чисел в столбце таблицы
-- 
SELECT EXP(SUM(LOG(pole))) FROM tabl -- произведение чисел в столбце "pole" таблицы tabl





