{{
    config(
      schema = 'reporting',
      format= 'parquet',
      tags = ['income']   
    )
}}

WITH monthly_actual AS (
    SELECT
        DATE(DATE_TRUNC('month', a.recorded_date)) AS reported_month,
        a.organisation_id,
        s.level3_detail,
        SUM(a.value) AS actual

    FROM {{ ref('fact_actual')}} AS a 
    LEFT JOIN {{ ref('dim_sub_ledger')}} AS s
    ON a.sub_ledger = s.sub_ledger_id
    GROUP BY 1,2,3  
)

SELECT
    a.reported_month,
    a.organisation_id,
    o.organisation_area,
    a.level3_detail,
    a.actual AS actual,
    b.value AS budget,
    f.value AS forecast

FROM monthly_actual AS a
LEFT JOIN {{ ref('fact_bugdet')}} AS b
ON a.level3_detail = b.level3 AND a.organisation_id = b.organisation_id AND a.reported_month = b.recorded_date
LEFT JOIN {{ ref('fact_forecast')}} AS f
ON a.level3_detail = f.level3 AND a.organisation_id = f.organisation_id AND a.reported_month = f.recorded_date
LEFT JOIN {{ ref('dim_org')}} AS o
ON a.organisation_id = o.organisation_id