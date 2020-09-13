# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,transaction_amount):
    pet_shop["admin"]["total_cash"] += transaction_amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] += sold_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    # BELOW IS MY ORIGINAL VERSION FOR VISIBILITY
    # pet_count = 0
    # for pet in pet_shop["pets"]:
    #     pet_count += 1
    # return pet_count    

def get_pets_by_breed(pet_shop, breed):
    pet_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_by_breed.append(breed)
    return pet_by_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet            

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, transaction_amount):
    customer["cash"] -= transaction_amount


# @unittest.skip("delete this line to run the test")
# def test_add_pet_to_stock(self):
#     add_pet_to_stock(self.cc_pet_shop, self.new_pet)
#     count = get_stock_count(self.cc_pet_shop)
#     self.assertEqual(7, count)