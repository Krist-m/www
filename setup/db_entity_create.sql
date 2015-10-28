---User table---
CREATE TABLE Users
(
ID SERIAL PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255) NOT NULL,
Phone varchar(15) UNIQUE NOT NULL,
Password varchar(255) NOT NULL,
Photo bytea,
ServiceProvider BOOLEAN DEFAULT FALSE
);


--- Address table ---
CREATE TABLE Address
(
UID int REFERENCES Users(ID) ON DELETE RESTRICT,
AddLabel varchar(10),
HouseNo varchar(255),
Street varchar(255),
City varchar(255),
State varchar(255),
Country varchar(255),
Pin varchar(255) NOT NULL,
AreaCode varchar(255),
PRIMARY KEY(UID, AddLabel)
);

--- Service ---
CREATE TABLE Services
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
SID int REFERENCES Services(ID) ON DELETE RESTRICT,
Timefrom TIMESTAMP WITH TIME ZONE,
AID varchar(255),
StatusID int REFERENCES Status(ID)
);