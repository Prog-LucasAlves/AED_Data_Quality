# 📊 Data Quality Checker com Streamlit e Faker

Este projeto é uma aplicação em **Streamlit** para análise da qualidade de dados. Ele permite upload de **arquivos CSV** ou a **geração de dados falsos** para avaliação de qualidade. A análise inclui:

- ✅ Verificação de valores ausentes.
- ✅ Identificação de linhas duplicadas.
- ✅ Checagem de tipos de dados.
- ✅ Detecção de outliers.
- ✅ Visualização da distribuição das variáveis.

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (Interface gráfica)
- [Pandas](https://pandas.pydata.org/) (Manipulação de dados)
- [Numpy](https://numpy.org/) (Cálculos estatísticos)
- [Seaborn](https://seaborn.pydata.org/) e [Matplotlib](https://matplotlib.org/) (Visualização de dados)
- [Faker](https://faker.readthedocs.io/en/master/) (Geração de dados falsos)

## 📌 Como Instalar e Executar

1️⃣ **Clone o Repositório**

```bash
git clone https://github.com/Prog-LucasAlves/AED_Data_Quality.git
cd data_quality
```

2️⃣ **Instale as Dependências**
```bash
pip install -r requirements.txt
```

3️⃣ **Execute a aplicação**
```bash
streamlit run app.py
```

## 🔹 Como Usar a Aplicação

1️⃣ **Escolha a opção de análise:**

- Fazer upload de um arquivo CSV
- Gerar um dataset faker automaticamente

## 🔧 Personalização

Quer modificar os dados gerados? Edite a função generate_fake_data() no código para alterar os campos gerados.

## 📜 Licença

Este projeto está licenciado sob a MIT [License](https://github.com/Prog-LucasAlves/AED_Data_Quality/blob/main/LICENSE) - veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

- Quer contribuir? Siga os passos:

1️⃣ Faça um fork do projeto
2️⃣ Crie uma branch com sua feature (git checkout -b minha-feature)
3️⃣ Commit suas mudanças (git commit -m 'Minha nova feature')
4️⃣ Faça um push para a branch (git push origin minha-feature)
5️⃣ Abra um Pull Request

☁️ Extra Deploy: https://aed-data-quality.onrender.com/
