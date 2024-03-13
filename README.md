# Automatização no Processo de Coleta de Dados com Selenium
Script em Python usando selenium. Projeto feito para automatizar a coleta de informações de pedidos na plataforma Logzz e repassar para o google sheets

# Pré-requisitos
Python 3<br>
Selenium<br>
Webdriver (Chrome, Firefox, etc.)<br>

# Como usar
1-Certifique-se de ter o Python e o Selenium instalados em seu ambiente de desenvolvimento<br>
2-Baixe o arquivo script.py deste repositório<br>
3-Abra o arquivo em um editor de texto e configure as credenciais de login e a URL do site conforme necessário<br>
4-Execute o script Python em seu vscode, terminal ou prompt de comando<br>

OBESERVAÇÕES:<br>
Este script está configurado para funcionar com o Chrome. Se você usar outro navegador, altere a variável driver no início do script<br>
O script faz login na plataforma Logzz automaticamente, mas você precisa resolver o reCAPTCHA manualmente no momento<br>
A etapa de acessar pedidos e escolher filtros precisa ser feita manualmente no momento<br>
O script coleta informações dos detalhes de cada pedido, como número do pedido, nome do cliente, entre outros (De acordo com XPATH usando no script)<br>
O script imprime os dados coletados no console<br>

# Melhorias
º Automatizar processo de recaptcha
º Implementar a seleção de filtros na página de pedidos<br>
º Enviar dados direto para planilha google sheets<br>

# Licença
Projeto não remunerado feito por parceria comercial. Auxilia no controle de rota, otimizando a coleta de dados dos clientes

# Dúvidas ou sugestões!?
Se você tiver dúvidas ou sugestões, sinta-se à vontade para compartilhar comigo
