#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Esse programa tem como função utilizar a api do chat gpt para que se produza um chatbot próprio para a
empresa ou para benéficios pessoas, uma vez que utiliza as ferramentas da openzi e por conta disso
pode ser utilizado de diversas formas. 


# In[18]:


import openai
openai.api_key = "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"


# In[19]:


#Função para gerar texto a aprtir do modelo da linguagem.
def gera_texto(texto):
    #Obtém a resposta do modelo de linguagem.
    response = openai.Completion.create(
        #Tipo de modelo usado(existem outros tipos).
        engine = "text-davinci-003",
        #Texto inicial da conversa com o bot.
        prompt = texto,
        #comprimento da resposta gerada pelo modelo.
        max_tokens = 200,
        #Quantas conclusões gerar para cada prompt.
        n = 5,
        #Texto retornado não conterá a sequência de parada.
        stop = None,
        #Uma medida da aleatoridade do texto gerado, entre 0 e 1.
        #Valores proximo a 1 significam qua a saída é mais aleatória.
        temperature = 0.8,
    )
    
    return response.choices[0].text.strip()


# In[22]:


def main():
    print("\nBem vindo ao FelipeBot")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")
    #Loop.
    while True:
        #Coleta a pergunta digitada pelo usuário.
        user_message = input('\nVocê:')
        #Se a mendagem for 'sair', finaliza o programa.
        if user_message.lower() == "sair":
            break
        #Coloca a mensagem digitada pelo usuario em uma variavel chamada gpt3.
        gpt3 = f"\nUsuário: {user_message}\nFelipeBot:"
        #Obtém a resposta do modelo executando a função gera_texto().
        FelipeBot_response = gera_texto(gpt3)
        #Imprime a resposta do FelipeBot
        print(f"\nFelipebot: {FelipeBot_response}")
#Execução do programa main() 
if __name__ == "__main__":
    main()


# In[ ]:




