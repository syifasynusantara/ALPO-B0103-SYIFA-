nama_hero = "Orhun"
level = 10
hp = 999
is_alive = True
inventory = ["Pedang Tanduk Rusa", "Busur Panjang", "Perisai Sisik Naga"]
atribut = {"kekuatan": 85, "kelincahan": 95}

print("Nama Hero  :", nama_hero)
print("Level      :", level)
print("HP         :", hp)
print("Masih Hidup:", is_alive)
print("Inventory  :", inventory)
print("Atribut    :", atribut)

print("\n=== TIPE DATA ===")
print("nama_hero :", nama_hero, "->", type(nama_hero))
print("level     :", level, "->", type(level))
print("hp        :", hp, "->", type(hp))
print("is_alive  :", is_alive, "->", type(is_alive))
print("inventory :", inventory, "->", type(inventory))
print("atribut   :", atribut, "->", type(atribut))

inventory.append("Ramuan HP")
level = float(level)
level = level + 0.5

print("\n=== PROFIL KARAKTER (UPDATE) ===")
print("Nama Hero  :", nama_hero)
print("Level      :", level)
print("HP         :", hp)
print("Masih Hidup:", is_alive)
print("Inventory  :", inventory)
print("Atribut    :", atribut)
print("Tipe data level sekarang:", type(level))