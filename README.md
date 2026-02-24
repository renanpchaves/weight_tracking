# 📉 Weight Tracking App:

Um script simples em Python para visualizar a variação de peso ao longo do tempo, com regressão linear para demonstrar tendência.

## Sobre:

Esse projeto trata do meu caso específico, coletando dados ao longo do tempo. Os dados preenchidos são somente a data e o peso (em kg). Gera um gráfico em alta resolução, com duas linhas: uma dos dados coletados em específico (em azul), e a outra determinando a tendência dos próximos registros (em vermelho). 

Esses dados são coletados a partir do arquivo **`data.csv`**, integrados ao script principal através do arquivo **`data.py`**.

## Exemplo de Output:

O script gera um arquivo chamado `weight_progress_high_resolution.png` com um gráfico, mostrando os seguintes valores:

- **Linha azul**: Perda de peso com o tempo
- **Linha vermelha**: Tendência linear (regressão)

## Requerimentos:

- Python 3.x
- `matplotlib`
- `numpy`

Instale as dependências pelo terminal com pip:

```bash
pip install matplotlib numpy
```

## Uso:

1. Edite a lista no arquivo data.csv com seus próprios registros. Datas precisam ser no formato `DD/MM/YYYY`.

2. Rode o script:

```bash
python main.py
```