import os

### 자신의 zone 또는 region, get-credentials 뒤에 클러스터명
os.system('gcloud container clusters --zone asia-northeast3-c get-credentials ttt')
