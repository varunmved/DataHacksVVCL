require("RPostgreSQL")

lumodbconn <- function(name) {
    driver = dbDriver("PostgreSQL")
    conn = NULL

    if(name == "postgres"){
        conn = dbConnect(driver
                        , user="chavli"
                        , password="99bottlesofbeer"
                        , dbname="chavli_datahack"
                        , host="chavli-datahack.cyxt7rugzh4d.us-west-1.rds.amazonaws.com"
                        , port=5432)
    }
    else{
        print(paste("Unknown Database: ", name))
    }
    return(conn)
}

executeReadQuery <- function(dbconn, query){
    results = data.frame()

    if(!is.null(dbconn)){
        results = dbGetQuery(dbconn, query)
    } else{
        print("invalid db connection")
    }

    return(results)
}
