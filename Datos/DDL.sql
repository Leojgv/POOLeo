
CREATE TABLE Address (
    id_address int  NOT NULL AUTO_INCREMENT,
    street varchar(100)  NOT NULL,
    suite varchar(100)  NOT NULL,
    city varchar(100)  NOT NULL,
    zip_code varchar(100)  NULL,
    lat varchar(50)  NULL,
    lng varchar(50)  NULL,
    User_id_user int  NULL,
    CONSTRAINT Address_pk PRIMARY KEY (id_address)
);


CREATE TABLE Companies (
    id_company int  NOT NULL AUTO_INCREMENT,
    name_company varchar(100)  NOT NULL,
    catchPhrase varchar(250)  NULL,
    bs varchar(250)  NULL,
    User_id_user int  NOT NULL,
    CONSTRAINT Companies_pk PRIMARY KEY (id_company)
);


CREATE TABLE Post (
    id_post int  NOT NULL AUTO_INCREMENT,
    post_title varchar(150)  NOT NULL,
    body_post text  NOT NULL,
    User_id_user int  NULL,
    CONSTRAINT Post_pk PRIMARY KEY (id_post)
);


CREATE TABLE ToDos (
    id_todo int  NOT NULL AUTO_INCREMENT,
    todo_title varchar(200)  NOT NULL,
    completed bool  NOT NULL,
    User_id_user int  NULL,
    CONSTRAINT ToDos_pk PRIMARY KEY (id_todo)
);


CREATE TABLE User (
    id_user int  NOT NULL AUTO_INCREMENT,
    username varchar(50)  NOT NULL,
    user_email varchar(150)  NOT NULL,
    user_website varchar(100)  NOT NULL,
    user_phone varchar(150)  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (id_user)
);


CREATE TABLE UserPasswords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    encrypted_password VARCHAR(255) NOT NULL,
    encryption_key VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id_user)
);

CREATE TABLE Busqueda (
    id_search int  NOT NULL AUTO_INCREMENT,
    keyword_search varchar(250)  NOT NULL,
    CONSTRAINT Busqueda_pk PRIMARY KEY (id_search)
);


CREATE TABLE Resultados (
    id_resultado int  NOT NULL AUTO_INCREMENT,
    titulo text  NOT NULL,
    url text  NOT NULL,
    descripcion text  NOT NULL,
    Busqueda_id_search int  NOT NULL,
    CONSTRAINT Resultados_pk PRIMARY KEY (id_resultado)
);


ALTER TABLE Address ADD CONSTRAINT Address_User FOREIGN KEY Address_User (User_id_user)
    REFERENCES User (id_user);

ALTER TABLE Companies ADD CONSTRAINT Companies_User FOREIGN KEY Companies_User (User_id_user)
    REFERENCES User (id_user);

ALTER TABLE Post ADD CONSTRAINT Post_User FOREIGN KEY Post_User (User_id_user)
    REFERENCES User (id_user);

ALTER TABLE ToDos ADD CONSTRAINT ToDos_User FOREIGN KEY ToDos_User (User_id_user)
    REFERENCES User (id_user);

ALTER TABLE Resultados ADD CONSTRAINT Resultados_Busqueda FOREIGN KEY Resultados_Busqueda (Busqueda_id_search)
    REFERENCES Busqueda (id_search);