--creating table 
create table sales_data (
    OrderID VARCHAR(50),
    Date DATE,
    CustomerID VARCHAR(50),
    Product VARCHAR(100),
    Quantity INT,
    UnitPrice FLOAT,
    ShippingAddress TEXT,
    PaymentMethod VARCHAR(50),
    OrderStatus VARCHAR(50),
    TrackingNumber VARCHAR(100),
    ItemsInCart INT,
    CouponCode VARCHAR(50),
    ReferralSource VARCHAR(50),
    TotalPrice FLOAT
);
--USE OF SELECT QUERY
--imported csv of cleaned_data and retrieved it 
select * from sales_data

--USE OF WHERE CLAUSE 
-- retrieving data where product is laptop and total price is less than 1200
select * from sales_data
where Product = 'Laptop' and TotalPrice < 1200

--USE OF ORDER BY 
-- arranged total price in descending order
select * from sales_data
order by TotalPrice desc;

-- USE OF COUNT
-- count the total orders 
select count(*) as total_orders 
from sales_data;

--USE OF SUM 
-- sum the total revenue 
select sum(TotalPrice) as total_revenue
from sales_data;

--USE OF AVG
-- calculating the average total price 
select avg(TotalPrice) as average_sales
from sales_data;

-- USE OF GROUP BY 
-- revenue by payment method
select PaymentMethod, sum(TotalPrice) as revenue
from sales_data 
group by PaymentMethod;

-- revenue by product 
select Product, sum(TotalPrice) as revenue
from sales_data
group by Product;

-- orders by order status 
select OrderStatus, count(*) as total_orders
from sales_data 
group by OrderStatus;

--average spending by referral source
select ReferralSource, avg(TotalPrice) as average_spending
from sales_data
group by ReferralSource;

-- USE OF ORDER BY AND GROUP BY
-- Total Quantity Sold per product
select Product, sum(Quantity) as total_quantity
from sales_data 
group by Product 
order by total_quantity desc;

--Highest Revenue Products
select Product, sum(TotalPrice) as revenue
from sales_data
group by Product 
order by revenue desc;
