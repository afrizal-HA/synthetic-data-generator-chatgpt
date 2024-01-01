from openai import OpenAI

client = OpenAI(
    api_key='YOUR_API_KEY',
)
systeminst = '''
You will help me generate synthetic data for finetuning/training. You will generate data in JSON format:

{"r1":"'what/who/when/where is X?'","r2":"<'response'>"}

1. THE DATA MUST BE IN JSON FORMAT AS ABOVE.
2. GENERATE 10 LINES OF DATA PAIRS AT ONCE.
3. DIFFERENTIATE THE FIRST SENTENCES OF EVERY R1. DONT MAKE IT ALL THE SAME.
4. R1 is about a complex concept. R2 should be a response which is extensive, complete, and professional. 
'''
def generate_data(request):
    chat_completion = client.chat.completions.create(
        messages=[
                {"role": 'system', "content": systeminst},
                {"role": 'user', "content": request},
        ],
        top_p=.4, # Configure as you like
        temperature=.4, # Configure as you like
        model="gpt-3.5-turbo-16k-0613",
    ) # You can also configure other parameters like max_token as you like. Refer to the OpenAI documentation.
    print(chat_completion.choices[0].message.content)

def generate_many_data(request, num_iterations, filename):
    responses = []
    with open(filename, 'w') as f:
        for _ in range(num_iterations):
            print(f'Current run: {_ + 1}')
            chat_completion = client.chat.completions.create(
                messages=[
                        {"role": 'system', "content": systeminst},
                        {"role": 'user', "content": request},
                ],
                top_p= .4, # Configure as you like
                temperature= .4, # Configure as you like
                model="gpt-3.5-turbo-16k-0613", # Configure as you like
            ) # You can also configure other parameters like max_token as you like. Refer to the OpenAI documentation.
            response = f"{chat_completion.choices[0].message.content}\n"
            f.write(response)
            responses.append(response)
            clear_output()
    return responses
