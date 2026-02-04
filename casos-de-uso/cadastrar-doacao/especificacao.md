# Caso de Uso: Cadastrar Doação

## Atores Envolvidos
- Doador

---

## Pré-condições
- O doador deve estar autenticado no sistema.

---

## Pós-condições
- A proposta de doação é registrada no sistema com status **Pendente**.

---

## Fluxo Principal
1. O doador informa os dados da doação (descrição, tipo e quantidade).  
2. O sistema valida os dados informados.  
3. O sistema registra a doação com status **Pendente**.  
4. O sistema exibe uma mensagem de confirmação ao doador.

---

## Fluxo de Exceção – Dados inválidos
- **2a.** Se algum campo obrigatório não for preenchido ou houver dados inválidos, o sistema solicita a correção das informações.

---

## Observação
A confirmação da doação pelo administrador é tratada em um caso de uso separado: **Confirmar Doação**.