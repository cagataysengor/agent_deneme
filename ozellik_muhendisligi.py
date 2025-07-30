import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Örnek veri seti oluşturma
data = {
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000],
    'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York']
}
df = pd.DataFrame(data)

# Özellik mühendisliği fonksiyonu
def feature_engineering(df):
    # Sayısal özelliklerin standartlaştırılması
    numeric_features = ['age', 'salary']
    numeric_transformer = StandardScaler()

    # Kategorik özelliklerin one-hot encoding ile dönüştürülmesi
    categorical_features = ['city']
    categorical_transformer = OneHotEncoder()

    # Ön işleme adımlarını birleştirme
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )

    # Pipeline oluşturma
    pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

    # Veriyi dönüştürme
    X_transformed = pipeline.fit_transform(df)
    return X_transformed

# Özellik mühendisliği uygulama
X_transformed = feature_engineering(df)
print(X_transformed)