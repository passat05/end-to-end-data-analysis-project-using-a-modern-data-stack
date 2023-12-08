{{
    config(
      schema = 'reporting',
      tags = ['income']   
    )
}}

SELECT 
    to_date(attribute, 'mm/dd/YYYY') AS recorded_date,
    organisationkey AS organisation_id,
    level3,
    value
    
FROM {{ source('accounting','bugdet')}}