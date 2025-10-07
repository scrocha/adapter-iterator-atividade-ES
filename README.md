# Adapter e Iterator - Atividade Guiada

## Objetivos de Aprendizagem
- Compreender o propósito e a aplicação dos padrões Adapter e Iterator.
- Implementar ambos os padrões e aplicar boas práticas de Engenharia de Software: documentação, tratamento de erros e testes unitários.

## Contexto do Problema
Uma equipe de Ciência de Dados precisa unificar o acesso a dados provenientes de diferentes fontes para análise posterior. Atualmente, há três origens distintas:
1. Um arquivo CSV local contendo registros tabulares.
2. Uma API externa que retorna dados em formato JSON.
3. Um objeto interno de uma classe Python que armazena dados manualmente.

Essas fontes são incompatíveis entre si, cada uma tem sua própria forma de fornecer dados. O objetivo é criar uma interface unificada que permita iterar sobre os registros sem que o código principal precise saber de onde vêm os dados.

## Padrões Utilizados

### Adapter
O padrão Adapter é utilizado para converter a interface de uma classe em outra interface esperada pelo cliente. Ele permite que classes com interfaces incompatíveis trabalhem juntas. Neste projeto, os adaptadores foram implementados para unificar o acesso às diferentes fontes de dados (CSV, API e objeto interno).

**Consequências de não usar o Adapter:**
- O código principal precisaria conhecer os detalhes de implementação de cada fonte de dados.
- A manutenção seria mais difícil, pois qualquer alteração em uma fonte exigiria mudanças no código principal.
- A reutilização de código seria limitada.

### Iterator
O padrão Iterator fornece uma maneira de acessar sequencialmente os elementos de uma coleção sem expor sua representação interna. Ele melhora a legibilidade e a manutenção do código ao encapsular a lógica de iteração.

**Como o Iterator melhora o código:**
- Separa a lógica de iteração da lógica de negócios.
- Permite alterar a forma como os dados são percorridos sem modificar o código principal.
- Facilita a implementação de diferentes estratégias de iteração (ex.: ordenação, reversão).

## Estrutura do Projeto
```
/atividade_adapter_iterator/
├── adapters.py # Contém as classes CSVAdapter, APIAdapter, ObjectAdapter
├── iterator.py # Classe DataIterator
├── main.py # Código principal (driver code)
├── tests/ # Módulo de testes unitários
│   ├── test_adapters.py
│   └── test_iterator.py
└── README.md # Instruções de execução e reflexão
```

## Instruções de Execução
1. Certifique-se de que o Python 3.11 (ou superior) está instalado.
2. Instale as dependências necessárias (se houver).
3. Execute o arquivo `main.py` para visualizar os resultados:
   ```bash
   python main.py
   ```
4. Para rodar os testes unitários, utilize o comando:
   ```bash
   pytest tests/
   ```

## Reflexão
- **Quais seriam as consequências de não usar o Adapter?**
  - O código principal ficaria preso às implementações específicas de cada fonte de dados, dificultando a manutenção e a escalabilidade.
- **Como o Iterator melhora a legibilidade e manutenção do código?**
  - Ele abstrai a lógica de iteração, permitindo que o código principal foque na lógica, sem se preocupar com os detalhes de como os dados são percorridos.