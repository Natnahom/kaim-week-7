SELECT
    id,
    date,
    message,
    views,
    media,
    LENGTH(message) AS message_length
FROM {{ source('kaim_week7', 'yetenaweg_messages') }}