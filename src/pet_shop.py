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

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return(pet)

        # @unittest.skip("delete this line to run the test")
        # def test_remove_pet_by_name(self):
        #     remove_pet_by_name(self.cc_pet_shop, "Arthur")
        #     pet = find_pet_by_name(self.cc_pet_shop,"Arthur")
        #     self.assertIsNone(pet)

            # def remove_pet_by_name(pet_shop, pet_name):
            #     for pet in pet_shop["pets"]:
            #         if pet["name"] == pet_name:
            #             del(pet)
            #             return(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"]

