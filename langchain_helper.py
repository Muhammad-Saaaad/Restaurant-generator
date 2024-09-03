from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda

prompt = ChatPromptTemplate.from_messages([
    ('system','''You are a wordwide food expert and you only give me the restrunt name for a specfic contary
     and there should be 1 answer and answer should be different and unique everytime'''),
    ('human','I want to open a resturant for {cuisine} food, Can you kindly suggest me a name for this')
])

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash" , api_key='AIzaSyA77gUQw_Fzk2L4hJx_6fzQOSZipJn_ZTg')


def food_prompt(restrunt_name):
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system','''You are a expert food reviewer and you will tell me the menu for restrunts for a 
             specfic contary and you also very good with knowing the menu for every contary and never messes up 
             specially menu for pakistan and india.
             
             also just provide me the menu and no other questions. please!
             also the title and the menu should always be on the seprate lines example: 

             ## restrunt_name  

             ### Menu:

             '''),
            'human','give me a menu for {restrunt_name} restrunt.'
        ]
    )

    return prompt.format_prompt(restrunt_name= restrunt_name)

food_names = (RunnableLambda(lambda x : food_prompt(x)) | model | StrOutputParser())

def generate_restrunt_menu(restunt_name):
    chain = prompt | model | StrOutputParser()
    restrunt_menu = chain | food_names

    result = restrunt_menu.invoke({'cuisine':restunt_name})
    return result

if __name__ == "__main__":
    print(generate_restrunt_menu('Italian'))