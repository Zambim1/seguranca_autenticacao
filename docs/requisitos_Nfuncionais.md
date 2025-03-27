# REQUISITOS NÃO FUNCIONAIS

## 1. Segurança

Garantir a proteção dos dados e da integridade do sistema contra ataques comuns.

### Requisitos  
| Requisito | Descrição |
|-----------|-----------|
| Hash de senhas | Senhas devem ser armazenadas com hash seguro (bycript) |
| Proteção contra ataques | Implementar medidas contra ataques comuns (SQL Injection, XSS, CSRF). |
| Criptografia de dados sensíveis | Informações sensíveis devem ser armazenadas criptografadas. |

## 2. Modularidade
 
O sistema deve ser projetado para facilitar futuras integrações com outras aplicações.

### Requisitos  
| Requisito | Descrição |
|-----------|-----------|
| Arquitetura modular | O sistema deve ser dividido em módulos reutilizáveis. |
| Integração com APIs | Permitir fácil integração com serviços externos. |
| Separação de responsabilidades | Código organizado em camadas (MVC). |

## 3. APIs Bem Documentadas

Facilitar o reaproveitamento e integração das funcionalidades do sistema por meio de APIs documentadas.

### Requisitos  
| Requisito | Descrição |
|-----------|-----------|
| Documentação clara | APIs devem conter documentação detalhada (OpenAPI/Swagger). |
| Exemplos de uso | Disponibilizar exemplos práticos para desenvolvedores. |
| Versionamento | Manter versionamento adequado para evitar impactos em integrações. |

## 4. Escalabilidade e Performance
 
Garantir que o sistema possa crescer de forma eficiente e suportar alta carga.

### Requisitos  
| Requisito | Descrição |
|-----------|-----------|
| Suporte a alta carga | O sistema deve ser capaz de lidar com múltiplas requisições simultâneas. |
| Banco de dados otimizado | Indexação e otimização de consultas para melhorar a performance. |
| Balanceamento de carga | Permitir escalabilidade horizontal com múltiplos servidores. |