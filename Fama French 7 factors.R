setwd("~/Documents/TLS")

#NOTICE: 
#0) All data has descending date with the lattest date on the top
#1) Always use smaller of [the dynamic length of the specific stock's return]
#   and [the length of the 7 factors]
#2) 7 factors and the risk free rate have the same length of data with no NA
#3) Since the stocks have different length of price, when reading price data,
#   the data type is actually "list".
#4) Log returns don't allow price to contain NA, thus
#   after use "lapply" to remove all NA, use [[]] to access each list's length
#   For simple return, can directly use the list with NA



#full history data of all 7 factors and risk free rate
x_data<-read.csv('7_factors_plus_rf.csv', header=T)
#######factor_length<-length(x_data[,1])
factor_length<-100
#risk free rate
risk_free<-x_data$RF

#full price data for 47 buffet stocks with differet lengths
price_original<-read.csv('47_last_price_series.csv', header=T)
#remove NA
price<-lapply(price_original, na.exclude)

#number of base stocks in Buffet's basket, not necessarily 47+date
#due lack of data, this time it's 46 + one column for date
basket_length<-length(price)
#min(RETURN length for each stock in the basket, factor length)
long<-rep(0,basket_length)
#coefficients for all stocks in the basket
base_coeff<-c()

for (hhh in 2:basket_length)
{
  # min(PRICE length for each stock in the basket, factor length)
  long_temp<-min(length(price[[hhh]]),factor_length)
  #retrive this stock's price history from price_original
  stock_price<-price_original[(1:long_temp),hhh]
  #excess return = log return - rf, NOTICE #return =#price -1=long_temp-1
  long[hhh]<-long_temp-1
  y_excess_return<-log(stock_price[-long_temp]/stock_price[-1])-risk_free[1:long[hhh]]
  #cutoff the factor table to fit the length of the return
  factor_table<-x_data[(1:long[hhh]),]
  #regression this stock's return on the 7 factors
  fit<-lm(y_excess_return~factor_table$Mkt.RF+factor_table$SMB+factor_table$HML+factor_table$RMW+factor_table$CMA+factor_table$BAB+factor_table$QMJ, na.action = "na.omit")
  base_coeff<-cbind(base_coeff,summary(fit)$coefficient[,1])
}
#check if there's any extreme value
write.csv(base_coeff,'base_coeff_100.csv')

#cut those base stocks with extreme values, here cut No.2 base stock
cut_list<-c(1,3:46)
base<-c()
for (cut in cut_list)
{
  base<-cbind(base, base_coeff[,cut])
}

#record the mean and sd of each row(factor) of the new base
base_coeff_mean<-c()
base_coeff_sd<-c()
#there are 8 coefficients for each regression
for (count in 1:8)
{
  base_coeff_mean<-rbind(base_coeff_mean,mean(base[count,]))
  base_coeff_sd<-rbind(base_coeff_sd,sd(base[count,]))
}
#candidate basket contain many potential stocks that may be chosen by WB

#read the price history of all candidates and remove NA
c_price_original<-read.csv('table.csv',header = T)
c_price<-lapply(c_price_original, na.exclude)
#number of candidates + one columen for date
candidate_length<-length(c_price)
#min(RETURN length for each candidate stock, factor length)
c_long<-rep(0,candidate_length)
#coefficients for all candidate stocks 
candidate_coeff<-c()

for (kkk in 2:candidate_length)
{
  # min(PRICE length for each candidate stock, factor length)
  c_long_temp<-min(length(c_price[[kkk]]),factor_length)
  #retrive this stock's price history from price_original
  c_stock_price<-c_price_original[(1:c_long_temp),kkk]
  #excess return = log return - rf, NOTICE #return =#price -1=long_temp-1
  c_long[kkk]<-c_long_temp-1
  c_y_excess_return<-log(c_stock_price[-c_long_temp]/c_stock_price[-1])-risk_free[1:(c_long[kkk])]
  #cutoff the factor table to fit the length of the return
  c_factor_table<-x_data[(1:c_long[kkk]),]
  #regression this stock's return on the 7 factors
  c_fit<-lm(c_y_excess_return~c_factor_table$Mkt.RF+c_factor_table$SMB+c_factor_table$HML+c_factor_table$RMW+c_factor_table$CMA+c_factor_table$BAB+c_factor_table$QMJ, na.action = "na.omit")
  candidate_coeff<-cbind(candidate_coeff,summary(c_fit)$coefficient[,1])
}

#transform z_score to B_score
transform_z_to_B<-function(value)
{
  if(abs(value)>1.3){B=1}
  else if(abs(value)>0.9){B=2}
  else if(abs(value)>0.55){B=3}
  else if(abs(value)>0.3){B=4}
  else {B=5}
  return (B)
}

z_score<-c()
B_score<-c()

for (mmm in 1:8)
{
  z<-(candidate_coeff[mmm,]-base_coeff_mean[mmm])/base_coeff_sd[mmm]
  B<-sapply(z,transform_z_to_B)
  z_score<-rbind(z_score,z)
  B_score<-rbind(B_score,B)
}
write.csv(B_score,'B_score_2.csv')

#Weights optimization is done in EXCEL

