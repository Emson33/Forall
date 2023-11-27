#labels

class label:
    

    def __init__(self,id, name, brewery, country, material, short_description):
        self.id = id
        self.name = name
        self.brewery = brewery   
        self.country = country
        self.material = material
        self.short_description = short_description

    def GetLabelData(self):
        print(f"Label id: {self.id}\nName: {self.name}\nBrewery: {self.brewery}\nCountry: {self.country}\nMaterial: {self.material}\nShort description: {self.short_description}")

tyskie = label("165","Tyskie", "Kompania Piwowarska", "Poland", "Paper", "Tyskie gronie" )
tyskie.GetLabelData()
<<<<<<< Updated upstream
=======
#2
>>>>>>> Stashed changes
