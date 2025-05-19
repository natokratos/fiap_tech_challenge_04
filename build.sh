export PKG_DIR="package"
export ZIP_DIR="package.zip"
export APP_PKG_DIR="app_package"
export APP_ZIP_DIR="app_package.zip"

rm -rf ${ZIP_DIR} || true 
rm -rf ${PKG_DIR} || true && mkdir -p ${PKG_DIR}
rm -rf ${APP_ZIP_DIR} || true 
rm -rf ${APP_PKG_DIR} || true && mkdir -p ${APP_PKG_DIR}

#sudo docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.6 \
#    pip install -r requirements.txt -t ${PKG_DIR}
cp -Rf requirements.txt ${PKG_DIR}
cp -Rf ./src/geckodriver*  ${PKG_DIR}

cp -Rf src/* ${APP_PKG_DIR}

zip -r9  ${ZIP_DIR} ${PKG_DIR}/
zip -r9  ${APP_ZIP_DIR} ${APP_PKG_DIR}/

rm -rf ${APP_PKG_DIR}

pip3.13 install poetry
pip3.13 install fastapi[standard]
pip3.13 install uvicorn[standard]