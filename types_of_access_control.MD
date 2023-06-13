**Controle de Acesso em Tecnologia da Informação (TI)**

Existem três principais formas de controle de acesso amplamente utilizadas em Tecnologia da Informação (TI) para proteger sistemas, redes e dados. São elas:

1. Controle de Acesso Baseado em Identidade (IBAC):
O controle de acesso baseado em identidade (IBAC) é uma abordagem em que o acesso aos recursos é concedido ou negado com base nas identidades dos usuários. Cada usuário é autenticado individualmente e recebe um conjunto específico de permissões com base em sua identidade. Isso é realizado por meio do gerenciamento de identidades, autenticação e atribuição de permissões específicas para cada usuário ou grupo de usuários.

2. Controle de Acesso Baseado em Função (RBAC):
O controle de acesso baseado em função (RBAC) é uma abordagem em que o acesso aos recursos é determinado pelas funções ou cargos atribuídos a cada usuário. Nesse modelo, os usuários são agrupados em diferentes funções com base em suas responsabilidades dentro da organização. Cada função possui um conjunto predefinido de permissões associadas, e os usuários herdam essas permissões ao serem atribuídos a uma função específica. Isso simplifica a administração de permissões, uma vez que as mudanças podem ser aplicadas a nível de função em vez de afetar cada usuário individualmente.

3. Controle de Acesso Baseado em Regras (RBAC):
O controle de acesso baseado em regras (RBAC) é uma abordagem em que o acesso aos recursos é determinado por um conjunto de regras predefinidas. Essas regras são definidas com base em condições específicas, como características do usuário, horário, localização ou outros critérios relevantes. As regras são aplicadas para determinar se um usuário tem permissão para acessar um recurso ou executar uma determinada ação com base nas condições estabelecidas.

Essas três formas de controle de acesso podem ser implementadas de maneira isolada ou combinada, dependendo dos requisitos de segurança e das necessidades da organização. Cada uma delas tem suas vantagens e é aplicável em diferentes cenários, proporcionando uma estrutura flexível e granular para gerenciar o acesso aos recursos de TI.





**Aplicação do conceito em uma empresa real: Utilizamos neste caso, o Google Drive**


**O Google Drive utiliza as três formas de controle de acesso - Controle de Acesso Baseado em Identidade (IBAC), Controle de Acesso Baseado em Função (RBAC) e Controle de Acesso Baseado em Regras (RBAC) - para gerenciar e controlar o acesso aos arquivos e pastas armazenados na plataforma. Vamos ver como cada um desses controles de acesso é aplicado no Google Drive:**

1. Controle de Acesso Baseado em Identidade (IBAC):
   - O Google Drive utiliza contas do Google para autenticação e controle de acesso baseado em identidade. Cada usuário precisa ter uma conta do Google e fazer login com suas credenciais para acessar o Google Drive. Isso garante que apenas usuários autenticados tenham acesso aos recursos do Google Drive. Além disso, o Google oferece recursos de autenticação em dois fatores para adicionar uma camada extra de segurança às contas.

2. Controle de Acesso Baseado em Função (RBAC):
   - O Google Drive incorpora o controle de acesso baseado em função por meio do compartilhamento de arquivos e pastas. O proprietário de um arquivo ou pasta no Google Drive tem controle total sobre as permissões de acesso. Eles podem atribuir funções específicas aos usuários, como "visualizador", "comentarista" ou "editor", com base nas necessidades de colaboração. Essas funções definem as permissões de acesso para cada usuário ou grupo de usuários, permitindo um controle mais granular.

3. Controle de Acesso Baseado em Regras (RBAC):
   - O Google Drive suporta o controle de acesso baseado em regras por meio das configurações de compartilhamento avançadas. Ao compartilhar um arquivo ou pasta, é possível definir regras específicas que determinam o acesso com base em condições predefinidas. Por exemplo, é possível configurar uma regra que concede acesso apenas a usuários específicos com base em suas contas do Google ou domínios associados. Além disso, o Google Drive permite definir datas de expiração para compartilhamentos e limitar o número de downloads de um arquivo compartilhado.

Essas três formas de controle de acesso são implementadas no Google Drive para garantir que os usuários tenham acesso seguro e controlado aos arquivos e pastas. Elas permitem que os proprietários de arquivos definam permissões específicas para cada usuário ou grupo de usuários, estabeleçam regras de compartilhamento personalizadas e controlem o acesso com base na identidade dos usuários. Isso ajuda a proteger a confidencialidade e a integridade dos dados armazenados no Google Drive.

**DEMONSTRAÇÃO DO CONTROLE DE ACESSO BASEADO EM IDENTIDADE NO GOOGLE DRIVE**

![image](https://github.com/mcruvinel/redes/assets/99694882/cfe240cd-cf3a-4de1-9891-ca7e64c20d73)


**AUTENTICAÇÃO DE DOIS FATORES, AINDA NO CONTROLE DE ACESSO BASEADO EM IDENTIDADES**

![image](https://github.com/mcruvinel/redes/assets/99694882/8520e5f2-cb9b-4288-b051-114e4c657fe3)
![image](https://github.com/mcruvinel/redes/assets/99694882/5a3311d5-dff2-4ec7-ada9-4b1d535de24f)


**CONTROLE DE ACESSO BASEADO EM FUNÇÃO**

![image](https://github.com/mcruvinel/redes/assets/99694882/5f349631-2fa5-430c-bf59-9a0bb8e8c0c8)

**AO COMPARTILHAR A PASTA, COMO SOU O ADMNISTRADOR E CRIADOR, CONSIGO DEFINIR FUNÇÃO AO NOVO INTEGRANTE, E ESSAS FUNÇÕES LHE GARANTEM ALGUNS ACESSOS, COMO EDITAR, INCLUIR E APAGAR ARQUIVOS, OU SOMENTE VISUALIZA-LOS**

![image](https://github.com/mcruvinel/redes/assets/99694882/52eb5cf9-5ca2-493a-9704-28d0d8f43856)


**CONTROLE DE ACESSO BASEADO EM REGRA**
Aqui, adicionei uma foto ao google drive
![image](https://github.com/mcruvinel/redes/assets/99694882/f6a0f63a-269e-42b5-8391-107c2ffecc7c)

E ao compartilha-la, posso preestabelecer regras de acesso a esse arquivo, como permitir ou não o download!!
![image](https://github.com/mcruvinel/redes/assets/99694882/a4c1eecf-efa6-4155-9112-6b1c8465587a)

Ou posso selecionar somente pessoas que podem acessa-las, liberando o email delas (identidade) ou posso deixar qualquer pessoa com o link acessar:
![image](https://github.com/mcruvinel/redes/assets/99694882/040a8edc-460a-4a94-ae4a-bc1b46c269b9)

E para encerrar, todos nos sabemos que o nome do arquivo é falso, o Vasco nao tem mundial!
![image](https://github.com/mcruvinel/redes/assets/99694882/40918dd1-8e6d-420a-ae0c-c483e64204a1)

