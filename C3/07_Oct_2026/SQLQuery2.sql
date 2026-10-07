CREATE DATABASE PRODUCT;
SELECT name FROM sys.tables;
USE PRODUCT;
GO
EXEC sp_rename 'Superstore','store';
SELECT *FROM store;
SELECT* FROM store WHERE Category = 'kurta';

SELECT Category ,SUM(Amount) As sales FROM store GROUP BY Category  ;
SELECT COUNT(*) As TOTAL_ROW FROM store ;

SELECT DISTINCT ship_country As state FROM store;