from django.test import TestCase
from models import Address, CreditCard
from models import User, AffiliateUser
from models import AdminUser, Store
from models import StoreLocation 

class AddressTest(TestCase):
    def test_should_have_user_as_addressable(self):
        """
        Prueba que una direccion pueda ser asociada
        a un usuario
        """

        user = User(email="nada@latinmail.com", name="nada", last_name="mas")
        user.save()

        address = Address()
        address.street1 = "Cra 7 # 6-19"
        address.addressable_object = user
        address.save()

        address_from_db = Address.objects.get(id=address.id)
        self.assertEqual(address_from_db.addressable_type.name, 'user')

    def test_should_have_affiliate_user_as_addressable(self):
        """
        Prueba que una direccion pueda ser asociada
        a un usuario
        """

        user = AffiliateUser(email="nada@latinmail.com", name="nada", last_name="mas")
        user.save()

        address = Address()
        address.street1 = "Cra 7 # 6-19"
        address.addressable_object = user
        address.save()

        address_from_db = Address.objects.get(id=address.id)
        self.assertEqual(address_from_db.addressable_type.name, 'affiliate user')

    def test_should_have_admin_user_as_addressable(self):
        """
        Prueba que una direccion pueda ser asociada
        a un usuario administrador
        """

        user = AdminUser(email="nada@latinmail.com", name="nada", last_name="mas")
        user.save()

        address = Address()
        address.street1 = "Cra 7 # 6-19"
        address.addressable_object = user
        address.save()

        address_from_db = Address.objects.get(id=address.id)
        self.assertEqual(address_from_db.addressable_type.name, 'admin user')

    def test_should_have_store_as_addressable(self):
        """
        Prueba que una direccion pueda ser asociada
        a una tienda
        """

        store = Store(name="My store")
        store.save()

        address = Address()
        address.street1 = "Cra 7 # 6-19"
        address.addressable_object = store 
        address.save()

        address_from_db = Address.objects.get(id=address.id)
        self.assertEqual(address_from_db.addressable_type.name, 'store')

    def test_should_have_store_location_as_addressable(self):
        """
        Prueba que una direccion pueda ser asociada
        a una ubicacion de tienda
        """

        store = StoreLocation(city="Chia")
        store.save()

        address = Address()
        address.street1 = "Cra 7 # 6-19"
        address.addressable_object = store 
        address.save()

        address_from_db = Address.objects.get(id=address.id)
        self.assertEqual(address_from_db.addressable_type.name, 'store location')

    def test_should_have_creditcard_as_addressable(self):
        """
        Prueba que una direccion pueda ser asociada
        a una tarjeta de credito
        """

        credit_card = CreditCard(number="1111111111")
        credit_card.save()

        address = Address()
        address.street1 = "Cra 7 # 6-19"
        address.addressable_object = credit_card 
        address.save()

        address_from_db = Address.objects.get(id=address.id)
        self.assertEqual(address_from_db.addressable_type.name, 'credit card')

    def test_should_count_the_users(self):
        """
        Prueba que se cuente el numero de usuarios
        """
        for i in range(3):
            User.objects.create(email="%s@i.com" % i, name="a", last_name="b")

        self.assertEqual(User.objects.count_the_number_of_users(), 3)

    def test_should_count_the_affiliate_users(self):
        """
        Prueba que se cuente el numero de usuarios afiliados
        """
        for i in range(3):
            AffiliateUser.objects.create(email="%s@i.com" % i, name="a", last_name="b")

        self.assertEqual(AffiliateUser.objects.count_the_number_of_users(), 3)

    def test_should_count_the_admin_users(self):
        """
        Prueba que se cuente el numero de usuarios administradores
        """
        for i in range(3):
            AdminUser.objects.create(email="%s@i.com" % i, name="a", last_name="b")

        self.assertEqual(AdminUser.objects.count_the_number_of_users(), 3)

