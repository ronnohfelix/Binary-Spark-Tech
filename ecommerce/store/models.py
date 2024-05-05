from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    # Define choices for country and city
    COUNTY_CHOICES = [
    ('baringo', 'Baringo'),
    ('bomet', 'Bomet'),
    ('bungoma', 'Bungoma'),
    ('busia', 'Busia'),
    ('elgeyo_marakwet', 'Elgeyo Marakwet'),
    ('embu', 'Embu'),
    ('garissa', 'Garissa'),
    ('homa_bay', 'Homa Bay'),
    ('isiolo', 'Isiolo'),
    ('kajiado', 'Kajiado'),
    ('kakamega', 'Kakamega'),
    ('kericho', 'Kericho'),
    ('kiambu', 'Kiambu'),
    ('kilifi', 'Kilifi'),
    ('kirinyaga', 'Kirinyaga'),
    ('kisii', 'Kisii'),
    ('kisumu', 'Kisumu'),
    ('kitui', 'Kitui'),
    ('kwale', 'Kwale'),
    ('laikipia', 'Laikipia'),
    ('lamu', 'Lamu'),
    ('machakos', 'Machakos'),
    ('makueni', 'Makueni'),
    ('mandera', 'Mandera'),
    ('meru', 'Meru'),
    ('migori', 'Migori'),
    ('marsabit', 'Marsabit'),
    ('mombasa', 'Mombasa'),
    ('muranga', 'Muranga'),
    ('nairobi', 'Nairobi'),
    ('nakuru', 'Nakuru'),
    ('nandi', 'Nandi'),
    ('narok', 'Narok'),
    ('nyamira', 'Nyamira'),
    ('nyandarua', 'Nyandarua'),
    ('nyeri', 'Nyeri'),
    ('samburu', 'Samburu'),
    ('siaya', 'Siaya'),
    ('taita_taveta', 'Taita Taveta'),
    ('tana_river', 'Tana River'),
    ('tharaka_nithi', 'Tharaka Nithi'),
    ('trans_nzoia', 'Trans Nzoia'),
    ('turkana', 'Turkana'),
    ('uasin_gishu', 'Uasin Gishu'),
    ('vihiga', 'Vihiga'),
    ('wajir', 'Wajir'),
    ('west_pokot', 'West Pokot')
    ];
    SUB_COUNTY_CHOICES = [
    ('C1', 'Changamwe'),
    ('J1', 'Jomvu'),
    ('K1', 'Kisauni'),
    ('N1', 'Nyali'),
    ('L1', 'Likoni'),
    ('M1', 'Mvita'),
    ('M2', 'Msambweni'),
    ('L2', 'Lunga Lunga'),
    ('K2', 'Kwale'),
    ('K3', 'Kinango'),
    ('B1', 'Bahari (Kilifi)'),
    ('K4', 'Kilifi South'),
    ('K5', 'Kaloleni'),
    ('R1', 'Rabai'),
    ('G1', 'Ganze'),
    ('M3', 'Malindi'),
    ('M4', 'Magarini'),
    ('T1', 'Tana Delta'),
    ('T2', 'Tana River'),
    ('B2', 'Bura (Tana North)'),
    ('L3', 'Lamu East'),
    ('L4', 'Lamu West'),
    ('T3', 'Taveta'),
    ('W1', 'Wundanyi (Taita)'),
    ('M5', 'Mwatate'),
    ('V1', 'Voi'),
    ('H1', 'Hulugho'),
    ('L5', 'Liara'),
    ('B3', 'Balambala'),
    ('L6', 'Lagdera'),
    ('D1', 'Dadaab'),
    ('F1', 'Fafi'),
    ('I1', 'Ijara'),
    ('W2', 'Wajir North'),
    ('W3', 'Wajir East'),
    ('B4', 'Buna'),
    ('H2', 'Habaswein'),
    ('T4', 'Tarbaj'),
    ('W4', 'Wajir West'),
    ('E1', 'Eldas'),
    ('W5', 'Wajir South'),
    ('M6', 'Mandera West'),
    ('B5', 'Banisa'),
    ('M7', 'Mandera North'),
    ('M8', 'Mandera Central'),
    ('M9', 'Mandera East'),
    ('L7', 'Lafey'),
    ('M10', 'Moyale'),
    ('M11', 'Marsabit'),
    ('H3', 'Horr North'),
    ('L8', 'Loiyangalani'),
    ('C2', 'Chalbi'),
    ('S1', 'Sololo'),
    ('M12', 'Marsabit South (Laisamis)'),
    ('G2', 'Garbatula'),
    ('I2', 'Isiolo'),
    ('M13', 'Merti'),
    ('I3', 'Igembe South'),
    ('I4', 'Igembe Central'),
    ('I5', 'Igembe North'),
    ('I6', 'Imenti South'),
    ('I7', 'Imenti North'),
    ('M14', 'Meru Central'),
    ('T5', 'Tigania Central'),
    ('T6', 'Tigania East'),
    ('T7', 'Tigania West'),
    ('B6', 'Buuri'),
    ('M15', 'Meru South'),
    ('M16', 'Maara'),
    ('T8', 'Tharaka South'),
    ('T9', 'Tharaka North'),
    ('E2', 'Embu East'),
    ('E3', 'Embu North'),
    ('E4', 'Embu West'),
    ('M17', 'Mbeere North'),
    ('M18', 'Mbeere South'),
    ('M19', 'Mwingi Central'),
    ('M20', 'Mwingi West'),
    ('M21', 'Mwingi East'),
    ('K6', 'Kitui West'),
    ('K7', 'Kitui Central'),
    ('N2', 'Nzambani'),
    ('M22', 'Mutomo'),
    ('M23', 'Mutomo'),
    ('I8', 'Ikutha'),
    ('K8', 'Katulani'),
    ('K9', 'Kisasi'),
    ('K10', 'Kyuso'),
    ('L9', 'Lower Yatta'),
    ('M24', 'Matinyani'),
    ('M25', 'Mumoni'),
    ('M26', 'Mutito'),
    ('M27', 'Masinga'),
    ('Y1', 'Yatta'),
    ('K11', 'Kangundo'),
    ('M28', 'Matungulu'),
    ('K12', 'Kathiani'),
    ('A1', 'Athi River'),
    ('M29', 'Machakos'),
    ('M30', 'Mwala'),
    ('K13', 'Kibwezi'),
    ('K14', 'Kilungu'),
    ('M31', 'Makindu'),
    ('M32', 'Makueni'),
    ('M33', 'Mbooni West'),
    ('M34', 'Mbooni East'),
    ('K15', 'Kathonzweni'),
    ('M35', 'Mukaa'),
    ('N3', 'Nzaui'),
    ('K16', 'Kinangop'),
    ('K17', 'Kipipiri'),
    ('M36', 'Mirangine'),
    ('N4', 'Nyandarua Central'),
    ('N5', 'Nyandarua North'),
    ('N6', 'Nyandarua South'),
    ('N7', 'Nyandarua West'),
    ('T10', 'Tetu'),
    ('K18', 'Kieni East'),
    ('K19', 'Kieni West'),
    ('M37', 'Mathira East'),
    ('M38', 'Mathira West'),
    ('M39', 'Mukurwe-ini'),
    ('N8', 'Nyeri Central'),
    ('N9', 'Nyeri South'),
    ('K20', 'Kirinyaga Central'),
    ('K21', 'Kirinyaga East'),
    ('K22', 'Kirinyaga West'),
    ('M40', 'Mwea East'),
    ('M41', 'Mwea West'),
    ('K23', 'Kangema'),
    ('M42', 'Mathioya'),
    ('K24', 'Kahuro'),
    ('K25', 'Kigumo'),
    ('M43', "Murang'a East"),
    ('K26', 'Kandara'),
    ('G3', 'Gatanga'),
    ('M44', "Murang'a South"),
    ('G4', 'Gatundu South'),
    ('G5', 'Gatundu North'),
    ('J2', 'Juja'),
    ('R2', 'Ruiru'),
    ('G6', 'Githunguri'),
    ('K27', 'Kiambu'),
    ('K28', 'Kiambaa'),
    ('K29', 'Kabete'),
    ('K30', 'Kikuyu'),
    ('L10', 'Limuru'),
    ('L11', 'Lari'),
    ('T11', 'Thika East'),
    ('T12', 'Thika West'),
    ('T13', 'Turkana North'),
    ('T14', 'Turkana West'),
    ('T15', 'Turkana Central'),
    ('L12', 'Loima'),
    ('T16', 'Turkana South'),
    ('T17', 'Turkana East'),
    ('K31', 'Kibish'),
    ('K32', 'Kipkomo'),
    ('P1', 'Pokot Central'),
    ('P2', 'Pokot North'),
    ('P3', 'Pokot South'),
    ('W6', 'West Pokot'),
    ('S2', 'Samburu Central'),
    ('S3', 'Samburu North'),
    ('S4', 'Samburu East'),
    ('K33', 'Kwanza'),
    ('E5', 'Endebes'),
    ('T18', 'Transzoia East'),
    ('K34', 'Kiminini'),
    ('T19', 'Transzoia West'),
    ('S5', 'Soy'),
    ('W7', 'Wareng'),
    ('M45', 'Moiben'),
    ('E6', 'Eldoret West'),
    ('E7', 'Eldoret East'),
    ('K35', 'Kesses'),
    ('M46', 'Marakwet East'),
    ('M47', 'Marakwet West'),
    ('K36', 'Keiyo'),
    ('K37', 'Keiyo South'),
    ('T20', 'Tinderet'),
    ('N10', 'Nandi Central'),
    ('N11', 'Nandi East'),
    ('C3', 'Chesumei'),
    ('N12', 'Nandi North'),
    ('N13', 'Nandi South'),
    ('E8', 'East Pokot'),
    ('B7', 'Baringo North'),
    ('B8', 'Baringo Central'),
    ('K38', 'Koibatek'),
    ('M48', 'Marigat'),
    ('M49', 'Mogotio'),
    ('L13', 'Laikipia West'),
    ('L14', 'Laikipia East'),
    ('L15', 'Laikipia North'),
    ('L16', 'Laikipia Central'),
    ('N14', 'Nyahururu'),
    ('M50', 'Molo'),
    ('N15', 'Njoro'),
    ('N16', 'Naivasha'),
    ('G7', 'Gilgil'),
    ('K39', 'Kuresoi'),
    ('K40', 'Kuresoi North'),
    ('S6', 'Subukia'),
    ('R3', 'Rongai'),
    ('N17', 'Nakuru'),
    ('N18', 'Nakuru West'),
    ('N19', 'Nakuru North'),
    ('N20', 'Narok North'),
    ('N21', 'Narok East'),
    ('N22', 'Narok South'),
    ('N23', 'Narok West'),
    ('T21', 'Transmara East'),
    ('T22', 'Transmara West'),
    ('K41', 'Kajiado North'),
    ('K42', 'Kajiado Central'),
    ('K43', 'Kajiado West'),
    ('I9', 'Isinya'),
    ('L17', 'Loitokitok'),
    ('M51', 'Mashuuru'),
    ('K44', 'Kipkelion'),
    ('K45', 'Kericho'),
    ('L18', 'Londiani'),
    ('B9', 'Bureti'),
    ('B10', 'Belgut'),
    ('S7', 'Sigowei/Soin'),
    ('S8', 'Sotik'),
    ('C4', 'Chepalungu'),
    ('B11', 'Bomet East'),
    ('B12', 'Bomet'),
    ('K46', 'Konoin'),
    ('L19', 'Lugari'),
    ('M52', 'Matete'),
    ('L20', 'Likuyani'),
    ('K47', 'Kakamega Central'),
    ('K48', 'Kakamega East'),
    ('N24', 'Navakholo'),
    ('M53', 'Mumias'),
    ('M54', 'Mumias East'),
    ('M55', 'Matungu'),
    ('B13', 'Butere'),
    ('K49', 'Khwisero'),
    ('K50', 'Kakamega North'),
    ('K51', 'Kakamega South'),
    ('V2', 'Vihiga'),
    ('S9', 'Sabatia'),
    ('H4', 'Hamisi'),
    ('L21', 'Luanda'),
    ('E9', 'Emuhaya'),
    ('M56', 'Mt. Elgon'),
    ('B14', 'Bungoma Central'),
    ('B15', 'Bungoma East'),
    ('B16', 'Bungoma North'),
    ('B17', 'Bungoma South'),
    ('B18', 'Bungoma West'),
    ('W8', 'Webuye West'),
    ('C5', 'Cheptais'),
    ('K52', 'Kimilili'),
    ('B19', 'Bumula'),
    ('T23', 'Teso North'),
    ('T24', 'Teso South'),
    ('N25', 'Nambale'),
    ('B20', 'Bunyala'),
    ('B21', 'Busia'),
    ('B22', 'Butula'),
    ('S10', 'Samia'),
    ('U2', 'Ugenya'),
    ('U3', 'Ugunja'),
    ('S11', 'Siaya'),
    ('G8', 'Gem'),
    ('B23', 'Bondo'),
    ('R4', 'Rarieda'),
    ('K53', 'Kisumu East'),
    ('K54', 'Kisumu West'),
    ('K55', 'Kisumu Central'),
    ('S12', 'Seme'),
    ('N26', 'Nyando'),
    ('M57', 'Muhoroni'),
    ('N27', 'Nyakach'),
    ('M58', 'Mbita'),
    ('R5', 'Rachuonyo East'),
    ('R6', 'Rachuonyo North'),
    ('R7', 'Rachuonyo South'),
    ('H5', 'Homa Bay'),
    ('N28', 'Ndhiwa'),
    ('R8', 'Rangwe'),
    ('S13', 'Suba'),
    ('R9', 'Rongo'),
    ('A2', 'Awendo'),
    ('M59', 'Migori'),
    ('S14', 'Suna West'),
    ('U4', 'Uriri'),
    ('N29', 'Nyatike'),
    ('K56', 'Kuria West'),
    ('K57', 'Kuria East'),
    ('G9', 'Gucha'),
    ('G10', 'Gucha South'),
    ('K58', 'Kenyenya'),
    ('K59', 'Kisii Central'),
    ('K60', 'Kisii South'),
    ('K61', 'Kitutu Central'),
    ('M60', 'Marani'),
    ('M61', 'Masaba South'),
    ('N30', 'Nyamache'),
    ('S15', 'Sameta'),
    ('M62', 'Manga'),
    ('M63', 'Masaba North'),
    ('B24', 'Borabu'),
    ('N31', 'Nyamira North'),
    ('N32', 'Nyamira South'),
    ('W9', 'Westlands'),
    ('D2', 'Dagoretti'),
    ('L22', 'Langata'),
    ('K62', 'Kibra'),
    ('K63', 'Kasarani'),
    ('E10', 'Embakasi'),
    ('M64', 'Makadara'),
    ('K64', 'Kamukunji'),
    ('S16', 'Starehe'),
    ('M65', 'Mathare'),
    ('N33', 'Njiru')

    ]

    # Add country and city fields with choices
    county = models.CharField(max_length=20, choices=COUNTY_CHOICES, null=True, blank=True)
    sub_county = models.CharField(max_length=3, choices=SUB_COUNTY_CHOICES, null=True, blank=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        # Return the name of the customer if available
        if self.name:
            return self.name
        # If name is empty, return the email if available
        elif self.email:
            return self.email
        # If both name and email are empty, return the username if available
        elif self.user and self.user.username:
            return self.user.username
        # Return a generic string if no other information is available
        return 'Unnamed Customer'

    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True) # new
    price = models.DecimalField(max_digits=7, decimal_places=2) # new
    digital = models.BooleanField(default=False, null=True, blank=False) # new
    image = models.ImageField(null=True, blank=True) # new
    additional_images = models.ManyToManyField('Image', related_name='additional_images', blank=True) # new
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self): # new
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) # new
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True) # new
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) # new
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self): # new
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) # new
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) # new
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.address:
            return self.address
        else:
            return f"ShippingAddress #{self.id} (No address provided)"

class Details(models.Model):
    country = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) # new
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True) # new
    date_created = models.DateTimeField(auto_now_add=True, null=True) # new
    

    def __str__(self):
        # Return the name of the customer if available
        if self.name:
            return self.name

"""class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name"""