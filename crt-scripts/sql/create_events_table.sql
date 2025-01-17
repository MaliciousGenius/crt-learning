CREATE TABLE IF NOT EXISTS events(
    `id` String,
    `type` String,
    `datetime` DateTime,
    `date` Date,
    `server` String,
    `ipAddress` String,
    `ipProxy` String,
    `country` String,
    `language` String,
    `searchType` String,
    `programType` String,
    `adType` String,
    `adDisplayType` String,
    `idFeed` String,
    `idAdvertiser` String,
    `idCampaign` String,
    `idGroup` String,
    `idAd` String,
    `idPublisher` String,
    `idSite` String,
    `idChannel` String,
    `idDomain` String,
    `idGroupSite` String,
    `idGroupSiteChannel` String,
    `position` String,
    `keywords` String,
    `freeKeywords` String,
    `destinationUrl` String,
    `refererUrl` String,
    `userAgent` String,
    `browser` String,
    `status` String,
    `fraudCause` String,
    `spent` String,
    `adminRevenue` String,
    `pubRevenue` String,
    `idSearchType` String,
    `idConversion` String,
    `conversionValue` String,
    `idCategory` String,
    `capping` String,
    `budget` String,
    `displayUrl` String,
    `misc1` String,
    `misc2` String,
    `misc3` String,
    `vars` String,
    `subId` String,
    `deviceType` String,
    `os` String,
    `vendor` String,
    `device` String,
    `carrier` String,
    `idGroupChannelType` String,
    `ns` String,
    `httpReferer` String,
    `source` String
)
ENGINE = MergeTree
ORDER BY datetime
