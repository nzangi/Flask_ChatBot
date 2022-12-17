import random
import json
import torch
from model import NeuralNetwork
from nltk_utils import bag_of_words,tokenize

device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
with open("intents.json") as file:
    intents = json.load(file)

FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data['tags']
model_state = data["model_state"]


model = NeuralNetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()


bot_name = "Nzangi"

def get_response(msg):
    while True:
        # sentence = input("You : ")

        sentence = tokenize(msg)
        # if msg.lower() == "quit":
        #     return "You have exited the chat box powered by AI, have a good day. It was pleasure to chat with you"
        #     break
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.80:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    return random.choice(intent['responses'])

        return "I did not understand what you said ..."
            # print(prob.item())

if __name__ == '__main__':
    print(f"Chat with {bot_name} or type 'quit' to exit")
    while True:
        sentence = input("You : ")
        if sentence.lower() == "quit":
            break

        answer = get_response(sentence)
        print(f"{bot_name} : {answer}")