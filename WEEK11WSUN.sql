CREATE DATABASE RetailDB;
USE RetailDB;
CREATE TABLE Sales (
    ProductName VARCHAR(100),
    Qty INT,
    Unit_Price DOUBLE,
    SaleDate DATETIME,
    CurrencyType VARCHAR(10),
    CustomerID VARCHAR(50),
    StoreID INT,
    Total_Price DOUBLE,
    Total_Price_OMR DOUBLE
);
DROP TABLE Sales;
CREATE TABLE Sales (
    ProductName VARCHAR(100),
    Qty INT,
    Unit_Price DOUBLE,
    SaleDate DATETIME,
    CurrencyType VARCHAR(10),
    CustomerID VARCHAR(50),
    StoreID VARCHAR(50),
    Total_Price DOUBLE,
    Total_Price_OMR DOUBLE
);
SELECT * FROM Sales LIMIT 10;
USE RetailDB;
SHOW TABLES;
CREATE TABLE Sales (
    ProductName VARCHAR(100),
    Qty INT,
    Unit_Price DOUBLE,
    SaleDate DATETIME,
    CurrencyType VARCHAR(10),
    CustomerID VARCHAR(50),
    StoreID VARCHAR(50),
    Total_Price DOUBLE,
    Total_Price_OMR DOUBLE
);
SHOW TABLES;
SELECT COUNT(*) FROM Sales;

