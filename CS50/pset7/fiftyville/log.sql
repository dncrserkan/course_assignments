-- Keep a log of any SQL queries you execute as you solve the mystery.

-- QUERY 1
-- Looking for what report say about case and using filters about place and date
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' AND year = 2021 AND month = 7 AND day = 28;

-- QUERY 2
-- Looking for withnesses' statements
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- QUERY 3
-- Look at security logs till 10 minutes after incident thief(s)'s escape
SELECT * FROM bakery_security_logs WHERE 
    year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25;

-- QUERY 3.1
-- Find the license plate owners
SELECT id, name FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs WHERE
        year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25);

-- QUERY 4
-- Check the phone records and look for caller
SELECT id, name FROM people WHERE phone_number IN
    (SELECT caller FROM phone_calls WHERE
        year = 2021 AND month = 7 AND day = 28 AND duration < 60);

-- QUERY 5
-- List of people from ATM records
SELECT id, name FROM people WHERE id IN
    (SELECT person_id FROM bank_accounts WHERE account_number IN
        (SELECT account_number FROM atm_transactions WHERE
            year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type LIKE '%With%')
    );

-- QUERY 6
-- Passengers who flight the next day with earliest flight
SELECT id, name FROM people WHERE passport_number IN
    (SELECT passport_number FROM passengers WHERE flight_id IN
        (SELECT id FROM flights WHERE 
            year = 2021 AND month = 7 AND day = 29 
            AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
            ORDER BY hour LIMIT 1
        )
    );

-- QUERY 7
-- Combine all data till now and see who are exist in all queries
SELECT id, name FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs WHERE
        year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25)
INTERSECT
SELECT id, name FROM people WHERE phone_number IN
    (SELECT caller FROM phone_calls WHERE
        year = 2021 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT id, name FROM people WHERE id IN
    (SELECT person_id FROM bank_accounts WHERE account_number IN
        (SELECT account_number FROM atm_transactions WHERE
            year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type LIKE '%With%')
    )
INTERSECT
SELECT id, name FROM people WHERE passport_number IN
    (SELECT passport_number FROM passengers WHERE flight_id IN
        (SELECT id FROM flights WHERE 
            year = 2021 AND month = 7 AND day = 29 
            AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
            ORDER BY hour, minute LIMIT 1
        )
    );


-- QUERY 8
-- Which city was the plane going
SELECT city FROM airports WHERE id =
    (SELECT destination_airport_id FROM flights WHERE 
        year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 
        (SELECT id FROM airports WHERE city = 'Fiftyville') 
    ORDER BY hour, minute LIMIT 1
    );


-- QUERY 9
-- Who help him
SELECT id, name FROM people WHERE phone_number =
    (SELECT receiver FROM phone_calls WHERE 
        year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller =
            (SELECT phone_number FROM people WHERE id = 686048)
    );