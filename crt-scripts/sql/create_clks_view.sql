CREATE MATERIALIZED VIEW IF NOT EXISTS clks
(
    `id` String,
    `type` Enum8('clk' = 1),
    `datetime` DateTime,
    `date` Date,
    `ip` UInt32
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(datetime)
ORDER BY tuple()
AS
SELECT 
    id,
    type,
    datetime,
    date,
    IPv4StringToNum(ipAddress) AS ip
FROM events
WHERE type == 'clk'
ORDER BY datetime
