cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.difference_update(cities_2)
print("The set after difference_update() method in cities_1 is :-\n",cities_3)