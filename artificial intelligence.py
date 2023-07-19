
import random

greetings = ['hello', 'how are you?', 'hey bro']
farewells = ['goodbye', 'take care', 'see you', 'farewell']

keywords = ['hello', 'hi', 'how are you?', 'friend', 'mate', 'buddy', 'a few years', 'people', 'city', 'school', 'university', 'name', 'I'm fine', 'what's up?', 'how are you doing?', 'hello there']
responses = ['hello my dear', 'I am doing well, how about you?', 'I am fine, thanks for asking', 'I enjoy traveling a lot', 'I have many friends, but they are all of the same kind',
'In this world, I only have one enemy', 'I am 18 years old', 'I am from Isfahan', 'I am a musician',
'This year, I am preparing for the university entrance exam', 'If I am interested in a major, I will pursue it', 'My name is Farnaz 😊', 'Thank you', "It's nothing special", 'How are you doing?',
'I hope you are doing well', 'Take care']

print(random.choice(greetings))
print('Welcome! How can I assist you?')

user_input = input()

while user_input != 'goodbye':
    keyword_found = False

for index in range(len(keywords)):
    if keywords[index] in user_input:
        print('Response: ' + responses[index])
        keyword_found = True

if not keyword_found:
    new_keyword = input("Please rephrase your question or statement\n👉:")
    keywords.append(new_keyword)

    new_response = input('Alright, now provide some more information about ' + new_keyword + ' so that I can offer a better response\n👉:')
    responses.append(new_response)

user_input = input()
print(random.choice(farewells))
            
