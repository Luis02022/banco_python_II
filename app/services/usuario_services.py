from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
       
        try:
            usuario = Usuario(nome=nome,email=email, senha=senha)
            consulta_usuario = self.repository.pesquisar_usuario(usuario.email)
            if consulta_usuario:
               print("Usuário já existe.")
               return 
             
            self.repository.salvar_usuario(usuario)
            print("Usuário salvo com sucesso!")
            

        except TypeError as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro um inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()