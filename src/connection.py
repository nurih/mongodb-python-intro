from urllib.parse import quote_plus

host = "10.20.30.40"
db = "demo"
user = "asdf@example.com"
password = "qwe:+3/"
options = [("replicaSet", "r1"), ("connectTimeoutMS", 3000)]

print(user)
print(quote_plus(user))

print(password)
print(quote_plus(password))

connectionOptions = "&".join(map(lambda e: f"{e[0]}={e[1]}", options))

connectionString = f"mongodb+srv://{quote_plus(user)}:{quote_plus(password)}@{host}/{db}?{connectionOptions}"

print(connectionString)
