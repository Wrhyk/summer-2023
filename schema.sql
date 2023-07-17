DROP TABLE IF EXISTS [users]

CREATE TABLE [users] (
    nickname VARCHAR(45) NOT NULL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    password CHAR(60) NOT NULL,
    fish_id INT,
    FOREIGN KEY ("fish_id") REFERENCES fish (fish_id)
);


DROP TABLE IF EXISTS[fish]

CREATE TABLE [fish] (
    fish_id INT NOT NULL PRIMARY KEY,
    fish_type VARCHAR(60) NOT NULL,
    size VARCHAR(20) NOT NULL,
    x_location DECIMAL(30) NOT NULL,
    y_location DECIMAL(30) NOT NULL,
    nickname varchar(45) NOT NULL,
    FOREIGN KEY (nickname) REFERENCES users (nickname)
);
