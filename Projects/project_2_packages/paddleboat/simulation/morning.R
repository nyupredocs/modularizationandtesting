#----------------------------------------------------------------------------------#
# Performs simulations from Sunday morning
# Authors: Harriet, Casey, Nadav, Joel

# Notes:
#   
#----------------------------------------------------------------------------------#


########################################################
######################## Set-up ########################
########################################################

# load libraries
packages <- c("dplyr", "data.table", "ggplot2", "tidyr")
new.packages <- packages[!(packages %in% installed.packages()[, "Package"])]
if(length(new.packages)) install.packages(new.packages)
lapply(packages, library, character.only = TRUE)


########################################################
####################### Functions ######################
########################################################

alpha <- 3
delta <- -2
gamma <- 1
psi <- 4

n <- 1000

price <- uniform(0, 1)


supply.shocks <- function(epsilon, n=n){
  eta <- rnorm(0, 1)
  z <- epsilon + eta
  
  return(z)
}


demand.shocks <- function(epsilon, n=n){
  eta <- rnorm(0, 1)
  z <- epsilon + eta
  
  return(z)
}


supply.function <- function(gamma, psi, price){
  epsilon <- rnorm(0, 1)
  q <- gamma + psi * price + supply.shocks(epsilon)
  
  return(q)
}


demand.function <- function(alpha, gamma, price, n){
  epsilon <- rnorm(0, 1)
  q <- alpha + gamma * price + demand.shocks(epsilon)
  
  return(q)
}


find.market.price <- function(price){
  q_d <- demand.function(alpha, delta, price, n)
  q_s <- supply.function(gamma, psi, price, n)
  
  while (sum(abs(q_d - q_s)) > 0.05) {
    p <- p + 0.1 * (q_d - q_s)
  }
  
  return(p)
}


markets <- 50
prices <- punif(0, 1, 50)
market_matrix <- data.frame()

for (market in markets) {
  find.market.price(price = prices[market])
}


