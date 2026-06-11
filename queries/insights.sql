--- 1. Number of Total Unicorns In The World
SELECT COUNT(*) FROM unicorn_companies;

--- 2. Top 10 Oldest Companies
SELECT company, company_age, year_founded FROM unicorn_companies
ORDER BY company_age DESC
LIMIT 10;

--- 3. Top 10 Youngest Companies
SELECT company, company_age, year_founded FROM unicorn_companies
ORDER BY company_age ASC
LIMIT 10;

--- 4. Top Startup Hubs
SELECT COUNT(company) AS total_startups, city FROM unicorn_companies
GROUP BY city
ORDER BY total_startups DESC
LIMIT 10;

--- 5. Top 10 Highest Funding Companies
SELECT company, funding_billion FROM unicorn_companies
ORDER BY funding_billion DESC
LIMIT 10;

--- 6. Top 10 Most Valuable Companies
SELECT company,valuation_billion FROM unicorn_companies
ORDER BY valuation_billion DESC
LIMIT 10;

--- 7. Number of Total Startups In Each Country
SELECT COUNT(company) AS total_startups, country FROM unicorn_companies
GROUP BY country
ORDER BY total_startups DESC;

--- 8. Countries Order By The Total Startups Valuations
SELECT SUM(valuation_billion) AS total_valuations, country FROM unicorn_companies
GROUP BY country
ORDER BY total_valuations DESC;

--- 9. Continents Order By The Total Number of Startups 
SELECT COUNT(company) AS total_number, continent FROM unicorn_companies
GROUP BY continent
ORDER BY total_number DESC;

--- 10. Hottest Industries By Total Funding Amount
SELECT industry, SUM(funding_billion) AS total_funding FROM unicorn_companies
GROUP BY industry
ORDER BY total_funding DESC
LIMIT 10;

--- 11. Top 10 Most Valuable Industries By Total Valuation
SELECT SUM(valuation_billion) AS total_valuation, industry FROM unicorn_companies
GROUP BY industry
ORDER BY total_valuation DESC
LIMIT 10;
