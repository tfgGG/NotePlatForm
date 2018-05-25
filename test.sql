-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- 主機: localhost
-- 產生時間： 2018-05-25 06:00:14
-- 伺服器版本: 5.7.17-log
-- PHP 版本： 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `test`
--

-- --------------------------------------------------------

--
-- 資料表結構 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add pet', 7, 'add_pet'),
(20, 'Can change pet', 7, 'change_pet'),
(21, 'Can delete pet', 7, 'delete_pet'),
(22, 'Can add profile', 8, 'add_profile'),
(23, 'Can change profile', 8, 'change_profile'),
(24, 'Can delete profile', 8, 'delete_profile'),
(25, 'Can add note', 9, 'add_note'),
(26, 'Can change note', 9, 'change_note'),
(27, 'Can delete note', 9, 'delete_note'),
(28, 'Can add notebook', 10, 'add_notebook'),
(29, 'Can change notebook', 10, 'change_notebook'),
(30, 'Can delete notebook', 10, 'delete_notebook'),
(31, 'Can add note list', 11, 'add_notelist'),
(32, 'Can change note list', 11, 'change_notelist'),
(33, 'Can delete note list', 11, 'delete_notelist');

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$3gKPQNXgF7Wq$C61YcUBA7YPBdQCxRm/CzH7RHjY1XriVTq4uqJmYS5A=', '2018-05-01 18:49:39.250932', 1, 'jessicahuang', '', '', 'jessicahuangtfg@gmail.com', 1, 1, '2018-04-27 11:42:56.099362'),
(2, 'pbkdf2_sha256$100000$ITmGfXiSQGnl$Qb5nkQW4dqX0Qlknn8mw0ngvKkO3AAXoMGKWxH93cZ4=', '2018-04-28 15:27:07.197678', 0, 'tim', '', '', 'timhuang@gmail.com', 0, 1, '2018-04-28 15:27:06.814788'),
(3, 'pbkdf2_sha256$100000$cZw5JrPtzHI1$qMXczryM2VU2kPSwybF5B1lqNu7Vj2mCjp/hTLlTuqc=', '2018-04-28 15:34:05.433075', 0, 'tfgGG', '', '', 'timhuang@gmail.com', 0, 1, '2018-04-28 15:34:05.058078'),
(4, 'pbkdf2_sha256$100000$CMr6ND9E8hle$xKM6e4Q6HBDahD6YD9PwNXC9VjdKUXSiOLMvOVBb62w=', '2018-04-28 15:46:01.829265', 0, 'hahaha', '', '', '1234567@gmail.com', 0, 1, '2018-04-28 15:46:01.434215'),
(5, 'pbkdf2_sha256$100000$mWruPb0rKpZB$EO8RjKDkd7uFH4fduiAKw4L0PzV74ejT3DEJdGVMYmQ=', '2018-05-02 06:13:21.562179', 0, 'haha', '', '', 'haha@gmail.com', 0, 1, '2018-04-28 15:47:07.782772'),
(7, 'pbkdf2_sha256$100000$qH3OgseRDPpI$2hIFGePeu5LWlliMpg/+lAlw2E1micov82pr5ecyu50=', NULL, 0, 'yes123', '', '', '', 0, 1, '2018-05-01 15:30:25.737817'),
(9, 'pbkdf2_sha256$100000$AzDgfaWY8KEF$vWYv1dlEH7nQJJrYNnWpWTRhfylRgjtc/RbE6IBO4lg=', '2018-05-01 16:34:50.182309', 0, 'yes12345', '', '', '', 0, 1, '2018-05-01 15:31:25.234615'),
(10, 'pbkdf2_sha256$100000$cR047ScOyqyY$6pMN68My1NrMikzofZtk+LTkf344yGDBS7riq/sYgxE=', '2018-05-01 17:21:26.697482', 0, 'yeh', '', '', 'tim@gmail.com', 0, 1, '2018-05-01 17:06:41.445898'),
(11, 'pbkdf2_sha256$100000$rZSRbeUsdbQR$c7UNW0QHLeN9NxarKnZXave7bL/qXghnK2Ihhbi7maI=', NULL, 0, 'yyyyy', '', '', 'jes@gmail.com', 0, 1, '2018-05-01 17:22:30.184098'),
(13, 'pbkdf2_sha256$100000$flXhlVsKfRMl$kNf3W4cY5KDz52KYdOdZYAOU9cvF4MG/N3G3PC37wo8=', '2018-05-01 18:00:53.802617', 0, 'ttttt', '', '', 'kkk@gmail.com', 0, 1, '2018-05-01 17:57:37.268381'),
(14, 'pbkdf2_sha256$100000$jVEVUTsmDqmU$HhaLjz3YXRmCyAUV8x9qHgtc0JbcXBxZ1m0FFBwqWEk=', '2018-05-01 18:01:41.151936', 0, 'uuu', '', '', 'jessicahuangtf@gmail.com', 0, 1, '2018-05-01 18:01:27.482738'),
(15, 'pbkdf2_sha256$100000$5PLelHTT9SAw$ZPpXh7BXB7t8gkN33m7Ej1aEb9D5KaiER0Xcntnpnak=', '2018-05-01 18:06:26.436833', 0, 'qq', '', '', 'iu@gmail.com', 0, 1, '2018-05-01 18:06:17.426611'),
(16, 'pbkdf2_sha256$100000$jM3FN3sVsTsC$MAQAtaECD0vNFFaJSHG1LfM2UXziIU5tVOgPA7Zp9sw=', NULL, 0, 'oo', '', '', 'iuss@gmail.com', 0, 1, '2018-05-01 18:08:46.402688'),
(18, 'pbkdf2_sha256$100000$eCqPl5eA5mZK$K2NCVE0PFWThr1QLx4Gp3F4aWCfrWikvgglGeEknXhI=', NULL, 0, 'qqww', '', '', 'asdadiu@gmail.com', 0, 1, '2018-05-01 18:10:15.364522'),
(19, 'pbkdf2_sha256$100000$xRoAd9jDQgac$Ke9so94JRH1xh5CXap4AcC0Bq1P7qwH16qwHM07GqTc=', '2018-05-01 18:22:09.823263', 0, 'qqwww', '', '', 'asdassssdiu@gmail.com', 0, 1, '2018-05-01 18:15:50.644501'),
(20, 'pbkdf2_sha256$100000$1Vat9TsJguzz$hqJLfYZPDecdKOupRK2y08B6CHHBXsTtmtQH2CAEHl0=', NULL, 0, 'pp', '', '', 'kkkkk@gmail.com', 0, 1, '2018-05-01 18:22:57.394724'),
(21, 'pbkdf2_sha256$100000$gvOES0VNNPj8$pjkMCuFgUmQmlnQC6g29v6vccxhUy5iUvizejt22/Ww=', NULL, 0, '4455', '', '', 'gweo@gmail.com', 0, 1, '2018-05-01 18:42:44.222264'),
(22, 'pbkdf2_sha256$100000$jvd2lAGpTggq$K5XVavNJIYR2QdP46cpuSxi4lOw53z+BKzbEtUJkdwY=', '2018-05-01 18:45:00.460581', 0, 'bbc', '', '', 'reeslkdg@gmail.com', 0, 1, '2018-05-01 18:44:51.352758'),
(23, 'pbkdf2_sha256$100000$weBuSGIDpkpm$FpmimE/orwbOm6PhZcN8vbCe5CIACzGqGcZTrXHht+k=', '2018-05-01 18:53:07.377644', 0, 'fff', '', '', 'ghxdgh@gmail.vom', 0, 1, '2018-05-01 18:52:56.279816'),
(24, 'pbkdf2_sha256$100000$06Et0mnZVtF5$la5a2zQpDmt0w048nmLI1SCm1BDLNs1kK+ggdRLGR68=', NULL, 0, 'lll', '', '', 'sdvmdvdv@gmail.com', 0, 1, '2018-05-01 19:01:17.895458'),
(25, 'pbkdf2_sha256$100000$q8u4exkkEX1c$QogetfSQNHJFoEb1qu6m+4Fx24zOOe5rlugBPT4PoQU=', NULL, 0, 'lllll', '', '', 'sdvmwwdvdv@gmail.com', 0, 1, '2018-05-01 19:02:59.249675'),
(26, 'pbkdf2_sha256$100000$jmbxj5QppWsG$B9L1klR9wKRIRFarPcvKC5+LkequgxzJ61Fo3d96DzU=', '2018-05-07 05:47:06.103928', 0, 'aaaaa', '', '', 'p@gmaul.com', 0, 1, '2018-05-01 19:07:29.225124'),
(33, 'pbkdf2_sha256$100000$Jb2zTHVzGdBR$QBfx4CtU99TdhnPBTfcZt4JgDzfo8QW3Po/dXm/sSwI=', NULL, 0, 'bbb', '', '', 'iwuy@gmail.com', 0, 1, '2018-05-01 19:31:56.693821'),
(34, 'pbkdf2_sha256$100000$K5X2D1WuD7f6$Oh0TbPf3RJidAiCmEzjo/mWTYyXPkeo/kgVBTglu2eA=', '2018-05-01 19:54:27.494832', 0, 'bbbbb', '', '', 'iwwwwuy@gmail.com', 0, 1, '2018-05-01 19:32:54.178024'),
(35, 'pbkdf2_sha256$100000$FNem592tQm4g$buWrMg5knCofuzTcbeSF9jjwh6NWj+3gP7r9LMbjqvQ=', '2018-05-01 19:59:41.434570', 0, 'yua', '', '', 'jkk@gmail.com', 0, 1, '2018-05-01 19:59:20.509570'),
(37, 'pbkdf2_sha256$100000$an4C7vYgNWpv$G26na4aBWUMZ4WZFMHyinYd40YTmKgid8+g/p8clxSY=', '2018-05-22 09:22:50.542467', 0, 'yyu', '', '', 'jesv@gmail.com', 0, 1, '2018-05-02 06:23:59.868067'),
(38, 'pbkdf2_sha256$100000$NN7bOBy0KSA2$7ebPq6TIBNHCuAWsl24vQxXbjGIYHpZs14iLPBYnlYI=', '2018-05-02 06:37:38.772226', 0, 'hh', '', '', 'jessicag@gmail.com', 0, 1, '2018-05-02 06:37:28.249270'),
(39, 'pbkdf2_sha256$100000$krQzyxsJcVJI$I1YBSAyZoCXbTjBWsvCcx5dlq6b/ez2Dt6PDQUrUoiU=', '2018-05-25 05:30:46.812769', 0, 'fred123', '', '', 'gfes980615@yahoo.com.tw', 0, 1, '2018-05-22 13:25:59.625019');

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'login', 'pet'),
(8, 'login', 'profile'),
(6, 'sessions', 'session'),
(9, 'upload', 'note'),
(10, 'upload', 'notebook'),
(11, 'upload', 'notelist');

-- --------------------------------------------------------

--
-- 資料表結構 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-04-24 08:13:16.410320'),
(2, 'auth', '0001_initial', '2018-04-24 08:13:17.274110'),
(3, 'admin', '0001_initial', '2018-04-24 08:13:17.491689'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-04-24 08:13:17.509737'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-04-24 08:13:17.629054'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-04-24 08:13:17.714282'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-04-24 08:13:17.801513'),
(8, 'auth', '0004_alter_user_username_opts', '2018-04-24 08:13:17.819561'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-04-24 08:13:17.897268'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-04-24 08:13:17.904786'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-04-24 08:13:17.924340'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-04-24 08:13:18.083263'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-04-24 08:13:18.161470'),
(14, 'sessions', '0001_initial', '2018-04-24 08:13:18.217118'),
(19, 'login', '0001_initial', '2018-05-01 13:16:19.713138'),
(20, 'login', '0002_auto_20180522_2237', '2018-05-22 14:37:21.946393'),
(21, 'upload', '0001_initial', '2018-05-22 14:37:22.036393');

-- --------------------------------------------------------

--
-- 資料表結構 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('174aq7x1pxkn11x9vl5bsx6k2eluyka7', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 18:49:05.513258'),
('1t410sii4fg8miuv8gqwybywwzf0o9dd', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 15:32:41.626459'),
('6o12gt9beu3p4c36s892jm5ejy0t3d02', 'Y2UyZWE0N2JjNDkyYWFmMTAxMTYwYzMwYmI0ZDY4ZjQ3MjNjZDQ1MDp7Il9hdXRoX3VzZXJfaWQiOiIzNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzg1ZGE1ODhiZmZjMTdmOWEwNTEzNGIyOWUwMTg3YWQwMjExYTI0MSJ9', '2018-06-05 09:22:50.549390'),
('7b6ze6i98yaepkpjqm33dg20pigjzpwm', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 13:52:22.357513'),
('b6gl4r53062j60e81evibl2c6rtwfpjz', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-12 15:34:05.428064'),
('cpwg3774ccdluji3hc007fkue4gw8vdl', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 14:18:16.147795'),
('do7fyr9x11fzqge0e0zdrjlzgditsbet', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 17:20:44.367859'),
('gofjfj8frgns0hjdyaglqsd5t070ct9p', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 18:48:12.580059'),
('idzx456hpopfmd5gstnliwzrntw9zy6m', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 18:01:41.147928'),
('iokt3t6f857z94ckesuc7sn4e5lr927d', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 18:45:00.456565'),
('kugaepc1513ox485wsjouhbhxezbsn7u', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 15:32:21.296049'),
('l3eetxuazyy7bfb6c89fh1fbwyg0s0zm', 'MDJhOWM2ZTBhY2E5YzQzMTg0MjMwZmFmMzRlZmM3MjQ2YTlhZWIzZTp7Il9hdXRoX3VzZXJfaWQiOiIzOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjA1NjVkYTk4NWRhZTZiYzI0NWJhOTBkMzdhNGUxN2QzNDQ3YzdjMyJ9', '2018-06-08 05:30:47.074784'),
('nuf8ki09dq3vl7ibbsmawmo4zbb0ns4b', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 18:00:53.797605'),
('o7ih56ggi0g9bbforpq1xdwn5qz8pnu3', 'Y2UyZWE0N2JjNDkyYWFmMTAxMTYwYzMwYmI0ZDY4ZjQ3MjNjZDQ1MDp7Il9hdXRoX3VzZXJfaWQiOiIzNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzg1ZGE1ODhiZmZjMTdmOWEwNTEzNGIyOWUwMTg3YWQwMjExYTI0MSJ9', '2018-06-03 05:37:22.531483'),
('tai2e31e9abtdqjwlfox35ja2onfxxqv', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 15:32:56.265771'),
('yvla9int7sja3tlxdjrpav6y6yxufgno', 'YTM0ZWMxZWY1ZGVhY2NkMWU0NmE1YmM0MDU1ZjEyOWM3NTViNWE2OTp7fQ==', '2018-05-15 18:06:26.431787');

-- --------------------------------------------------------

--
-- 資料表結構 `note`
--

CREATE TABLE `note` (
  `idnote` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `field` varchar(10) NOT NULL,
  `subjects` varchar(10) NOT NULL,
  `textbook` varchar(10) NOT NULL,
  `intro` varchar(45) DEFAULT NULL,
  `permission` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `note`
--

INSERT INTO `note` (`idnote`, `user_id`, `title`, `field`, `subjects`, `textbook`, `intro`, `permission`) VALUES
(1, 37, 'this is title', '', '', '', 'sefknaslkefnQLEFKN\\nawdawd', 0),
(2, 38, 'dfv', '', '', '', 'cv SDfkNSALKGVnSLDK', 0),
(3, NULL, '', '', '', '', '', 1),
(4, 1, 'ayht', 'aya', '國文', '6', '微分 積分', 1),
(5, 1, '國文作業', '語文', '國文', '6', '微分 積分', 0);

-- --------------------------------------------------------

--
-- 資料表結構 `notebook`
--

CREATE TABLE `notebook` (
  `id` int(11) NOT NULL DEFAULT '0' COMMENT ' ',
  `field` varchar(10) NOT NULL,
  `subjects` varchar(10) NOT NULL,
  `textbook` varchar(10) NOT NULL,
  `introduction` text NOT NULL,
  `permission` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `notebook`
--

INSERT INTO `notebook` (`id`, `field`, `subjects`, `textbook`, `introduction`, `permission`) VALUES
(0, 'language', 'chinese', 'book', 'english', 1),
(1, '', '', '', '', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `note_list`
--

CREATE TABLE `note_list` (
  `idnote_list` int(10) UNSIGNED NOT NULL,
  `list_text` varchar(45) DEFAULT NULL,
  `list_num` int(10) UNSIGNED DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  `noteid` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `note_list`
--

INSERT INTO `note_list` (`idnote_list`, `list_text`, `list_num`, `note`, `noteid`) VALUES
(59, 'gfnsrgn', 1, 'gggggggggggggg', 2),
(60, 'This is  a', 2, 'gnsrtnrw', 2),
(61, 'This is  b', 3, 'fghmdgfymdf', 2),
(62, 'This is  c', 4, 'yh', 2),
(63, 'This is d', 5, 'sfgngnsrfgnsfgn**bold**', 2),
(64, 'this is e', 6, 'sfbetbwet', 2),
(89, '3f23', 1, '23r23r23\r\n23r23r23r23r', 1),
(90, 'dgdg', 2, 'fehtgh', 1),
(91, 'this is seven', 3, 'awdawdfnklsKDV\r\nasLdejfbLAWEKF\r\nSZLKNGSKLE', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `pet`
--

CREATE TABLE `pet` (
  `name` varchar(20) DEFAULT NULL,
  `owner` varchar(20) DEFAULT NULL,
  `species` varchar(20) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `death` date DEFAULT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `pet`
--

INSERT INTO `pet` (`name`, `owner`, `species`, `sex`, `birth`, `death`, `ID`) VALUES
('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL, 1),
('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', NULL, 2),
('Claws', 'Gwen', 'cat', 'm', '1994-03-17', NULL, 3),
('Buffy', 'Harold', 'dog', 'f', '1989-05-13', NULL, 4),
('Fang', 'Benny', 'dog', 'm', '1990-08-27', NULL, 5),
('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29', 6),
('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', NULL, 7),
('Whistle', 'Gwen', 'bird', NULL, '1997-12-09', NULL, 8),
('Slim', 'Benny', 'snake', 'm', '1996-04-29', NULL, 9),
('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', '0000-00-00', 10);

-- --------------------------------------------------------

--
-- 資料表結構 `polls_document`
--

CREATE TABLE `polls_document` (
  `iddoc` int(11) NOT NULL,
  `notelistid` int(10) UNSIGNED DEFAULT NULL,
  `document` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `polls_document`
--

INSERT INTO `polls_document` (`iddoc`, `notelistid`, `document`, `uploaded_at`) VALUES
(1, 90, 'document/1s.png', '2018-05-05 17:28:29.677853');

-- --------------------------------------------------------

--
-- 資料表結構 `profile`
--

CREATE TABLE `profile` (
  `idProfile` int(10) UNSIGNED NOT NULL,
  `school` varchar(20) DEFAULT NULL,
  `grade` int(11) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `intro` longtext,
  `user_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `profile`
--

INSERT INTO `profile` (`idProfile`, `school`, `grade`, `birth`, `intro`, `user_id`) VALUES
(1, 'SEfd', 2, '2018-04-27', 'dsvsdv', 1),
(27, 'sdfbnk', 2, '2017-08-07', 'aefnabemr;bl\r\naefnba ;emrlbm', 32),
(28, 'sfnlk', 2, '2017-08-07', 'safbwm;rlbm\r\nSDFb L:SDKFBN:F\r\n;SKLMNfb', 33),
(29, 'sfnlk', 2, '2017-08-07', 'safbwm;rlbm\r\nSDFb L:SDKFBN:F\r\n;SKLMNfb', 34),
(30, '輔仁大學', 3, '1997-04-14', 'HI ,IM FROM fjcu', 35),
(31, 'ererc', 2, '2014-08-07', 'dfsbdaerb df \r\nasf asfb', 37),
(32, 'SCWQED', 2, '2014-08-07', 'EFVERB', 38),
(33, 'fju', 3, NULL, 'hi', 39);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 資料表索引 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- 資料表索引 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- 資料表索引 `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- 資料表索引 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- 資料表索引 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- 資料表索引 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- 資料表索引 `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- 資料表索引 `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- 資料表索引 `note`
--
ALTER TABLE `note`
  ADD PRIMARY KEY (`idnote`),
  ADD KEY `user_note_idx` (`user_id`);

--
-- 資料表索引 `notebook`
--
ALTER TABLE `notebook`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`);

--
-- 資料表索引 `note_list`
--
ALTER TABLE `note_list`
  ADD PRIMARY KEY (`idnote_list`),
  ADD KEY `notelist_note_idx` (`noteid`);

--
-- 資料表索引 `pet`
--
ALTER TABLE `pet`
  ADD PRIMARY KEY (`ID`);

--
-- 資料表索引 `polls_document`
--
ALTER TABLE `polls_document`
  ADD PRIMARY KEY (`iddoc`),
  ADD KEY `notelistid_pic_idx` (`notelistid`);

--
-- 資料表索引 `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`idProfile`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
--
-- 使用資料表 AUTO_INCREMENT `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- 使用資料表 AUTO_INCREMENT `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- 使用資料表 AUTO_INCREMENT `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- 使用資料表 AUTO_INCREMENT `note`
--
ALTER TABLE `note`
  MODIFY `idnote` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用資料表 AUTO_INCREMENT `note_list`
--
ALTER TABLE `note_list`
  MODIFY `idnote_list` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;
--
-- 使用資料表 AUTO_INCREMENT `pet`
--
ALTER TABLE `pet`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- 使用資料表 AUTO_INCREMENT `profile`
--
ALTER TABLE `profile`
  MODIFY `idProfile` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
--
-- 已匯出資料表的限制(Constraint)
--

--
-- 資料表的 Constraints `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 資料表的 Constraints `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 資料表的 Constraints `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的 Constraints `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的 Constraints `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的 Constraints `note`
--
ALTER TABLE `note`
  ADD CONSTRAINT `user_note` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- 資料表的 Constraints `note_list`
--
ALTER TABLE `note_list`
  ADD CONSTRAINT `notelist_note` FOREIGN KEY (`noteid`) REFERENCES `note` (`idnote`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- 資料表的 Constraints `polls_document`
--
ALTER TABLE `polls_document`
  ADD CONSTRAINT `notelistid_pic` FOREIGN KEY (`notelistid`) REFERENCES `note_list` (`idnote_list`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
