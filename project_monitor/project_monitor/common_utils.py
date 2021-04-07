from firebase_admin import credentials, firestore, auth
import firebase_admin

firebaseConfig = {
  "type": "service_account",
  "project_id": "ubuntu-ea452",
  "private_key_id": "39332ac2c1465f2eedea16043e7c65be6243eecc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCQsovGjjVqetln\nelszCRYzRrIsKxa7dKoYqrr6rGpaEkTG7vAJ3FSP/XJt6UNnBZnx5/3jBEbVwK4+\npYegc8boinSrNSG+MnncUL+/qqQ+D9qMs0g6cjSUUMGK+O+zjDpgZN9upR/b7VMe\nvIlVz8KvHuJizDquhhYZ/ugsXCP6el38GqeC1qU6tLEsa9805qSQHOtVF38BrZ7t\n1zosm+rP/DJswzzaM+zO8U34N4D2TM0mrZgZ2rE7g6BvLPz9m2a/UBCKgetofo8s\nGZsHCo7gD+J3vcrdcz97FRImKw/WJbKh7+Bknk6uG4nJV2/NBfN19Faroq8rxsiL\nw5CX2hjJAgMBAAECggEABAHh4BCDPl7VH/EcwKdH9yVNZBlfEKkK5tJDbT5WHj+m\ncSSKotHxOmEZTDo+vKmnzPIbyAUeDTXVW8aGbxcGpvmNHTxn4fgUEfaJ/PM5axR8\nmYwgHCoMRMryiph19lf+ujmlZwh7ad6b1aAOz8DWnqgk1t2wDc6zP0bIlbPsyprL\nQXkT8rUFhqMwj5w0KUa3Lmob7+DrMPcCC23+LxbJxSmWKkre7DH4eV/pGoR4TPEo\ngbD5A9J8xHGKIAnPekqPSdT8EjxCs5Hj/RiqtYKnQ1PM2ic5IIp1NUPUMGgFfHkx\nSlWuChZU9U56I1aoWKIC5PnmTiapL0+wrFEgCeJshQKBgQDCSBj8sdPpRBxanh35\n6Sl0f1cHt20MzqD+vWF/rWGbQALvjBz+96Ajz/1P2sJLVog3lMkpG5wEymLtfXr5\n/K+WvKFuga6fV9cI8NWk55esxpFKWg+p2GDqrGfjxSp3NJ4QC7t8T4/wLJnzISRM\nGI1nLCEHp0ikrAAuL+vGl1GrJQKBgQC+qgcNwx4+h1LRdSAvtSPo1tZNdrv8Cz0g\nyqnWGU2tYjeQiikQytqOzzPFeui/Lrf0zNkV7MhKCqmZwLQC8zgHMp5RFz9Wos+K\nmxFWkYi859uCbdZ5qRY0zEYFdFzDtIarWudK40AQuUZlkHFmeuDOuOFQjbLhFDou\n9chPac731QKBgFcZRYJ8IrnQHDoP6vZwLnKY6CaAeDYmqIyr0HsR+tFEKEzGbvVr\nhHKpuzHCrBpkZ9srK+fvBcosBZ/dAnXyb7HPTTwijWvIUJIkjlNItHnz540CxUTq\nycBLnKPDb99TSo19BQedD7Wn+TjDoecvlq0rXn904p9YsRgDydsVWbq1AoGBAKft\npUzPv8Ge+qiVGoYqarhXEGUl4Kg7Vdmd5jw2CR5e1UWvCkBKCnmhsZ2LhZdtlIQ+\nMC2JYVclUP+kpGe8xGpCgQI3EYhC2bzgm0K958tKAyI7j52T+YUDLeD7/gA47iva\nYsCoqvKP3Jrzv41dSMeKOpjyVMy9PgnCXGzlam8JAoGBAKSPa5mf3vVSX0B6xCXL\nzD27q5vNwaLo4tx2UCnEXYWsUcDaR8oRcsCAVzokCigrd2zFbVMQnBnulmCrQ8oi\na4r1VN5/J2vpsHHTPmKsuEZcoE5Y+C9PSxtpUb6qp2agOnP40P+noV2Hq7lvqVEU\nn5PK2jMq9iiMr4X23yXGU25z\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-n83r1@ubuntu-ea452.iam.gserviceaccount.com",
  "client_id": "118156260357453720158",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-n83r1%40ubuntu-ea452.iam.gserviceaccount.com"
}


cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)
db = firestore.client()





