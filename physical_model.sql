CREATE DATABASE db_music;
USE db_music;

CREATE TABLE tb_artists (
    art_id INT AUTO_INCREMENT PRIMARY KEY,
    art_name VARCHAR(255) NOT NULL,
    art_bio TEXT,
    art_country VARCHAR(50)
);

CREATE TABLE tb_genres (
    gen_id INT AUTO_INCREMENT PRIMARY KEY,
    gen_name VARCHAR(50) NOT NULL
);tb_albums

CREATE TABLE tb_albums (
    alb_id INT AUTO_INCREMENT PRIMARY KEY,
    alb_name VARCHAR(255) NOT NULL,
    alb_release_year YEAR,
    alb_art_id INT NOT NULL,
    alb_gen_id INT NOT NULL,
    FOREIGN KEY (alb_art_id)
        REFERENCES tb_artists (art_id),
    FOREIGN KEY (alb_gen_id)
        REFERENCES tb_genres (gen_id)
);

CREATE TABLE tb_songs (
    son_id INT AUTO_INCREMENT PRIMARY KEY,
    son_name VARCHAR(255) NOT NULL,
    son_alb_id INT NOT NULL,
    son_duration FLOAT,
    son_lyrics TEXT,
    FOREIGN KEY (son_alb_id)
        REFERENCES tb_albums (alb_id)
);
