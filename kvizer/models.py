from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Korisnik(models.Model):
    TIP = (("Učenik", "Učenik"),
           ("Profesor", "Profesor"), )
    tip = models.CharField(choices=TIP, max_length=200)
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    lozinka = models.CharField(max_length=50)


class Kviz(models.Model):
    PREDMETI = (("Matematika", "Matematika"),
                ("Fizika", "Fizika"),
                ("Srpski jezik i književnost", "Srpski jezik i književnost"),
                ("Srpski kao nematernji jezik", "Srpski kao nematernji"),
                ("Bosanski jezik i književnost", "Bosanski jezik i književnost"),
                ("Engleski jezik", "Engleski jezik"),
                ("Nemački jezik", "Nemački jezik"),
                ("Francuski jezik", "Francuski jezik"),
                ("Latinski jezik", "Latinski jezik"),
                ("Istorija", "Istorija"),
                ("Geografija", "Geografija"),
                ("Biologija", "Biologija"),
                ("Hemija", "Hemija"),
                ("Računarstvo i informatika", "Računarstvo i informatika"),
                ("Muzička kultura", "Muzička kultura"),
                ("Likovna kultura", "Likovna kultura"),
                ("Fizičko vaspitanje", "Fizičko vaspitanje"),
                ("Građansko vaspitanje", "Građansko vaspitanje"),
                ("Islamska veronauka", "Islamska veronauka"),
                ("Pravoslavna veronauka", "Pravoslavna veronauka"),
                ("Jezik medija i kultura", "Jezik medija i kultura"),
                ("Primenjene nauke", "Primenjene nauke"),
                ("Umetnost i dizajn", "Umetnost i dizajn"),
                ("Zdravlje i sport", "Zdravlje i sport"),
                ("Psihologija", "Psihologija"),
                ("Filozofija", "Filozofija"),
                ("Sociologija", "Sociologija"),
                ("Ustav i prava građana", "Ustav i prava građana"),
                )

    GODINE = (("Prva godina", "Prva godina"),
              ("Druga godina", "Druga godina"),
              ("Treća godina", "Treća godina"),
              ("Četvrta godina", "Četvrta godina"), )
    naziv = models.CharField(max_length=300)
    predmet = models.CharField(choices=PREDMETI, max_length=40)
    godina = models.CharField(choices=GODINE, max_length=40)
    id_korisnika = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    trajanje_kviza = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.naziv}'


class Pitanje(models.Model):
    id_kviza = models.ForeignKey(Kviz, on_delete=models.CASCADE)
    pitanje = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.pitanje}'


class Odgovor(models.Model):
    id_pitanja = models.ForeignKey(Pitanje, on_delete=models.CASCADE)
    odgovor = models.TextField(max_length=300)
    tacnost = models.BooleanField()

    def __str__(self):
        return f'{self.odgovor}'


class Rezultat(models.Model):
    id_kviza = models.ForeignKey(Kviz, on_delete=models.CASCADE)
    id_korisnika = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    bodovi = models.SmallIntegerField()

# accounts.models.py


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model


class User(AbstractBaseUser):  # from step 2

    objects = UserManager()
    TIP = (("Učenik", "Učenik"),
           ("Profesor", "Profesor"), )
    tip = models.CharField(choices=TIP, max_length=200)
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
