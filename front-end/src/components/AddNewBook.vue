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
    <div>{{ barcodeData }}</div>
    <v-row justify="center">
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
          } catch (e) {
            console.log(e);
          }
        });
    },
    executeSearch() {
      console.log(this.search);
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
            } catch (e) {
              console.log(e);
            }
          });
      }
    },
  },
};
</script>

<style scoped>
.card-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
  border-radius: 8px;
  background-color: #f0f0f0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-button-content {
  width: 100%;
  height: 100%;
  font-size: 24px;
}
.border-dashed {
  border: 2px dashed white;
}

.button-text {
  color: black;
  font-weight: bold;
}
</style>
