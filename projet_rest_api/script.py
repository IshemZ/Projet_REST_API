import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#définit le modèle de base de données
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    website = Column(String)

#Créer une connexion à la base de données SQLite
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

#Créer une session
Session = sessionmaker(bind=engine)
session = Session()

#Récuperer les données de l'API
response = requests.get("https://jsonplaceholder.typicode.com/users")
users_data = response.json()

#Insérer les données dans la BDD
for user_data in users_data:
    user = User(
        id=user_data['id'],
        name=user_data['name'],
        username=user_data['username'],
        email=user_data['email'],
        phone=user_data['phone'],
        website=user_data['website']
    )
    session.add(user)

#Valider les changements
session.commit()

print("Les données ont été enregistrées dans la base de données les gars !")

#Fermer la session
session.close()