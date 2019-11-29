from MobilityDB import *

connectionObject = None

try:
	# Set the connection parameters to PostgreSQL
	connectionObject = psycopg2.connect(host='127.0.0.1', database='sf0_005', user='postgres', password='ulb')
	connectionObject.autocommit = True

	# Register MobilityDB data types
	MobilityDBRegister(connectionObject)

	cursor = connectionObject.cursor()

	# var = TFloatS('{[10@2019-09-08, 20@2019-09-09, 20@2019-09-10]}')
	# print(var)

	# var1 = TFloat('10@2019-09-08')
	# print(var1)
	# var2 = TFloatInst('20@2019-09-09')
	# print(var2)

	# var3 = TFloat([var1, var2])
	# print(var3)

	var1 = TFloat('[10@2019-09-08]')
	print(var1)
	var2 = TFloat('[20@2019-09-09]')
	print(var2)

	var3 = TFloat([var1, var2])
	print(var3)

except psycopg2.DatabaseError as e:

	print('Error {e}')

finally:

	if connectionObject:
		connectionObject.close()
