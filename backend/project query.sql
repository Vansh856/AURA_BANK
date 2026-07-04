CREATE DATABASE AuraBank;
USE AuraBank;
CREATE TABLE UserLogin(
	UserId INT PRIMARY KEY IDENTITY(1,1),
	UserName VARCHAR(100) UNIQUE,
	Balance INT DEFAULT 1000,);
SELECT * FROM UserLogin;

ALTER TABLE UserLogin ADD Password VARCHAR(225);

-- creating table to track login attempts

CREATE TABLE login_attempts_audit (
    
    attempt_id INT IDENTITY(1,1) PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL, 
    attempt_time DATETIME DEFAULT GETDATE(), 
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (UserName) REFERENCES UserLogin(UserName)
);

--creating table to track users economy

CREATE TABLE UserEconomy (
    EconomyID INT PRIMARY KEY IDENTITY(1,1),
    UserName VARCHAR(100) NOT NULL,
    AuraScore INT DEFAULT 750,
    AuraPoints INT DEFAULT 1000,
    CardTier VARCHAR(20) DEFAULT 'Bronze',
    FOREIGN KEY (UserName) REFERENCES UserLogin(UserName)
);