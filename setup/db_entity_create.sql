---User table---
CREATE TABLE Users
(
ID SERIAL PRIMARY KEY,
LastName varchar(255),
FirstName varchar(255) NOT NULL,
Phone varchar(15),
Password varchar(255)
);

--- Address Type like HOME, WORD etc ---
CREATE TABLE AddressType
(
ID SERIAL PRIMARY KEY,
Lable varchar(255) UNIQUE NOT NULL
);

--- Address table ---
CREATE TABLE Address
(
UID int REFERENCES Users(ID) ON DELETE RESTRICT,
AID int REFERENCES AddressType(ID) ON DELETE RESTRICT,
HouseNo varchar(255),
Street varchar(255),
City varchar(255),
State varchar(255),
Country varchar(255),
Pin varchar(255) UNIQUE NOT NULL,
AreaCode varchar(255) UNIQUE NOT NULL,
PRIMARY KEY(UID, AID)
);

--- Service ---
CREATE TABLE Service
(
ID SERIAL PRIMARY KEY,
Name varchar(255) UNIQUE NOT NULL,
Key varchar(255) UNIQUE NOT NULL,
Category varchar(255)
);

--- Service provider table that shopkeers ---
CREATE TABLE ServiceProvider
(
UID int,
SID int,
PRIMARY KEY(UID, SID)
);

--- Status discription In progress, Done, Canceled etc ---
CREATE TABLE Status
(
ID SERIAL PRIMARY KEY,
LABLE varchar(255) UNIQUE NOT NULL
);

--- Order table---
CREATE TABLE Orders
(
ID SERIAL PRIMARY KEY,
UID int REFERENCES Users(ID),
SID int REFERENCES Service(ID) ON DELETE RESTRICT,
WhenTo TIMESTAMP WITH TIME ZONE,
WhenFrom TIMESTAMP WITH TIME ZONE,
AID int,
StatusID int REFERENCES Status(ID),
CONSTRAINT AID FOREIGN KEY(UID, AID)
REFERENCES Address(UID,AID)
);