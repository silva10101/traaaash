from Class_learn import Private_house


list_of_citizen = [('Anna', '24', 'f'), ('Nick', '20', 'm'), ('Rita', '48', 'f'), ('Jone', '49', 'm')]

list_of_citizen1 = [('Anna1', '241', 'f1'), ('Nick1', '201', 'm1')]

house1 = Private_house('Политехническая', 2, 2, 4)
house1.show_info()
house1.draw_house()
house1.describe_residents(list_of_citizen)
house1.show_residents()

house1.add_residents(2)
house1.describe_residents(list_of_citizen1)
house1.show_residents()




# house2 = Apartment('Политехническая', 3, 10, 400, 4)
# house3 = Private_house('Политехническая', 10, 1)
#
#
# house1.add_flours(4)
# house1.draw_house()
# # house2.show_info()
# # house2.draw_house()
# # house3.show_info()
# # house3.draw_house()
