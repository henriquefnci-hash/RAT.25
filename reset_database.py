import os
import sys

# Ajustar o caminho para encontrar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rumo_ao_topo_app'))

from flask import Flask
from src.models.user import db, User
from werkzeug.security import generate_password_hash

# Configurar a aplicação Flask
app = Flask(__name__)

# Verificar o caminho correto do banco de dados
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rumo_ao_topo_app', 'src')
os.makedirs(db_path, exist_ok=True)
db_file = os.path.join(db_path, 'rumo_ao_topo.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(f"Usando banco de dados em: {db_file}")

db.init_app(app)

def reset_database():
    with app.app_context():
        # Remover todas as tabelas
        db.drop_all()
        
        # Recriar todas as tabelas
        db.create_all()
        
        # Criar o administrador
        admin = User(
            name='Administrador',
            email='henriquefnci@gmail.com',
            role='admin'
        )
        admin.set_password('Henrique@4')
        
        # Adicionar o administrador ao banco de dados
        db.session.add(admin)
        db.session.commit()
        
        print("Banco de dados resetado com sucesso!")
        print("Administrador criado:")
        print(f"Email: henriquefnci@gmail.com")
        print(f"Senha: Henrique@4")

if __name__ == '__main__':
    reset_database()
