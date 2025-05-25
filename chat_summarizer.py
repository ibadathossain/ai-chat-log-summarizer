def load_chat(file_path):
    user_msgs = []
    ai_msgs = []
    

    try:
        with open(file_path , 'r' , encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("User:"):
                    user_msgs.append(line.replace("User:" , "").strip())
                elif line.startswith("AI:"):
                    ai_msgs.append(line.replace("AI:" , "").strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return user_msgs , ai_msgs

def show_stats(user_msgs, ai_msgs):
    total = len(user_msgs) + len(ai_msgs)
    print("\n--- Message Stats ---")
    print(f"Total messages exchanged: {total}")
    print(f"User messages: {len(user_msgs)}")
    print(f"AI messages: {len(ai_msgs)}")

if __name__ == "__main__":
    user_msgs, ai_msgs = load_chat("chat.txt")
    print("User Messages:", user_msgs)
    print("AI Messages:", ai_msgs)
    show_stats(user_msgs, ai_msgs)

  