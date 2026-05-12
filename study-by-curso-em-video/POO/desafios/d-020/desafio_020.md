# Desafio 020

## Descrição
- Criar uma classe **Gamer**, onde poderá ser cadastrado **nome**, **nick** e os **jogos favoritos** de uma pessoa.
- Crie também um método que permita **mostrar a ficha** desse gamer.

### Exemplo do código de Instanciamento
```python
j1 = Gamer(
    nome:"Fabricio da Silva",
    nick:"detonator2025"
)

j1.add_favoritos(
    jogo:"Mario Bros."
)

j1.add_favoritos(
    jogo:"Sonic"
)

j1.add_favoritos(
    jogo:"God of War"
)

j1.add_favoritos(
    jogo:"Fortnite"
)

j1.ficha()

j2 = Gamer(
    nome:"Olívia Souza",
    nick:"peach_raivosa"
)

j2.add_favoritos(
    jogo:"Mario Bros."
)

j2.add_favoritos(
    jogo:"Call of Duty"
)

j2.ficha()
```

### Exemplo da Saída no terminal
| Jogador <detonator2025\> |
|--------------------------|
| Nome real: <span style="background-color:blue; color:white; padding:2px 10px"> Fabricio Silva </span> |
| Jogos Favoritos: |
| :video_game: <span style="color:blue">Fortnite</span> |
| :video_game: <span style="color:blue">Gof od War</span> |
| :video_game: <span style="color:blue">Mario Bros.</span> |
| :video_game: <span style="color:blue">Sonic</span> |

| Jogador <peach_raivosa\> |
|--------------------------|
| Nome real: <span style="background-color:blue; color:white; padding:2px 10px"> Olívia souza </span> |
| Jogos Favoritos: |
| :video_game: <span style="color:blue">Call of Duty</span> |
| :video_game: <span style="color:blue">Mario Bros.</span> |