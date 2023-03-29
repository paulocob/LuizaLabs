# LuizaLabs
Desafio Técnico

O Projeto armazenado neste repositório está organizado em duas principais pastas, denominadas simple_code e SOLID_applied. A primeira, simple_code realiza todo o processamento dos dados e disponibilização em JSON, implementada sob os conceitos de código simples e limpo. A segunda pasta, SOLID_applied, possui códigos que foram implementados de acordo com conceitos SOLID, além dos conceitos de código simples e limpo. 

Para execução do código o usuário deverá escolher uma das duas versões(simple_code ou SOLID_applied), caminhar até os arquivos desta pasta e executar o arquivo process_orders.py utilizando o seguinte comando: python process_orders.py

Basicamente, este código recebe os arquivos de dados que foram repassados e gera um arquivo JSON estruturado que é armazenado na mesma pasta do código que foi executado.

Outros artefatos adicionais também foram implementados e estão disponiveis neste repositório: um arquivo de teste, denominado "tests_process_orders.py" em que foram implementados testes para verificar se, ao receber uma entrada de dados conforme foi repassada, o código é capaz de retornar um JSON de acordo com a estrutura solicitada. Além disso, também foi desenvolvido um pipeline de CI/CD simples, utilizado e integrado para testar a execução do arquivo de testes ao realizar um novo commit + push no repositório.
