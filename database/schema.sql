CREATE EXTENSION fuzzystrmatch;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
CREATE EXTENSION postgis_tiger_geocoder;

create table sf_evictions as (
    id                      serial primary key,
    eviction_id             varchar(16),
    address                 varchar(256),
    zip                     varchar(16),
    filedate                date,
    district                int,
    neighborhood            varchar(256),
    block_number            int
    street_name             varchar(256),
    longitude               float,
    latitude                float,
    non_payment             int,
    breach                  int,
    nuisance                int,
    illegal_use             int,
    renewal_failure         int,
    access_denial           int,
    unapproved_subtenant    int,
    owner_movein            int,
    demolition              int,
    capital_improvement     int,
    substantial_rehab       int,
    ellis_act               int,
    condo_conversion        int,
    roommate_same_unit      int,
    other                   int,
    late_payment            int,
    lead_remediation        int,
    development             int
);
create index sf_evictions_location on sf_evictions(latitude, longitude);
create index sf_evictions on sf_evictions(filedate);

create table sf_businesses as (
    id                      serial primary key,
    location_end_date       date,
    business_name           varchar(512),
    class_code              int,
    business_end_date       date,
    location_start_date     date,
    ownership_name          varchar(512),
    pbc_code                int,
    address                 varchar(256),
    zip                     varchar(16),
    latitude                float,
    longitude               float
);
create index sf_business_location on sf_businesses(latitude, longitude);
create index sf_business_start_date on sf_businesses(local_start_date);
