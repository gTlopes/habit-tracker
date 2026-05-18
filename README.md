# Habit Tracker

## Aplicação Online

Acesse a aplicação:
https://entrega-intermediaria-bootcamp.streamlit.app/

---

## Sobre o Projeto

O Habit Tracker é uma aplicação desenvolvida para auxiliar pessoas na criação e acompanhamento de hábitos diários, incentivando organização pessoal, disciplina e bem-estar.

A aplicação também integra dados climáticos em tempo real utilizando a API pública Open-Meteo, incentivando hábitos saudáveis como hidratação diária.

## Problema

Muitas pessoas enfrentam dificuldades para manter hábitos saudáveis no dia a dia, como beber água regularmente, estudar ou praticar atividades físicas.

## Solução

Aplicação em linha de comando (CLI) que permite registrar e acompanhar hábitos diários.

## Público-alvo

Qualquer pessoa que deseja melhorar sua rotina.

## Funcionalidades

- Adicionar hábitos
- Listar hábitos
- Concluir hábitos
- Remover hábitos
- Persistência de dados em JSON
- Integração com API de clima
- Interface CLI
- Interface Web com Streamlit
- Testes automatizados
- Integração contínua com GitHub Actions

## Funcionalidade de clima

A aplicação consome a API pública Open-Meteo para exibir a temperatura atual e incentivar hábitos saudáveis como hidratação diária.

## Tecnologias

* Python
* Pytest
* Ruff

## Execução

pip install -r requirements.txt
python src/app.py

## Testes

python -m pytest

## Lint

ruff check .

## Versão

1.0.0

## Autor

Gustavo Soares Lopes

## Repositório

https://github.com/gTlopes/habit-tracker

## Exemplo de uso (PRINT)

https://prnt.sc/7PWgE0MxNR-J
