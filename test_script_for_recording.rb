# coding: UTF-8

# 作品の試し撮りのため、ここでは「画像を重ねる」という仕様を12回だけ満たしている
# 本番の展示を想定する場合はcronで制御すべきである
12.times do
  # 録音する（Raspberry Pi環境下専用）
  `arecord -D plughw:1,0 -d 5 -r 16000 -c 1 -f S16_LE outernet.wav`

  # APIを通じて、録音音声をテキスト化する
  text = `python3 voice-texting.py`

  # 文章構造を取り出すスクリプトを走らせる
  # 文章構造の把握に即した言葉を抽出することで、会話とは脈絡のない言葉の検索を防ぐ
  # なお、文章構造を把握する複数のパターンが返ってくる中、今回は便宜上、最初のパターンのみを取り出す
  # （タプル内の最初のパターンは、主語-述語の関係を表すパターンとなる）
  queries = `python3 ./filter_nouns.py "#{text}"`.split
  final_queries = `python3 ./filter_structure.py "#{queries[0]}" "#{queries[1] || 'No-Text-Found'}" "#{text}"`.split
  final_queries = final_queries.take(2) if final_queries.size > 2

  # final_queriesが空の時、全てをやり直す
  next if final_queries.empty?

  # 抽出された言葉で画像検索を行い、それをpythonの画像処理ライブラリを用いて重ね合わせる
  final_queries.each_with_index do |q, idx|
    `python3 ./search.py "#{q}" "#{idx + 1}"`
    `python3 ./overlap.py "#{idx + 1}"`
  end

  # 次回動作まで、任意の時間だけ待つ
  sleep 10
end
