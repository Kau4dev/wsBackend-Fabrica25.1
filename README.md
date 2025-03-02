# 🎬 Cinemark API

## 📌 Sobre o Projeto
A **Cinemark API** permite que os usuários pesquisem filmes utilizando a **OMDb API**, adicionem filmes aos seus favoritos e removam-nos quando desejarem. O projeto utiliza **Django** e **Django Template** para gerenciar a interface e a lógica do backend.

---

## 🚀 Tecnologias Utilizadas
- **Django** (Framework Web)
- **Django ORM** (Gerenciamento de banco de dados)
- **SQLite** (Banco de dados padrão)
- **OMDb API** (Fonte de dados para filmes)
- **Docker** (Para ambiente de desenvolvimento)

---

## 📂 Estrutura do Projeto

```
📁 wsBackend-Fabrica25.1
│-- 📁 movies  # Aplicação principal
│   │-- 📄 models.py  # Modelos do banco de dados
│   │-- 📄 views.py  # Lógica das requisições
│   │-- 📄 urls.py  # Rotas
│   │-- 📄 templates/  # Arquivos HTML
│
│-- 📁 users  # Gerenciamento de usuários
│   │-- 📄 views.py  # Login, registro e logout
│   │-- 📄 urls.py  # Rotas de autenticação
│
│-- 📄 Dockerfile  # Configuração para container Docker
│-- 📄 requirements.txt  # Dependências do projeto
│-- 📄 manage.py  # Comando para rodar o servidor
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/Kau4dev/wsBackend-Fabrica25.1.git
cd wsBackend-Fabrica25.1
```

### 2️⃣ Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar as Migrações do Banco de Dados
```bash
python manage.py migrate
```

### 5️⃣ Criar um Superusuário para o Admin (Opcional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Iniciar o Servidor
```bash
python manage.py runserver
```

A API estará disponível em: `http://127.0.0.1:8000/`

---

## 🔗 Endpoints Disponíveis

### 🎥 Movies
- **`GET /movies/pagina_inicial`** - Lista os filmes favoritados pelo usuário.
- **`GET /movies/busca?entrada=<titulo>`** - Busca filmes pelo título na OMDb API.
- **`POST /movies/adicionar_filme_favorito/<imdb_id>`** - Adiciona um filme aos favoritos do usuário.
- **`DELETE /movies/remover_filme_favorito/<imdb_id>`** - Remove um filme dos favoritos.

### 👤 Users
- **`GET /users/login`** - Página de login.
- **`POST /users/login`** - Autenticação do usuário.
- **`GET /users/registrar`** - Página de registro.
- **`POST /users/registrar`** - Criar uma nova conta.
- **`POST /users/logout`** - Faz logout do usuário.

---

## 🛠️ Validações e Regras de Negócio
- O usuário deve estar **logado** para acessar qualquer funcionalidade de filmes.
- **Somente** o dono do filme pode favoritar ou remover um filme da sua lista.
- O **IMDB ID** é único para cada filme no banco de dados.

---

## 🐳 Rodando com Docker
Caso queira rodar o projeto via Docker:

### 1️⃣ Construir a imagem Docker
```bash
docker build -t cinemark .
```

### 2️⃣ Rodar o container
```bash
docker run -p 8000:8000 cinermark
```

O servidor estará disponível em `http://127.0.0.1:8000/`

---

## 📜 Licença
Projeto desenvolvido para fins de aprendizado.

---

**Desenvolvido por [Kauã Victor Irineu Santana](https://github.com/Kau4dev)** 🚀

