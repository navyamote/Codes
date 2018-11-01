install.packages("ggplot2", repos='http://cran.us.r-project.org')
install.packages("mclust", repos='http://cran.us.r-project.org')
install.packages("cluster", repos='http://cran.us.r-project.org')

library(ggplot2)
library(mclust)
library(cluster)

sp500_px <- read.csv('sp500_px.csv')

## K-means 
set.seed(1010103)
df <- sp500_px[row.names(sp500_px)>='2011-01-01', c('XOM', 'CVX')]
km <- kmeans(df, centers=4, nstart=1)

df$cluster <- factor(km$cluster)
print(df)

centers <- data.frame(cluster=factor(1:4), km$centers)
centers

## Graph: K-means clusters for two stocks
png("StockClusters.png", width = 4, height=3, units='in', res=300)

ggplot(data=df, aes(x=XOM, y=CVX, color=cluster, shape=cluster)) +
  geom_point(alpha=.3) +
  scale_shape_manual(values = 1:4,
                     guide = guide_legend(override.aes=aes(size=1))) + 
  geom_point(data=centers,  aes(x=XOM, y=CVX), size=2, stroke=2)  +
  theme_bw() +
  scale_x_continuous(expand=c(0,0), lim=c(-2, 2)) + 
  scale_y_continuous(expand=c(0,0), lim=c(-2.5, 2.5)) 

dev.off()

