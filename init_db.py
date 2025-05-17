# init_db.py
import os
from sqlalchemy import create_engine
from models import Base  # Assure-toi que models.py est au même niveau

def main():
    # 1) Récupérer l'URL depuis la variable d'environnement
    db_url = os.getenv("EPICEVENTS_DB")
    if not db_url:
        raise RuntimeError("❌ La variable EPICEVENTS_DB n'est pas définie")

    # 2) Créer l'engine SQLAlchemy (SQLite crée le fichier s'il n'existe pas)
    engine = create_engine(db_url, echo=True)

    # 3) Générer le fichier .sqlite et toutes les tables
    Base.metadata.create_all(engine)

    print("✅ Base initialisée et fichier créé :", db_url)

if __name__ == "__main__":
    main()
