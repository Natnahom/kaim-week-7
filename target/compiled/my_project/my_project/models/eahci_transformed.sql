SELECT
    id,
    date,
    message,
    views,
    media,
    LENGTH(message) AS message_length
FROM "kaim_week7"."public"."eahci_messages"