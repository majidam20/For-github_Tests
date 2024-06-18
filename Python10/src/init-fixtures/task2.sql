CREATE TABLE travelers (
    name TEXT PRIMARY KEY,
    age  INT  NOT NULL
);

INSERT INTO travelers VALUES
    ('Lisa',     30),
    ('Marta',    27),
    ('John',     32),
    ('Sam',      41),
    ('Alex',     12),
    ('Aristides',43),
    ('Cindi',     1)
    ;

CREATE TABLE guest_list (
    hotel TEXT NOT NULL,
    traveler TEXT NOT NULL REFERENCES travelers(name)
);

INSERT INTO guest_list VALUES
    ('Hotel Marigold', 'Lisa'),
    ('Hotel Marigold', 'Marta'),
    ('Hotel Marigold', 'John'),
    ('Hotel Sleep-well', 'Lisa'),
    ('Hotel Sleep-well', 'Marta'),
    ('Hotel Sleep-well', 'Alex'),
    ('Hotel Sleep-well', 'Sam'),
    ('Grand Hotel', 'Aristides'),
    ('Grand Hotel', 'John'),
    ('Grand Hotel', 'Cindi')
    ;

