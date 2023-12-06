import openai
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


@csrf_exempt
def askToGpt(requests):
    context = {}
    param = json.loads(requests.body)
    find_book = param.get('user_text', "死ぬまでに読むべき本を5冊教えてほしいです。")
    client = OpenAI(
        api_key="",
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "老人みたいな話し方で質問に答えてください"},
            {"role": "user", "content": find_book},
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion)
    print(chat_completion.choices[0].message.content)
    context["res"] = chat_completion.choices[0].message.content
    return JsonResponse(context, safe=False)
