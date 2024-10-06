# Desafio Smarti
Este repositório contém uma API desenvolvida em Python utilizando o framework FastAPI, como parte do desafio técnico para a vaga de Desenvolvedor BackEnd Jr. Abaixo estão as instruções para que você possa clonar o repositório e rodar o projeto localmente utilizando uma IDE como VSCode ou PyCharm.

## Pré-Requisitos
Certifique-se de que você tenha os seguintes itens instalados:

1. Git: Para clonar o repositório. <br/>
Instalação: <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">Instruções para instalar o Git.</a>

2. Python: Linguagem de programação utilizada no projeto. <br/>
Instalação: <a href="https://www.python.org/downloads/">Instruções para instalar o Python.<a/> <br/>
<strong>Certifique-se de que você tenha a versão 3.10 ou superior.</strong>

3. IDE: Recomendo o uso de <a href="https://code.visualstudio.com/">VSCode</a> ou <a href="https://www.jetbrains.com/pycharm/">PyCharm.</a>

## Passo a Passo
1. <strong>Clonando Repositório e entrando na pasta raíz do projeto</strong>
    ```bash
    git clone https://github.com/Caio-Sdk8/Desafio_Smarti.git
    cd Desafio_Smarti
    ```
2. <strong>Abrindo o projeto na IDE (Atenção, abra a pasta DesafioSmarti e não a pasta principal do repositório)</strong>
<br/><p>Confira se está na pasta correta. <br/>Abra a pasta na IDE previamente instalada<p/>
3. <strong>Instale as dependências do projeto (no terminal da sua IDE)</strong>
   ```bash
    pip install -r requirements.txt
    ```
4. <strong>Ainda no terminal, rode o projeto com o comando abaixo</strong>
   ```bash
    uvicorn main:app --reload
    ```
5. <strong>Se tudo der certo aparecerá algo como:</strong>
    ```bash
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```
    <br/>
    <p>Caso dê certo, acesse a api pela url http://127.0.0.1:8000/docs para ter acesso a documentação swagger <br/> Em caso de erro sinta-se livre para me contatar, para que assim eu possa te ajudar a rodar este projeto.</p>

## Referências utilizadas
- https://www.geeksforgeeks.org/fastapi-sqlite-databases/
- https://medium.com/@shaliamekh/clean-architecture-with-python-d62712fd8d4f
- https://fastapi.tiangolo.com/pt/tutorial/#rode-o-codigo
- https://youtu.be/4Cp8gPl6aZU?si=5Tm32wXP-2MH4_iU
- https://youtu.be/sRGpvbhOhQs?si=qqlG9kcJlhL0k2cW

## Sobre o projeto
Deseja saber mais sobre mim ou sobre o projeto, nesse vídeo do youtube (https://youtu.be/jGsVh66TEh4) conto um pouco sobre ele, e sobre mim é só mandar uma mensagem ou e-mail.
