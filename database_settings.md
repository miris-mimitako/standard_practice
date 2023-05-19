# Database settings

This document covers using MariaDB for settings.
## Create database

You must define charset in create database sentence.

```mariadb

CREATE DATABASE your_database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

```

## create table

If you forgot setting charset at create database, you can specify charset in create table.

```mariadb

CREATE TABLE your_table_name (
    column1 VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    column2 VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    ...
);

```

## modify charset

### Database

```query

ALTER DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

```

### Table

```query

ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

```
