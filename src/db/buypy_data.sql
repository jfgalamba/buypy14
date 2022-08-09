/*
    DML for the BuyPy Online Store.

    (c) Joao Galamba, 2022
 */

USE BuyPy;

DELETE FROM `Order`;
DELETE FROM `Client`;

INSERT INTO `Client` 
    (firstname, surname, email, `password`,
        address, zip_code, city, country,
        phone_number, birthdate)
VALUES
    ('Alberto', 'Antunes', 'alb@mail.com', '123abC',
        'Rua do Almada, n. 23', 9877, 'Lisboa', 'Portugal',
        '351213789123', '1981-05-23'),
    ('Arnaldo', 'Avelar', 'arnaldo@coldmail.com', '123abC',
        'Av. América, n. 23', 2877, 'Porto', 'Portugal',
        '351213789123', '1981-05-23')
;

INSERT INTO `Order`
    (payment_card_number, payment_card_name, payment_card_expiration, client_id)
VALUES
    (121, 'DR. ALBERTO ANTUNES', '2023-05-23', (SELECT id FROM `Client` WHERE firstname = 'alberto' LIMIT 1))
;

SELECT * FROM `Client`;
SELECT * FROM `Order`;

SELECT SHA2('123abC', 256), LENGTH(SHA2('123abC', 256));

SELECT LEFT('919234108', 3);

/*
    Clientes inválidos
INSERT INTO `Client` 
    (firstname, surname, email, `password`)
VALUES
    ('armando', 'almeida', 'arm@xpto.com', '123abC')
;
*/