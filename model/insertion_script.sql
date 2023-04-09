USE db_music;

-- Insert data into the artists table
INSERT INTO tb_artists (art_name, art_bio, art_country) 
VALUES ('The Beatles', 'The Beatles were an English rock band formed in Liverpool in 1960.', 'England');

INSERT INTO tb_artists (art_name, art_bio, art_country) 
VALUES ('Michael Jackson', 'Michael Joseph Jackson was an American singer, songwriter, and dancer.', 'USA');

-- Insert data into the genres table
INSERT INTO tb_genres (gen_name)
VALUES ('Rock');

INSERT INTO tb_genres (gen_name)
VALUES ('Pop');

-- Insert data into the albums table
INSERT INTO tb_albums (alb_name, alb_release_year, alb_art_id, alb_gen_id)
VALUES ('Abbey Road', 1969, 1, 1);

INSERT INTO tb_albums (alb_name, alb_release_year, alb_art_id, alb_gen_id)
VALUES ('Thriller', 1982, 2, 2);

-- Insert data into the songs table
INSERT INTO tb_songs (son_name, son_alb_id, son_duration, son_lyrics)
VALUES ('Come Together', 1, 4.2, 'Here come old flattop, he come grooving up slowly...');

INSERT INTO tb_songs (son_name, son_alb_id, son_duration, son_lyrics)
VALUES ('Beat It', 2, 4.18, 'They told him, "Don''t you ever come around here. Don''t wanna see your face, you better disappear..."');
