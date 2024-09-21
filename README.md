# Flashcard App (Flashy)

## Introdução
Esse projeto foi feito para o estudo das palavras mais comuns do francês. A tradução das palavras está no inglês para a prática dos dois idiomas. 

![Flashy-demo](https://github.com/user-attachments/assets/4e305379-d376-4547-977f-e5c36b1366c5)


## Principais tecnologias e ferramentas utilizadas
* **Python (v3.12)**
* **Pandas Library**
* **Tkinter**

## Principais funcionalidades
### Flashcard frente e verso
O programa inicia mostrando o flashcard em francês. Após 3 segundos, o flashcard é virado revelando qual a tradução da palavra para o francês. 

![Flashcard-in-French](https://github.com/user-attachments/assets/5665e0be-d868-4c81-a352-e657b5fa6338)

![Flashcard-in-English](https://github.com/user-attachments/assets/47d5aa4a-2727-45b7-87a5-be0378c37758)

### Salvamento do progresso
As palavras são armazenadas no arquivo `french_words.csv`. Ao marcar o botão ✔️, o flashcard é apagado da lista e um novo arquivo é gerado contendo apenas as palavras que ainda não foram aprendidas para que sejam vistas nas próximas utilizações do programa. Ao marcar o botão ✖️, o programa segue para o próximo flashcard e mantém o anterior na lista. 
