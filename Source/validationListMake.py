## Onur Yilmaz
## CENG 463 - Term Project

## File for validation list creation

## Import for file operation
import yaml 

## List of URLS
validationList=[
('http://www.beyazperde.com/filmler/film-145397/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-214686/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-54343/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-193101/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-190267/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-201797/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-176279/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-145646/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-205375/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-203662/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-198903/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-196306/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-209296/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-194879/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-185999/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-145646/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-190794/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-195834/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-132874/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-192858/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-192067/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-178980/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-146622/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-128188/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-183369/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-203597/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-190799/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-181443/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-185970/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-141564/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-187864/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-140459/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-205984/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-196699/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-201649/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-205968/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-178179/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-182404/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-196676/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-183144/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-146628/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-204106/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-197153/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-186349/elestiriler-beyazperde/', 'NEUTRAL'),
('http://www.beyazperde.com/filmler/film-188159/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-189944/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-144687/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-201209/elestiriler-beyazperde/', 'NEGATIVE'),
('http://www.beyazperde.com/filmler/film-175594/elestiriler-beyazperde/', 'POSITIVE'),
('http://www.beyazperde.com/filmler/film-136181/elestiriler-beyazperde/', 'POSITIVE'),
]

# Saving the list
file_writing = file('validationList.yaml', 'w') 
yaml.dump(validationList, file_writing) 
file_writing.close() 

print "Done!"

## End of code
