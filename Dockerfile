#docker buildx build --platform linux/amd64 -t dominiqueulrixh/streamlit .
#docker run --name streamlit -p 9000:8501 dominiqueulrixh/streamlit

#az group create --name mdm-streamlit-ulricdo1 --location switzerlandnorth
#az appservice plan create --name mdm-streamlit-ulricdo1 --resource-group mdm-streamlit-ulricdo1 --sku F1 --is-linux
#az webapp create --resource-group mdm-streamlit-ulricdo1 --plan mdm-streamlit-ulricdo1 --name mdm-streamlit-ulricdo1 --deployment-container-image-name dominiqueulrixh/streamlit:latest
#az webapp config appsettings set --resource-group mdm-streamlit-ulricdo1 --name mdm-streamlit-ulricdo1 --settings WEBSITES_PORT=8501

FROM python:3.10.11-slim

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501
CMD ["sh", "-c", "streamlit run --server.port 8501 /usr/app/streamlit_app.py"]