# Jogo de Bingo automatizado (Python)
  Simulador de jogo de bingo desenvolvido em Python com geração automatizadas de cartelas e validação de regras de vitória. 

# Funcionalidades
  Geração de Cartela Personalizada: Cria uma grade 5x5 com números aleatórios organizados por faixas de colunas (B, I, N, G, O), inserindo a sigla do jogador no centro exato da cartela.
  
  Menu Interativo: Sistema controlado por loop contínuo para navegar entre a geração, definição de regras e o sorteio.
  
  Sorteador Inteligente (Globo de Pedras): Sorteia números de 1 a 75 sem repetição e exibe o histórico de pedras já sorteadas em ordem crescente.
  
  
  Validação de Vitória Dupla: Sistema capaz de verificar ganhadores tanto pela regra tradicional de "Cartela Cheia" quanto pelas regras de "Linha, Coluna ou Diagonal" através de varredura cruzada.

# Tecnologias e Conceitos Aplicados
   Lógica de programação estruturada e modularização com funções (`def`).
   Estruturas matriciais avançadas (Matrizes: Listas dentro de Listas `[[]]`).
   Geração de números pseudoaleatórios com a biblioteca `random`.
   Manipulação e formatação de Strings (máscara de exibição de zeros à esquerda com `:02d`).
   Ordenação de dados em tempo real utilizando o método `sorted()`.

