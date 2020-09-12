# WRITE YOUR FUNCTIONS HERE

# def test_pet_shop_name(self):
#         name = get_pet_shop_name(self.cc_pet_shop)
#         self.assertEqual("Camelot of Pets", name)

def get_pet_shop_name(shop_name):
    return shop_name["name"]


# @unittest.skip("delete this line to run the test")
# def test_total_cash(self):
#     sum = get_total_cash(self.cc_pet_shop)
#     self.assertEqual(1000, sum)

def get_total_cash(total_shop_cash):
    return total_shop_cash["admin"]["total_cash"]


def add_or_remove_cash(total_cash,transaction_amount):
    total_cash["admin"]["total_cash"] = total_cash["admin"]["total_cash"] + transaction_amount

 