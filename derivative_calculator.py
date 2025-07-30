import sympy as sp

def turev_hesapla(fonk_str, degisken_str):
    degisken = sp.symbols(degisken_str)
    fonksiyon = sp.sympify(fonk_str)
    turev = sp.diff(fonksiyon, degisken)
    return turev

# Örnek kullanım:
fonksiyon = "x**2 + 3*x + 5"
degisken = "x"
print("Türevi:", turev_hesapla(fonksiyon, degisken))