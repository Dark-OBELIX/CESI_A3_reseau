def dechiffrer_cesar(phrase_chiffree, decalage):
    resultat = ""
    for caractere in phrase_chiffree:
        if caractere.isalpha():
            decalage_caractere = 65 if caractere.isupper() else 97
            lettre_dechiffree = chr((ord(caractere) - decalage_caractere - decalage) % 26 + decalage_caractere)
            resultat += lettre_dechiffree
        else:
            resultat += caractere
    return resultat

def generer_decryptions_cesar(phrase_chiffree):
    decalages_possibles = range(26)
    for decalage in decalages_possibles:
        dechiffre = dechiffrer_cesar(phrase_chiffree, decalage)
        print(f"Décalage {decalage}: {dechiffre}")

#generer_decryptions_cesar("oh kdfkdjh yrxv shuphwwudlw gdvvxuhu od frqilghqwldolwh vlpsohphqw")
print(dechiffrer_cesar("le hachage vous permettrait dassurer la confidentialite simplement",23))