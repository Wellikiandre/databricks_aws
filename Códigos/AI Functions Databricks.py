# Databricks notebook source
# MAGIC %md
# MAGIC # AI Functions Databricks
# MAGIC
# MAGIC ### Resumido por : Wellikiandre Martins
# MAGIC
# MAGIC ##### Se você ainda não me segue nas minhas redes sociais, ficarei muito feliz em conectar com você por lá. Acompanhe meu trabalho e conteúdos sobre dados, tecnologia, e muito mais:
# MAGIC
# MAGIC - Hub: https://datacementhub.substack.com/
# MAGIC - Datacement: https://datacement.com.br/
# MAGIC - Instagram: https://www.instagram.com/wellikiandre/
# MAGIC - LinkedIn: https://www.linkedin.com/in/wellikiandre/
# MAGIC - YouTube: https://www.youtube.com/@wellikiandre
# MAGIC
# MAGIC ###### Obrigado novamente pelo seu apoio! Vamos continuar aprendendo e evoluindo juntos!
# MAGIC ####### Documentação oficial: [LInk](https://learn.microsoft.com/en-us/azure/databricks/large-language-models/ai-functions)

# COMMAND ----------

# MAGIC %md
# MAGIC 1. **ai_query**
# MAGIC    -  **"Descrição"** A função ai_query é usada para invocar um modelo de IA específico para processar um prompt fornecido pelo usuário. No exemplo fornecido, o modelo databricks-meta-llama-3-1-70b-instruct é utilizado para analisar o conteúdo do campo message_response e retornar o motivo da falha, incluindo campos de erros ou avisos.
# MAGIC
# MAGIC 2. **ai_analyze_sentiment**
# MAGIC    - **Descrição:** Retorna o sentimento de um texto.
# MAGIC    - **Problema Resolvido:** Útil para análise de sentimentos em textos, como avaliações de clientes, postagens em redes sociais, ou qualquer outro conteúdo textual onde se deseja entender a opinião ou emoção expressa.
# MAGIC
# MAGIC 3. **ai_classify**
# MAGIC    - **Descrição:** Classifica o conteúdo fornecido em um dos rótulos fornecidos.
# MAGIC    - **Problema Resolvido:** Usada para categorizar textos em diferentes classes ou categorias, como classificar e-mails como "spam" ou "não spam", ou categorizar notícias em tópicos como "esportes", "política", "tecnologia", etc.
# MAGIC
# MAGIC 4. **ai_extract**
# MAGIC    - **Descrição:** Extrai entidades especificadas por rótulos de um texto dado.
# MAGIC    - **Problema Resolvido:** Útil para extração de informações específicas de textos, como nomes de pessoas, locais, datas, etc., em processamento de linguagem natural (NLP) para estruturar dados não estruturados.
# MAGIC
# MAGIC 5. **ai_fix_grammar**
# MAGIC    - **Descrição:** Corrige erros gramaticais em um texto dado.
# MAGIC    - **Problema Resolvido:** Melhora a qualidade do texto corrigindo erros gramaticais, tornando-o mais legível e profissional. Útil para revisão de textos, correção de redações, e-mails, documentos, etc.
# MAGIC
# MAGIC 6. **ai_gen**
# MAGIC    - **Descrição:** Invoca um modelo de IA generativo das APIs do Databricks Foundation Model para responder ao prompt fornecido pelo usuário.
# MAGIC    - **Problema Resolvido:** Gera texto baseado em um prompt fornecido. Útil para criação de conteúdo, respostas automáticas, geração de diálogos, etc.
# MAGIC
# MAGIC 7. **ai_mask**
# MAGIC    - **Descrição:** Mascará entidades especificadas dentro de um texto dado.
# MAGIC    - **Problema Resolvido:** Útil para anonimização de dados, ocultando ou substituindo informações sensíveis como nomes, endereços, números de telefone, etc., para proteger a privacidade.
# MAGIC
# MAGIC 8. **ai_similarity**
# MAGIC    - **Descrição:** Compara duas strings e calcula a pontuação de similaridade semântica.
# MAGIC    - **Problema Resolvido:** Mede a similaridade entre dois textos. Útil em sistemas de recomendação, verificação de plágio, correspondência de documentos, etc.
# MAGIC
# MAGIC 9. **ai_summarize**
# MAGIC    - **Descrição:** Gera um resumo de um texto dado.
# MAGIC
# MAGIC 10. **ai_translate**
# MAGIC    -  **Descrição:** Traduza o texto para um idioma alvo especificado. Problema Resolvido: Esta função é usada para tradução automática de textos entre diferentes idiomas, facilitando a comunicação e acessibilidade de conteúdo para falantes de diferentes línguas.
# MAGIC
# MAGIC 11. **ai_query**
# MAGIC    -  **"Descrição"** A função ai_query é usada para invocar um modelo de IA específico para processar um prompt fornecido pelo usuário. No exemplo fornecido, o modelo databricks-meta-llama-3-1-70b-instruct é utilizado para analisar o conteúdo do campo message_response e retornar o motivo da falha, incluindo campos de erros ou avisos.

# COMMAND ----------

# DBTITLE 1,ai_query
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW api_responses AS
# MAGIC SELECT 'Erro: Campo "username" é obrigatório.' AS message_response;
# MAGIC
# MAGIC -- Use a função ai_query para analisar a resposta da API
# MAGIC SELECT ai_query(
# MAGIC     'databricks-meta-llama-3-1-70b-instruct', 
# MAGIC     CONCAT('O campo message_response é a resposta de uma API, me retorne o motivo da falha, incluindo se houver campos de erros ou se houver campos de avisos.', message_response)
# MAGIC ) AS resposta_falha
# MAGIC FROM api_responses;

# COMMAND ----------

# DBTITLE 1,ai_analyze_sentiment
# MAGIC %sql
# MAGIC select ai_analyze_sentiment(descricao_user) as resposta_Exemplo from xxxx

# COMMAND ----------

# DBTITLE 1,ai_classify
# MAGIC %sql
# MAGIC select ai_classify("Este é um e-mail de phishing.",array("spam", "não spam")) as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_extract
# MAGIC %sql
# MAGIC select ai_extract("John Doe nasceu em 5 de maio de 1990 em Nova York.",array("nome", "data", "local") ) as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_fix_grammar
# MAGIC %sql
# MAGIC select ai_fix_grammar("Eu gost# d# programar em Python.") as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_gen
# MAGIC %sql
# MAGIC select ai_gen("Escreva uma história curta sobre um dragão e um cavaleiro.") as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_mask
# MAGIC %sql
# MAGIC select ai_mask('Foi feita uma venda para o cpf 13983182129, cujo endereço é avenida faria lima numero 3293',array("cpf", "endereço", "numero")) as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_similarity
# MAGIC %sql
# MAGIC     select ai_similarity("eu gosto de maças", "eu como maças") as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_summarize
# MAGIC %sql
# MAGIC select ai_summarize("Databricks é uma plataforma de análise de dados que unifica engenharia de dados, ciência de dados e aprendizado de máquina. 
# MAGIC Ela permite que as empresas processem grandes volumes de dados e extraiam insights valiosos.") as resposta_Exemplo

# COMMAND ----------

# DBTITLE 1,ai_translate
# MAGIC %sql
# MAGIC select ai_translate('I Love you Databricks','pt-br') as resposta_Exemplo
