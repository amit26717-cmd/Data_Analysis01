# #integer value 

# i = 200
# print(i+50)
# print(i-20)
# print(i%7)
# print(i//20)
# print(divmod)
# print("\n")


# #floating value
# f = 200.10
# print(round(f,1),type(f).__name__)
# print(abs(-3.5))
# print("\n")

# #complex 
# c= 3+4j
# print(c.real)
# print(c.imag)
# print(c.conjugate())
# print("\n")

# a,b= 17,5

# print(a+b)
# print(a/b)
# print(a//b)
# print(a%b)
# print("\n")

#conversion

# print(int(12.58))
# print(float("30.5"))
# print(complex(54,10))
# print("\n")

# #boolean type
# is_auth = True
# failed_attempt =4

# print(failed_attempt >3)
# print(is_auth and failed_attempt<5)
# print(not is_auth)
# print("\n")

# #Truth value conversion

# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool("admin"))
# print("\n")

#string type

port = "https"

print(port[0])
print(port[-1])
print(port[1:4])
print(port +" traffic")
print("T"in port )
print(port.upper())
print("\n")

log = "ALERT : Suspicias VPN traffic"
print(log.strip())
print(log.lower())
print(log.replace("VAN ", "proxy"))
print(log.split())
print("-".join(["tcp","443"]))
print(log.count("s"))
print(log.find("VPN"))
print(log.startswith("ALERT"))
print("\n")

ip = "192.168.1.10"
octets = ip.split(".")
print(octets)
user , role = "Rohit:Admin".split(":")
print(f"User = {user} , Role = {role}")



