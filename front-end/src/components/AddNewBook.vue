<template>
  <v-container class="mt-4">
    <v-row justify="center" align="center">
      <v-col cols="6">
        <v-text-field
          v-model="search"
          clearable
          counter
          prepend-inner-icon="mdi-magnify"
          label="キーワード検索"
          ref="searchField"
          @keyup.enter="executeSearch"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center" class="mb-4">
      <v-col cols="3" class="text-center">
        <v-btn
          class="rounded-xl border-dashed"
          block
          width="50%"
          height="400px"
          @click="activateSearch"
        >
          <span class="button-text">キーワード検索</span>
        </v-btn>
      </v-col>
      <v-col cols="3" class="text-center">
        <v-btn
          class="rounded-xl border-dashed"
          block
          width="50%"
          height="400px"
          @click="openCamera('camera')"
        >
          <span class="button-text">カメラ検索 </span>
        </v-btn>
      </v-col>
    </v-row>

    <div v-if="searchResults && searchResults.length > 0">
      <v-row justify="center">
        <v-col v-for="(item, i) in searchResults" :key="i" cols="6">
          <v-card color="#385F73" dark class="hover-card">
            <!-- 追加登録ボタン -->
            <v-btn
              fab
              small
              class="card-button"
              color="primary"
              @click="addNewBookBtn(item)"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
            <div class="d-flex flex-no-wrap">
              <v-col cols="4" class="pa-3 d-flex justify-center">
                <v-avatar size="auto" tile>
                  <v-img
                    v-if="item.pics"
                    :src="item.pics"
                    :style="{ 'max-width': '100%', 'max-height': '100%' }"
                  ></v-img>
                  <v-img
                    v-else
                    :src="require('../assets/logo.png')"
                    :style="{ 'max-width': '100%', 'max-height': '100%' }"
                  ></v-img>
                </v-avatar>
              </v-col>
              <v-col cols="7" class="pa-3">
                <div class="text-h5 md-3 pb-5">{{ item.title }}</div>
                <v-row class="pb-3">
                  <v-col cols="6">
                    <div class="word-wrap normal pt-7">
                      {{ "著者： " + item.author }}
                    </div>
                    <div>{{ "出版日： " + item.pub_date }}</div>
                    <div>{{ "ジャンル： " + item.category }}</div>
                    <div>{{ "ページ数： " + item.pages }}</div>
                  </v-col>
                  <v-col cols="6" class="pa-3">
                    <div class="word-wrap normal pt-7">
                      {{
                        item.text.length > 100
                          ? item.text.slice(0, 100) + "..."
                          : item.text
                      }}
                    </div>
                  </v-col>
                </v-row>
              </v-col>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <!-- カメラの表示用ダイアログ -->
    <v-dialog v-model="cameraDialog" max-width="500px">
      <v-card>
        <v-card-text>
          <v-card-text
            >本のバーコードが表示させるようにしてください</v-card-text
          >
          <video ref="videoElement" width="100%" height="100%"></video>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="closeCamera">閉じる</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 新規登録用ダイアログ -->
    <v-dialog
      v-model="addNewBookDialog"
      max-width="800px"
      style="overflow: hidden"
      persistent
    >
      <v-card>
        <v-toolbar class="mb-3" rounded dark color="purple">
          この本を追加しますか？
        </v-toolbar>
        <v-card>
          <v-row no-gutters justify="center">
            <v-col cols="5" class="d-flex justify-center">
              <v-avatar size="auto" class="pa-5" tile>
                <v-img
                  v-if="addNewBookItem.pics"
                  :src="addNewBookItem.pics"
                  :style="{ 'max-width': '100%', 'max-height': '100%' }"
                ></v-img>
                <v-img
                  v-else
                  :src="require('../assets/logo.png')"
                  :style="{ 'max-width': '100%', 'max-height': '100%' }"
                ></v-img>
              </v-avatar>
            </v-col>
            <v-col cols="6" class="pa-5">
              <v-row>
                <v-col>
                  <div class="text-h5 md-3 pb-5">
                    {{ addNewBookItem.title }}
                  </div>
                  <div>{{ "著者： " + addNewBookItem.author }}</div>
                  <div>{{ "出版日： " + addNewBookItem.pub_date }}</div>
                  <div>{{ "ジャンル： " + addNewBookItem.category }}</div>
                  <div>{{ "ページ数： " + addNewBookItem.pages }}</div>

                  <v-card-text
                    class="word-wrap normal d-flex align-center pl-0"
                  >
                    <v-icon
                      v-for="index in 5"
                      :key="index"
                      :class="[
                        'mdi',
                        index <= selectedStar
                          ? 'mdi-star yellow--text'
                          : 'mdi-star-outline',
                      ]"
                      @click="updateSelectedStar(index)"
                    ></v-icon>
                    <v-spacer></v-spacer>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row no-gutters justify="center">
            <v-col cols="10" class="justify-center">
              <v-textarea
                v-model="userSummary"
                filled
                label="本の感想・メモ"
                color="purple"
                @blur="trimText"
                counter="1000"
                clearable
                auto-grow
              ></v-textarea>
            </v-col>
          </v-row>
        </v-card>
        <v-card-actions class="justify-space-between mt-3">
          <v-col cols="auto" color="blue">
            <v-btn text outlined @click="closeAddNewDialog">閉じる</v-btn>
          </v-col>
          <v-col cols="auto" color="blue">
            <v-btn text outlined @click="addNewBook">登録</v-btn>
          </v-col>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="showSnackbar" rounded="pill" color="purple">
      {{ snackbarText }}

      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="showSnackbar = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from "axios";
import Quagga from "quagga";
export default {
  name: "AddNewBook",
  data() {
    return {
      search: "",
      cameraDialog: false,
      codeReader: null,
      apiCount: 0,
      barcodeData: "", // バーコードのデータを保存するデータプロパティ
      isbn: "",
      searchResults: [],
      addNewBookDialog: false,
      addNewBookItem: [],
      showSnackbar: false,
      snackbarText: "",
      selectedStar: 0,
      userSummary: "",
    };
  },
  methods: {
    // 検索フィールドを活性化する
    activateSearch() {
      this.$refs.searchField.focus();
    },
    // バーコードの値取得処理
    scanBarcode() {
      const videoElement = this.$refs.videoElement;

      Quagga.init(
        {
          inputStream: {
            name: "Live",
            type: "LiveStream",
            target: videoElement,
          },
          decoder: {
            readers: ["ean_reader"],
          },
        },
        (err) => {
          if (err) {
            console.error("Quagga initialization failed:", err);
            return;
          }

          Quagga.onDetected((result) => {
            const barcodeData = result.codeResult.code;
            console.log("Detected barcode:", barcodeData);

            // EAN-13形式のバーコードからISBNを取得
            // 一瞬で何回も読み取られる時がある。
            if (
              barcodeData.length === 13 &&
              barcodeData.startsWith("978") &&
              this.apiCount === 0
            ) {
              this.apiCount += 1;
              this.barcodeData = barcodeData;
              this.isbn = barcodeData.slice(3, 12);
              console.log("ISBN:", this.isbn);

              Quagga.stop();
              this.closeCamera();

              // 5秒間の待機処理
              setTimeout(() => {
                // バーコードの値から本の検索API
                this.searchBookByCamera(this.barcodeData, this.isbn);
              }, 5000);
            }
          });

          Quagga.start();
        }
      );
    },
    // カメラを起動
    openCamera() {
      this.cameraDialog = true;

      navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
          const videoElement = this.$refs.videoElement;
          videoElement.srcObject = stream;
          videoElement.play();

          this.scanBarcode(); // バーコードの読み取り処理を開始
        })
        .catch((error) => {
          console.error("カメラの起動に失敗しました:", error);
          // カメラの起動に失敗したことをダイアログで表示したい
        });
    },
    // カメラを終了
    closeCamera() {
      this.apiCount = 0;
      this.cameraDialog = false;
      const videoElement = this.$refs.videoElement;
      if (videoElement) {
        if (videoElement.srcObject) {
          videoElement.srcObject.getTracks().forEach((track) => track.stop());
        }
        videoElement.pause();
        videoElement.srcObject = null;
      }
    },
    // バーコードで検索する処理
    searchBookByCamera(barcodeData, isbn) {
      let param = {
        barcodeData: barcodeData,
        isbn: isbn,
      };
      axios
        .post("http://127.0.0.1:8000/book/searchBookByCamera", param)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
            this.searchResults = data.book_info;
          } catch (e) {
            console.log(e);
          }
        });
    },
    executeSearch() {
      // ローディング付けたい
      if (this.search.length > 0) {
        let param = {
          keyword: this.search,
        };
        axios
          .post("http://127.0.0.1:8000/book/searchBookByKeyword", param)
          .then((res) => {
            try {
              let data = JSON.parse(JSON.stringify(res.data));
              console.log(data);
              this.searchResults = data.book_info;
              // ローディング付けたい
            } catch (e) {
              console.log(e);
            }
          });
      }
    },
    addNewBookBtn(item) {
      this.addNewBookDialog = true;
      this.addNewBookItem = item;
    },
    closeAddNewDialog() {
      this.makeInitInfo();
    },
    addNewBook() {
      this.showSnackbar = true;
      this.snackbarText = "登録しました";
      // console.log(this.addNewBookItem);
      this.addNewBookApi();
    },
    updateSelectedStar(index) {
      this.selectedStar = index; // クリックされた星のインデックスを取得し、selectedStarに代入
    },
    makeInitInfo() {
      this.addNewBookDialog = false;
      this.addNewBookItem = [];
      this.selectedStar = 0;
      this.userSummary = "";
    },
    trimText() {
      if (this.userSummary && this.userSummary.length > 1000) {
        this.userSummary = this.userSummary.slice(0, 1000);
      }
    },
    addNewBookApi() {
      if (this.addNewBookItem.length < 0) {
        this.showSnackbar = true;
        this.snackbarText = "登録できませんでした";
        return;
      }
      let param = {
        book_item: this.addNewBookItem,
        user_review: this.selectedStar,
        user_summary: this.userSummary,
      };
      axios
        .post("http://127.0.0.1:8000/book/registerNewBook", param)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
            if (data.error_msg.length > 0) {
              this.snackbarText = data.error_msg;
            } else {
              this.snackbarText = "本棚に登録しました";
            }
            this.showSnackbar = true;
            // ローディング付けたい
          } catch (e) {
            console.log(e);
          } finally {
            this.makeInitInfo();
          }
        });
    },
  },
};
</script>

<style scoped>
.border-dashed {
  border: 2px dashed white;
}

.button-text {
  color: black;
  font-weight: bold;
  font-size: 24px;
}
.card-button {
  position: absolute;
  top: 5px;
  right: 5px;
  z-index: 1;
}
</style>
