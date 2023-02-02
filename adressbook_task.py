class AdressbookTask():
    def __init__(self, name, surname, corpo_name, job_role, email_adress):
        self.name = name
        self.surname = surname
        self.corpo_name = corpo_name
        self.job_role = job_role
        self.email_adress = email_adress
    
    @property
    def naming_length(self):
        return len(self.name) + len(self.surname) + 1
       
    def __str__(self):
        return f"{self.name} {self.surname} {self.corpo_name} {self.job_role} {self.email_adress}"    

    def contact(self):
        return f"Kontaktuję się z {self.name} {self.surname} {self.job_role} {self.email_adress}"


bronia = AdressbookTask(name="Bronisława", surname="Kaczmarek", corpo_name = "Realty-Solution", job_role = "diesel-train-engineer", email_adress = "BronislawaKaczmarek@jourrapide.com")
ruta = AdressbookTask(name = "Ruta", surname = "Maciejewska", corpo_name = "The-Pink-Pig-Tavern", job_role= "Compensation-benefits-technician", email_adress = "RutaMaciejewska@jourrapide.com")
serafin = AdressbookTask(name = "Serafin", surname= "Olszewski", corpo_name="Laura-Ashley", job_role="Event-planner", email_adress= "SerafinOlszewski@armyspy.com")
eustachy = AdressbookTask(name= "Eustachy", surname= "Czerwinski", corpo_name= "You-Are-Successful", job_role= "Agricultural-engineer", email_adress= "EustachyCzerwinski@jourrapide.com")
zdzisia = AdressbookTask(name= "Zdzisława", surname= "Nowak",corpo_name= "Computer-City", job_role= "Concrete-paving-machine-operator", email_adress= "ZdzislawaNowak@jourrapide.com")

adressbook_people = [bronia, ruta, serafin, eustachy, zdzisia]

print(ruta.contact())

for i in adressbook_people:
    print(i.name, i.surname, i.corpo_name, i.job_role, i.email_adress)

from faker import Faker
fake = Faker()


def instances_creator(f_name, f_surname, f_corpo, f_job, f_email):
    example_adressbook = AdressbookTask(name = f_name, surname = f_surname, corpo_name=f_corpo, job_role=f_job, email_adress=f_email)
    adressbook_people.append(example_adressbook)
    print(example_adressbook.name, example_adressbook.surname, example_adressbook.corpo_name, example_adressbook.job_role, example_adressbook.email_adress)

instances_creator(fake.name(), fake.name(), fake.company(), fake.job(), fake.email())


print("SPRAWDZENIE WYWOŁANIA FUNKCJI")

contact_list = []
#contact_card_type = None
def create_contacts(contact_card_type=str, quantity=int):
    for i in range(1, quantity+1):
        contact_card_type = AdressbookTask(name = fake.name(), surname=fake.name(), corpo_name= fake.company(), job_role=fake.job(), email_adress = fake.email())
        contact_list.append(contact_card_type)
        print(contact_card_type.name, contact_card_type.surname, contact_card_type.corpo_name, contact_card_type.job_role, contact_card_type.email_adress)
        
create_contacts("Business", 3)


by_name = sorted(adressbook_people, key=lambda names: names.name)
for i in by_name:
    print("SORTOWANIE-1: ", str(i.name), str(i.surname), str(i.corpo_name), str(i.job_role), str(i.email_adress))

by_surname = sorted(adressbook_people, key=lambda names: names.surname)
for i in by_surname:
    print("SORTOWANIE-2: ", str(i.name), str(i.surname), str(i.corpo_name), str(i.job_role), str(i.email_adress))

by_email = sorted(adressbook_people, key=lambda names: names.email_adress)
for i in by_email:
    print("SORTOWANIE-3: ", str(i.name), str(i.surname), str(i.corpo_name), str(i.job_role), str(i.email_adress))

print(bronia)

print(bronia.contact())

print("Naming = ", bronia.naming_length)

class BaseContact(AdressbookTask):
    def __init__(self, name, surname, priv_tel, email_adress, *args, **kwargs):
        super().__init__(name, surname, priv_tel, email_adress)
        self.priv_tel = priv_tel

    def contact(self):
        return f"Wybieram numer {self.priv_tel} i dzwonię do {self.name} {self.surname}"

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)

class BusinessContact(BaseContact):
    def __init__(self, job_role, corpo_name, company_tel, *args, **kwargs):
        super().__init__(job_role, corpo_name, company_tel)
        self.corpo_name = corpo_name
        self.company_tel = company_tel

    def contact(self):
        return f"Wybieram numer {self.company_tel} i dzwonię do {self.name} {self.surname}"

    @property
    def label_length(self):
        return super().label_length()
    
