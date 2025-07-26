<div align="center" id="topo">

<img src="https://media.giphy.com/media/iIqmM5tTjmpOB9mpbn/giphy.gif" width="200px" alt="Gif animado"/>

# <code><strong>Resolução de Sistemas Lineares pelo Método de Gauss-Seidel</strong></code>

<em>Primeiro trabalho da disciplina de Análise Numérica com foco em implementar o método de Gauss-Seidel para resolução de sistemas lineares.</em>

[![Python Usage](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge\&logo=python)]()
[![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)]()
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Visite%20meu%20perfil-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rian-carlos-valcanaia-b2b487168/)

</div>

## Índice

- [📌 Objetivos](#-objetivos)
- [📥 Entradas do sistema](#-entradas-do-sistema)
- [🧰 Funcionalidades](#-funcionalidades)
- [📂 Como executar](#-como-executar)
- [👨‍🏫 Envolvidos](#-envolvidos)
- [📅 Curso](#-curso)
- [📄 Código-fonte](#-código-fonte)

## 📌 Objetivos

- Implementar o **método de Gauss-Seidel** em Python.
- Realizar o **teste de convergência** baseado no critério de linhas (diagonal dominante).
- Aplicar **troca de linhas** quando necessário para satisfazer o critério.
- Avaliar a **qualidade do ajuste** utilizando o **vetor resíduo** `r = Ax - b`.

## 📥 Entradas do sistema

Sistema linear resolvido:

  7x₁ +  x₂ -  x₃ + 4x₄ = -10  
  x₁  - 5x₂ +  x₃ - 2x₄ =   2  
  x₁  +     3x₃ -  x₄ =  11  
  3x₁ +  x₂ - 3x₃ + 8x₄ = -24

- **Chute inicial**: `[-0.3, 1.3, 2.8, -2.3]`
- **Critério de parada**: ε ≤ 0.0005

## 🧰 Funcionalidades

- `casas_precisao()` — informa o número de casas necessárias para atingir o critério de convergência
- `ajusta_convergencia()` — verifica e ajusta a matriz para satisfazer o critério de linhas
- `arredondamento()` — arredonda o número conforme norma
- `gauss_seidel()` — resolve o sistema linear iterativamente
- `qualidadeAjusteVetorResiduo()` — calcula o vetor resíduo r = Ax - b 
- `print_matriz()` — exibe a matriz formatada em forma matricial

## 📊 Resultados esperados

- Vetor solução aproximada x̄:
  ```
  [0.00004, 1.00002, 2.99993, -2.00004]
  ```

- Vetor resíduo:
  ```
  [0.00021, -0.00005, -0.00013, 0.00003]
  ```

## 📂 Como executar

1. Copie o código do arquivo "trabalho.py" no [Google Colab](https://colab.research.google.com)
2. Rodar as células passo a passo
3. Os resultados serão exibidos no console

Ou fazendo o dowload e rodar com:
```bash
python3 trabalho.py
```


## 👨‍🏫 Envolvidos

- Professor: Jarbas Ferrari
- Estudantes:
  - [Lucas Macedo](https://github.com/lucasomac0)
  - [Rian Carlos Valcanaia](https://github.com/RianValcanaia)

## 📅 Curso

- Universidade: Universidade do Estado de Santa Catarina (UDESC)
- Disciplina: Análise Numérica
- Semestre: 4º

## 📄 Código-fonte

🔗 [https://github.com/RianValcanaia/ANN_TC1_Metodo_Gauss_Seidel](https://github.com/RianValcanaia/ANN_TC1_Metodo_Gauss_Seidel)

[⬆ Voltar ao topo](#topo)

