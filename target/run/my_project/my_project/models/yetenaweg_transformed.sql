
  
    

  create  table "kaim_week7"."public"."yetenaweg_transformed__dbt_tmp"
  
  
    as
  
  (
    SELECT
    id,
    date,
    message,
    views,
    media,
    LENGTH(message) AS message_length
FROM "kaim_week7"."public"."yetenaweg_messages"
  );
  