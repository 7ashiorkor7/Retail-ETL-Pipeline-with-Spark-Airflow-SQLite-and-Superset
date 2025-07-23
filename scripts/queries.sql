-- Get all inventory records for a specific store
SELECT * 
FROM inventory
WHERE store_key = 248;

-- Get all active products
SELECT prod_key, prod_name, brand_name, status_code_name
FROM product
WHERE status_code_name = 'active';

-- Get sales on a particular date
SELECT *
FROM sales
WHERE trans_dt = '2020-01-04';

-- Get store details for stores in the US
SELECT store_key, store_desc, city, region, cntry_nm, prov_state_desc
FROM store
WHERE cntry_cd = 'US';

-- Inventory items that are out of stock
SELECT prod_key, store_key, inventory_on_hand_qty
FROM inventory
WHERE out_of_stock_flg = 1;

-- Sales with discount greater than 10
SELECT trans_id, prod_key, store_key, sales_qty, discount
FROM sales
WHERE discount > 10;

-- Total sales amount per store for a given date
SELECT store_key, SUM(sales_amt) AS total_sales
FROM sales
WHERE trans_dt = '2020-01-04'
GROUP BY store_key;

-- Average inventory on hand per product
SELECT prod_key, AVG(inventory_on_hand_qty) AS avg_stock
FROM inventory
GROUP BY prod_key;

-- Count of stores per country
SELECT cntry_cd, COUNT(store_key) AS num_stores
FROM store
GROUP BY cntry_cd;

-- Join sales with product to get product names with sales info
SELECT s.trans_id, s.prod_key, p.prod_name, s.store_key, s.sales_qty, s.sales_amt
FROM sales s
JOIN product p ON s.prod_key = p.prod_key
WHERE s.trans_dt = '2020-01-04';

-- Join inventory with store to see stock info along with store location
SELECT i.store_key, st.city, st.store_desc, i.prod_key, i.inventory_on_hand_qty, i.out_of_stock_flg
FROM inventory i
JOIN store st ON i.store_key = st.store_key
WHERE i.out_of_stock_flg = 1;

-- Total sales amount by product category
SELECT p.category_name, SUM(s.sales_amt) AS total_sales_amt
FROM sales s
JOIN product p ON s.prod_key = p.prod_key
GROUP BY p.category_name
ORDER BY total_sales_amt DESC;

-- Sales count per day
SELECT trans_dt, COUNT(trans_id) AS num_sales
FROM sales
GROUP BY trans_dt
ORDER BY trans_dt;

-- Sales in a specific time range (e.g., evening sales)
SELECT *
FROM sales
WHERE trans_time BETWEEN 17 AND 21;

-- Count how many sales had discount vs no discount
SELECT
  SUM(CASE WHEN discount > 0 THEN 1 ELSE 0 END) AS sales_with_discount,
  SUM(CASE WHEN discount = 0 THEN 1 ELSE 0 END) AS sales_without_discount
FROM sales;

-- Label inventory stock status
SELECT
  prod_key,
  store_key,
  inventory_on_hand_qty,
  CASE
    WHEN inventory_on_hand_qty = 0 THEN 'Out of Stock'
    WHEN inventory_on_hand_qty < 10 THEN 'Low Stock'
    ELSE 'In Stock'
  END AS stock_status
FROM inventory;
