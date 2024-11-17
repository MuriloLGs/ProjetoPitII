Homebroker - Análise de Ações das 50 Maiores Empresas de Tecnologia
Descrição
Este projeto consiste em uma aplicação web interativa que permite visualizar as oscilações das ações das 50 maiores empresas de tecnologia listadas na bolsa de valores. Através de gráficos e dados de histórico de ações, o usuário pode analisar as flutuações do preço das ações ao longo do tempo.

A aplicação é desenvolvida utilizando Streamlit para a interface do usuário e yfinance para obter dados financeiros em tempo real. O projeto segue a arquitetura MVC (Model-View-Controller) para garantir uma boa organização do código.

Funcionalidades
Visualização de Ações: Exibe as oscilações das ações de até 2 empresas de tecnologia de uma vez.
Seleção de Empresas: Permite que o usuário escolha até 2 empresas entre as 50 mais valiosas de tecnologia para comparar.
Gráficos Interativos: Utiliza a biblioteca Altair para apresentar gráficos de preço de fechamento das ações ao longo do tempo.
Atualização em Tempo Real: Utiliza a API yfinance para buscar dados atualizados sobre as ações selecionadas.
Tecnologias Utilizadas
Python 3.x: Linguagem principal utilizada para desenvolvimento.
Streamlit: Framework para criação de interfaces web interativas.
yfinance: Biblioteca para obter dados financeiros em tempo real.
Pandas: Biblioteca para manipulação e análise de dados.
Altair: Biblioteca para criação de gráficos interativos.
MVC: Arquitetura utilizada para separar as responsabilidades do código em Model, View e Controller.
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/homebroker.git
cd homebroker
Crie e ative um ambiente virtual (opcional, mas recomendado):

Para Windows:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
Para Mac/Linux:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Estrutura de Pastas
A estrutura de pastas do projeto segue o padrão MVC (Model-View-Controller):

bash
Copiar código
homebroker/
│
├── model/ # Contém a lógica de manipulação de dados
│ ├── **init**.py
│ ├── financeiro.py # Funções de obtenção e manipulação de dados das ações
│
├── controller/ # Contém a lógica de controle entre Model e View
│ ├── **init**.py
│ ├── controller.py # Funções de controle para obter dados das ações e interagir com a View
│
├── view/ # Contém a interface do usuário
│ ├── **init**.py
│ ├── app.py # Interface Streamlit para exibição dos dados e gráficos
│
├── Dados/ # Contém os dados necessários para o funcionamento do app
│ └── acoes.json # Dados das 50 maiores empresas de tecnologia
Como Usar
Execute o arquivo Streamlit:

Navegue até a pasta view e execute o comando:

bash
Copiar código
streamlit run app.py
Interaja com a interface:

Na barra lateral, selecione até 2 empresas de tecnologia para comparar.
O gráfico exibirá a oscilação do preço de fechamento das ações das empresas selecionadas ao longo do tempo.
Exemplo de Uso
Seleção de Empresas: O usuário pode escolher até 2 empresas entre as 50 maiores de tecnologia, como Apple, Microsoft, Google, etc.
Gráfico Interativo: O gráfico irá mostrar a evolução do preço de fechamento das ações de cada empresa, permitindo comparações diretas entre elas.
Contribuições
Se você deseja contribuir para o projeto, siga os passos abaixo:

Faça um fork do repositório.
Crie uma branch para a sua feature (git checkout -b minha-nova-feature).
Faça commit das suas mudanças (git commit -am 'Adicionando nova feature').
Envie para o repositório remoto (git push origin minha-nova-feature).
Abra um Pull Request para revisar suas alterações.