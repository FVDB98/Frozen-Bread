from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, email, password_hash, address_line1, address_line2,
                 city, postcode, country, created_at, is_admin):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.postcode = postcode
        self.country = country
        self.created_at = created_at
        self.is_admin = is_admin
