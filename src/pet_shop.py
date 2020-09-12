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