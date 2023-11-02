def main():
    eiro = eiro_uz_float(input("Cik maksāja maltīte? ").replace(",",".").strip(" €"))
    procenti = procenti_uz_float(input("Kādu procentuālo daļu vēlaties atstāt kā dzeramnaudu? "))
    dzeramnauda = eiro * procenti
    print(f"Atstājiet {dzeramnauda:.2f} €")
    return dzeramnauda


def eiro_uz_float(eiro):
    jamaksa = float(eiro)
    return jamaksa
    # jāizdara


def procenti_uz_float(procenti):
    dzeram_procenti = float(procenti)/100
    return dzeram_procenti
    # jāizdara


main()
