CREATE TABLE hotels (
    hotel_id INT PRIMARY KEY,
    country TEXT NOT NULL
);

INSERT INTO hotels VALUES
    (5001,  'Germany'),
    (5002,  'United Kingdom'),
    (5003,  'Spain'),
    (5004,  'Spain'),
    (5005,  'Italy'),
    (5006,  'Austria');

CREATE TABLE clicks (
    advertiser_id INT,
    hotel_id INT NOT NULL REFERENCES hotels(hotel_id),
    number_clicks INT
);

INSERT INTO clicks VALUES
    (21, 5001,  100),
    (22, 5001,  50),
    (21, 5002,  20),
    (22, 5003,  10);

CREATE TABLE bookings (
    advertiser_id INT,
    hotel_id INT NOT NULL REFERENCES hotels(hotel_id),
    number_bookings INT
);

INSERT INTO bookings VALUES
    (21, 5001,  10),
    (22, 5001,  5),
    (21, 5002,  1),
    (23, 5005,  1);
