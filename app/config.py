class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = 'smtp.google.com'
    MAIL_SERVER = 'smtp.mailtrap.io'
    # MAIL_PORT = 587
    MAIL_PORT = 2525
    # MAIL_USE_TLS = True
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_USERNAME = '33310a5cd2dc8a'
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_PASSWORD = 'efb89b5e8ebf21'
