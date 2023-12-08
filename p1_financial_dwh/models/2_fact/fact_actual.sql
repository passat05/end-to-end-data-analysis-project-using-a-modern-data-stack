{{
    config(
      schema = 'reporting',
      tags = ['income']   
    )
}}

SELECT 
    organizationkey AS organisation_id,
    sub_ledger,
    to_date("date", 'mm/dd/YYYY') AS recorded_date,
    value

FROM {{ source('accounting','actual')}}