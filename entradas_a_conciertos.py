boletas = int(input("Ingresa la cantidad de boletas a comprar :" ))
palco = str(input("En que palco deseas reservar (A - B - C ) :"))
semana = str(input("Es fin de semana ? Si o No?"))


a_palco = 5.05 #Valor en fin de semana

b_palco = 5.04

c_palco = 5

descuento_a = 0.2 #Descuento por cantidades
descuento_b = 0.1
descuento_c = 0.05

if "Si" in semana :

    if "A" in palco :   
        if boletas >= 20:
            descuento = (boletas*a_palco) 
            descuento = descuento - (descuento_a *(boletas*a_palco))

        elif boletas > 6 and  boletas < 10:    
            descuento = (boletas*a_palco) 
            descuento = descuento -  (descuento_b*(boletas*b_palco))
        elif boletas >2 and  boletas < 5:    
            descuento = (boletas*a_palco) 
            descuento = descuento - (descuento_c*(boletas * c_palco))
        else : descuento = boletas * a_palco     
    elif "B" in palco:
        if boletas >= 20:
            descuento = (boletas*b_palco) 
            descuento = descuento - (descuento_a*(boletas*a_palco))
        elif boletas >6 and  boletas < 10:    
            descuento = (boletas*b_palco) 
            descuento = descuento - (descuento_b*(boletas*b_palco))
        elif boletas  > 2 and  boletas < 5 :    
            descuento = (boletas*b_palco) 
            descuento = descuento - (descuento_c*(boletas*c_palco))
        else : descuento = boletas*b_palco    

    elif "C" in palco :      
        if boletas >= 20:
            descuento = (boletas*c_palco) 
            descuento = descuento- (descuento_a*(boletas*a_palco))
        elif boletas >6 and  boletas < 10:     
            descuento = (boletas*c_palco) 
            descuento = descuento - (descuento_b*(boletas*b_palco))
        elif boletas >2 and  boletas < 5:    
            descuento = (boletas*5) 
            descuento = descuento - (descuento_c*(boletas*c_palco))
        else : descuento =  boletas*c_palco    

elif "No" in semana:

    if boletas > 20:
        descuento = (boletas*5) 
        descuento = descuento - (descuento * descuento_a)

    elif boletas > 6 and boletas < 10:    
        descuento = (boletas*5) 
        descuento = descuento - (descuento * descuento_b)

    elif boletas > 2 and boletas < 6:    
        descuento = (boletas*5)
        descuento = descuento - (descuento *descuento_c )
    else : 
        descuento = boletas*5  
        

print(f"El precio de las boletas es {descuento}, Compraste {boletas} boletas")    