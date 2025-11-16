-- Task 4: Print full description of the books table
-- Current Date and Time (UTC): 2025-11-16 22:17:46
-- Current User's Login: AirdropGucci
-- Note: Not using DESCRIBE or EXPLAIN statements

SELECT 
  COLUMN_NAME,
  COLUMN_TYPE,
  IS_NULLABLE,
  COLUMN_KEY,
  COLUMN_DEFAULT,
  EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;