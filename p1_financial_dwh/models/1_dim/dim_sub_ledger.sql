{{
    config(
      schema = 'reporting',
      format= 'parquet',
      tags = ['income']   
    )
}}

SELECT
  {{ dbt_utils.generate_surrogate_key(['sub_ledger']) }} as sub_ledger_key,
  sub_ledger as sub_ledger_id,
  level3_detail

FROM {{ source('accounting', 'subledgermapping')}}