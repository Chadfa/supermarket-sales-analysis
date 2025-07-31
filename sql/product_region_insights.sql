-- 1. Total Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 2. Top 5 Most Profitable Sub-Categories
SELECT Sub_Category, SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Sub_Category
ORDER BY Total_Profit DESC
LIMIT 5;

-- 3. Sales and Profit by Customer Category
SELECT Customer_Category, 
       SUM(Sales) AS Total_Sales, 
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Customer_Category;

-- 4. City-Wise Sales and Profit
SELECT City, 
       SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY City
ORDER BY Total_Sales DESC;

-- 5. Average Discount by Region
SELECT Region, 
       ROUND(AVG(CAST(REPLACE(Discount, '%', '') AS DECIMAL(5,2))), 2) AS Avg_Discount
FROM sales
GROUP BY Region
ORDER BY Avg_Discount DESC;

-- 6. Monthly Sales Trend
SELECT 
    MONTH(Order_Date) AS Sale_Month,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY MONTH(Order_Date)
ORDER BY Sale_Month;

-- 7. Sub-Categories with Net Loss
SELECT Sub_Category, SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Sub_Category
HAVING SUM(Profit) < 0;