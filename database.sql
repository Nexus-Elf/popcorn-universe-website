-- Create a new database called 'UserAccounts'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'UserAccounts'
)
CREATE DATABASE UserAccounts
GO

-- Add a new column 'premiumuser' to table 'TableName' in schema 'Premium'
ALTER TABLE Premium.UserAccounts
    ADD PremiumUser /*new_column_name*/ int /*new_column_datatype*/ NULL /*new_column_nullability*/
GO
/* Trey = Premium */ 

CREATE TABLE
-- Create a new table called 'UserAccounts' in schema 'Premium'
-- Drop the table if it already exists
IF OBJECT_ID('Premium.UserAccounts', 'U') IS NOT NULL
DROP TABLE Premium.UserAccounts
GO
-- Create the table in the specified schema
CREATE TABLE Premium.UserAccounts
(
    UserAccountsId INT NOT NULL PRIMARY KEY, -- primary key column
    Column1 [NVARCHAR](50) NOT NULL,
    Column2 [NVARCHAR](50) NOT NULL
    -- specify more columns here
);
