#first task

radius= float ( input(" Enter the radius of the circle : ")) 
area=  3.1415* radius *radius 
print  ("Area of the circle is {}".format  (area))


#second task

filename = input("Input the Filename") 
f_extns = filename.split(".") 
print(" The extension if the file is: "+ repr(f_extns[-1]))
