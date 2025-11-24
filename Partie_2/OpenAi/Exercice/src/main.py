
from Configuration.ai_models import AIFactory


def main():
	print("Bienvenue dans le chatbot IA!")
	print("Choisissez le rôle du chatbot parmi les options suivantes :")
	roles = {
		"1": ("Code Reviewer", "get_code_reviewer_response"),
		"2": ("Technical Writer", "get_doc_writer_response"),
		"3": ("Test Generator", "get_test_generator_response"),
		"4": ("Python Expert", "get_python_expert_response"),
		"5": ("Git Expert", "get_git_expert_response"),
		"6": ("Assistant Technique", "get_Assitant_technique_response"),
		"7": ("Tuteur Pédagogique", "get_Tuteur_pedagogique_patient_response"),
		"8": ("Expert en Code", "get_Expert_En_code_response"),
	}
	for k, v in roles.items():
		print(f"{k}. {v[0]}")
	choice = None
	while choice not in roles:
		choice = input("Entrez le numéro du rôle: ").strip()
	role_name, method_name = roles[choice]
	print(f"Rôle sélectionné : {role_name}")
	print("Posez vos questions. Pour quitter, écrivez 'quit'.")

	factory = AIFactory()
	history = []
	method = getattr(factory, method_name)

	while True:
		user_input = input("Vous: ")
		if user_input.strip().lower() == "quit":
			print("Chat terminé.")
			break
		history.append({"role": "user", "content": user_input})
		# Call the selected role method
		answer = method(user_input)
		print(f"IA: {answer}")
		history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
	main()

