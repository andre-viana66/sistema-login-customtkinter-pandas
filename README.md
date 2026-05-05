# 🖥️ Sistema de Login com CustomTkinter

Sistema de login com interface gráfica desenvolvido em Python, utilizando CustomTkinter para a UI e Pandas para gerenciamento do banco de dados de usuários em CSV.

---

## 📋 Funcionalidades

- **Login de usuário** — valida usuário e senha contra o banco de dados
- **Cadastro de usuário** — permite criar novos usuários com confirmação de senha
- **Validação de campos** — exibe mensagens de erro diretamente na janela
- **Banco de dados em CSV** — armazena usuários e senhas em arquivo local

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3 | Linguagem principal |
| CustomTkinter | Interface gráfica moderna |
| Pillow (PIL) | Carregamento de imagens |
| Pandas | Leitura e escrita do banco de dados CSV |
| OS | Verificação de arquivos no sistema |

---

## 📁 Estrutura do projeto

```
📦 projeto-sistema-login
 ┣ 📄 main.py               # Código principal
 ┣ 📄 banco_de_senhas.csv   # Banco de dados de usuários (gerado automaticamente)
 ┣ 🖼️ pc_image.png          # Imagem da tela de login
 ┗ 🖼️ pc_image_2.png        # Imagem da tela de cadastro
```

---

## ⚙️ Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências
```bash
pip install customtkinter pillow pandas
```

### 3. Execute o programa
```bash
python main.py
```

---

## 🚀 Como usar

### Tela de Login
1. Digite seu **usuário** e **senha**
2. Clique em **Entrar**
3. Caso o usuário não exista, clique em **Cadastrar usuário**

### Tela de Cadastro
1. Digite o **usuário** desejado
2. Digite a **senha** e **repita a senha**
3. Clique em **Enviar**
4. O usuário será salvo automaticamente no banco de dados

---

## ⚠️ Observações

- O arquivo `banco_de_senhas.csv` é criado automaticamente na primeira vez que um usuário é cadastrado
- As senhas são armazenadas em **texto puro** — para uso em produção, recomenda-se aplicar criptografia (ex: `bcrypt`)
- As imagens `pc_image.png` e `pc_image_2.png` devem estar na mesma pasta do arquivo principal

---

## 📌 Melhorias futuras

- [ ] Criptografia de senhas
- [ ] Tela principal após login bem-sucedido
- [ ] Opção de recuperação de senha
- [ ] Validação de força da senha

---

## 👤 Autor

Feito por **André Viana** — sinta-se à vontade para contribuir!
