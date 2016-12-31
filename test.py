# import boto.ec2
# import time
# import datetime
#
#
# # l = [1, 2, 3]
# # enumerate(l)
# #
# # # boto.connect_ec2()
# #
# # instance_type = "t2.micro"
# # ami = "ami-501c8860"
# # access_key = "xxx"
# # secret_key = "xxx"
# # region = "us-west-2"
# #
# # user = boto.config.get('default', 'aws_access_key_id')
# # print("User: {}".format(user))
# # password = boto.config.get('default', 'aws_secret_access_key')
# # print("password: {}".format(password))
#
# # conn = boto.ec2.connect_to_region(region, aws_access_key_id="x", aws_secret_access_key="x")
#
#
# # def close_connection(conn):
# #     print("Closing connection")
# #     conn.close()
# #     print("Connection is closed")
#
#
# # conn = boto.ec2.connect_to_region(region, is_secure=False)
# conn = boto.ec2.connect_to_region(region, aws_access_key_id=user, aws_secret_access_key=password)
# # regions = boto.ec2.regions()
# time.sleep(2)
# print(datetime.datetime.now().time())
# print("Connection established")
# params = conn.get_params()
# print(params)
#
# print("'{}'".format(conn.aws_access_key_id))
#
# print("'{}'".format(conn.aws_secret_access_key))
# conn.debug = 1
# print(conn.debug)
# try:
#     conn.get_all_reservations()
#
#     time.sleep(2)
# except Exception as e:
#     close_connection(conn)
#     import traceback
#     traceback.print_exc()
#
# close_connection(conn)
#
# # input("\nPress enter to continue...")
# # print("Closing connection")
# # conn.close()
# # print("Connection is closed")
#
# # reservations = conn.get_all_reservations()
# # statuses = conn.get_all_instance_status()
# # input("\nPress enter to continue...")
# #
# # print("continue.....")
#
# # print("something")
# #
# #
# # def even(x): return x %2 == 0
# #
# #
# # def inc(x): return x + 1
# #
# #
# # list1 = [1, 2, 3]
# # list2 = [inc(x) for x in list1]
# # list3 = list(map(lambda x:x+11, list2))
# #
# # print(list2[0])
# #
# # print("list1: ", list1)
# # print("list2: ", list2)
# # print("list3: ", list3)
# #
# # my_list = [2,3,4,5]
# # my_list2 = [x**2 for x in my_list if x % 2]
# #
# # print(my_list2)
#
