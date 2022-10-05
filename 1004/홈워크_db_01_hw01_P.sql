
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 180, 210,  5);

-- 오류가 나진 않지만, 테이블 순서와 타입의 순서가 제대로 맞지 않아 원하는 결과를 얻지 못합니다.
-- 따라서 순서에 맞도록 바꿔주었습니다.


-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(11, 'alligator', 'carnivore', 250, 50);

-- rowid는 중복되어선 안되는 숫자입니다. 그래서 오류가 나므로 따라서 겹치지 않도록 숫자를 바꿔주었습니다.


-- 3)
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore',180, 3);

--weight는 NULL의 값을 담을 수 없습니다. 따라서 weight에 대한 정보를 추가해줬습니다.