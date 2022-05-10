# Import:
library(ggplot2)
library(dplyr)



# Change these file paths 
# according to your local
# machine's settings:

  # Read in the main csv file from HDD:
  all_indoor_delays <- read.csv("F:\\lorax_measurements\\plots_data\\r_codes\\all_indoor_delays.csv")
  
  
  

# --------------- Un-comment below lines to get summaries of the data frames (if necessary) --------------------------

# summary(data) # summary of the data frame containing all_indoor_delays
# summary(data_outdoor) # summary of the data frame containing all_outdoor_delays

                              # ---------------------------- #
    
    # --- Summary of only the UL and DL columns of outdoor measurement where distance is 2 meters
    # summary(data_outdoor%>%select(UL_Delay,Distance)%>%filter(Distance == "2 meters"))

    # --- Summary of only the UL and DL columns of outdoor measurement where distance is 10 meters
    # summary(data_outdoor%>%select(UL_Delay,Distance)%>%filter(Distance == "10 meters"))


# ----------------------------------------------------------------------------------------------------






# --------------------------------- Box/ Violin Plots -------------------------------------------------

# Adjust distance factors so they appear in the correct order
# Note that I preprocessed the data to remove the "meters" portion of the measurement
all_indoor_delays$Distance <- factor(all_indoor_delays$Distance, levels = c(2, 10, 20, 50))

    # -------------- Indoor ------------------------------------------------------------
   
    # MV: Set up a PNG file with proper margins
    png(filename="~/Desktop/IMWUT_violin_uplink_delay_indoor.png", res=300, units = "in", height=4, width=6)
    par(mar=c(5,5,5,2))
 
    # Plot UL:
    # Note: you may need to play with the scale_y_continuous limits. 
    dodge<-position_dodge(width = 1)
    ggplot(all_indoor_delays, aes(x=Distance, y=UL_Delay, fill=LOS_NLOS)) + geom_violin(trim=FALSE, position=dodge) + geom_boxplot(width=.1, outlier.colour=NA, position = dodge) + scale_fill_brewer(palette="Blues") + theme_minimal() + 
    scale_y_continuous(expand = c(0, 0), limits = c(0, 3200)) + theme(axis.text=element_text(size=12),axis.title=element_text(size=14,face="bold")) + guides(fill=guide_legend(title=NULL)) + labs(title="Uplink Delay (Indoor)", x="Distance between Compound Repeaters (m)", y="Delay (ms)")

    dev.off()
    
    # MV: Set up a PNG file with proper margins
    png(filename="~/Desktop/IMWUT_violin_downlink_delay_indoor.png", res=300, units = "in", height=4, width=6)
    par(mar=c(5,5,5,2))

   # Plot DL:
    # Note: you may need to play with the scale_y_continuous limits. 
    dodge<-position_dodge(width = 1)
    ggplot(all_indoor_delays, aes(x=Distance, y=DL_Delay, fill=LOS_NLOS)) + geom_violin(trim=FALSE, position=dodge) + geom_boxplot(width=.1, outlier.colour=NA, position = dodge) + scale_fill_brewer(palette="Blues") + theme_minimal() +
    scale_y_continuous(expand = c(0, 0), limits = c(0, 3200)) + theme(axis.text=element_text(size=12),axis.title=element_text(size=14,face="bold")) + guides(fill=guide_legend(title=NULL)) + labs(title="Downlink Delay (Indoor)", x="Distance between Compound Repeaters (m)", y="Delay (ms)") 
    
    dev.off()

    # MV: Set up a PNG file with proper margins
    png(filename="~/Desktop/IMWUT_violin_RTT_delay_indoor.png", res=300, units = "in", height=4, width=6)
    par(mar=c(5,5,5,2))

   # Plot RTT:
    # Note: you may need to play with the scale_y_continuous limits. 
    dodge<-position_dodge(width = 1)
    ggplot(all_indoor_delays, aes(x=Distance, y=RTT_Delay, fill=LOS_NLOS)) + geom_violin(trim=FALSE, position=dodge) + geom_boxplot(width=.1, outlier.colour=NA, position = dodge) + scale_fill_brewer(palette="Blues") + theme_minimal() +
    scale_y_continuous(expand = c(0, 0), limits = c(0, 3200)) + theme(axis.text=element_text(size=12),axis.title=element_text(size=14,face="bold")) + guides(fill=guide_legend(title=NULL)) + labs(title="RTT (Indoor)", x="Distance between Compound Repeaters (m)", y="Delay (ms)")

    dev.off()







    
