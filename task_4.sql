-- Task 4: Print full description of the books table
-- Current Date and Time (UTC): 2025-11-16 22:22:57
-- Current User's Login: AirdropGucci
-- Note: Not using DESCRIBE or EXPLAIN or ANALYZE statements

USE alx_book_store;

SELECT 
  COLUMN_NAME AS 'Field',
  COLUMN_TYPE AS 'Type',
  IS_NULLABLE AS 'Null',
  COLUMN_KEY AS 'Key',
  COLUMN_DEFAULT AS 'Default',
  EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;