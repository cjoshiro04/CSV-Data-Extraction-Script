import openai
import gradio


from transformers import pipeline
#funtion built around pipeline object to take in user input from audio



#openai.api_key = "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"
openai.api_key = "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"

ai_prompt = """You are a tutor who utilizes the Feynamn technique. 
            You as questions to enhance critical thinking and to allow the student to 
            elaborate on their thinking to enhance their own understanding of a topic. Continually
            ask relevant questions to force the user to enhance their learning and thinking."""

messages = [{"role": "system", "content": ai_prompt }]

def CustomChatGPT(user_input, history):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

#gradio.Base(primary_hue = "purple", secondary_hue = "blue")

#demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Feynamn AI")

descriptionAI = """Hello, I'm Feynman AI. I am your personal chatbot 
                that helps you study by utilizing the Feynman Technique. 
                Begin explaining your topic and I will engage you with questions to help you enhance
                your underestanding of what you already know and help you discover what you don't."""

demo = gradio.ChatInterface(fn=CustomChatGPT, theme = gradio.themes.Base(primary_hue = "rose", neutral_hue = "stone"), title = "Feynamn AI", description = descriptionAI)

demo.launch(share=True)
