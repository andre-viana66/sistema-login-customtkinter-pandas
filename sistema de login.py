from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton
from PIL import Image
import pandas as pd
import os
from time import sleep


def exibir_informacoes(entre_usuario, entre_senha):
    """Exibe as informações do usuário logado no terminal e limpa os campos de entrada."""
    print(entre_usuario.get())
    print(entre_senha.get())
    entre_usuario.delete(0, END)
    entre_senha.delete(0, END)


def janela_login():
    """Cria e exibe a janela principal de login do sistema."""

    # criando janela principal
    janela = ctk.CTk()
    janela.geometry("700x400")
    janela.resizable(width=False, height=False)

    # carregando e exibindo imagem decorativa
    image_pc = ctk.CTkImage(light_image=Image.open("imagens-janelas/pc_image.png"),
                            dark_image=Image.open("imagens-janelas/pc_image.png"),
                            size=(300, 300))
    ctk.CTkLabel(janela, image=image_pc, text=None).place(x=80, y=30)

    # titulo da janela
    ctk.CTkLabel(janela, font=("arial bold", 20, "bold"), text="SISTEMA DE LOGIN").place(x=475, y=100)

    # campos de entrada de usuário e senha
    entre_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário:", corner_radius=20)
    entre_senha = ctk.CTkEntry(janela, placeholder_text="Senha:", show="*", corner_radius=20)
    entre_usuario.place(x=500, y=150)
    entre_senha.place(x=500, y=200)

    def verificar_login():
        """Verifica se o usuário e senha digitados existem no banco de dados CSV."""
        arquivo = "banco_de_senhas.csv"
        df = pd.read_csv(arquivo)

        # filtra o banco de dados pelo usuário e senha informados
        resultado = df[
            (df["usuario"] == entre_usuario.get()) &
            (df["senha"] == entre_senha.get())
        ]

        if not resultado.empty:
            # usuário encontrado — exibe informações e limpa os campos
            exibir_informacoes(entre_usuario, entre_senha)
        else:
            # usuário não encontrado — exibe mensagem de erro na janela
            texto = ctk.CTkLabel(janela, text_color="white", text="Usuário ou senha incorretos")
            texto.place(x=495, y=350)

    # botão para efetuar login
    botao_1 = ctk.CTkButton(janela, text="Entrar", corner_radius=20, command=verificar_login)

    # botão para abrir a janela de cadastro
    botao_2 = ctk.CTkButton(janela, text="Cadastrar usuario", corner_radius=20, command=janela_cadastro)

    botao_2.place(x=500, y=300)
    botao_1.place(x=500, y=250)

    janela.mainloop()


def janela_cadastro():
    """Cria e exibe a janela secundária de cadastro de novo usuário."""

    # criando janela secundária (filha da janela principal)
    janela = ctk.CTkToplevel()
    janela.geometry("700x400")
    janela.resizable(width=False, height=False)

    # titulo da janela
    ctk.CTkLabel(janela, font=("arial bold", 20, "bold"), text="CADASTRO DE USUÁRIO").place(x=450, y=100)

    # carregando e exibindo imagem decorativa
    image_pc_2 = ctk.CTkImage(light_image=Image.open("imagens-janelas/pc_image_2.png"),
                              dark_image=Image.open("imagens-janelas/pc_image_2.png"),
                              size=(300, 300))
    ctk.CTkLabel(janela, image=image_pc_2, text=None).place(x=80, y=30)

    # campos de entrada para cadastro
    cadastro_usuario = ctk.CTkEntry(janela, placeholder_text="Usuario:", corner_radius=20)
    cadastro_senha = ctk.CTkEntry(janela, placeholder_text="Senha:", corner_radius=20, show="*")
    cadastro_senha_2 = ctk.CTkEntry(janela, placeholder_text="Repita a senha:", corner_radius=20, show="*")
    cadastro_usuario.place(x=500, y=150)
    cadastro_senha.place(x=500, y=200)
    cadastro_senha_2.place(x=500, y=250)

    def verificar():
        """Valida os campos antes de salvar o novo usuário no banco de dados."""
        if cadastro_senha.get() != cadastro_senha_2.get():
            # exibe erro se as senhas não coincidem
            error_senha = ctk.CTkLabel(janela, text="Usuário ou senhas incorretos",
                                       font=("arial bold", 14), text_color="white")
            error_senha.place(x=480, y=330)
        elif cadastro_usuario.get() == "":
            # exibe erro se o campo usuário estiver vazio
            erro_usuario = ctk.CTkLabel(janela, text="Usuario ou senhas incorretas",
                                        font=("arial bold", 14), text_color="white")
            erro_usuario.place(x=480, y=330)
        else:
            # tudo válido — salva o usuário no banco de dados
            banco_senhas(cadastro_usuario, cadastro_senha, cadastro_senha_2)

    # botão para enviar o cadastro
    botao_3 = ctk.CTkButton(janela, text="Enviar", corner_radius=20, command=verificar)
    botao_3.place(x=500, y=300)


def banco_senhas(cadastro_usuario, cadastro_senha, cadastro_senha_2):
    """Salva o novo usuário e senha no arquivo CSV, sem sobrescrever os dados existentes."""
    arquivo = "banco_de_senhas.csv"

    # cria um dataframe com os dados do novo usuário
    df = pd.DataFrame(columns=["usuario", "senha"])
    novo_usuario = pd.DataFrame([[cadastro_usuario.get(), cadastro_senha.get()]], columns=["usuario", "senha"])

    # adiciona ao CSV — cria o cabeçalho apenas se o arquivo ainda não existir
    novo_usuario.to_csv(arquivo, mode="a", header=not os.path.exists(arquivo), index=False)

    # limpa os campos após o cadastro
    cadastro_usuario.delete(0, END)
    cadastro_senha.delete(0, END)
    cadastro_senha_2.delete(0, END)


# ponto de entrada do programa
janela_login()