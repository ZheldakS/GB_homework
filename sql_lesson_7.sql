
-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

select * from users where id in (SELECT user_id from orders)


-- Выведите список товаров products и разделов catalogs, который соответствует товару.

select products.id, products.name, products.description, products.price, catalogs.name as catalog_group from products join catalogs where products.catalog_id = catalogs.id 




-- (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.

select flights.id, tb1.name, tb2.name  from flights join cities as tb1 on flights.from_=tb1.label join cities as tb2 on flights.to_=tb2.label ORDER by flights.id 