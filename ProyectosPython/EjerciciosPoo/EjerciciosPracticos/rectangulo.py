class Rectangulo:    
    def perimetroRectangulo(self, largo, ancho):
        self.base = float(largo);
        self.altura = float(ancho);
        return f"el perimetro de el triangulo es: {(largo+ancho)*2}";
        
    def areaRectangulo(self, base, altura):
        self.base = float(base);
        self.altura = float(altura);
        return f"el area de el triangulo es: {base*altura}";