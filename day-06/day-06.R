library(tidyverse)
library(ggplot2)
library(glue)

bestManDist <- function(row, points) {
  dists <- abs(row[['x']] - points[['x']]) + abs(row[['y']] - points[['y']])
  if (sum(dists == min(dists)) == 1) {
    return(which.min(dists))
  } else {
    return(9999)
  }
}

points <- read.csv('../data/06-input.txt', header = FALSE)
colnames(points) <- c('x', 'y')

max_x <- max(points$x)
max_y <- max(points$y)

grid <- expand.grid(1:max_x, 1:max_y)
colnames(grid) <- c('x', 'y')

grid$nearest <- apply(grid, 1, bestManDist, points = points)

inf_points <- grid %>% 
  filter(x %in% c(1, max_x) | y %in% c(1, max_y)) %>% 
  pull(nearest) %>% 
  unique()

biggest_region <- grid %>% 
  filter(!(nearest %in% inf_points)) %>% 
  group_by(nearest) %>% 
  summarize(n = n()) %>% 
  ungroup() %>% 
  arrange(desc(n)) %>% 
  head(1)

cat("::: PART A\n")
cat(glue("Point #{biggest_region['nearest']} has size {biggest_region['n']}"), "\n\n")

#===============================================================================

sumManDist <- function(row, points) {
  dists <- abs(row[['x']] - points[['x']]) + abs(row[['y']] - points[['y']])
  return(sum(dists))
}

grid$sum_dist <- apply(grid, 1, sumManDist, points = points)
grid$in_region <- grid$sum_dist < 10000

grid_region <- grid[grid$in_region,]

in_region <- nrow(grid_region) 

cat("::: PART B\n")
cat(glue("There were {in_region} points within 10,000 units of each point."), "\n")

p <- ggplot(grid, aes(x, y)) +
  theme_void() +
  geom_point(aes(color = factor(nearest)), size = 0.1) +
  geom_point(data = grid_region, color = 'black', alpha = 0.1) +
  theme(legend.position = 'none')
ggsave(filename = 'region.png', plot = p, dpi = 300)