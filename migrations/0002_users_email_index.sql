CREATE UNIQUE INDEX CONCURRENTLY users_email_idx ON users (lower(email));
