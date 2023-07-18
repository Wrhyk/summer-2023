DROP TABLE IF EXISTS [users]

CREATE TABLE [users] (
    nickname VARCHAR(45) NOT NULL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    password CHAR(60) NOT NULL
);


DROP TABLE IF EXISTS[fish]

CREATE TABLE [fish] (
    fish_id INT PRIMARY KEY,
    fish_type VARCHAR(60) NOT NULL,
    f_weight VARCHAR(20) NOT NULL,
    f_length INT NOT NULL,
    x_location DECIMAL(30) NOT NULL,
    y_location DECIMAL(30) NOT NULL,
    nickname varchar(45) NOT NULL,
    FOREIGN KEY (nickname) REFERENCES users (nickname),
    FOREIGN KEY (fish_type) REFERENCES fish_types (fish_type)
);

DROP TABLE IF EXISTS [basket]

CREATE TABLE [basket] (
    nickname VARCHAR(45) NOT NULL PRIMARY KEY,
    fish_id INT,
    FOREIGN KEY (nickname) REFERENCES users (nickname),
    FOREIGN KEY (fish_id) REFERENCES fish (fish_id)
);

DROP TABLE IF EXISTS [fish_types]

CREATE TABLE [fish_types] (
    fish_type VARCHAR(70) PRIMARY KEY 
);

/* Found data on https://fiskeriforum.no/fiskearter-i-saltvann/ */
INSERT INTO [fish_types] (fish_types)
    VALUES 
    ('Lyr'),
    ('Torsk'),
    ('Sei'),
    ('Hyse'),
    ('Hvitting'),
    ('Kolmule'),
    ('Breiflabb'),
    ('Lange'),
    ('Brosme'),
    ('Gråsteinbit'),
    ('Rognkjeks'),
    ('Uer'),
    ('Berggylt'),
    ('Blaastaal'),
    ('Gronngylt'),
    ('Bergnebb'),
    ('Rodnebb'),
    ('Ulke'),
    ('Tangsprell'),
    ('Tangsnelle'),
    ('Tangstikling'),
    ('Kystringbuk'),
    ('Trepigget stingsild'),
    ('Brisling'),
    ('Lodde'),
    ('Sild'),
    ('Makrell'),
    ('orret'),
    ('Laks'),
    ('Rødspette'),
    ('Sandflyndre'),
    ('Lomre'),
    ('Skrubbe'),
    ('Piggskate'),
    ('Horngjel'),
    ('Fjesing'),
    ('Floyfisk'),
    ('Paddetorsk'),
    ('Havabbor'),
    ('St. Petersfisk'),
    ('Mulle'),
    ('Pigghaa'),
    ('Svarthaa'),
    ('Haagjel'),
    ('Håbrann'),
    ('Slimaal'),
    ('Laksesild'),
    ('Lysing'),
    ('Mora'),
    ('Havbrasme'),
    ('Brudefisk'),
    ('Vassild'),
    ('Skolest')
;