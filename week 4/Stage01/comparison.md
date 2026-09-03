Question	                                                     Human version	                                                                                                                    AI version
Easy to understand?		        It it easy to uundertsand my code since it is basic python principles liem input, print, if, else, raise        The AI version was also pretty easy to undertand due to its limited amount of lines and it told me about lists before
Runs successfully?		        My works as intended, but i am slightly restricted by the amount of patients I can have at anytime                 The Ai one works as well and can store infinite amounts of patients but it doesnt raise any errors for double books
Uses only required features?	            Yes my code only uses required feautures at the moment                                                                      The AI version also only uses the reuired feutures, although missing the error handling
Adds assumptions?		                        Assumes thast there are only 2 available patients                                                                           Assumes that there arent going to be people booking at the same time
Handles errors?		        My one handles booking errors, if they have booked the same doctor at the same time it raises an error                                                      The AI code doesnt flag and errors
Could I explain it?		                                    Yes i could explain my code                                                                                                         yes i can explain the AI code



My code: My code start with the initial print stament welcoming the patient, I then ask for there name, the doctor they are here to see and at what time, The terminal will show up with these questions one after each other storing them under each variable since they are input functions. I repeat this process but with a second patient. I then go onto say that if both patients have stated theay are here to see the same doctor at the same time then it will stop the code and raise the value error and say that you cannot schedule an apointment at the sometime. Otherwise it will greet both pateints with there name, the doctor they are seeing and at what time.

AI code: The AI code starts by defining its function, it allows it to be reuasbale for more than patient. It than gathers the information for that patient who is currently filling out the form, asking for the patient name, practitioner and booking time same as my code did. It then creates a dictionary to store everything and it uses keys to map to them. Like how "Patient" is mapped to the input given early when asked "enter patient name", It repeats this for all inputs. Then it prints "Appointment saved" and returns the appointment dictionary to whover calls for it. When we simply type create_appointment() it is calling on the definition and it will start asking for the inputs.


