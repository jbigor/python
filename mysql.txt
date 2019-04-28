-- INSERT
use shop;
INSERT INTO `shop`.`category` (`name`, `discount`, `alias_name`) VALUES ('Женская Обувь', '10', '0');
INSERT INTO `shop`.`category` (`name`, `discount`, `alias_name`) VALUES ('Мужская Обувь', '15', '0');
INSERT INTO `shop`.`category` (`name`, `discount`, `alias_name`) VALUES ('Женская Одежда', '10', '0');
INSERT INTO `shop`.`category` (`name`, `discount`, `alias_name`) VALUES ('Мужская Одежда', '10', '0');


INSERT INTO shop.brand (name) VALUES ('Marco Polo');
INSERT INTO `shop`.`brand` (`name`) VALUES ('Allcott');
INSERT INTO `shop`.`brand` (`name`) VALUES ('Gesse');

use prodyct_type;
INSERT INTO `shop`.`prodyct_type` (`name`) values ('Женская одежда');
INSERT INTO `shop`.`prodyct_type` (`name`,`discount`) values ('Мужская одежда','5');


-- SELECT

select * from shop where id 3;
use shop;
CREATE TABLE `shop`.`product` ( id = inito(11)
 );
 

select * from category ;
select * from category where alias_name is null;
select discount from category;
select * from category order by discount;
select * from categorya order by dyscont desc;
use brand;
select * from shop where id 3;

-- UPDATE

update `shop`.`category` SET `name` = 'Головные уборы' where (`id` = '4');
UPDATE `shop`.`category` SET `alias_name` = 'man\'shoes' WHERE (`id` = '5');
UPDATE `shop`.`category` SET `discount` = 3 WHERE id =2 OR id = 5;
UPDATE `shop`.`category` SET `discount` = 2 WHERE id IN ( 2 , 5 );
delete from category where id = 5;

UPDATE `shop`.`category` SET `alias_name` = 'man\'shoes' WHERE (`id` = '4');
INSERT INTO `shop`.`category` (`id`,`name`, `discount`, `alias_name`) VALUES ('4','Женская Обувь', '15', '0');
INSERT INTO `shop`.`category` (`name`, `discount`, `alias_name`) VALUES ('Женская Обувь', '10', '0');
delete from category where id = 7;
update `shop`.`category` SET `alias_name` = 's couting' where id in ( 1, 2,3 );
UPDATE `shop`.`category` SET `alias_name` = 'man\'shoes' WHERE id in (1,2,3,4);

-- SELECT INNER JOIN

use shop;
select * from prodyct;
select * from category;
select * from category where id = 1 or id = 2  or id = 3;
select * from category where id => 1 and id <= 3;
select * from category where id IN (1,2,3);
select * from category
	inner join prodyct  on category_id = category.id;
select prodyct.id, price, name,discount,alias_name from category
	inner join prodyct  on category_id = category.id;

select * from category
	inner join prodyct  on category_id = category.id
    -- where price > 600;
    where discount > 0;

select * from prodyct
	inner join category on category_id = category.id
    inner join brand on brand.id = prodyct.brand_id;
    inner join prodyct_type on prodyct_type.id = category.prodyct_type_id;

Агрегирующии функции

SELECT * FROM shop.prodyct;

select count(*) from shop.prodyct;

use shop;

select count(*) from shop.prodyct 
	where prodyct.price < 100; 

select sum(price) as total_price, min(price) as min_price, max(price) as max_price from shop.prodyct;

Groop by

select *, price * `count` as total_price  from `order`
	inner join shop.order_product on shop.order_product.order_id = `order`.id
    inner join shop.prodyct on shop.prodyct.id = shop.prodyct.prodyct_id
    where `order`.id = 1;

insert into `shop`.`user_bank_account` (id, money, user_name) values ('1', '100', 'Р”РјРёС‚СЂРёР№');
insert into `shop`.`user_bank_account` (id, money, user_name) values ('2', '200', 'Р•РІРіРµРЅРёР№');

select * from `shop`.`user_bank_account`;

start transaction;
	update `shop`.`user_bank_account` set money = money - 100 where id = 1;
    update `shop`.`user_bank_account` set money = money + 100 where id = 2;
commit;

use shop;
select count(*) from shop.prodyct where prodyct.price < 100; 
select sum(price) as total_price, min(price) as min_price, max(price) as max_price from shop.prodyct;
use shop;
select *, price * `count` as total_price  from `order`
	inner join shop.order_product on shop.order_product.order_id = `order`.id
    inner join shop.prodyct on shop.prodyct.id = shop.prodyct.prodyct_id
    -- where user_name = 'Вася'
    where `order`.id = 1;


