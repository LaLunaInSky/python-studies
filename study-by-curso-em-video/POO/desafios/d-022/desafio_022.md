# Desafio 022

## Descrição
- Criar uma classe **ControleRemoto**, onde **simulará** o funcionamento de um controle simples (**canal**, **volume** e **liga**/**desliga**) 

### Exemplo da Saída no terminal
- TV Desligada

| [TV\] |
|-------|
|:no_entry_sign: <span style="color:red; margin:0px 5px">A TV está desligada </span> |

<span style="margin:0px 5px"><</span>CH1<span style="margin:0px 5px">></span> <span style="margin-left:20px"><span style="margin:0px 5px">-</span> VOL2 <span style="margin:0px 5px">+</span></span> <span style="background-color:gray; padding:3px 5px; margin-left:8px"></span>

- TV Ligada - canal 1 - volume 2
(Modelo quando liga a TV)

| [TV\] |
|-------|
| <span style="padding:0px 7px">CANAL</span> = <span style="color:yellow; background-color:#8B8000; padding:1px 6px; margin-right:5px">1</span> <span style="padding:1px 6px; margin-right:5px">2</span> <span style="padding:1px 6px; margin-right:5px">3</span> <span style="padding:1px 6px; margin-right:5px">4</span> <span style="padding:1px 6px">5</span> |
| VOLUME = <span style="background-color:#008b8b; padding:0px 25px; margin-left:5px"></span><span style="background-color:#d3d3d3; padding:0px 46px"></span> |

<span style="margin:0px 5px"><</span>CH1<span style="margin:0px 5px">></span> <span style="margin-left:20px"><span style="margin:0px 5px">-</span> VOL2 <span style="margin:0px 5px">+</span></span> <span style="background-color:gray; padding:3px 5px; margin-left:8px"></span>

- TV Ligada - canal 3 - volume 5

| [TV\] |
|-------|
| <span style="padding:0px 7px">CANAL</span> = <span style="padding:1px 6px; margin-right:5px">1</span> <span style="padding:1px 6px; margin-right:5px">2</span> <span style="color:yellow; background-color:#8B8000; padding:1px 6px; margin-right:5px">3</span> <span style="padding:1px 6px; margin-right:5px">4</span> <span style="padding:1px 6px">5</span> |
| VOLUME = <span style="background-color:#008b8b; padding:0px 71px; margin-left:5px"></span><span style="background-color:#d3d3d3; padding:0px 0px"></span> |

<span style="margin:0px 5px"><</span>CH3<span style="margin:0px 5px">></span> <span style="margin-left:20px"><span style="margin:0px 5px">-</span> VOL5 <span style="margin:0px 5px">+</span></span> <span style="background-color:gray; padding:3px 5px; margin-left:8px"></span>

- TV Ligada - canal 5 - volume 0

| [TV\] |
|-------|
| <span style="padding:0px 7px">CANAL</span> = <span style="padding:1px 6px; margin-right:5px">1</span> <span style="padding:1px 6px; margin-right:5px">2</span> <span style="padding:1px 6px; margin-right:5px">3</span> <span style="padding:1px 6px; margin-right:5px">4</span> <span style="color:yellow; background-color:#8B8000; padding:1px 6px">5</span> |
| VOLUME = <span style="background-color:#008b8b; padding:0px 0px; margin-left:5px"></span><span style="background-color:#d3d3d3; padding:0px 71px"></span> |

<span style="margin:0px 5px"><</span>CH3<span style="margin:0px 5px">></span> <span style="margin-left:20px"><span style="margin:0px 5px">-</span> VOL0 <span style="margin:0px 5px">+</span></span> <span style="background-color:gray; padding:3px 5px; margin-left:8px"></span>