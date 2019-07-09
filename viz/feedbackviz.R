library(ggplot2)

library(plyr)
library(dplyr)






mean_data <- group_by(closeness_raw, game) %>%
  summarise(score = mean(score, na.rm = TRUE)) 
closeness_raw$game <- as.numeric(closeness_raw$game)
head(mean_data)

dat2 <- ddply(closeness_raw, .(game), summarise, 
              M = mean(score), SE = sd(score) / sqrt((length(score))), 
              SD = sd(score))
names(dat2)[2] <- "score"
dat2

# p <- ggplot(closeness_raw, aes(x=game,y=score)) +
stat_summary(geom = "line", fun.y=mean)
# p

p <- ggplot(na.omit(dat2),aes(x=game,y=score),group=1) +
    geom_errorbar(aes(ymin=score-SE, ymax=score+SE), width=.1,color='steelblue',alpha=0.8) + geom_point(color='steelblue', size=4) + geom_line(color='steelblue', size=2) 
p <- p + expand_limits(y=1)
p
