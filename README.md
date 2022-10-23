# NLA-computational-project-2
For the KIU subject Numerical linear algebra I had to come up with real life use of K-means algorithm.
I choose to use K-means algorithm so I model cities according to
humidity and temperature. This kind of modelling could be useful for different reason. 
For example, websites like Amazon can group people living in the cities of the same cluster 
and offer them suitable equipment, clothes and so on.
My program gets names of random cities out of csv file.
Then used openweathermap.com’s rest API to get real data.
I get current temperature and humidity of the given city
I store these values into vector. Then I implemented K-means algorithm from scratch which clasters 
it  and visualises the output.
