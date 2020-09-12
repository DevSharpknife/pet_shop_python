# WRITE YOUR FUNCTIONS HERE

# def test_pet_shop_name(self):
#         name = get_pet_shop_name(self.cc_pet_shop)
#         self.assertEqual("Camelot of Pets", name)

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


# @unittest.skip("delete this line to run the test")
# def test_total_cash(self):
#     sum = get_total_cash(self.cc_pet_shop)
#     self.assertEqual(1000, sum)

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop,transaction_amount):
    pet_shop["admin"]["total_cash"] += transaction_amount


# @unittest.skip("delete this line to run the test")
# def test_pets_sold(self):
#     sold = get_pets_sold(self.cc_pet_shop)
#     self.assertEqual(0, sold)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#     @unittest.skip("delete this line to run the test")
# def test_increase_pets_sold(self):
#     increase_pets_sold(self.cc_pet_shop,2)
#     sold = get_pets_sold(self.cc_pet_shop)
#     self.assertEqual(2, sold)

def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] += sold_pets

# @unittest.skip("delete this line to run the test")
# def test_stock_count(self):
#     count = get_stock_count(self.cc_pet_shop)
#     self.assertEqual(6, count)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    # pet_count = 0
    # for pet in pet_shop["pets"]:
    #     pet_count += 1
    # return pet_count    


# def test_all_pets_by_breed__found(self):
#     pets = get_pets_by_breed(self.cc_pet_shop, "British Shorthair")
#     self.assertEqual(2, len(pets))

# def get_pets_by_breed(pet_shop, breed):
#     pet_by_breed = []
#     for pet in pet_shop["pets"]:
#         if pet["breed"] == breed:
#             pet_by_breed.append(pet)
#         return(pet_by_breed)

    # @unittest.skip("delete this line to run the test")
    # def test_all_pets_by_breed__not_found(self):
    #     pets = get_pets_by_breed(self.cc_pet_shop, "Dalmation")
    #     self.assertEqual(0, len(pets))

    # @unittest.skip("delete this line to run the test")
    # def test_find_pet_by_name__returns_pet(self):
    #     pet = find_pet_by_name(self.cc_pet_shop, "Arthur")
    #     self.assertEqual("Arthur", pet["name"])

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return(pet)



