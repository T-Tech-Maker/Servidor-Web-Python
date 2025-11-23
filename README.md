#  Servidor Web Simples em Python

Este projeto implementa um servidor Web básico capaz de lidar com uma única requisição HTTP GET, retornando o arquivo solicitado ou uma resposta **`404 Not Found`** se o arquivo não existir.

##  Pré-requisitos

  * **Python:** É necessário ter o Python instalado na sua máquina (versão 3.x recomendada).

##  Como Rodar o Servidor

Siga os passos abaixo para configurar e executar seu servidor Web.

### 1\. Como Executar o Servidor

1.  **Abra o Terminal/Prompt de Comando** e navegue até o diretório onde você salvou os arquivos.

2.  **Execute o script Python** usando o comando:

    ```bash
    python webserver.py
    ```

3.  O servidor será iniciado e exibirá a mensagem de status:

    ```
    Ready to serve...
    ```

### 2\. Testar a Conexão no Navegador

Enquanto o servidor estiver em execução, abra seu navegador de preferência para enviar requisições.

#### Teste 1: Arquivo Existente (200 OK)

Digite o seguinte endereço na barra de navegação para solicitar o arquivo de teste:

```
http://127.0.0.1:6789/HelloWorld.html
```

  * **`127.0.0.1`**: O endereço de *loopback* (sua máquina local).
  * **`6789`**: A porta utilizada pelo servidor Python.

**Resultado Esperado:** Você deverá ver a página com o texto **"Hello, World\!"**.

#### Teste 2: Arquivo Não Existente (404 Not Found)

Tente acessar um arquivo que você sabe que não existe no diretório do servidor:

```
http://127.0.0.1:6789/naoexiste.html
```

**Resultado Esperado:** O navegador deverá exibir uma mensagem de erro indicando **"404 Not Found"** ou um conteúdo similar, conforme definido na sua lógica de tratamento de erro no `webserver.py`.

-----

>  **Nota:** Se a porta `6789` já estiver em uso por outro serviço Web em sua máquina, você deverá alterar o número da porta no seu script `webserver.py` e usá-la no endereço de acesso.
