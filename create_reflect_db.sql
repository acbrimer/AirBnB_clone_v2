-- Template database for AirBnB v2 table structure
-- Used to create a "dummy" instance of the AirBnB database to reflect using ./reflect_db.py
DROP DATABASE IF EXISTS `hbtn_airbnb_reflect`;
CREATE DATABASE `hbtn_airbnb_reflect`;
USE `hbtn_airbnb_reflect`;
CREATE TABLE states (
	id varchar(60) PRIMARY KEY
	, name varchar(128) NOT NULL 
);

CREATE TABLE cities (
	id varchar(60) PRIMARY KEY
	, name varchar(128) NOT NULL
	, state_id varchar(60) NOT NULL
	, CONSTRAINT FK_cities__state FOREIGN KEY (state_id)
		REFERENCES states(id)
);

CREATE TABLE users (
	id varchar(60) PRIMARY KEY
	, email varchar(128) NOT NULL 
	, password varchar(128) NOT NULL
	, first_name varchar(128) NULL
	, last_name varchar(128) NULL
);

CREATE TABLE places (
	id varchar(60) PRIMARY KEY
	, city_id varchar(60) NOT NULL
	, user_id varchar(60) NOT NULL
	, name varchar(128) NOT NULL
	, description varchar(1024) NULL
	, number_rooms int NOT NULL DEFAULT 0
	, number_bathrooms int NOT NULL DEFAULT 0
	, max_guests int NOT NULL DEFAULT 0
	, price_by_night int NOT NULL DEFAULT 0
	, latitude float NULL
	, longitude float NULL
	, CONSTRAINT FK_place__city FOREIGN KEY (city_id)
		REFERENCES cities(id)
	, CONSTRAINT FK_place__user FOREIGN KEY (user_id)
		REFERENCES users(id)
);

CREATE TABLE reviews (
	id varchar(60) PRIMARY KEY
	, place_id varchar(60) NOT NULL
	, user_id varchar(60) NOT NULL
	, CONSTRAINT FK_reviews__places FOREIGN KEY (place_id)
		REFERENCES places(id)
	, CONSTRAINT FK_reviews__users FOREIGN KEY (user_id)
		REFERENCES users(id)
);

CREATE TABLE amenities (
	id varchar(60) PRIMARY KEY
	, name varchar(128) NOT NULL
);

CREATE TABLE place_amenity (
	place_id varchar(60) NOT NULL
	, amenity_id varchar(60) NOT NULL
	, CONSTRAINT FK_place_amenity__place FOREIGN KEY (place_id)
		REFERENCES places(id)
	, CONSTRAINT FK_place_amenity__ameity FOREIGN KEY (amenity_id)
		REFERENCES amenities(id)
);