#Building a function to apply these transformations

def transformations(data):
    from pandas import get_dummies

    #Creating the size_type feature
    data['size_type'] = data['size']+"-"+data['type']

    #Dropping not used collumns
    data = data.drop(columns=['size', 'cylinders', 'type', 'fuel', 'transmission'])

    #One-hot-encoding categorical variable
    data = get_dummies(data)
    
    #Normalizing the numerical variables
    #data['price'] = (data['price'] - data['price'].min()) / (data['price'].max() - data['price'].min())
    #data['year'] = (data['year'] - data['year'].min()) / (data['year'].max() - data['year'].min())
    #data['odometer'] = (data['odometer'] - data['odometer'].min()) / (data['odometer'].max() - data['odometer'].min())
    
    return data.to_numpy()