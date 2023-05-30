# -*- coding: utf-8 -*-
import MeCab
from wordcloud import WordCloud
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

FONT_PATH = 'C:/Windows/Fonts/HGRGM.TTC'
IMAGE_PATH = "C:\\Users\\vivi_\\PycharmProjects\\bookshelf\\front-end\\src\\assets\\img\\"

# テキストデータを形態素解析して指定した品詞の単語のみを抽出する関数
def analyze_text():
    mecab = MeCab.Tagger( r' -Owakati -d "C:\\Program Files\\MeCab\\dic\\ipadic" -u "C:\\Program Files\\MeCab\\dic\\NEologd\\NEologd.20200910-u.dic"')  # 品詞情報を取得するためのMeCabの設定
    # テキストデータ
    # text = """
    # 「二八そば」は、笑いを取るために考えられた落語の演目です。物語は、二八そば屋で働く若い主人公が、さまざまな騒動やトラブルに巻き込まれる様子を描いています。
    # 主人公は、お客さんが注文する際に「二八そば」と聞き取り、そのまま注文を受けるというおちょくりが特徴です。しかし、実は「二八そば」とは具体的な料理の名称ではなく、注文する客の言葉の継ぎ合わせです。
    # 物語は、客が注文する際に様々なユーモラスな言葉遊びをする場面や、主人公が注文を取り違えたり混乱したりする場面などで展開されます。最終的には、主人公が騒動を乗り越えて笑いを取るという結末があります。
    # この落語は、日本の伝統的なエンターテイメントの一つであり、言葉遊びやトリックを楽しむことができます。聞き手を笑わせるための巧妙な話術や表現方法が駆使されており、聴衆を楽しませることが目的とされています。
    # 落語の世界にはさまざまな演目があり、それぞれに特徴や面白さがあります。「二八そば」もその一つであり、日本の伝統文化を体感することができる素晴らしいエンターテイメントです。
    # """
    # text = """
    #     5月31日は、様々な歴史的な出来事が起きた日です。例えば、1902年のこの日、南アフリカ共和国がイギリスから独立し、独自の国家として誕生しました。また、1961年の5月31日には、南アフリカのアパルトヘイト政策に反対する国際的な運動である「アフリカ解放の日」が制定されました。
    #     一方、1991年のこの日には、ソ連の大統領であったミハイル・ゴルバチョフがモスクワで開催された共和国間協定に署名し、ソビエト連邦が崩壊しました。この出来事は、冷戦終結と新たな時代の幕開けを象徴するものとなりました。
    #     また、2005年の5月31日には、インドの首都デリーで最初の地下鉄路線が開通しました。これにより、デリー市内の交通機関が大幅に改善され、都市の発展に寄与しました。
    #     5月31日は、南アフリカ共和国の独立、アフリカ解放の日、ソビエト連邦の崩壊、デリー地下鉄の開通など、多くの重要な出来事が起きた日として歴史に刻まれています。
    # """
    text = """彼女は、キーボードの前に座り、眠りに落ちるまでコードを書き続けた。彼女の名前はエミリー。プログラミングの世界で生きる彼女は、数え切れないほどの夜更かしとカップ麺を食べながら、プロジェクトに没頭していた。

ある日、彼女は会社の新しいプロジェクトに割り当てられた。それは、画期的なアプリケーションの開発だった。彼女は興奮し、即座に取り組み始めた。日々のミーティングやコードの書き込み、バグの修正に追われながらも、彼女は情熱を持ってプロジェクトに取り組んだ。

しかし、彼女のプログラミングの世界には、予期しない出来事が訪れることになる。彼女はチームの中で素晴らしい人と出会い、彼との関係が深まっていった。彼の名前はアレックス。彼もまたプログラマであり、彼女と同じく技術への情熱を持っていた。

二人は共通の趣味や興味を持ち、プログラミングの話で夜遅くまで語り合った。しかし、彼らの関係は不適切であると知っていた。彼女は会社の倫理規定に反してしまうことを恐れ、内心葛藤していた。

時間が経つにつれ、彼らの関係はさらに深まり、禁断の恋に発展していく。彼らはプログラミングの世界での成功と、禁じられた愛の狭間で揺れ動く。彼女はモラルと情熱の間で苦悩し、自分自身と向き合う決断を迫られる。

彼女は、最終的にはプログラミングの世界と倫理のバランスを取る方法を見つけ出す。彼女は、自分のキャリアと倫理観を両立させる道を模索し、困難な道を選び続ける決断をする。

このプログラマの小説は、技術と倫理、愛と情熱の交錯する世界を描きながら、主人公の心の葛藤と成長を描いています。彼女の物語は、プログラマとしての情熱と人間の複雑な感情を絡めて、読者に考えさせることでしょう。

（※このテキストはフィクションであり、実在の人物や出来事とは関係ありません。）"""
    
    node = mecab.parseToNode(text)
    words = []
    while node:
        if node.feature.split(',')[0] in ['名詞', '動詞', '形容詞', '副詞']:
            words.append(node.surface)
        node = node.next
    return words


# ワードクラウドを生成する
def generate_wordcloud(words):
    context = {}
    word_freq = {}  # 単語の出現頻度を記録する辞書
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    print(word_freq)
    # valueを数値でソートして取り出す
    sorted_items = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    # ソートされた結果を表示
    print(type(sorted_items))
    context["word_rank"] = sorted_items

    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=FONT_PATH).generate_from_frequencies(word_freq)
    # ワードクラウドを画像ファイルとして保存する
    wordcloud.to_file(IMAGE_PATH + "wordcloud.png")
    context["image_path"] = "wordcloud.png"
    return context


# テキストデータを形態素解析してワードクラウドを生成する
@csrf_exempt
def create_wordcloud(requests):
    param = json.loads(requests.body)
    keyword = param.get('wordcloud_target', 0)
    words = analyze_text()
    context = generate_wordcloud(words)
    return JsonResponse(context, safe=False)
