setwd("~/Documents/TLS")

#all the data sets are large, remember to delete

library("quantmod", lib.loc="/Library/Frameworks/R.framework/Versions/3.2/Resources/library")

#read all tickers
sp<-read.csv("sp.csv",header = T)
mysymbol<-as.character(sp$Symbol)

#get OPEN/HIGH/LOW/VOL/CLOSE data
#quantmod only contains data from 2007/1/1
#the following line takes about 10 mins
getSymbols(mysymbol,from =as.Date("2007-5-1"),to=as.Date("2016-5-15"))

#extract all the monthly close prices
ClosePrices <- do.call(merge, lapply(mysymbol, function(x) Cl(to.monthly(get(x)))))
#since the above line will lose all the ticker name
#the following line only help retrive the ticker name
header <- do.call(merge, lapply(mysymbol, function(x) Cl(get(x))))
write.csv(header,"header.csv")

head(ClosePrices)
#copy the header from "header.csv" to "closeprice.csv"
#change the date from 1,2,3 to the actual date for "closeprice.csv"
write.csv(ClosePrices,"closeprice.csv")

#now DELETE everything but the closeprice.csv used from this code file
#Change closeprices to descending order!!
