"""
..Task
..Given an integer, perform the following conditional actions:

.. If n  is odd, print Weird
.. If n is even and in the inclusive range of 2 to 5, print Not Weird
.. If n is even and in the inclusive range of 6 to 20, print Weird
.. If n is even and greater than 20, print Not Weird
"""

sample = int(input("Digite un valor "))

if sample % 2 != 0:
    print("The number typed: {} is Weird".format(sample))
    
elif sample % 2 == 0 and sample in range(2,5):
    print("The number typed: {} isn't Weird".format(sample)) 
      
elif sample % 2 ==0 and sample in range(6,21):
    print("The number typed: {} is Weird".format(sample))
    
else:
    print("The numbes is Not Weird")         
    