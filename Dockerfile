# ベースイメージを指定
FROM node:14 as build-stage

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# 依存パッケージをインストール
RUN npm install

# ソースコードをコピー
COPY . .

# アプリケーションをビルド
RUN npm run build

# 本番用の軽量なイメージを使う
FROM nginx:stable-alpine as production-stage

# Nginxの設定ファイルを上書き
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ビルドステージからビルドしたアプリケーションをコピー
COPY --from=build-stage /app/dist /usr/share/nginx/html

# ポートを公開
EXPOSE 80

# Nginxを起動
CMD ["nginx", "-g", "daemon off;"]