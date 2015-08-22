library(dplyr)
library(lubridate)

properDateYear <- function(x){
  m <- year(x) %% 100
  year(x) <- ifelse(m > 15 %% 100, 1900+m, 2000+m)
  return(x)
}

setwd("/home/cha/Programming/DataHack2015")
raw_data <- read.csv("raw-data/eviction-notices/raw-eviction-notices.csv")

# pick out data columns
working_data <- raw_data %>%
    select(EVICTION_ID:ADDRESS, ZIP:DEVELOPMENT, SUPERVISOR_DISTRICT:CLIENT_LOCATION) %>%
    mutate(CLIENT_LOCATION=as.character(CLIENT_LOCATION), ADDRESS=as.character(ADDRESS))

# split the location into separate lat and long
latlong <- matrix(
    unlist(
        strsplit(gsub("[() ]", "", working_data$CLIENT_LOCATION), ",")
        ),
    ncol=2,
    byrow=TRUE
    )

working_data <- working_data %>%
    select(-CLIENT_LOCATION) %>%
    mutate(latitude=latlong[,1], longitude=latlong[,2], latitude=as.numeric(latitude),
           longitude=as.numeric(longitude), FILE.DATE=properDateYear(mdy(FILE.DATE)))

block_number = sapply(strsplit(working_data$ADDRESS, " "), function(x) {
    result = as.numeric(paste(head(x, 1), collapse=" "))
    })

street_names = sapply(strsplit(working_data$ADDRESS, " "), function(x) {
    result = paste(tail(x, -1), collapse=" ")
    })

working_data <- working_data %>%
    mutate(block_number=block_number, street_name=street_names)

write.csv(working_data, "cleaned-data/eviction-notices.csv", row.names=F)