-- 1. Overall campaign response
SELECT
    COUNT(*) AS total_customers,
    SUM(Response) AS responders,
    ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate
FROM customers;


-- 2. Acceptance rate for each campaign
SELECT 'AcceptedCmp1' AS campaign, COUNT(*) AS customers,
       SUM(AcceptedCmp1) AS accepted,
       ROUND(100.0 * SUM(AcceptedCmp1) / COUNT(*), 2) AS acceptance_rate
FROM customers
UNION ALL
SELECT 'AcceptedCmp2', COUNT(*), SUM(AcceptedCmp2),
       ROUND(100.0 * SUM(AcceptedCmp2) / COUNT(*), 2)
FROM customers
UNION ALL
SELECT 'AcceptedCmp3', COUNT(*), SUM(AcceptedCmp3),
       ROUND(100.0 * SUM(AcceptedCmp3) / COUNT(*), 2)
FROM customers
UNION ALL
SELECT 'AcceptedCmp4', COUNT(*), SUM(AcceptedCmp4),
       ROUND(100.0 * SUM(AcceptedCmp4) / COUNT(*), 2)
FROM customers
UNION ALL
SELECT 'AcceptedCmp5', COUNT(*), SUM(AcceptedCmp5),
       ROUND(100.0 * SUM(AcceptedCmp5) / COUNT(*), 2)
FROM customers
UNION ALL
SELECT 'Response', COUNT(*), SUM(Response),
       ROUND(100.0 * SUM(Response) / COUNT(*), 2)
FROM customers;


-- 3. Response by age band
SELECT
    CASE
        WHEN Age < 30 THEN '18-29'
        WHEN Age < 45 THEN '30-44'
        WHEN Age < 60 THEN '45-59'
        ELSE '60+'
    END AS age_band,
    COUNT(*) AS customers,
    SUM(Response) AS responders,
    ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate
FROM customers
GROUP BY age_band
ORDER BY MIN(Age);


-- 4. Response by country
SELECT
    Country,
    COUNT(*) AS customers,
    SUM(Response) AS responders,
    ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate
FROM customers
GROUP BY Country
ORDER BY response_rate DESC;


-- 5. Response and average spend by education
SELECT
    Education,
    COUNT(*) AS customers,
    SUM(Response) AS responders,
    ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate,
    ROUND(AVG(Total_Spend), 2) AS average_spend
FROM customers
GROUP BY Education
ORDER BY response_rate DESC;


-- 6. Responders and non-responders: income, spend, and visits
SELECT
    Response,
    COUNT(*) AS customers,
    ROUND(AVG(Income), 2) AS average_income,
    ROUND(AVG(Total_Spend), 2) AS average_spend,
    ROUND(AVG(NumWebVisitsMonth), 2) AS average_web_visits
FROM customers
GROUP BY Response
ORDER BY Response;


-- 7. High spender segment
-- Threshold 1564 is the dataset's calculated 90th percentile.
SELECT
    CASE
        WHEN Total_Spend > 1564 THEN 'High Spender'
        ELSE 'Other Customer'
    END AS customer_segment,
    COUNT(*) AS customers,
    SUM(Response) AS responders,
    ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate,
    ROUND(AVG(Total_Spend), 2) AS average_spend
FROM customers
GROUP BY customer_segment;


-- 8. Potential underserved segment:
-- more than 5 monthly web visits and below-average spend (640.33).
SELECT
    COUNT(*) AS customers,
    SUM(Response) AS responders,
    ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate,
    ROUND(AVG(NumWebVisitsMonth), 2) AS average_web_visits,
    ROUND(AVG(Total_Spend), 2) AS average_spend
FROM customers
WHERE NumWebVisitsMonth > 5
  AND Total_Spend < 640.33;