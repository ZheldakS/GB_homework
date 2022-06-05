
-- i. Заполнить все таблицы БД vk данными (не больше 10-20 записей в каждой таблице)


-- ii. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке
SELECT DISTINCT firstname FROM users ORDER BY firstname ; 

-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)

ALTER TABLE vk.profiles ADD is_activ ENUM('false','true') NOT NULL DEFAULT 'True';
UPDATE vk.profiles SET is_activ = 'false' WHERE unix_timestamp(NOW()) - unix_timestamp(birthday) <= 504921600; -- 504921600 это 16 лет в секундах :)
 

-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
DELETE FROM messages WHERE now() - created_at < 0;