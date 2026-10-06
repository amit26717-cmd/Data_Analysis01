CREATE DATABASE Amit;
CREATE TABLE Customer(
Customer_id INT,
Customer_Name Varchar(50),
Customer_City Varchar(50),
Customer_Category Varchar(50),
);
SELECT * FROM Customer;
INSERT INTO Customer Values
(1024 , 'Amit' , 'Jaunpur' , 'Electronics'),
(1023,'Himesh','Jaunpur','Furniture'),
(1025,'Ayush','Varanashi','Clothes'),

(1001, 'Rohit', 'Prayagraj', 'Electronics'),
(1002, 'Suresh', 'Varanasi', 'Furniture'),
(1003, 'Pooja', 'Lucknow', 'Clothes'),
(1004, 'Sneha', 'Kanpur', 'Books'),
(1010, 'Anjali', 'Mirzapur', 'Grocery'),
(1005, 'Vikas', 'Jaunpur', 'Grocery'),
(1006, 'Anil', 'Gorakhpur', 'Footwear'),
(1007, 'Deepak', 'Mirzapur', 'Electronics'),
(1008, 'Kavita', 'Azamgarh', 'Clothes'),
(1009, 'Manish', 'Ballia', 'Furniture'),
(1010, 'Ritu', 'Agra', 'Books'),
(1011, 'Sandeep', 'Prayagraj', 'Grocery'),
(1012, 'Neelam', 'Varanasi', 'Footwear'),
(1013, 'Rajesh', 'Lucknow', 'Electronics'),
(1014, 'Shweta', 'Kanpur', 'Clothes'),
(1015, 'Mohit', 'Jaunpur', 'Furniture'),
(1016, 'Pankaj', 'Gorakhpur', 'Books'),
(1017, 'Anjali', 'Mirzapur', 'Grocery'),
(1007, 'Anjali', 'Mirzapur', 'Grocery'),
(1018, 'Tarun', 'Azamgarh', 'Electronics'),
(1019, 'Divya', 'Ballia', 'Footwear'),
(1020, 'Gaurav', 'Agra', 'Clothes');


SELECT TOP 2 Customer_Name , Customer_City
FROM Customer
WHERE Customer_Name LIKE 'A%'
ORDER BY Customer_Name;

SELECT Customer_ID, Customer_Name, Customer_City, Customer_Category, COUNT(*) AS Total
FROM Customer
GROUP BY Customer_ID, Customer_Name, Customer_City, Customer_Category
HAVING COUNT(*) > 1;

SELECT * INTO Customers_Backup FROM Customer;
SELECT *FROM Customers_Backup

SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY Customer_ID, Customer_Name, Customer_City, Customer_Category ORDER BY (SELECT NULL)) AS RowNum
    FROM Customer
) AS T
WHERE RowNum > 1;

WITH CTE AS (
    SELECT ROW_NUMBER() OVER (PARTITION BY Customer_ID, Customer_Name, Customer_City, Customer_Category ORDER BY (SELECT NULL)) AS RowNum
    FROM Customer
)
DELETE FROM CTE WHERE RowNum > 1;