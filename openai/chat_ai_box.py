# # import libary
# import openai
#
# # key
# openai.api_key = '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'
#
# # model engine
# my_model_engine = 'gpt-3.5-turbo'
#
# question = 'hello, how are you'
#
# complete_command = openai.ChatCompletion.create(
#     engine=my_model_engine,
#     prompt=question,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5
# )
# answer = complete_command.choices[0].text
# print(answer)

import openai

openai.api_key = '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'
model_id = 'gpt-3.5-turbo'


def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


conversation = []
conversation.append({'role': 'system', 'content': 'How may I help you?'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

while True:
    prompt = input('User:')
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
