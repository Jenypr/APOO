# Caso de Uso: Atualizar Dados do Administrador

## **Atores Envolvidos**
- **Administrador**

---

## **Pré-condições**
- O administrador deve estar conectado à internet.
- O administrador deve estar cadastrado no sistema.

---

## **Pós-condições**
- Os dados do administrador devem estar atualizados no sistema.

---

## **Fluxo Principal – Atualizar Dados**
1. O administrador acessa a tela de atualização de dados.  
2. O sistema solicita o **ID do administrador**, que é o identificador único do usuário no sistema.  
3. O administrador informa o **ID** e os dados que deseja atualizar.  
4. O sistema utiliza o **ID informado** para localizar o administrador no banco de dados.  
5. O sistema atualiza os dados do administrador no banco de dados.  
6. O sistema redireciona o administrador para a área principal do sistema.

---

## **Fluxo Alternativo – ID não encontrado**
1. O administrador informa um **ID inválido**.  
2. O sistema não encontra o administrador no banco de dados.  
3. O sistema exibe uma **mensagem de erro**.  
4. O sistema retorna à **tela de atualização de dados**.