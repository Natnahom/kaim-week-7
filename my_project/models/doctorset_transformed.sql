SELECT
    id,
    date,
    message,
    views,
    media,
    LENGTH(message) AS message_length
FROM {{ ref('doctorset_messages') }}