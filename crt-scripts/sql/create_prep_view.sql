CREATE MATERIALIZED VIEW IF NOT EXISTS prepview TO prep(
    `id` String,
    `type` String,
    `datetime` DateTime,
    `date` Date,
    `ip` UInt32
)
AS SELECT
  id AS id,
  type AS type,
  datetime AS datetime,
  date AS date,
  IPv4StringToNum(ipAddress) AS ip
FROM logs
