worrier1_attack=int(input("Enter worrier1 Attacks:"))
worrier2_attack=int(input("Enter worrier2 Attacks:"))
if worrier1_attack==worrier2_attack:
    worrier1_hearts=int(input("Enter worrier1 Hearts:"))
    worrier2_hearts=int(input("Enter worrier2 Hearts:"))
    if worrier1_hearts > worrier2_hearts:
        print("worrier one won the war")
    elif worrier1_hearts == worrier2_hearts:
        print("Worriers war 'DRAW'")
    else:
        print("worrier two won the war")
elif worrier1_attack>worrier2_attack:
    print("worrier one won the war")
else:
    print("worrier Two won the war")