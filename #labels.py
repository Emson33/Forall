#labels

class label:
    

    def __init__(self,id,name, country, material, short_description):
        self.id = id
        self.name = name   
        self.country = country
        self.material = material
        self.short_description = short_description

    def GetLabelData(self):
        print("Label name: " + self.name + "\nId: " + self.id + "\nCountry" + self.country + "\nMaterial: " + self.material + "\nShort description: " + self.short_description)


tyskie = label("Tyskie", "165", "Polska", "Paper", "Tyskie gronie" )
tyskie.GetLabelData()
#test