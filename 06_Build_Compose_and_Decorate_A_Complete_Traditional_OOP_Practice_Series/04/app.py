# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.



class Bank:
    bank_name = "xyz bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing bank name:")
    print(f"User1 bank name: {user1.bank_name}")   
    print(f"User2 bank name: {user2.bank_name}")

    Bank.change_bank_name("abc bank")

    print("\nAfter changing bank name:")
    print(f"User1 bank name: {user1.bank_name}")
    print(f"User2 bank name: {user2.bank_name}")
    
    