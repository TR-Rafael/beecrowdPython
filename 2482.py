number_of_languages = int(input())
languages = []
for i in range(number_of_languages):
    lang = input()
    message = input()
    languages.append({"lang": lang, "message": message})

number_of_children = int(input())

for i in range(number_of_children):
    name = input()
    lang = input()
    message = next((x["message"] for x in languages if x['lang'] == lang), None)
    print(name)
    print(message)
    print()
