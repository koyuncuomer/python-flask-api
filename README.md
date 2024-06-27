# python-flask-api

Bu proje, Flask ve PostgreSQL kullanarak oluşturulmuş kullanıcı, gönderi, yorum, albüm, fotoğraf ve yapılacaklar listesi modellerinden oluşan bir API içerir. 

### Kurulumu

1. Projeyi klonlayın:
   
   ```
   git clone https://github.com/koyuncuomer/python-flask-api.git
   cd python-flask-api
   ```
2. Sanal ortam oluşturun ve etkinleştirin:
   
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Gerekli Python kütüphanelerini yükleyin:
   
   ```
   pip install Flask Flask-SQLAlchemy Flask-Migrate python-dotenv psycopg2-binary
   ```
4. .env dosyasını oluşturun ve gerekli ortam değişkenini ekleyin:
   
   ```
   DATABASE_URL=postgresql://<kullanici_adi>:<parola>@localhost:5432/<veritabani_adi>
   ```
5. Veritabanını oluşturun ve migration çalıştırın:
       
    Eğer `migrations` klasörü zaten mevcutsa:

    ```
    flask db stamp head
    flask db migrate -m "init migration"
    flask db upgrade
    ```

    Eğer `migrations` klasörü mevcut değilse:

    ```
    flask db init
    flask db migrate -m "init migration"
    flask db upgrade
    ```
6. Uygulamayı çalıştırın:

   ```
   python run.py
   ```
