select
    date_trunc('month', filedate) eviction_month
    , count(*)
from
    sf_evictions
where
    filedate >= '2000-01-01'
    and (
        ellis_act = 1
        or
        demolition = 1
        or
        development = 1
        or
        condo_conversion = 1
        or
        capital_improvement = 1
        or
        substantial_rehab = 1
        or
        lead_remediation = 1
    )
group by
    date_trunc('month', filedate)
order by
    date_trunc('month', filedate) desc


select
    date_trunc('month', location_start_date)
    , count(*)
from
    sf_businesses
where
    location_start_date >= '2000-01-01'
    and (
        business_name ~* 'whole foods market'
        or
        business_name ~* 'coffee'
        or
        business_name ~* '[^a-zA-Z0-9]spa[^a-zA-Z0-9]'
        or
        business_name ~* 'crossfit'
    )
group by
    date_trunc('month', location_start_date)
order by
    date_trunc('month', location_start_date) desc