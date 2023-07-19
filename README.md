# Simple_AI

1. The greetings list contains phrases such as "hello" and "how are you?" that are used to generate initial messages.
2. The farewells list contains phrases such as "goodbye" and "take care" that are used to generate farewell messages.
3. The keywords list includes keywords that may appear in user messages and are checked against.
4. The responses list contains corresponding responses for each keyword in the keywords list.
5. Using the random.choice() function, one of the phrases from greetings is selected and printed.
6. The message "Welcome! How can I assist you?" is printed.
7. User input is stored in the user_input variable.
8. A while loop begins and continues as long as the user input is not "goodbye".
9. At each iteration of the loop, it checks if a keyword is present in the user input. If found, the corresponding response from responses is retrieved and printed.
10. If no keyword is found, a new keyword is obtained from the user in new_keyword and added to the keywords list.
11. Additionally, the corresponding response from the user is obtained in new_response and added to the responses list.
12. User input is obtained again, and the loop continues.
13. At the end of the loop, one of the phrases from farewells is selected and printed.
