
--     Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем (написал ему сообщений).


SELECT from_user_id, COUNT(id) as count_m FROM messages WHERE to_user_id  = 5 GROUP BY from_user_id ORDER BY count_m DESC LIMIT 1;

-- честно говоря не получилось обработать полученную таблицу с from_user_id, COUNT(id) ли


--     Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

SELECT COUNT(id) FROM likes WHERE user_id IN (SELECT user_id  FROM profiles WHERE TIMESTAMPDIFF(year,birthday,now())<=10);


--     Определить кто больше поставил лайков (всего): мужчины или женщины.

SELECT 
	CASE 
		when (SELECT count(id) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f'))>
		(SELECT count(id) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm')) THEN 'female'
		when (SELECT count(id) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f'))<
		(SELECT count(id) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm')) THEN 'male'
	END
	AS 'more likes'
	

	

