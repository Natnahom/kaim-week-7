
  
    

  create  table "kaim_week7"."public"."my_second_dbt_model__dbt_tmp"
  
  
    as
  
  (
    -- Use the `ref` function to select from other models

select *
from "kaim_week7"."public"."my_first_dbt_model"
where id = 1
  );
  