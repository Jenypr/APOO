# Caso de Uso: Confirmar Doação

## Atores Envolvidos
- Administrador

---

## Pré-condições
- O administrador deve estar autenticado no sistema.  
- Deve existir uma proposta de doação previamente cadastrada.

---

## Pós-condições
- A proposta de doação terá seu status atualizado para **Aceita** ou **Rejeitada** no sistema.

---

## Fluxo Principal – Aceitar Doação
1. O administrador visualiza a lista de propostas de doação.  
2. O administrador seleciona uma proposta específica.  
3. O administrador confirma a proposta.  
4. O sistema atualiza o status da doação para **Aceita**.  
5. O sistema armazena a atualização no banco de dados.  
6. O sistema exibe uma mensagem de confirmação ao administrador.

---

## Fluxo Alternativo – Rejeitar Doação
1. O administrador visualiza a proposta de doação.  
2. O administrador rejeita a proposta.  
3. O sistema atualiza o status da doação para **Rejeitada**.  
4. O sistema armazena a atualização no banco de dados.  
5. O sistema exibe o status da doação ao doador.