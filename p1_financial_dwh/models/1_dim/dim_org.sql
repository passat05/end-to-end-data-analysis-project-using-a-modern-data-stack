{{
    config(
      schema = 'reporting',
      format= 'parquet',
      tags = ['income']   
    )
}}

SELECT
  {{ dbt_utils.generate_surrogate_key(['organisationkey']) }} as organisation_key,
  organisationkey AS organisation_id,
  geography AS organisation_area,
  image AS image_url

FROM {{ source('accounting', 'orgmapping')}}