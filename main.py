#Get number of miles driven from user
miles= float(input ('Please enter number of miles driven '))
#Get number of gallons of gas used
gallons= float (input ('Please enter number of gallons of gas used '))
#calculate miles per gallon
milesPerGallon= miles/gallons
#output the results
print ('Driving', miles, 'miles using', gallons, 'gallons of gas gives a MPG of', round (milesPerGallon,2), 'miles per gallon')