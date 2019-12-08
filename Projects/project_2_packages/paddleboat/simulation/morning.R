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
