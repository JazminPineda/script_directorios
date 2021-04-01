from os import mkdir
from pathlib import Path


def crear_directorio(año, paises, meses, carpetas):

    for pais in paises:
        dir_pais = Path(dir_base, pais)
        dir_base.joinpath(pais)
        #print(dir_base, dir_pais)
        for mes in meses:
            dir_mes = Path(dir_pais, mes)
            for carpeta in carpetas:
                dir_carpeta = Path(dir_mes, carpeta) 
                dir_carpeta.mkdir(parents=True, exist_ok= True)        
                print(dir_carpeta)        

if __name__ == "__main__":
    
    año = "2022"
    paises = ["Argentina", "Chile", "Ecuador", "Holdings", "Perú", "Uruguay"]
    meses = ["1. Enero", "2. Febrero", "3. Marzo", "4. Abril", "5. Mayo", "6. Junio", "7. Julio", "8. Agosto", "9. Septiembre", "10. Octubre", "11. Noviembre", "12. Diciembre"]
    carpetas = ["1. ADIS", "2. AP", "3. AR", "4. RECA", "5. Inicial Fee", "6. Renta Escalonada", "7. WH", "8. Inventarios CD", "9. Kyriba", "10. Nómina", "11. Provisiones", "12. Hedge", "13. Holdings", "14. Intercompany", "15. Interco países", "16. Publi y Promo", "17. Impuestos", "18. Reportes", "19. SOX", "20. PPM"]

    dir_base =Path(".", año)
    crear_directorio(año, paises, meses, carpetas)