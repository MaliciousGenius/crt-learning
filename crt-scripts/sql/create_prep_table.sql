CREATE TABLE IF NOT EXISTS prep(
    `id` String,
    `type` String,
    `datetime` DateTime,
    `date` Date,
    `ip` UInt32
)
ENGINE = MergeTree
ORDER BY datetime
