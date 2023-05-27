from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.pensarcursos.com.br/entrar")
    pagina.fill('xpath= /html/body/main/div/div/div/div[2]/form/label[1]/input', "brunnasixx2011@hotmail.com")
    pagina.fill('xpath = /html/body/main/div/div/div/div[2]/form/label[2]/input', "sua senha")
    pagina.locator('xpath= /html/body/main/div/div/div/div[2]/form/button').click()



    time.sleep(10)