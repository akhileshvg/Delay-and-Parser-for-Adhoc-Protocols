import csv
with open('Project2Results.csv') as csv_file:
	csv_reader=csv.reader(csv_file)
	next(csv_reader)
	p=[]
	for line in csv_reader:
		p.append(line[2])	
		

	j=map(int,p)
	

	sum=0

	for k in j:
		sum=sum+k
	print "The total number of packets received: ",sum	
