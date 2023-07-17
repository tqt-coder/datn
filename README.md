# Quesion Answering Web


## Report


Link recording trình bày:https://youtu.be/UtpsrP1clBg
## Demo


Link video demo: https://youtu.be/PX6ez2VT1M0
## Deploy
## link: http://35.209.117.190

## Link download model PhoBERT from the Google drive and place it in the "model/phobert_model" path
  ```
     https://drive.google.com/file/d/1S4WJx1m8t01gSNLGvZTuyAFyUKZlZloT/view?usp=sharing
  ```
- If you want to download in terminal for Unix OS:
  ```
      pip install gdown
      gdown --id <id_file in GG drive>
  ```
1. Create virtual marchine in Azure:

- OS: Linux x64 
- Size: 2 CPU, 16 GB RAM
- SSD: 50
- Inbound port: 443, 80, 22
- Outbound: 80

2. Download source code:

   ```
   git clone https://github.com/tqt-coder/datn
   ```

   ```
   cd /datn
   ```

3. Build image
   ```
   docker build -t app .
   ```
4. Run container
   ```
   docker run -d -p 80:5000 app
   ```

## Run Application

1. Prerequisites:
- Python: 3.8.0
- Check your computer has GPU

2. Install

- Download all libraries in the requirement.txt

  ```
     pip install -r requirements.txt
  ```

3. Run website

   ```
   flask run
   ```
