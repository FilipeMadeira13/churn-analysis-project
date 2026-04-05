# 1. Taxa de churn geral
SELECT COUNT(*) AS total_clientes,
    SUM(Churn) AS clientes_churn,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percent
FROM customers;
# 2. Churn por tipo de contrato
SELECT Contract,
    COUNT(*) AS total,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate
FROM customers
GROUP BY Contract
ORDER BY churn_rate DESC;
# 3. Churn por tempo de cliente (tenure)
SELECT CASE
        WHEN tenure < 12 THEN '0-1 ano'
        WHEN tenure < 24 THEN '1-2 anos'
        ELSE '2+ anos'
    END AS faixa_tempo,
    COUNT(*) AS total,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate
FROM customers
GROUP BY faixa_tempo
ORDER BY churn_rate DESC;
# 4. Churn por suporte técnico
SELECT TechSupport,
    COUNT(*) AS total,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate
FROM customers
GROUP BY TechSupport
ORDER BY churn_rate DESC;
# 5. Churn por tipo de internet
SELECT InternetService,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate
FROM customers
GROUP BY InternetService
ORDER BY churn_rate DESC;
# 6. Churn por método de pagamento
SELECT PaymentMethod,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;
# 7. Perfil de alto risco
SELECT *
FROM customers
WHERE Contract = 'Month-to-month'
    AND tenure < 12
    AND Churn = 1;