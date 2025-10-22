# 📝 Gerenciador de Tarefas (To-Do List)

Um projeto **Django** simples criado para praticar **desenvolvimento back-end** e o uso de **Class-Based Views (CBVs)**.  
Permite **criar, listar, editar e excluir tarefas**, além de marcar como concluídas.

---

## 🚀 Tecnologias utilizadas

- Python 🐍
- Django 🕸️
- HTML + CSS (templates simples)

---

## ⚙️ Funcionalidades

- 📋 Listar todas as tarefas
- ➕ Criar novas tarefas
- ✏️ Editar tarefas existentes
- ❌ Excluir tarefas
- ✅ Marcar tarefas como concluídas

---

## 🧠 Conceitos Django praticados

- **Class-Based Views (CBVs):**
  - `ListView`
  - `DetailView`
  - `CreateView`
  - `UpdateView`
  - `DeleteView`
- Sistema de rotas com `urls.py`
- Templates HTML dinâmicos com o Django Template Language
- Organização de apps e pastas
- `get_absolute_url` e `reverse_lazy`

---

## 🧩 Estrutura do projeto

todo_project/
│
├── manage.py
├── app/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── todolist/
| ├── models.py
| ├── views.py
| ├── urls.py
| ├── templates/
| ├── new_todos.html
| ├── todo_delete.html
| ├── todo_detail.html
| ├── todo_update.html
| └── todos.html

---

🧾 Observações

O projeto foi desenvolvido em ambiente virtual (venv) para isolamento das dependências.
Ideal para quem está aprendendo Django e quer entender melhor como funcionam Class-Based Views.
Pode ser facilmente expandido com autenticação de usuários ou integração com Django REST Framework.
