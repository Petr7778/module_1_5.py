#"Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = 1,2,3,5.2,'лист',True
print(immutable_var)
#immutable_var[2] = 10
#print(immutable_var)
mutable_list = [15,12,5,'урок',5.6]
print(mutable_list)
mutable_list[3] = 8
print(mutable_list)

