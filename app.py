import eel

eel.init('Gui')
         
@eel.expose
def App(): #App main function
    
    @eel.expose
    def App():
        print('Application Running')
App()
eel.start("mainn.html" ,size=(500,600))
    